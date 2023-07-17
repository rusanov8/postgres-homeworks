-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)

alter table products add constraint chk_products_unit_price check (unit_price > 0)

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1

alter table products add constraint chk_products_discontinued check (discontinued in (0, 1))


-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)

select * into discontinued_products from products where discontinued = 1


-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.

alter table order_details drop constraint fk_order_details_products;

delete from order_details
where product_id in (select product_id from products where discontinued=1);
delete from products where discontinued=1;

alter table order_details add constraint fk_order_details_products foreign key(product_id) references products(product_id)