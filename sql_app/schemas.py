from typing import List, Union

from pydantic import BaseModel


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
    property_owners: List[PropertyOwners] = []

    class Config:
        orm_mode = True


class SecurityManagerBase(BaseModel):
    worker_id: int
    #description: Union[str, None] = None


class SecurityManagerCreate(SecurityManagerBase):
    pass


class SecurityManager(SecurityManagerBase):
    id: int
    worker_id: int

    class Config:
        orm_mode = True