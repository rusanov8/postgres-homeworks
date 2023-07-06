import psycopg2
import csv
import os


class Table:
    """Класс для работы с таблицами"""

    db_host = 'localhost'
    db_port = '5432'
    db_name = 'north'
    db_user = 'postgres'
    db_password = 'ais40609054'

    def __init__(self, table_name):
        self.table_name = table_name

    def load_data_from_csv(self, path_to_csv):
        """Метод для загрузки данных из csv файлов и заполнения ими наших таблиц"""
        with open(path_to_csv, 'r', newline='') as file:
            csv_data = csv.reader(file)
            next(csv_data)
            for row in csv_data:
                self.cursor.execute(f"INSERT INTO {self.table_name} VALUES ({','.join(['%s'] * len(row))})", row)

        self.connection.commit()

    def connect_to_database(self):
        """Метод для подключения к БД"""
        self.connection = psycopg2.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password)

        self.cursor = self.connection.cursor()

    def get_path_to_csv(self):
        """Метод для получения путей к csv файлам"""
        data_folder = os.path.abspath('north_data')
        csv_file_name = f'{self.table_name}_data.csv'
        path_to_csv = os.path.join(data_folder, csv_file_name)
        return path_to_csv

    def close_connection(self):
        """Метод для закрытия соединения с БД"""
        self.cursor.close()
        self.connection.close()
