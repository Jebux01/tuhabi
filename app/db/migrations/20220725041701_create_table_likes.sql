-- migrate:up

CREATE TABLE `likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status_historial_id_uindex` (`id`),
  KEY `likes_property_id_fk` (`property_id`),
  KEY `likes_user_id_fk` (`user_id`),
  CONSTRAINT `likes_property_id_fk` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`),
  CONSTRAINT `likes_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=latin1;

-- migrate:down
DROP TABLE `likes`;

