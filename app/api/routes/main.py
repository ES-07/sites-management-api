
from fastapi import FastAPI, Depends, HTTPException, status, Response,  Response, APIRouter
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from core import config
from models.schemas import HealthResponse
from models.models import SecurityManager, PropertyOwner, Building, Device, Intrusion
from db.database import engine, Base, get_db
from db.crud import  PropertyOwnerRepository, SecurityManagerRepository, BuildingRepository, DeviceRepository , IntrusionRepository
from models import schemas
from typing import List, Union
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

BASE_PREFIX = "/sites-management-api"

app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.VERSION,    
    openapi_url="/openapi.json",
    docs_url="/docs")  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############# OWNERS #############


@app.get(BASE_PREFIX + '/', response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")

@app.get(BASE_PREFIX + '/hello')
def hello_world():
    return {'msg': 'hello!'}

@app.get(BASE_PREFIX + '/owners', response_model=schemas.PropertyOwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owners(request: schemas.PropertyOwnerRequest, db: Session = Depends(get_db)):
    #solucao trolha, do over again 
    owner = PropertyOwnerRepository.save(db,PropertyOwner(**request.dict()) )
    return schemas.PropertyOwnerResponse.from_orm(owner)

@app.get(BASE_PREFIX + '/owners', response_model=List[schemas.PropertyOwnerResponse])
def find_all(db: Session = Depends(get_db)):
    owners = PropertyOwnerRepository.find_all(db)
    return [schemas.PropertyOwnerResponse.from_orm(owner) for owner in owners]

@app.get(BASE_PREFIX + '/owners/{id}', response_model=schemas.PropertyOwnerResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    owner = PropertyOwnerRepository.find_by_id(db, id)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    return schemas.PropertyOwnerResponse.from_orm(owner)

@app.get(BASE_PREFIX + "/owners/cognito/{id}", response_model=schemas.PropertyOwnerResponse)
def find_by_cognito_id(id: str, db: Session = Depends(get_db)):
    owner = PropertyOwnerRepository.find_by_cognito_id(db, id)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    return schemas.PropertyOwnerResponse.from_orm(owner)


@app.get(BASE_PREFIX + "/owners/email/{email}", response_model=schemas.PropertyOwnerResponse)
def find_by_email(email: str, db: Session = Depends(get_db)):
    owner = PropertyOwnerRepository.find_by_email(db, email)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    return schemas.PropertyOwnerResponse.from_orm(owner)

@app.delete(BASE_PREFIX + "/owners/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not PropertyOwnerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    PropertyOwnerRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put(BASE_PREFIX + "sites-management-api/owners/{id}", response_model=schemas.PropertyOwnerResponse)
def update(id: int, request: schemas.PropertyOwnerRequest, db: Session = Depends(get_db)):
    if not PropertyOwnerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )
    owner = PropertyOwnerRepository.save(db,PropertyOwner(id=id,**request.dict()) )
    return schemas.PropertyOwnerResponse.from_orm(owner)  


class User(BaseModel):
    email: str
    password: str

@app.get(BASE_PREFIX + '/owners/login')
async def login_owner(user: User, db: Session = Depends(get_db)):
    owner: PropertyOwner = PropertyOwnerRepository.find_by_email(db, user.email)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found"
        )

    # alterar mais tarde, hardcoded máximo
    if owner.hashed_password == user.password:
        return status.HTTP_200_OK, owner

    else:
        return status.HTTP_401_UNAUTHORIZED


############# SECURITY MANAGER #############

@app.get(BASE_PREFIX + '/managers', response_model=schemas.SecurityManagerResponse, status_code=status.HTTP_201_CREATED)
def create_managers(request: schemas.SecurityManagerRequest, db: Session = Depends(get_db)):
    manager = SecurityManagerRepository.save(db,SecurityManager(**request.dict()) )
    return schemas.SecurityManagerResponse.from_orm(manager)

@app.get(BASE_PREFIX + '/managers', response_model=List[schemas.SecurityManagerResponse])
def find_all(db: Session = Depends(get_db)):
    managers = SecurityManagerRepository.find_all(db)
    return [schemas.SecurityManagerResponse.from_orm(manager) for manager in managers]

@app.get(BASE_PREFIX + '/managers/{id}', response_model=schemas.SecurityManagerResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    manager = SecurityManagerRepository.find_by_id(db, id)
    if not manager:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Security Manager not found"
        )
    return schemas.SecurityManagerResponse.from_orm(manager)

@app.delete(BASE_PREFIX + "/managers/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not SecurityManagerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Security Manager not found"
        )
    SecurityManagerRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put(BASE_PREFIX + "/managers/{id}", response_model=schemas.SecurityManagerResponse)
def update(id: int, request: schemas.SecurityManagerRequest, db: Session = Depends(get_db)):
    if not SecurityManagerRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Security Manager not found"
        )
    manager = SecurityManagerRepository.save(db, SecurityManager(id=id, **request.dict()))
    return schemas.SecurityManagerResponse.from_orm(manager)  


############# BUILDINGS #############

@app.get(BASE_PREFIX + '/buildings', response_model=schemas.BuildingResponse, status_code=status.HTTP_201_CREATED)
def create_buildings(request: schemas.BuildingRequest, db: Session = Depends(get_db)):
    building = BuildingRepository.save(db,Building(**request.dict()) )
    return schemas.BuildingResponse.from_orm(building)

@app.get(BASE_PREFIX + '/buildings', response_model=List[schemas.BuildingResponse])
def find_all(db: Session = Depends(get_db)):
    buildings = BuildingRepository.find_all(db)
    return [schemas.BuildingResponse.from_orm(building) for building in buildings]

@app.get(BASE_PREFIX + '/buildings/{id}', response_model=schemas.BuildingResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    building = BuildingRepository.find_by_id(db, id)
    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Building not found"
        )
    return schemas.BuildingResponse.from_orm(building)

@app.get(BASE_PREFIX + "/buildings/owner/{id}", response_model=List[schemas.BuildingResponse])
def find_by_owner_id(id: int, db: Session = Depends(get_db)):
    print("here")
    buildings = BuildingRepository.find_by_owner_id(db, id)
    print("these are the buildings", buildings)
    if not buildings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This owner has no buildings"

        )
    return [schemas.BuildingResponse.from_orm(building) for building in buildings]

