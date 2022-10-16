import datetime
import enum
from typing import List
from enum import Enum

from pydantic import BaseModel
from sqlalchemy import Date
from .enums import DeviceType, DeviceState, NotificationType

## ENUMS



## DEVICE

class DeviceBase(BaseModel):
    device_id: int


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    device_type: DeviceType
    state: DeviceState
    
    #nao sei como meter aqui a pessoa

    class Config:
        orm_mode = True

## BUILDINGS

class BuildingBase(BaseModel):
    building_id: int


class BuildingCreate(BuildingBase):
    pass


class Building(BuildingBase):
    address:str
    devices: List[Device]
    #nao sei como meter aqui a pessoa

    class Config:
        orm_mode = True

## SECURITY MANAGER


class SecurityManagerBase(BaseModel):
    worker_id: int


class SecurityManagerCreate(SecurityManagerBase):
    pass


class SecurityManager(SecurityManagerBase):
    worker_id: int
    buildings: List[Building] = []
    #nao sei como meter aqui a pessoa

    class Config:
        orm_mode = True

## PROPERTY OWNER


class PropertyOwnerBase(BaseModel):
    propery_owner_id: int


class PropertyOwnerCreate(SecurityManagerBase):
    pass


class PropertyOwner(SecurityManagerBase):
    property_owner_id: int
    contract_date: datetime.date
    notification_type :NotificationType 
    buildings: List[Building] = []
    #nao sei como meter aqui a pessoa

    class Config:
        orm_mode = True


## PERSON

class PersonBase(BaseModel):
    name: str
    email: str
    address: str
    cellphone : int
    #é suposto meter aqui a data de nascimento?


class PersonCreate(PersonBase):
    password: str

class Person(PersonBase):
    id: int
    security_managers: List[SecurityManager] = []
    property_owners: List[PropertyOwner] = []

    class Config:
        orm_mode = True


