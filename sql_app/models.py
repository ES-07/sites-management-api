from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum, Identity
from sqlalchemy.orm import relationship

from sql_app.enums import DeviceState, Notification_type
from .database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer,Identity(start=1, cycle=True), unique=True, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    address = Column(String)
    cellphone = Column(Integer)
    birthday = Column(Date)
    property_owners = relationship("PropertyOwner", back_populates="person")
    security_managers = relationship("SecurityManager", back_populates="person")


class SecurityManager(Person):
    __tablename__ = "securitymanager"

    worker_id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    person = relationship("Person", back_populates="security_managers")

class PropertyOwner(Person):
    __tablename__ = "propertyowner"

    property_owner_id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    contract_date = Column(Date)
    notification_type = Column(Enum(Notification_type, default=Notification_type.TXT_MSG))
    person = relationship("Person", back_populates="property_owners")
    buildings = relationship("Building", back_populates="owner")

class Building(Base):
    __tablename__ = "building"

    building_id = Column(Integer, primary_key=True)
    address = Column(String)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("propertyowner.property_owner_id"))
    owner = relationship("PropertyOwner", back_populates="buildings")
    cameras = relationship("Camera", back_populates="building")
    sensors = relationship("Sensor", back_populates="building")

class Camera(Base):
    __tablename__ = "camera"

    camera_id = Column(Integer, primary_key=True)
    specifications = Column(String)
    state = Column(Enum(DeviceState, default=DeviceState.OFF))
    building_id = Column(Integer, ForeignKey("building.building_id"))
    building = relationship("Building", back_populates="cameras")

class Sensor(Base):
    __tablename__ = "sensor"

    sensor_id = Column(Integer, primary_key=True)
    specifications = Column(String)
    state = Column(Enum(DeviceState, default=DeviceState.OFF))
    building_id = Column(Integer, ForeignKey("building.building_id"))
    building = relationship("Building", back_populates="sensors")