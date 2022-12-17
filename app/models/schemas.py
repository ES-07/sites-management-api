from datetime import datetime, date
import enum
from typing import List, Optional, Union
from enum import Enum
from uuid import UUID
from fastapi import Security
from uuid import UUID
from psycopg2 import Timestamp

from pydantic import BaseModel, Field
from sqlalchemy import Date
from datetime import datetime, timezone

from models.enums import DeviceState, DeviceType, Notification_type



# Class for healthcheck of the API
class HealthResponse(BaseModel):
    status: str


## PERSON

class PersonBase(BaseModel):
    email: str
    hashed_password: str
    name: str
    address: str
    cellphone : str
    birthday: date 
    cognito_id: str

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
    id:int
    class Config:
        orm_mode = True


## DEVICE
class DeviceBase(BaseModel): 
    specifications: str
    state: DeviceState
    type: DeviceType
    building_id: int

class DeviceRequest(DeviceBase):
    pass

class DeviceResponse(DeviceBase):
    id:int  
    class Config:
        orm_mode = True

## BUILDING

class BuildingBase(BaseModel): 
    address:str
    name: str
    owner_id : int
    devices: List[DeviceResponse] = []

class BuildingRequest(BuildingBase):
    pass

class BuildingResponse(BuildingBase):
    id:int
    class Config:
        orm_mode = True 


## PROPERTY OWNER
class PropertyOwnerBase(PersonBase):
    
  pass
class PropertyOwnerRequest(PropertyOwnerBase):
    pass  

class PropertyOwnerResponse(PropertyOwnerBase):

    buildings: List[BuildingResponse]=[]  #help, maybe está mal
    contract_date: Optional[date]
    id:int
    notification_type : Union[Notification_type, None]= Field(default=None, example=Notification_type.TXT_MSG)

    class Config:
        use_enum_values = True
        orm_mode = True

        
## INTRUSION

class IntrusionBase(BaseModel):
    timestamp: str  
    building_id: int
    device_id: int

class IntrusionRequest(IntrusionBase):
    pass

class IntrusionResponse(IntrusionBase):
    id:int
    class Config:
        orm_mode = True