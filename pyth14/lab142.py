import lab14
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, Session
engine = create_engine("sqlite:///sqlite3.db")
session = Session(bind=engine)
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



class Super():

    def __str__(product,color):
        return '\t'+str(product.id)+')'+product.name.title()+', цвет - '+color.color+', цена - '+str(product.price)+', в наличии - '+product.have

    def __repr__(color):
        return '\t'+color.color+' -> '+str(len(color.products))

    def add_product():
        name = input("Название товара: ")
        price = input("Стоимость товара: ")

        types = session.query(lab14.Type).all()
        all_types = []
        while True:
            print("Выберите тип товара:")
            for type in types:
                print(f"\t{type.id}){type.type}")
            type_id = input("")
            all_types.append(type_id)
            print("""
        1)Выбрать ещё один тип\t
        2)Выбрать цвет""")
            inp = input('Выбор действия: ')
            if inp == '1':
                continue
            else:
                break

        colors = session.query(lab14.Color).all()
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

        colors = session.query(lab14.Color).filter(lab14.Color.id == color_id)
        assert colors.count(), f"Цвет с ID:<{color_id}> не найден"
        color = colors.first()



        id = session.query(lab14.Product).filter(lab14.Product.name == name).first()
        if id == None:
            id = 1
        else:
            id += id.id + 1
        new_product = lab14.Product(
            name=name,
            price=price,
            have=have,
            color_id=color
        )

        color.products.append(new_product)

        for type_id in all_types:
            types = session.query(lab14.Type).filter(lab14.Type.id == type_id)
            assert types.count(), f"Тип с ID:<{type_id}> не найден"
            type = types.first()
            new_type = lab14.Association_table(products_id=id, types_id=type_id)
            type.products.append(new_type)

        session.add(new_product)
        session.commit()

    def add_color():
        color = input("Название цвета: ")
        id = session.query(lab14.Color).count()
        new_color = lab14.Color(id=id+1, color=color)
        session.add(new_color)
        session.commit()

    def add_type():
        type = input("Вид товара: ")
        id = session.query(lab14.Type).count()
        new_type = lab14.Type(id=id+1, type=type)
        session.add(new_type)
        session.commit()

    def output_product():
        products=session.query(lab14.Product).all()
        print("Все товары:")
        for product in products:
            color = session.query(lab14.Color).filter(lab14.Color.id == product.color_id).first()
            print(Super.__str__(product,color))

    def output_colors():
        colors = session.query(lab14.Color).all()
        print("Все цвета (цвет -> кол-во товаров):")
        for color in colors:
            print(Super.__repr__(color))

class Main():
    def __init__(self):
        if session.query(lab14.Color).count() == 0:
            colors = ['красный', 'синий', 'зелёный', 'жёлтый', 'белый', 'чёрный', 'серый', 'розовый']
            id = 1
            while id<=8:
                new_color = lab14.Color(id=id, color=colors[id-1])
                session.add(new_color)
                id+=1
            session.commit()

        if session.query(lab14.Type).count() == 0:
            types = ['техника', 'бытовая техника', 'посуда', 'провизия', 'оружие', 'люди', 'мебель', 'инструменты']
            id = 1
            while id<=8:
                new_type = lab14.Type(id=id, type=types[id-1])
                session.add(new_type)
                id+=1
            session.commit()
        while True:
            inp = input("Выбор действия:")
            if inp == "1":
                a = Super.add_product()
            elif inp == "2":
                a = Super.add_color()
            elif inp == "3":
                a = Super.add_type()
            elif inp == "4":
                a = Super.output_product()
            elif inp == "5":
                a = Super.output_colors()

a = Main()
