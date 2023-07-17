-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar

create table students
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
)

-- 2. Добавить в таблицу student колонку middle_name varchar

alter table students add column middle_name varchar


-- 3. Удалить колонку middle_name

alter table students drop column middle_name


-- 4. Переименовать колонку birthday в birth_date

alter table students rename birthday to birth_date


-- 5. Изменить тип данных колонки phone на varchar(32)

alter table students alter column phone set data type varchar(32)


-- 6. Вставить три любых записи с автогенерацией идентификатора

insert into students (first_name, last_name, birth_date, phone) values
('John', 'Lennon', '1940-10-09', '8-800-555-35-35'),
('James', 'McCartney', '1942-06-18', '8-800-555-35-36'),
('George', 'Harrison', '1943-02-25', '8-800-555-35-37'),
('Ringo', 'Starr', '1940-07-07', '8-800-555-35-38')


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

truncate table students restart identity
