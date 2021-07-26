ALTER TABLE `newdb`.`customers`
    ADD PRIMARY KEY (customerNumber);
ALTER TABLE `newdb`.`employees`
    ADD PRIMARY KEY (employeeNumber);
ALTER TABLE `newdb`.`offices`
    ADD PRIMARY KEY (officeCode);
ALTER TABLE `newdb`.`orderdetails`
    ADD PRIMARY KEY (orderNumber, productCode);
ALTER TABLE `newdb`.`orders`
    ADD PRIMARY KEY (orderNumber),
    ADD KEY (customerNumber);
ALTER TABLE `newdb`.`payments`
    ADD PRIMARY KEY (customerNumber, checkNumber);
ALTER TABLE `newdb`.`productlines`
    ADD PRIMARY KEY (productLine);
ALTER TABLE `newdb`.`products `
    ADD PRIMARY KEY (productCode),
    ADD KEY (buyPrice),
    ADD KEY (productLine);
ALTER TABLE `newdb`.`productvariants`
    ADD PRIMARY KEY (variantId),
    ADD KEY (buyPrice),
    ADD KEY (productCode);