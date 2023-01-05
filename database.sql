-- docker mysql:5.7 실행 옵션
-- docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

-- 사용자 생성 및 권한 추가
CREATE USER 'ledger_user'@'%' IDENTIFIED BY 'helloworld';
GRANT ALL PRIVILEGES ON ledger_database.* TO ledger_user;
GRANT ALL PRIVILEGES ON test_ledger_database.* TO ledger_user;

-- 데이터베이스 및 테이블 생성
CREATE DATABASE ledger_database CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;

USE ledger_database;

CREATE TABLE `user` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`password` VARCHAR(128) NOT NULL COLLATE 'utf8mb4_unicode_ci',
	`last_login` DATETIME(6) NULL DEFAULT NULL,
	`email` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_unicode_ci',
	PRIMARY KEY (`id`) USING BTREE,
	UNIQUE INDEX `email` (`email`) USING BTREE
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;

CREATE TABLE `ledger` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`amount` INT(11) NOT NULL,
	`description` VARCHAR(200) NOT NULL COLLATE 'utf8mb4_unicode_ci',
	`create_date` DATETIME(6) NOT NULL,
	`user_id` BIGINT(20) NOT NULL,
	PRIMARY KEY (`id`) USING BTREE,
	INDEX `ledgermodel_ledger_user_id_cae93012_fk_user_id` (`user_id`) USING BTREE,
	CONSTRAINT `ledgermodel_ledger_user_id_cae93012_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON UPDATE RESTRICT ON DELETE RESTRICT
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;

CREATE TABLE `short_url` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`code` VARCHAR(7) NOT NULL COLLATE 'utf8mb4_unicode_ci',
	`expired_dt` DATETIME(6) NOT NULL,
	`ledger_id` BIGINT(20) NOT NULL,
	PRIMARY KEY (`id`) USING BTREE,
	UNIQUE INDEX `code` (`code`) USING BTREE,
	INDEX `shortenermodel_shortener_ledger_id_6af5685c_fk_ledger_id` (`ledger_id`) USING BTREE,
	CONSTRAINT `shortenermodel_shortener_ledger_id_6af5685c_fk_ledger_id` FOREIGN KEY (`ledger_id`) REFERENCES `ledger` (`id`) ON UPDATE RESTRICT ON DELETE RESTRICT
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;