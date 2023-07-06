"""Скрипт для заполнения данными таблиц в БД Postgres."""
from Table import Table

# Объекты класса Table (таблицы)
tables = [Table('customers'), Table('employees'), Table('orders')]


# Вызываем методы у объектов класса, используя полиморфизм
for table in tables:
    table.connect_to_database()
    path_to_file = table.get_path_to_csv()
    table.load_data_from_csv(path_to_file)
    table.close_connection()