@app.get(BASE_PREFIX + "/buildings/cognito/{id}", response_model=List[schemas.BuildingResponse])
def find_by_cognito_id(id: str, db: Session = Depends(get_db)):
    print("here")
    buildings = BuildingRepository.find_by_cognito_id(db, id)
    print("these are the buildings", buildings)
    if not buildings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This owner has no buildings"
        )
    return [schemas.BuildingResponse.from_orm(building) for building in buildings]

@app.delete(BASE_PREFIX + "/buildings/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not BuildingRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Building not found"
        )
    BuildingRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put(BASE_PREFIX + "/buildings/{id}", response_model=schemas.BuildingResponse)
def update(id: int, request: schemas.BuildingRequest, db: Session = Depends(get_db)):
    if not BuildingRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Building not found"
        )
    building = BuildingRepository.save(db, Building(id=id,**request.dict()))
    return schemas.BuildingResponse.from_orm(building)  




############# DEVICE #############

@app.get(BASE_PREFIX + '/devices', response_model=schemas.DeviceResponse, status_code=status.HTTP_201_CREATED)
def create_devices(request: schemas.DeviceRequest, db: Session = Depends(get_db)):
    device = DeviceRepository.save(db,Device(**request.dict()) )
    return schemas.DeviceResponse.from_orm(device)

@app.get(BASE_PREFIX + '/devices', response_model=List[schemas.DeviceResponse])
def find_all(db: Session = Depends(get_db)):
    devices = DeviceRepository.find_all(db)
    return [schemas.DeviceResponse.from_orm(device) for device in devices]

