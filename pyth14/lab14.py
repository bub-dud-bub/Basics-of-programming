from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, CheckConstraint, select
from sqlalchemy.orm import relationship, backref, Session
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
Base = declarative_base()
engine = create_engine("sqlite:///sqlite3.db")
session = Session(bind=engine)
association_table = Table(
    "association_table", Base.metadata,
    Column("products_id", Integer(), ForeignKey("products.id")),
    Column("types_id", Integer(), ForeignKey("types.id")),
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
    types = relationship("Type", secondary=association_table, backref=backref("products"))


class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String())



Base.metadata.create_all(bind=engine)

print(
    """
Выберите действие:
    1. Добавить товар в БД
    2. Добавить цвет
    3. Добавить вид товара
    4. Вывести список всех товаров
    5. Вывести список всех цветов
"""
)
id = 0
while True:
    inp = input("Выбор действия:")
    if inp == "1":
        name = input("Название товара: ")
        price = input("Стоимость товара: ")

        types = session.query(Type).all()
        print("Выберите тип товара:")
        for type in types:
            print(f"\t{type.id}){type.type}")
        types_id = input("")

        colors = session.query(Color).all()
        print("Выберите цвет товара:")
        for color in colors:
            print(f"\t{color.id}){color.color}")
        color_id = input("")
        while True:
            have = int(input("\nНаличие товара(1 - Присутствует, 0 - Отсутствует):"))
            if have == 1 or have == 0: break
        if have == 1:
            have = 'Присутствует'
        else:
            have = 'Отсутствует'

        colors = session.query(Color).filter(Color.id == color_id)
        assert colors.count(), f"Цвет с ID:<{color_id}> не найден"
        color = colors.first()

        new_product = Product(
            name=name,
            price=price,
            have=have,
            color_id=color
        )

        color.products.append(new_product)


        session.add(new_product)
        session.commit()
    elif inp == "2":
        colors = ['красный', 'синий', 'зелёный', 'жёлтый', 'белый', 'чёрный', 'серый', 'розовый']
        while True:
            print("Выберите цвет:")
            for i in range(0, len(colors)):
                print((i+1),colors[i])
            color_id = int(input(""))
            if color_id > 0 and color_id < 9:
                color = colors[color_id-1]
                break
        new_color = Color(color=color)
        session.add(new_color)
        session.commit()

    elif inp == "3":
        type = input("Вид товара: ")
        new_type = Type(type=type)
        session.add(new_type)
        session.commit()

    elif inp == "4":
        products = session.query(Product).all()
        print("Все дисциплины:")
        for product in products:
            color = session.query(Color).filter(Color.id == product.color_id).first()
            print(f"\t{product.id}) {product.name.title()} ({color.color}): цена - {product.price}, в наличии - {product.have}")

    elif inp == "5":
        colors = session.query(Color).all()
        print("Все цвета (цвет -> кол-во товаров):")
        for color in colors:
            print(f"\t{color.color} -> {len(color.products)}")
