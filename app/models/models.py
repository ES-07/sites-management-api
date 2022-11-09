from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum, Identity
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.models.enums import DeviceState, DeviceType, Notification_type
from app.db.database import Base


class Person(Base):
    __tablename__ = "person"

    id =  Column(Integer,Identity(start=1, cycle=True), unique=True, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    address = Column(String)
    cellphone = Column(Integer)
    birthday = Column(Date)
    property_owners = relationship("PropertyOwner", back_populates="person", cascade="delete, merge, save-update",passive_deletes=True)
    security_managers = relationship("SecurityManager", back_populates="person", cascade="delete, merge, save-update", passive_deletes=True)


class SecurityManager(Person):
    __tablename__ = "securitymanager"

    worker_id = Column(Integer, ForeignKey("person.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    person = relationship("Person", back_populates="security_managers")

class PropertyOwner(Person):
    __tablename__ = "propertyowner"

    property_owner_id = Column(Integer, ForeignKey("person.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    contract_date = Column(Date)
    notification_type = Column(Enum(Notification_type, default=Notification_type.TXT_MSG))
    person = relationship("Person", back_populates="property_owners")
    buildings = relationship("Building", back_populates="owner")

class Building(Base):
    __tablename__ = "building"

    id = Column(Integer, primary_key=True, nullable=False)
    address = Column(String)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("propertyowner.property_owner_id",  onupdate="CASCADE", ondelete="CASCADE"))
    owner = relationship("PropertyOwner", back_populates="buildings", cascade="delete, merge, save-update")
    devices = relationship("Device", back_populates="building", cascade="delete, merge, save-update")
    intrusions = relationship("Intrusion", back_populates="building", cascade="delete, merge, save-update")


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True, nullable=False)
    specifications = Column(String)
    state = Column(Enum(DeviceState, default=DeviceState.OFF))
    type = Column(Enum(DeviceType))
    building_id = Column(Integer, ForeignKey("building.id", onupdate="CASCADE", ondelete="CASCADE"))
    building = relationship("Building", back_populates="devices")

class Intrusion(Base):
    __tablename__ = "intrusion"

    id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(Date)
    building_id = Column(Integer, ForeignKey("building.id", onupdate="CASCADE", ondelete="CASCADE"))
    device_id = Column(Integer, ForeignKey("device.id", onupdate="CASCADE", ondelete="CASCADE"))
    building = relationship("Building", back_populates="intrusions")