@app.get(BASE_PREFIX + '/devices/{id}', response_model=schemas.DeviceResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    device = DeviceRepository.find_by_id(db, id)
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )
    return schemas.DeviceResponse.from_orm(device)

@app.get(BASE_PREFIX + "/devices/building/{id}", response_model=List[schemas.DeviceResponse])
def find_by_building_id(id: int, db: Session = Depends(get_db)):
    devices = DeviceRepository.find_by_building_id(db, id)
    if not devices:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This building has no devices"
        )
    return [schemas.DeviceResponse.from_orm(device) for device in devices]



@app.delete(BASE_PREFIX + "/devices/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not DeviceRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )
    DeviceRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put(BASE_PREFIX + "/devices/{id}", response_model=schemas.DeviceResponse)
def update(id: int, request: schemas.DeviceRequest, db: Session = Depends(get_db)):
    if not DeviceRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )
    device = DeviceRepository.save(db, Device(id=id,**request.dict()))
    return schemas.DeviceResponse.from_orm(device)  
    

############# INTRUSION #############

@app.get(BASE_PREFIX + '/intrusions', response_model=schemas.IntrusionResponse, status_code=status.HTTP_201_CREATED)
def create_intrusions(request: schemas.IntrusionRequest, db: Session = Depends(get_db)):
    intrusion = IntrusionRepository.save(db,Intrusion(**request.dict()) )
    return schemas.IntrusionResponse.from_orm(intrusion)

@app.get(BASE_PREFIX + '/intrusions', response_model=List[schemas.IntrusionResponse])
def find_all(db: Session = Depends(get_db)):
    intrusions = IntrusionRepository.find_all(db)
    return [schemas.IntrusionResponse.from_orm(intrusion) for intrusion in intrusions]

@app.get(BASE_PREFIX + '/intrusions/{id}', response_model=schemas.IntrusionResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    intrusion = IntrusionRepository.find_by_id(db, id)
    if not intrusion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Intrusion not found"
        )
    return schemas.IntrusionResponse.from_orm(intrusion)

@app.get(BASE_PREFIX + "/intrusions/device/{id}", response_model=List[schemas.IntrusionResponse])
def find_by_device_id(id: int, db: Session = Depends(get_db)):
    intrusions = IntrusionRepository.find_by_device_id(db, id)
    if not intrusions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This device has no intrusions"
        )
    return [schemas.IntrusionResponse.from_orm(intrusion) for intrusion in intrusions]

@app.get(BASE_PREFIX + "/intrusions/building/{id}", response_model=List[schemas.IntrusionResponse])
def find_by_building_id(id: int, db: Session = Depends(get_db)):
    intrusions = IntrusionRepository.find_by_building_id(db, id)
    if not intrusions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This building has no intrusions"
        )
    return [schemas.IntrusionResponse.from_orm(intrusion) for intrusion in intrusions]

@app.get(BASE_PREFIX + "/intrusions/owner/{id}", response_model=List[schemas.IntrusionResponse])
def find_by_owner_id(id: int, db: Session = Depends(get_db)):
    intrusions = IntrusionRepository.find_by_owner_id(db, id)
    if not intrusions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This owner has no intrusions"
        )
    return [schemas.IntrusionResponse.from_orm(intrusion) for intrusion in intrusions]


@app.delete(BASE_PREFIX + "/intrusions/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not IntrusionRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Intrusion not found"
        )
    IntrusionRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put(BASE_PREFIX + "/intrusions/{id}", response_model=schemas.IntrusionResponse)
def update(id: int, request: schemas.IntrusionRequest, db: Session = Depends(get_db)):
    if not IntrusionRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Intrusion not found"
        )
    intrusion = IntrusionRepository.save(db, Intrusion(id=id,**request.dict()))
    return schemas.IntrusionResponse.from_orm(intrusion)  

