# База данных была создана и заполнена данными из файла fill_db.sql через PG admin
# В данной программе мы создаем таблицу suppliers, заполняем ее данными из файла json
# И связываем через foreign_key с таблицей products

from config import config
from utils import create_suppliers_table, get_suppliers_data, insert_suppliers_data, add_foreign_keys


def main():

    json_file = 'suppliers.json'
    db_name = 'northwind'
    params = config()

    create_suppliers_table(db_name, params)
    suppliers_data = get_suppliers_data(json_file)
    insert_suppliers_data(db_name, params, suppliers_data)
    add_foreign_keys(db_name, params, suppliers_data)


if __name__ == '__main__':
    main()
