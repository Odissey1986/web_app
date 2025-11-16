from database.db import Base, Sessionlocal, engine
from models.orders import Order
from models.products import Product


def init_database():
    Base.metadata.drop_all(bind=engine) # Удалить все таблички базы из данных
    Base.metadata.create_all(bind=engine) # Создать все таблички в базе данных

    session = Sessionlocal()

    pl = Product(name = "Молоко 1л", price=85, count=15)
    session.add(pl)

    lst = [
        Product(name = "Хлеб", price=25, count=5),
        Product(name = "Гречка", price=85, count=56),
        Product(name = "Сахар 1кг", price=60, count=15)
    ]

    lst2 = [
        Order(customer_name="Петя", 
              phone_number="89991112233", 
              product_id=1, 
              count=5),

        Order(customer_name="Вася", 
              phone_number="89995556677", 
              product_id=2, 
              count=3),

        Order(customer_name="Костя", 
              phone_number="89998001918", 
              product_id=3, 
              count=6)
    ]

    session.add_all(lst)
    session.commit()

    session.close()

if __name__ == "__main__":
    init_database()