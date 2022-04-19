from sqlalchemy import create_engine, Column, Text, Integer,BigInteger, ForeignKey, Date, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.sql import case
from datetime import datetime

engine = create_engine('sqlite:///mockblacklion.db') # my databse that will contain all the Tables belows(defined in class)
engine.connect()

Base = declarative_base()


class Doctors(Base): # defining Doctor table

    __tablename__ = "Doctors"

    doctor_id= Column(Integer,primary_key=True,unique=True)
    doctor_firstName=Column(Text,nullable=False)
    doctor_lastName=Column(Text,nullable=False)
    doctor_email=Column(Text,nullable=False)
    doctor_phoneNumber=Column(BigInteger,nullable=False)

    def __init__(self, doctor_firstName, doctor_lastName, doctor_email, doctor_phoneNumber):

        self.doctor_firstName = doctor_firstName
        self.doctor_lastName = doctor_lastName
        self.doctor_email = doctor_email
        self.doctor_phoneNumber = doctor_phoneNumber

        

class Patients(Base): # defining Patients table

    __tablename__ = "Patients"

    patient_id=Column(Integer,primary_key=True, unique=True)
    doctor_id = Column(Integer, ForeignKey('Doctors.doctor_id'))
    department_id = Column(Integer, ForeignKey('Departments.department_id'))
    patient_firstName=Column(String(25),nullable=False)
    patient_lastName=Column(String(25),nullable=False)
    patient_email=Column(String(80),nullable=False)
    patient_phoneNumber=Column(BigInteger,nullable=False)

    def __init__(self,doctor_id,department_id ,patient_firstName,patient_lastName, patient_email, patient_phoneNumber):
        self.doctor_id = doctor_id
        self.department_id = department_id
        self.patient_firstName = patient_firstName
        self.patient_lastName = patient_lastName
        self.patient_email = patient_email
        self.patient_phoneNumber = patient_phoneNumber



class Departments(Base): # defining Departments table

    __tablename__ = "Departments"
    department_id=Column(Integer,primary_key=True,unique=True)
    department_name=Column(String, nullable=False)
    department_total_bedrooms=Column(Integer,nullable=False)
    doctor_id = Column(Integer, ForeignKey('Doctors.doctor_id'))
    patient_id = Column(Integer, ForeignKey('Patients.patient_id'))


    def __init__(self, department_name, department_total_bedrooms,doctor_id, patient_id):
        self.department_name = department_name
        self.department_total_bedrooms = department_total_bedrooms
        self.doctor_id = doctor_id
        self.patient_id = patient_id




Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
