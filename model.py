import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

Base=declarative_base()

class Product(Base):
	__tablename__='Products'

	product_id=Column(Integer,primary_key=True)
	product_name=Column(String(30),nullable=False)
	product_price=Column(Integer,nullable=False)
	seller_name=Column(String(30),nullable=False)

class Employee(Base):
	__tablename__='Employees'

	employee_id = Column(Integer,primary_key=True)
	employee_name = Column(String(1),nullable=False)
	employee_gender = Column(String(30),nullable=False)
	employee_dob = Column(String(10),nullable=False)
	employee_salary = Column(Integer,nullable=False)
	employee_phno = Column(Integer,nullable=False)

class Customer(Base):
	__tablename__ = 'Customers'

	customer_id = Column(Integer,primary_key=True)
	customer_name = Column(String(30),nullable=False)
	customer_phno = Column(Integer,nullable=False)
	customer_address = Column(String(100),nullable=False)

engine = create_engine("sqlite:///ziplines.db")
Base.metadata.create_all(engine)



