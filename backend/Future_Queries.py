from Table_Skeleton import Doctors, Patients, Departments , engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Index
from sqlalchemy import func, extract, insert

Session = sessionmaker(bind=engine)

session  = Session()




