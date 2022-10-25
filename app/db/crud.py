from sqlalchemy.orm import Session
from models.models import Building, Device, SecurityManager, PropertyOwner, Intrusion


class SecurityManagerRepository:

    @staticmethod
    def find_all(db: Session):
        return db.query(SecurityManager).all()
    

    @staticmethod
    def save(db: Session, manager: SecurityManager):
        if manager.id:
            db.merge(manager)
        else:
            db.add(manager)
        db.commit()
        return manager

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(SecurityManager).filter(SecurityManager.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(SecurityManager).filter(SecurityManager.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        manager = db.query(SecurityManager).filter(SecurityManager.id == id).first()
        if manager is not None:
            db.delete(manager)
            db.commit()


class PropertyOwnerRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(PropertyOwner).all()
    

    @staticmethod
    def save(db: Session, owner: PropertyOwner):
        if owner.id:
            db.merge(owner)
        else:
            db.add(owner)
        db.commit()
        return owner

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(PropertyOwner).filter(PropertyOwner.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(PropertyOwner).filter(PropertyOwner.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        print("im here AAAAAAAAAAAAAAA")

        owner = db.query(PropertyOwner).filter(PropertyOwner.id == id).first()
        print("I have a owner", owner)
        if owner is not None:
            db.delete(owner)
            print("I passed", owner)
            db.commit()


class BuildingRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(Building).all()
    

    @staticmethod
    def save(db: Session, building: Building):
        if building.id:
            db.merge(building)
        else:
            db.add(building)
        db.commit()
        return building

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Building).filter(Building.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(Building).filter(Building.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        building = db.query(Building).filter(Building.id == id).first()
        if building is not None:
            db.delete(building)
            db.commit()


class DeviceRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(Device).all()
    

    @staticmethod
    def save(db: Session, device: Device):
        if device.id:
            db.merge(device)
        else:
            db.add(device)
        db.commit()
        return device

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Device).filter(Device.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(Device).filter(Device.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        device = db.query(Device).filter(Device.id == id).first()
        if device is not None:
            db.delete(device)
            db.commit()



class IntrusionRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(Intrusion).all()
    

    @staticmethod
    def save(db: Session, intrusion: Intrusion):
        if intrusion.id:
            db.merge(intrusion)
        else:
            db.add(intrusion)
        db.commit()
        return intrusion

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Intrusion).filter(Intrusion.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(Intrusion).filter(Intrusion.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        intrusion = db.query(Intrusion).filter(Intrusion.id == id).first()
        if intrusion is not None:
            db.delete(intrusion)
            db.commit()