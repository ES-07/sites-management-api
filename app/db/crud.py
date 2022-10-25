from sqlalchemy.orm import Session
from models.models import Building, Camera, SecurityManager, PropertyOwner, Sensor, Intrusion


class SecurityManagerRepository:

    @staticmethod
    def find_all(db: Session):
        return db.query(SecurityManager).all()
    

    @staticmethod
    def save(db: Session, manager: SecurityManager):
        print("Im saving")
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
        print("im here AAAAAAAAAAAAAAA")
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
        if building.building_id:
            db.merge(building)
        else:
            db.add(building)
        db.commit()
        return building

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Building).filter(Building.building_id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(Building).filter(Building.building_id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        building = db.query(Building).filter(Building.building_id == id).first()
        if building is not None:
            db.delete(building)
            db.commit()


class CameraRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(Camera).all()
    

    @staticmethod
    def save(db: Session, camera: Camera):
        if camera.camera_id:
            db.merge(camera)
        else:
            db.add(camera)
        db.commit()
        return camera

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Camera).filter(Camera.camera_id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(Camera).filter(Camera.camera_id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        camera = db.query(Camera).filter(Camera.camera_id == id).first()
        if camera is not None:
            db.delete(camera)
            db.commit()


class SensorRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(Sensor).all()
    

    @staticmethod
    def save(db: Session, sensor: Sensor):
        if sensor.id:
            db.merge(sensor)
        else:
            db.add(sensor)
        db.commit()
        return sensor

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Sensor).filter(Sensor.sensor_id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(Sensor).filter(Sensor.sensor_id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        sensor = db.query(Sensor).filter(Sensor.sensor_id == id).first()
        if sensor is not None:
            db.delete(sensor)
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