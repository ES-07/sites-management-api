from datetime import datetime, date
import enum
from typing import List
from enum import Enum
from fastapi import Security

from pydantic import BaseModel
from sqlalchemy import Date

from sql_app.models import PropertyOwner
from .enums import DeviceState, Notification_type


'''
 TO DO, IMPLEMENTAR CAMERAS E SENSORES
 '''


## PERSON

class PersonBase(BaseModel):
    email: str
    password: str
    id: int
    name: str
    address: str
    cellphone : int
    birthday: datetime = None

class PersonRequest(PersonBase):
    pass

class PersonResponse(PersonBase):
    id_number: int
    class Config:
        orm_mode = True




## PROPERTY OWNER
class PropertyOwnerBase(BaseModel):
    contract_date: date 
    notification_type :Notification_type 

  
class PropertyOwnerRequest(PropertyOwnerBase):
    pass  

class PropertyOwnerResponse(PropertyOwnerBase):
    property_owner_id: int
    class Config:
        use_enum_values = True
        orm_mode = True



## SECURITY MANAGER

class SecurityManagerBase(BaseModel):
    pass

class SecurityManagerRequest(SecurityManagerBase):
    pass

class SecurityManagerResponse(SecurityManagerBase):
    id_number: int
    class Config:
        orm_mode = True
   

## BUILDINGS

class BuildingBase(BaseModel): 
    address:str
    name: str
    client : int 
    #devices: List[Device]
    #nao sei como meter aqui a pessoa

class BuildingRequest(BuildingBase):
    pass

class BuildingResponse(BuildingBase):
    building_id: int
    class Config:
        orm_mode = True 