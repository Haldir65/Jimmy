CREATE TABLE `user` (
 `user_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
 `user_name` VARCHAR(60) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
 `user_password` VARCHAR(30) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
 `user_nickname` VARCHAR(50) COLLATE utf8mb4_unicode_ci DEFAULT '',
 `user_email` VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '', PRIMARY KEY (`user_id`), KEY `user_name`jrdash (`user_name`), KEY `user_email` (`user_email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;