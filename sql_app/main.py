from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .models import SecurityManager, Person, PropertyOwner
from .database import engine, Base, get_db
from .crud import PropertyOwnerRepository, SecurityManagerRepository
from . import schemas
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.post("/owners", response_model=schemas.PropertyOwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owners(request: schemas.PropertyOwnerRequest, db: Session = Depends(get_db)):
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
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    owner = PropertyOwnerRepository.save(db, PropertyOwner(id=id, **request.dict()))
    return schemas.PropertyOwnerResponse.from_orm(owner)  


    
''' 
@app.get("/managers", response_model=List[schemas.SecurityManagerSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_security_managers(db, skip=skip, limit=limit)
    return users '''