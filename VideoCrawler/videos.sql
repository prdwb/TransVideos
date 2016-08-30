CREATE DATABASE videodb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COMMENT '标题',
  `description` varchar(200) COMMENT '描述',
  `url` varchar(100) NOT NULL COMMENT 'url',
  `upload_date` varchar(32) NOT NULL COMMENT '上传时间',
  `author` varchar(32) NOT NULL COMMENT 'up主',
  `tags` varchar(200) COMMENT '标签',
  `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP  COMMENT '插入时间',
  `download_finished` int(1) NOT NULL DEFAULT 0,
  `upload_finished` int(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
