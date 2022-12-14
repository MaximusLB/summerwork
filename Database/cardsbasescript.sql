-- MySQL Script generated by MySQL Workbench
-- Fri Oct  7 10:33:32 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Publishers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Publishers` (
  `Publisher_ID` INT NOT NULL AUTO_INCREMENT,
  `Publisher_Name` VARCHAR(45) NULL,
  PRIMARY KEY (`Publisher_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cards` (
  `Card_ID` INT NOT NULL AUTO_INCREMENT,
  `Card _Name` VARCHAR(45) NULL,
  `Publisher_ID` INT NULL,
  `Size` INT NULL,
  `Price` INT NULL,
  PRIMARY KEY (`Card_ID`),
  CONSTRAINT ``
    FOREIGN KEY ()
    REFERENCES `mydb`.`Publishers` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Sales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Sales` (
  `Sale_ID` INT NOT NULL AUTO_INCREMENT,
  `Customer_ID` VARCHAR(45) NULL,
  `Date` VARCHAR(45) NULL,
  `Card_ID` VARCHAR(45) NULL,
  `Total_Price` VARCHAR(45) NULL,
  PRIMARY KEY (`Sale_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customers` (
  `` INT NOT NULL DEFAULT ,
  `Username` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  `Access` VARCHAR(45) NULL,
  PRIMARY KEY (``))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


