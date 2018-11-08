from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Product,Base,Employee,Customer


engine=create_engine("sqlite:///ziplines.db")
Base.metadata.bind=engine

Session=sessionmaker(bind=engine)

session=Session()

def create_product(pname,pprice,seller_name):

	product=Product(product_name=pname,product_price=pprice,seller_name=seller_name)

	session.add(product)
	session.commit()

def create_employee(ename,egender,edob,esalary,ephno):
	
	employee = Employee(employee_name=ename,employee_gender=egender,employee_dob=edob,employee_salary=esalary,employee_phno=ephno)

	session.add(employee)
	session.commit()

def create_customer(cname,cphno,caddress):

	customer = Customer(customer_name=cname,customer_phno=cphno,customer_address=caddress)

	session.add(customer)
	session.commit