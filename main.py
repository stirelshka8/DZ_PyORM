import configparser, sqlalchemy, json, os
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
def json_file():
    with open('tests_data.json', 'r', encoding='UTF-8') as open_file:
        ext_data = json.load(open_file)
        # print(ext_data)

        return ext_data


if __name__ == "__main__":
    # Создаем подключение к базе данных
    engine = sqlalchemy.create_engine(connectiondb)
    tables_create(engine)
    Session = sessionmaker(bind=engine)
    sessions = Session()
