CREATE TABLE IF NOT EXISTS `shop`.`employee` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `age` INT NOT NULL,
  `department` VARCHAR(45) NOT NULL,
  `salary` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Петя',23,'ИТ',1000);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Сашя',42,'Бухгалтерия',2500);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Ваня',35,'Администрация',3000);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Анатолий',27,'ИТ',1700);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Иван',41,'ИТ',2800);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Аркадий',40,'Администрация',5000);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Владимир',27,'Администрация',1800);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Андрей',33,'Бухгалтерия',1500);
INSERT INTO `shop`.`employee` (`name`,`age`,`department`,`salary`) VALUES ('Алексей',32,'ИТ',2200);
