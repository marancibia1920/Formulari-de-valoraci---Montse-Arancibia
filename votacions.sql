DROP DATABASE IF exists votacions;
CREATE DATABASE votacions;
USE votacions;

CREATE TABLE votacion(
    id_votacio INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    dni VARCHAR(50) NOT NULL,
    poblacio VARCHAR(50) NOT NULL,
    valoracio VARCHAR(50) NOT NULL
);

CREATE TABLE opcionsVotacio (
    id_opcioVotacio INT AUTO_INCREMENT PRIMARY KEY,
    opcioVotacio VARCHAR(100)
);


