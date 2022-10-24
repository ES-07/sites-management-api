from datetime import datetime, date
import enum
from typing import List
from enum import Enum
from uuid import UUID
from fastapi import Security
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import Date

from models.models import Building, Camera, PropertyOwner, Sensor
from models.enums import DeviceState, Notification_type



# Class for healthcheck of the API
class HealthResponse(BaseModel):
    status: str


## PERSON

class PersonBase(BaseModel):
    email: str
    hashed_password: str
    id: UUID
    name: str
    address: str
    cellphone : int
    birthday: date 

class PersonRequest(PersonBase):
    pass

class PersonResponse(PersonBase):
    id: int
    class Config:
        orm_mode = True


## SECURITY MANAGER

class SecurityManagerBase(PersonBase):
    pass

class SecurityManagerRequest(SecurityManagerBase):
    pass

class SecurityManagerResponse(SecurityManagerBase):
    class Config:
        orm_mode = True


class CameraBase(BaseModel): 
    specifications: str
    state: DeviceState
    building_id: int

class CameraRequest(CameraBase):
    pass

class CameraResponse(CameraBase):
    camera_id:int  

    class Config:
        orm_mode = True



class SensorBase(BaseModel):
    specifications: str
    state: DeviceState
    building_id: int

class SensorRequest(SensorBase):
    pass

class SensorResponse(SensorBase):
    sensor_id:int

    class Config:
        orm_mode = True
        use_enum_values = True

class BuildingBase(BaseModel): 
    address:str
    building_id:int
    name: str
    owner_id : int
    cameras: List[CameraResponse] = []
    sensors: List[SensorResponse] = []


class BuildingResponse(BuildingBase):
    class Config:
        orm_mode = True 

## PROPERTY OWNER
class PropertyOwnerBase(PersonBase):
    contract_date: date 
    notification_type :Notification_type 
    buildings: List[BuildingResponse]=[]  #help, sei que está mal
  
class PropertyOwnerRequest(PropertyOwnerBase):
    pass  

class PropertyOwnerResponse(PropertyOwnerBase):
    class Config:
        use_enum_values = True
        orm_mode = True
        
## BUILDINGS


class BuildingRequest(BuildingBase):
    pass


class IntrusionBase(BaseModel):
    notes: str
    timestamp: datetime
    building_id: int

class IntrusionRequest(IntrusionBase):
    pass

class IntrusionResponse(IntrusionBase):
    intrusion_id:int

    class Config:
        orm_mode = True




