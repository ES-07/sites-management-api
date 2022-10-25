from telnetlib import SE
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import config
from models.schemas import HealthResponse
from models.models import SecurityManager, PropertyOwner, Building, Camera, Sensor, Intrusion
from db.database import engine, Base, get_db
from db.crud import  PropertyOwnerRepository, SecurityManagerRepository, BuildingRepository, CameraRepository , SensorRepository, IntrusionRepository
from models import schemas
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.VERSION,    
    openapi_url="/openapi.json",
    docs_url="/docs",)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
############# OWNERS #############


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")

@app.get('/hello')
def hello_world():
    return {'msg': 'hello!'}

@app.post("/owners", response_model=schemas.PropertyOwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owners(request: schemas.PropertyOwnerRequest, db: Session = Depends(get_db)):
    #solucao trolha, do over again 
    owner = PropertyOwnerRepository.save(db,PropertyOwner(**request.dict()) )
    return schemas.PropertyOwnerResponse.from_orm(owner)

@app.get("/owners", response_model=List[schemas.PropertyOwnerResponse])
def find_all(db: Session = Depends(get_db)):
    owners = PropertyOwnerRepository.find_all(db)
    return [schemas.PropertyOwnerResponse.from_orm(owner) for owner in owners]

@app.get("/owners/{id}", response_model=schemas.PropertyOwnerResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    owner = PropertyOwnerRepository.find_by_id(db, id)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    return schemas.PropertyOwnerResponse.from_orm(owner)

@app.delete("/owners/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not PropertyOwnerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    PropertyOwnerRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/owners/{id}", response_model=schemas.PropertyOwnerResponse)
def update(id: int, request: schemas.PropertyOwnerRequest, db: Session = Depends(get_db)):
    if not PropertyOwnerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    owner = PropertyOwnerRepository.save(db,PropertyOwner(**request.dict()) )
    return schemas.PropertyOwnerResponse.from_orm(owner)  

############# SECURITY MANAGER #############

@app.post("/managers", response_model=schemas.SecurityManagerResponse, status_code=status.HTTP_201_CREATED)
def create_managers(request: schemas.SecurityManagerRequest, db: Session = Depends(get_db)):
    manager = SecurityManagerRepository.save(db,SecurityManager(**request.dict()) )
    return schemas.SecurityManagerResponse.from_orm(manager)

@app.get("/managers", response_model=List[schemas.SecurityManagerResponse])
def find_all(db: Session = Depends(get_db)):
    managers = SecurityManagerRepository.find_all(db)
    return [schemas.SecurityManagerResponse.from_orm(manager) for manager in managers]

@app.get("/managers/{id}", response_model=schemas.SecurityManagerResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    manager = SecurityManagerRepository.find_by_id(db, id)
    if not manager:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Security Manager not found"
        )
    return schemas.SecurityManagerResponse.from_orm(manager)

@app.delete("/managers/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not SecurityManagerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Security Manager not found"
        )
    SecurityManagerRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/managers/{id}", response_model=schemas.SecurityManagerResponse)
def update(id: int, request: schemas.SecurityManagerRequest, db: Session = Depends(get_db)):
    if not SecurityManagerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Security Manager not found"
        )
    manager = SecurityManagerRepository.save(db, SecurityManager(**request.dict()))
    return schemas.SecurityManagerResponse.from_orm(manager)  


############# BUILDINGS #############

@app.post("/buildings", response_model=schemas.BuildingResponse, status_code=status.HTTP_201_CREATED)
def create_buildings(request: schemas.BuildingRequest, db: Session = Depends(get_db)):
    building = BuildingRepository.save(db,Building(**request.dict()) )
    return schemas.BuildingResponse.from_orm(building)

@app.get("/buildings", response_model=List[schemas.BuildingResponse])
def find_all(db: Session = Depends(get_db)):
    buildings = BuildingRepository.find_all(db)
    return [schemas.BuildingResponse.from_orm(building) for building in buildings]

@app.get("/buildings/{id}", response_model=schemas.BuildingResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    building = BuildingRepository.find_by_id(db, id)
    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Building not found"
        )
    return schemas.BuildingResponse.from_orm(building)

@app.delete("/buildings/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not BuildingRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Building not found"
        )
    BuildingRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/buildings/{id}", response_model=schemas.BuildingResponse)
def update(id: int, request: schemas.BuildingRequest, db: Session = Depends(get_db)):
    if not BuildingRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Building not found"
        )
    building = BuildingRepository.save(db, Building(**request.dict()))
    return schemas.BuildingResponse.from_orm(building)  


