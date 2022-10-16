from sqlalchemy.orm import Session

from . import models, schemas


def get_person(db: Session, id_number: int):
    return db.query(models.Person).filter(models.Person.id_number == id_number).first()


def get_person_by_email(db: Session, email: str):
    return db.query(models.Person).filter(models.Person.email == email).first()


def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.PersonCreate):
    fake_hashed_password = person.password + "notreallyhashed"
    db_person = models.Person(email=person.email, hashed_password=fake_hashed_password)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

