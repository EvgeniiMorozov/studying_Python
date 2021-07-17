CREATE TABLE `shop`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` TEXT(255) NOT NULL,
  `price` INT NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `shop`.`cart` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

-- создание таблицы Корзина и создание внешнего ключа
CREATE TABLE `shop`.`cart` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
    FOREIGN KEY (`customer_id`)
    REFERENCES `shop`.`customer` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

-- многотабличный запрос
SELECT customer.id, customer.name, cart.id from customer, cart where customer.id = cart.customer_id;