############# CAMERAS #############

@app.post("/cameras", response_model=schemas.CameraResponse, status_code=status.HTTP_201_CREATED)
def create_cameras(request: schemas.CameraRequest, db: Session = Depends(get_db)):
    camera = CameraRepository.save(db,Camera(**request.dict()) )
    return schemas.CameraResponse.from_orm(camera)

@app.get("/cameras", response_model=List[schemas.CameraResponse])
def find_all(db: Session = Depends(get_db)):
    cameras = CameraRepository.find_all(db)
    return [schemas.CameraResponse.from_orm(camera) for camera in cameras]

@app.get("/cameras/{id}", response_model=schemas.CameraResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    camera = CameraRepository.find_by_id(db, id)
    if not camera:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found"
        )
    return schemas.CameraResponse.from_orm(camera)

@app.delete("/cameras/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CameraRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found"
        )
    CameraRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/cameras/{id}", response_model=schemas.CameraResponse)
def update(id: int, request: schemas.CameraRequest, db: Session = Depends(get_db)):
    if not CameraRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found"
        )
    camera = CameraRepository.save(db, Camera(**request.dict()))
    return schemas.CameraResponse.from_orm(camera)  


############# SENSOR #############

@app.post("/sensors", response_model=schemas.SensorResponse, status_code=status.HTTP_201_CREATED)
def create_sensors(request: schemas.SensorRequest, db: Session = Depends(get_db)):
    sensor = SensorRepository.save(db,Sensor(**request.dict()) )
    return schemas.SensorResponse.from_orm(sensor)

@app.get("/sensors", response_model=List[schemas.SensorResponse])
def find_all(db: Session = Depends(get_db)):
    sensors = SensorRepository.find_all(db)
    return [schemas.SensorResponse.from_orm(sensor) for sensor in sensors]

@app.get("/sensors/{id}", response_model=schemas.SensorResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    sensor = SensorRepository.find_by_id(db, id)
    if not sensor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found"
        )
    return schemas.SensorResponse.from_orm(sensor)

@app.delete("/sensors/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not SensorRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found"
        )
    SensorRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/sensors/{id}", response_model=schemas.SensorResponse)
def update(id: int, request: schemas.SensorRequest, db: Session = Depends(get_db)):
    if not SensorRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found"
        )
    sensor = SensorRepository.save(db, Sensor(**request.dict()))
    return schemas.SensorResponse.from_orm(sensor)  
    

############# INTRUSION #############

@app.post("/intrusions", response_model=schemas.IntrusionResponse, status_code=status.HTTP_201_CREATED)
def create_intrusions(request: schemas.IntrusionRequest, db: Session = Depends(get_db)):
    intrusion = IntrusionRepository.save(db,Intrusion(**request.dict()) )
    return schemas.IntrusionResponse.from_orm(intrusion)

@app.get("/intrusions", response_model=List[schemas.IntrusionResponse])
def find_all(db: Session = Depends(get_db)):
    intrusions = IntrusionRepository.find_all(db)
    return [schemas.IntrusionResponse.from_orm(intrusion) for intrusion in intrusions]

@app.get("/intrusions/{id}", response_model=schemas.IntrusionResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    intrusion = IntrusionRepository.find_by_id(db, id)
    if not intrusion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Intrusion not found"
        )
    return schemas.IntrusionResponse.from_orm(intrusion)

@app.delete("/intrusions/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not IntrusionRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Intrusion not found"
        )
    IntrusionRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/intrusions/{id}", response_model=schemas.IntrusionResponse)
def update(id: int, request: schemas.IntrusionRequest, db: Session = Depends(get_db)):
    if not IntrusionRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Intrusion not found"
        )
    intrusion = IntrusionRepository.save(db, Intrusion(**request.dict()))
    return schemas.IntrusionResponse.from_orm(intrusion)  

