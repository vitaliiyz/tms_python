from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Clients
from models import Products
from models import Orders

engine = create_engine('postgresql://root:12345@localhost:6666/my_database')
Session = sessionmaker(bind=engine)
session = Session()

new_product = Products(name="Football uniform", price=109.99, qty=11)
new_client = Clients(name="John Doe", birthday="1990-02-15", city="Warszawa")

session.add(new_product)
session.add(new_client)

session.add_all([new_product, new_client])
session.commit()

clients = session.query(Clients).all()

for client in clients:
    print(client.id, client.name, client.city)

print(session.query(Products).first().name)
print(session.query(Products).count())
print(f"Where: {session.query(Products.name).filter(Products.id == 2).all()}")
