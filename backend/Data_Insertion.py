from Table_Skeleton import Doctors, Patients, Departments , engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from datetime import datetime



Session = sessionmaker(bind=engine)  #binding the engine to make sure that we are adding data to the same DB we created in Table_Skeleton.py

session = Session() # initializing session

#Doctors class will recieve the data in the following format :-
#Doctors(doctor_firstName, doctor_lastName, doctor_email, doctor_phoneNumber)

doctor1 = Doctors('Abenezer', 'Molla','abenmolla@gmail.com', 4153778679) 
doctor2 = Doctors('Mark', 'Eric','markeric@gmail.com', 4156789086)
doctor3 = Doctors('Philip', 'Boaz','philipboaz@gmail.com', 4155678947)
doctor4 = Doctors('Ahmed', 'Khalid','ahmedk@gmail.com', 4155679302)
doctor5 = Doctors('Suzan', 'Tefera','suzant@gmail.com', 4159038809)
doctor6 = Doctors('Lily', 'Ademe','lilyademe@gmail.com', 41530981837)


# The 6 lines of code below will add the doctor instance created above into Doctors table

session.add(doctor1) 
session.add(doctor2)
session.add(doctor3)
session.add(doctor4)
session.add(doctor5)
session.add(doctor6)


######

#Patients class will recieve the data in the following format :-
#Patients(doctor_id, department_id, patient_firstName, patient_lastName, patient_email, patient_phoneNumber)

patient1 = Patients(3, 1, 'Mister1', 'Nakachew','mister1@gmail.com', 2136789503)
patient2 = Patients(17,2, 'Mister2', 'Teferi','mister2@gmail.com', 2136784098)
patient3 = Patients(46, 3, 'Mister3', 'Berihun','mister3@gmail.com', 2130928659)
patient4 = Patients(38, 4,'Mister4' ,'Firew', 'mister4@gmail.com', 2138030027)
patient5 = Patients(19, 4, 'Mister5', 'Adamu','mister5@gmail.com', 2130289170)
patient6 = Patients(80, 2,'Mister6', 'Yosef','mister6@gmail.com', 2137048372)

# The 6 lines of code below will add the patient instance created above into Patients table

session.add(patient1)
session.add(patient2)
session.add(patient3)
session.add(patient4)
session.add(patient5)
session.add(patient6)


#####

# Departments class will recieve the data in the following format :-
#Departments(department_total_bedrooms,department_total_bedrooms,doctor_id, patient_id)

department1 = Departments('Pediatrics', 45, 3, 87)
department2 = Departments('Gynecology and Obstetrics', 63, 17, 24)
department3 = Departments('Chronic Illness', 24, 46, 19)
department4 = Departments('Emergency Room', 29, 38, 51)


# The 6 lines of code below will add the department instances created above into Departments table

session.add(department1)
session.add(department2)
session.add(department3)
session.add(department4)


session.commit()




