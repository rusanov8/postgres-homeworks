-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)

select customers.company_name as customer, concat(first_name, ' ', last_name) as employee from customers
join orders using(customer_id)
join employees on orders.employee_id=employees.employee_id
join shippers on orders.ship_via=shippers.shipper_id
where customers.city = 'London' and employees.city = 'London'
and shippers.shipper_id=2


-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.

select product_name, units_in_stock, contact_name, phone from products
join suppliers using(supplier_id)
where category_id in (2, 4) and products.discontinued = 0 and products.units_in_stock<25
order by units_in_stock


-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа

select company_name from customers
where not exists (select * from orders where customers.customer_id=orders.customer_id)


-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.

select product_name
from products
where product_id in (select product_id from order_details where quantity=10)