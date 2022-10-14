from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from .database import Base


class Person(Base):
    __tablename__ = "person"

    id_number = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    address = Column(String)
    cellphone = Column(Integer)
    birthday = Column(Date)

    property_owners = relationship("PropertyOwner", back_populates="person")
    security_managers = relationship("SecurityManager", back_populates="person")

#acho que bastava um enum para distinguir

class SecurityManager(Base):
    __tablename__ = "securitymanager"

    worker_id = Column(Integer, ForeignKey("person.id_number"), primary_key=True)
    person = relationship("Person", back_populates="security_managers")
    buildings =relationship("Building", back_populates="security_manager")

class PropertyOwner(Base):
    __tablename__ = "propertyowner"

    property_owner_id = Column(Integer, ForeignKey("person.id_number"), primary_key=True)
    contract_date = Column(Date)
    notification_style = Column(Enum)
    person = relationship("Person", back_populates="property_owners")
    buildings = relationship("Building", back_populates="owner")

class Building(Base):
    __tablename__ = "building"

    building_id = Column(Integer, primary_key=True)
    address = Column(String)
    security_manager_id = Column(Integer, ForeignKey("securitymanager.worker_id"))
    owner_id = Column(Integer, ForeignKey("propertyowner.property_owner_id"))
    security_manager =relationship("Building", back_populates="buildings")
    owner = relationship("PropertyOwner", back_populates="buildings")
    devices = relationship("Devices", back_populates="building")

class Device(Base):
    __tablename__ = "device"

    device_id = Column(Integer, primary_key=True)
    device_type = Column(Enum)
    state = Column(Enum)
    building_id = Column(Integer, ForeignKey("building.building_id"))
    building = relationship("Building", back_populates="devices")