
-- -----------------------------------------------------
-- Table `urls`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `urls` (
  `idurl` INTEGER PRIMARY KEY AUTOINCREMENT,
  `url` VARCHAR(2000) NULL DEFAULT NULL);


-- -----------------------------------------------------
-- Table `page_rank`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `page_rank` (
  `idurl` INTEGER,
  `nota` FLOAT NOT NULL,
  PRIMARY KEY (`idurl`),
  CONSTRAINTEGER `fk_page_rank_idurl`
    FOREIGN KEY (`idurl`)
    REFERENCES `urls` (`idurl`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `palavras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `palavras` (
  `idpalavra` INTEGER PRIMARY KEY AUTOINCREMENT,
  `palavra` VARCHAR(200));


-- -----------------------------------------------------
-- Table `palavra_localizacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `palavra_localizacao` (
  `idpalavra_localizacao` INTEGER(11) NOT NULL AUTOINCREMENT,
  `idurl` INTEGER(11) NOT NULL,
  `idpalavra` INTEGER(11) NOT NULL,
  `localizacao` INTEGER(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idpalavra_localizacao`),
  INDEX `fk_palavra_localizacao_idurl` (`idurl` ASC),
  INDEX `idx_palavra_localizacao_idpalavra` (`idpalavra` ASC),
  CONSTRAINTEGER `fk_palavra_localizacao_idpalavra`
    FOREIGN KEY (`idpalavra`)
    REFERENCES `palavras` (`idpalavra`),
  CONSTRAINTEGER `fk_palavra_localizacao_idurl`
    FOREIGN KEY (`idurl`)
    REFERENCES `urls` (`idurl`))
ENGINE = InnoDB
AUTOINCREMENT = 376606
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `url_ligacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `url_ligacao` (
  `idurl_ligacao` INTEGER(11) NOT NULL AUTOINCREMENT,
  `idurl_origem` INTEGER(11) NOT NULL,
  `idurl_destino` INTEGER(11) NOT NULL,
  PRIMARY KEY (`idurl_ligacao`),
  INDEX `idx_url_ligacao_idurl_origem` (`idurl_origem` ASC),
  INDEX `idx_url_ligacao_idurl_destino` (`idurl_destino` ASC),
  CONSTRAINTEGER `fk_url_ligacao_idurl_destino`
    FOREIGN KEY (`idurl_destino`)
    REFERENCES `urls` (`idurl`),
  CONSTRAINTEGER `fk_url_ligacao_idurl_origem`
    FOREIGN KEY (`idurl_origem`)
    REFERENCES `urls` (`idurl`))
ENGINE = InnoDB
AUTOINCREMENT = 68783;


-- -----------------------------------------------------
-- Table `url_palavra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `url_palavra` (
  `idurl_palavra` INTEGER(11) NOT NULL AUTOINCREMENT,
  `idpalavra` INTEGER(11) NOT NULL,
  `idurl_ligacao` INTEGER(11) NOT NULL,
  PRIMARY KEY (`idurl_palavra`),
  INDEX `fk_url_palavra_idurl_ligacao` (`idurl_ligacao` ASC),
  INDEX `idx_url_palavra_idpalavra` (`idpalavra` ASC),
  CONSTRAINTEGER `fk_url_palavra_idpalavra`
    FOREIGN KEY (`idpalavra`)
    REFERENCES `palavras` (`idpalavra`),
  CONSTRAINTEGER `fk_url_palavra_idurl_ligacao`
    FOREIGN KEY (`idurl_ligacao`)
    REFERENCES `url_ligacao` (`idurl_ligacao`))
ENGINE = InnoDB
AUTOINCREMENT = 966013;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

