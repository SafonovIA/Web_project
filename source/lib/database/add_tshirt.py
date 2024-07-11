from models import *
from faker import Faker
import random
from datetime import datetime
from sqlalchemy import func
faker = Faker('ru_RU')


def generate_fake_users(count=20):
    try:
        for _ in range(count):
            user = User(
                first_name=faker.first_name(),
                second_name=faker.last_name(),
                phone_number=faker.random_number(digits=9),
                city=faker.city(),
                created_at=faker.date_time_this_decade(),
                deleted_at=None
            )

            db.session.add(user)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()

def generate_fake_users_adress(count=20):
    try:
        for _ in range(count):
            user_adress = User_adress(
                adress = faker.address(),
                city = faker.city(),
                postal_code = faker.postal_code(),
                country = faker.country()
            )

            db.session.add(user_adress)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()

def generate_fake_reviews(count=100):
    try:
        for _ in range(count):
            review = Review(
                rating = random.randint(0, 5),
                review = faker.text(),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
            )
            
            random_product_type = random.choice(['t_shirts', 'sweatwears', 'outwears', 'shoes', 'trousers',
                                                 'socks', 'accessories'])
            product = None

            if random_product_type == 'tshirts':
                product = Tshirt.query.order_by(func.random()).first()
                if product:
                    review.t_shirts.append(product)
            elif random_product_type == 'sweatwears':
                product = Sweatwear.query.order_by(func.random()).first()
                if product:
                    review.sweatwears.append(product)
            elif random_product_type == 'outwears':
                product = Outwear.query.order_by(func.random()).first()
                if product:
                    review.outwears.append(product)
            elif random_product_type == 'shoes':
                product = Shoes.query.order_by(func.random()).first()
                if product:
                    review.shoes.append(product)
            elif random_product_type == 'trousers':
                product = Shoes.query.order_by(func.random()).first()
                if product:
                    review.shoes.append(product)
            elif random_product_type == 'accessories':
                product = Shoes.query.order_by(func.random()).first()
                if product:
                    review.shoes.append(product)
            elif random_product_type == 'socks':
                product = Shoes.query.order_by(func.random()).first()
                if product:
                    review.shoes.append(product)
        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()

def generate_fake_tshirt(count=20):
    try:
        for _ in range(count):
            tshirt = Tshirt(
                type_item = 'Футболка',
                picture = 'https://ir.ozone.ru/s3/multimedia-1-x/wc1000/7047582153.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
            )

            db.session.add(tshirt)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
        
def generate_fake_sweatwear(count=20):
    try:
        for _ in range(count):
            sweatwear = Sweatwear(
                type_item = 'Кофта',
                picture = 'https://ir.ozone.ru/s3/multimedia-1-q/wc1000/6914683250.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
                )

            db.session.add(sweatwear)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
        
def generate_fake_outwear(count=20):
    try:
        for _ in range(count):
            outwear = Outwear(
                type_item = 'Куртка',
                picture = 'https://ir.ozone.ru/s3/multimedia-m/wc1000/6439177342.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
                )

            db.session.add(outwear)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
    
def generate_fake_shoes(count=20):
    try:
        for _ in range(count):
            shoes = Shoes(
                type_item = 'Обувь',
                picture = 'https://ir.ozone.ru/s3/multimedia-t/wc1000/6697340237.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
                )

            db.session.add(shoes)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
        
def generate_fake_trousers(count=20):
    try:
        for _ in range(count):
            trousers = Trousers(
                type_item = 'Штаны',
                picture = 'https://ir-1.ozone.ru/s3/multimedia-z/wc1000/6844054211.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
                )

            db.session.add(trousers)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
        
def generate_fake_accessories(count=20):
    try:
        for _ in range(count):
            accessories = Accessories(
                type_item = 'Аксессуары',
                picture = 'https://ir.ozone.ru/s3/multimedia-1-l/wc1000/7002698637.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
                )

            db.session.add(accessories)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
       
def generate_fake_socks(count=20):
    try:
        for _ in range(count):
            socks = Socks(
                type_item = 'Носки',
                picture = 'https://ir.ozone.ru/s3/multimedia-1-l/wc1000/7002698637.jpg',
                brand = faker.company(),
                gender = faker.random_element(elements=('мужской', 'женский', 'детский')),
                size = faker.random_element(elements=('S', 'M', 'L', 'XL')),
                material = faker.random_element(elements=('хлопок', 'лен', 'кожа', 'синтетика')),
                description = faker.text(),
                price = random.uniform(1000.00, 9000.00),
                discount = random.randint(0, 30),
                amount = faker.random_int(min=1, max=100),
                created_at = faker.date_time_this_decade(),
                modified_at = None,
                deleted_at = None
                )

            db.session.add(socks)

        db.session.commit()

    except Exception as e:
        db.session.rollback()

    finally:
        db.session.close()
        
def generate_fake_data():
        generate_fake_users()
        generate_fake_users_adress()
        generate_fake_reviews()
        generate_fake_tshirt()
        generate_fake_sweatwear()
        generate_fake_outwear()
        generate_fake_shoes()
        generate_fake_trousers()
        generate_fake_accessories()
        generate_fake_socks()
        
if __name__ == '__main__':
        
    with app.app_context():
        generate_fake_data()