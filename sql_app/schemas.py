from datetime import datetime, date
import enum
from typing import List
from enum import Enum
from fastapi import Security

from pydantic import BaseModel
from sqlalchemy import Date

from sql_app.models import Building, Camera, PropertyOwner, Sensor
from .enums import DeviceState, Notification_type


'''
 TO DO, IMPLEMENTAR CAMERAS E SENSORES
 '''


## PERSON

class PersonBase(BaseModel):
    email: str
    hashed_password: str
    id: int
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

## PROPERTY OWNER
class PropertyOwnerBase(PersonBase):
    contract_date: date 
    notification_type :Notification_type 
    building: str #help, sei que está mal
  
class PropertyOwnerRequest(PropertyOwnerBase):
    pass  

class PropertyOwnerResponse(PropertyOwnerBase):
    class Config:
        use_enum_values = True
        orm_mode = True
        
## BUILDINGS

class BuildingBase(BaseModel): 
    address:str
    building_id:int
    name: str
    client : PropertyOwnerBase
    cameras: List[CameraBase]
    sensors: List[SensorBase]

class BuildingRequest(BuildingBase):
    pass


class BuildingResponse(BuildingBase):
    class Config:
        orm_mode = True 




