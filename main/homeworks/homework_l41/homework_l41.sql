CREATE DATABASE local_network;
USE local_network;
CREATE TABLE users (
    id: int AUTO_INCREMENT,
    name: varchar(30) NOT NULL,
    ip_address: varchar(15) NOT NULL,
	comp_name: varchar(40) NOT NULL,
	"domain": varchar(40) NOT NULL
    
);
