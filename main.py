import configparser, sqlalchemy, json, os, psycopg2
from sqlalchemy.orm import sessionmaker
from model import Publisher, Book, Shop, Stock, Sale, tables_create

# Подключаем configparser
configpath = "confdb.conf"
config = configparser.ConfigParser()
config.read(configpath)

# Читаем параметры подключеия к базе из файла конфигурации
namedb = config["POSTGRESQL"]["NAME"]
userdb = config["POSTGRESQL"]["USER"]
passdb = config["POSTGRESQL"]["PASSWORD"]
hostdb = config["POSTGRESQL"]["HOST"]
portdb = config["POSTGRESQL"]["PORT"]
typedb = config["POSTGRESQL"]["TYPE"]

# Собираем адрес для соединения с базой данных
connectiondb = typedb + '://' + userdb + ':' + passdb + '@' + hostdb + ':' + portdb + '/' + namedb


# print(connectiondb)

# Функция извлечения данных из json файла
def __json_file_read():
    with open('tests_data.json', 'r', encoding='UTF-8') as open_file:
        ext_data = json.load(open_file)
        # print(ext_data)
    return ext_data


# Функция добавления данных из json файла
def json_input_pos():
    ext_data_json = __json_file_read()
    for parametr in ext_data_json:
        if parametr['model'] == 'publisher':
            parametr_publisher = Publisher(name=parametr['fields']['name'])
            sessions.add(parametr_publisher)
            sessions.commit()
        elif parametr['model'] == 'book':
            parametr_book = Book(title=parametr['fields']['title'], id_published=parametr['fields']['id_publisher'])
            sessions.add(parametr_book)
            sessions.commit()
        elif parametr['model'] == 'shop':
            parametr_shop = Shop(name=parametr['fields']['name'])
            sessions.add(parametr_shop)
            sessions.commit()
        elif parametr['model'] == 'stock':
            parametr_stock = Stock(id_book=parametr['fields']['id_book'], id_shop=parametr['fields']['id_shop'],
                                   count=parametr['fields']['count'])
            sessions.add(parametr_stock)
            sessions.commit()
        elif parametr['model'] == 'sale':
            parametr_sale = Sale(id_stock=parametr['fields']['id_stock'], price=parametr['fields']['price'],
                                 date_sale=parametr['fields']['date_sale'], count=parametr['fields']['count'])
            sessions.add(parametr_sale)
            sessions.commit()


if __name__ == "__main__":
    # Создаем подключение к базе данных
    engine = sqlalchemy.create_engine(connectiondb)
    tables_create(engine)
    Session = sessionmaker(bind=engine)
    sessions = Session()
    # Заполняем базу из json файла
    json_input_pos()
    # Закрываем сессию
    sessions.close()
