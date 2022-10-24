from sqlalchemy.orm import Session
from .models import Building, Camera, SecurityManager, PropertyOwner, Sensor


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
'''

SECURITY MANAGER
def get_security_manager(db: Session, id: int):
    return db.query(models.SecurityManager).filter(models.SecurityManager.worker_id == id).first()

def get_security_managers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SecurityManager).offset(skip).limit(limit).all()


def create_security_manager(db: Session, securityManager: schemas.SecurityManagerSchema):
    fake_hashed_password = securityManager.password + "notreallyhashed"
    db_sec_manager = models.SecurityManager(email=securityManager.email, hashed_password=fake_hashed_password)
    db.add(db_sec_manager)
    db.commit()
    db.refresh(db_sec_manager)
    return db_sec_manager

# PROPERTY OWNER
def get_property_owner(db: Session, id: int):
    return db.query(models.PropertyOwner).filter(models.PropertyOwner.property_owner_id == id).first()



def create_property_owner(db: Session, securityManager: schemas.PropertyOwnerSchema):
    fake_hashed_password = securityManager.password + "notreallyhashed"
    db_owner = models.SecurityManager(email=securityManager.email, hashed_password=fake_hashed_password)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner



# PERSON (property owner + security manager)
def get_person_by_email(db: Session, email: str):
    return db.query(models.Person).filter(models.Person.email == email).first()


 '''
