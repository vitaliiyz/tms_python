import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)
    price = sa.Column(sa.NUMERIC(10, 2), nullable=False)
    qty = sa.Column(sa.Integer, nullable=False)


class Clients(Base):
    __tablename__ = 'clients'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)
    birthday = sa.Column(sa.Date, nullable=False)
    city = sa.Column(sa.Text, nullable=False)


class Orders(Base):
    __tablename__ = 'orders'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'), nullable=False)
    client_id = sa.Column(sa.Integer, sa.ForeignKey('clients.id'), nullable=False)
    qty = sa.Column(sa.Integer, nullable=False)
    amount = sa.Column(sa.NUMERIC(10, 2), nullable=False)
    order_date = sa.Column(sa.Date, nullable=False)


engine = create_engine('postgresql://root:12345@localhost:6666/my_database')
Base.metadata.create_all(engine)
