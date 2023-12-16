from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, CheckConstraint, select
from sqlalchemy.orm import relationship, backref, Session
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
Base = declarative_base()
engine = create_engine("sqlite:///sqlite3.db")
session = Session(bind=engine)


#class Association_table(Base):
 #   __tablename__ = "association_table"

 #   products_id = Column(Integer(), primary_key=True, autoincrement=True, ForeignKey("products.id"))
#    types_id = Column(Integer(), primary_key=True, autoincrement=True, ForeignKey("types.id"))
association_table = Table(
    "association_table", Base.metadata,
    Column("products_id", Integer(), ForeignKey("products.id")),
    Column("types_id", Integer(), ForeignKey("types.id"))
 )
class Color(Base):
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    color = Column(String())

    products = relationship("Product")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    price = Column(Integer())
    have = Column(Integer())

    color_id = Column(Integer(), ForeignKey('colors.id'))
    types = relationship("Type", secondary=association_table, backref='products')


class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String())

    #products = relationship("Product", secondary=association_table, back_populates='type')






Base.metadata.create_all(bind=engine)


# id = 0

#
# if session.query(Color).count() == 0:
#     colors = ['красный', 'синий', 'зелёный', 'жёлтый', 'белый', 'чёрный', 'серый', 'розовый']
#     id = 1
#     while id<=8:
#         new_color = Color(id=id, color=colors[id-1])
#         session.add(new_color)
#         id+=1
#     session.commit()
#
# if session.query(Type).count() == 0:
#     types = ['техника', 'бытовая техника', 'посуда', 'провизия', 'оружие', 'люди', 'мебель', 'инструменты']
#     id = 1
#     while id<=8:
#         new_type = Type(id=id, type=types[id-1])
#         session.add(new_type)
#         id+=1
#     session.commit()

#Это через str и repr:
# while True:
#     inp = input("Выбор действия:")
#     if inp == "1":
#         name = input("Название товара: ")
#         price = input("Стоимость товара: ")
#
#         types = session.query(Type).all()
#         print("Выберите тип товара:")
#         for type in types:
#             print(f"\t{type.id}){type.type}")
#         type_id = input("")
#
#         colors = session.query(Color).all()
#         print("Выберите цвет товара:")
#         for color in colors:
#             print(f"\t{color.id}){color.color}")
#         color_id = input("")
#         while True:
#             have = int(input("\nНаличие товара(1 - Присутствует, 0 - Отсутствует):"))
#             if have == 1 or have == 0: break
#         if have == 1:
#             have = 'Присутствует'
#         else:
#             have = 'Отсутствует'
#
#         colors = session.query(Color).filter(Color.id == color_id)
#         assert colors.count(), f"Цвет с ID:<{color_id}> не найден"
#         color = colors.first()
#
#         types = session.query(Type).filter(Type.id == type_id)
#         assert types.count(), f"Тип с ID:<{type_id}> не найден"
#         type = types.first()
#
#         new_product = Product(
#             name=name,
#             price=price,
#             type_id=type.id,
#             have=have,
#             color_id=color,
#         )
#
#         color.products.append(new_product)
#
#
#         session.add(new_product)
#         session.commit()
#     elif inp == "2":
#         color = input("Название цвета: ")
#         id = session.query(Color).count()
#         new_color = Color(id=id+1, color=color)
#         session.add(new_color)
#         session.commit()
#
#     elif inp == "3":
#         type = input("Вид товара: ")
#         id = session.query(Type).count()
#         new_type = Type(id=id+1, type=type)
#         session.add(new_type)
#         session.commit()
#
#     elif inp == "4":
#         products = session.query(Product).all()
#         print("Все товары:")
#         for product in products:
#             type = session.query(Type).filter(Type.id == product.type_id).first()
#             color = session.query(Color).filter(Color.id == product.color_id).first()
#             print(f"\t{product.id}) {product.name.title()}, тип - {type.type}, цвет - {color.color}, цена - {product.price}, в наличии - {product.have}")
#
#     elif inp == "5":
#         colors = session.query(Color).all()
#         print("Все цвета (цвет -> кол-во товаров):")
#         for color in colors:
#             print(f"\t{color.color} -> {len(color.products)}")
