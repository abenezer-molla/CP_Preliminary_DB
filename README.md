# CP_Preliminary_DB

Steps to run this program:

MacOS >

Requirements

- inside backend directory - pipenv install sqlalchemy
- python_version = "3.9"

Steps:

1.  Open terminal (if you are using Visual Studuo Code, the keyboard shortcut will be "ctrl~")
2.  change directory to CP_Preliminary_DB(if it is not opened in this directory already) - type > cd backend
3.  change directory to backend folder - type > cd backend

- here - pipenv install sqlalchemy

4.  initilize virtual environment - type > pipenv shell
5.  run the Table_Skeleton.py file - type > python Table_Skeleton.py
6.  run the Data_Insertion.py file - type > python Data_Insertion.py

Tables

- Doctors
  Columns

  - doctor_id (int) - PRIMARY KEY
  - doctor_firstName (string)
  - doctor_lastName (string)
  - doctor_email (string)
  - doctor_phoneNumber (big_int)

- Patients
  Columns

  - patient_id(int) - PRIMARY KEY
  - doctor_id(string) - ForeignKey('Doctors.doctor_id')
  - department_id - ForeignKey('Departments.department_id')
  - patient_firstName(string)
  - patient_lastName(string)
  - patient_email(string)
  - patient_phoneNumber(big_int)

- Departments
  Columns

  - department_id(int) - PRIMARY KEY
  - department_name(string)
  - department_total_bedrooms
  - doctor_id - ForeignKey('Doctors.doctor_id')
  - patient_id - ForeignKey('Patients.patient_id')
  
Areas to expand on this one will be-->

DB for authentication(I think) should be together with this one instead of it being separate. 


####

Optional cool features to explore if you are opening this with VS Code:-

VS Code has a SQLite Explorer that you can install by following simple steps -

- click on the "Extentions" button on the left side of VSCode
- search "SQLite"
- click install
- Now, right-click on the db (mockblacklion.db), then click "open database."
- Now you should be seeing your database apearing at the bottom lefthand corner(under SQLITE EXPLORER)
- there, you can click on each table listed within the db, and you will be able to view a beautiful table.
