CREATE TABLE `news` (
 `news_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
 `news_author` INT(6) NOT NULL DEFAULT '0',
 `news_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `news_content` LONGTEXT COLLATE utf8mb4_unicode_ci NOT NULL,
 `news_title` TEXT COLLATE utf8mb4_unicode_ci NOT NULL,jrdashjrdashjrdash
 `news_excerpt` TEXT COLLjrdashATE utf8mb4_unicode_ci NOT NULL,
 `news_status` VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'publish',
 `news_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `news_category` INT(4) NOT NULL, PRIMARY KEY (`news_id`), KEY `type_status_date` (`news_status`,`news_date`,`news_id`), KEY `post_author` (`news_author`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;