from sqlalchemy.orm import Session
from .models import SecurityManager, PropertyOwner


class SecurityManagerRepository:

    @staticmethod
    def find_all(db: Session):
        return db.query(SecurityManager).all()
    

    @staticmethod
    def save(db: Session, manager: SecurityManager):
        if manager.id_number:
            db.merge(manager)
        else:
            db.add(manager)
        db.commit()
        return manager

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(SecurityManager).filter(SecurityManager.id_number == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(SecurityManager).filter(SecurityManager.id_number == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        manager = db.query(SecurityManager).filter(SecurityManager.id_number == id).first()
        if manager is not None:
            db.delete(manager)
            db.commit()


class PropertyOwnerRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(PropertyOwner).all()
    

    @staticmethod
    def save(db: Session, owner: PropertyOwner):
        if owner.id_number:
            db.merge(owner)
        else:
            db.add(owner)
        db.commit()
        return owner

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(PropertyOwner).filter(PropertyOwner.id_number == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int):
        return db.query(PropertyOwner).filter(PropertyOwner.id_number == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int):
        owner = db.query(PropertyOwner).filter(PropertyOwner.id_number == id).first()
        if owner is not None:
            db.delete(owner)
            db.commit()


'''

SECURITY MANAGER
def get_security_manager(db: Session, id_number: int):
    return db.query(models.SecurityManager).filter(models.SecurityManager.worker_id == id_number).first()

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
def get_property_owner(db: Session, id_number: int):
    return db.query(models.PropertyOwner).filter(models.PropertyOwner.property_owner_id == id_number).first()



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
