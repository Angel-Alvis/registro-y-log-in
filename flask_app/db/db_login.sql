-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_login
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_login
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_login` DEFAULT CHARACTER SET utf8mb3 ;
-- -----------------------------------------------------
-- Schema db_estudiantes_cursos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_estudiantes_cursos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_estudiantes_cursos` DEFAULT CHARACTER SET utf8mb3 ;
USE `db_login` ;

-- -----------------------------------------------------
-- Table `db_login`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_login`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_login`.`misiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_login`.`misiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(150) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `numero_voluntarios` INT NOT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_misiones_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_misiones_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_login`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `db_estudiantes_cursos` ;

-- -----------------------------------------------------
-- Table `db_estudiantes_cursos`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_estudiantes_cursos`.`cursos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_estudiantes_cursos`.`estudiantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_estudiantes_cursos`.`estudiantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `edad` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `curso_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_estudiantes_cursos_idx` (`curso_id` ASC) VISIBLE,
  CONSTRAINT `fk_estudiantes_cursos`
    FOREIGN KEY (`curso_id`)
    REFERENCES `db_estudiantes_cursos`.`cursos` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
