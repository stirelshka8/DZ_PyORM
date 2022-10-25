import os
import sqlalchemy
import configparser

configpath = "configuration.conf"
config = configparser.ConfigParser()
config.read(configpath)


def cprint_upred(text):
    print("\033[1m\033[31m{}\033[0m".format(text))


def cprint_yellow(text):
    print("\033[33m{}\033[0m".format(text))


def cprint_blue(text):
    print("\033[34m{}\033[0m".format(text))


def start_programm():
    if os.path.exists(configpath):
        cprint_yellow(f"[INFO] Программа запущена!\n\n")
    else:
        cprint_upred("""По всей вероятности это первый запуск программы. 
Для корректной работы необходимо настроить некоторые параметры, данное действие необходимо сделать однократно.
Приступим!
""")
        config.add_section("DATABASE")
        add_dbname = input("[SET]Введите имя базы данных - ")
        add_dbuser = input("[SET]Введите имя пользователя базы данных - ")
        add_dbpass = input("[SET]Введите пароль базы данных - ")
        add_dbhost = input("[SET]Введите адрес хоста базы данных - ")
        add_dbport = input("[SET]Введите номер порта базы данных (по умолчанию - 5432) - ")

        config.set("DATABASE", "NAME", add_dbname)
        config.set("DATABASE", "USER", add_dbuser)
        config.set("DATABASE", "PASSWORD", add_dbpass)
        config.set("DATABASE", "HOST", add_dbhost)
        config.set("DATABASE", "PORT", add_dbport)

        config.add_section("INSTALLATIONS")
        config.set("INSTALLATIONS", "CHECK", "True")

        with open(configpath, "w") as config_file:
            config.write(config_file)

        os.system("clear")
        cprint_yellow(f"[INFO] Файл конфигурации {configpath} создан.")
        cprint_yellow(f"[INFO] Программа запущена!\n\n")


if __name__ == "__main__":
    start_programm()
