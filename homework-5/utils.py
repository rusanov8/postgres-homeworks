import psycopg2
import json


def create_suppliers_table(database_name: str, params: dict):
    """Создает таблицу suppliers"""
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS suppliers (
                        supplier_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(50) NOT NULL,
                        contact VARCHAR(255),
                        address VARCHAR(255),
                        phone VARCHAR(255),
                        fax VARCHAR(255),
                        homepage VARCHAR(255)
                    )
                 """)

    conn.commit()
    conn.close()


def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    with open(json_file) as file:
        suppliers_data = json.load(file)

    return suppliers_data


def insert_suppliers_data(database_name, params, suppliers_data: list[dict]) -> None:
    """Заполняет таблицу suppliers данными из списка словарей suppliers_data"""
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for supplier in suppliers_data:
            cur.execute(
                """
                INSERT INTO suppliers (company_name, contact, address, phone, fax, homepage)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING supplier_id
                """,
                (supplier['company_name'], supplier['contact'], supplier['address'], supplier['phone'], supplier['fax'], supplier['homepage'])
            )

    conn.commit()
    conn.close()


def add_foreign_keys(database_name, params, suppliers_data):
    """Создает поле supplier_id в таблице products
    И связывает таблицы products и suppliers по полю supplier_id"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute(
            """
            ALTER TABLE products
            ADD COLUMN IF NOT EXISTS supplier_id INT
        """)
        cur.execute(
            """
            ALTER TABLE products
            ADD CONSTRAINT fk_products_suppliers 
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        """)

        for suppliers in suppliers_data:
            for product_name in suppliers['products']:
                cur.execute(
                    """
                    UPDATE products
                    SET supplier_id = (
                    SELECT supplier_id 
                    FROM suppliers 
                    WHERE company_name = %s
                    LIMIT 1
                    )
                    WHERE product_name = %s
                """,
                    (suppliers['company_name'], product_name)
                )

    conn.commit()
    conn.close()
