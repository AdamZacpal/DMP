-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: myflaskapp
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `myflaskapp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `myflaskapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

USE `myflaskapp`;

--
-- Table structure for table `clanky`
--

DROP TABLE IF EXISTS `clanky`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `clanky` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nazev` varchar(255) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `body` text,
  `create_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `title` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clanky`
--

LOCK TABLES `clanky` WRITE;
/*!40000 ALTER TABLE `clanky` DISABLE KEYS */;
INSERT INTO `clanky` VALUES (2,'Zajímavý článek','Adam Zacpal','Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent id justo in neque elementum ultrices. Integer rutrum, orci vestibulum ullamcorper ultricies, lacus quam ultricies odio, vitae placerat pede sem sit amet enim. Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Etiam ligula pede, sagittis quis, interdum ultricies, scelerisque eu. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Quisque tincidunt scelerisque libero. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Proin in tellus sit amet nibh dignissim sagittis. Nullam rhoncus aliquam metus.\r\n\r\nUt tempus purus at lorem. Maecenas lorem. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Vivamus porttitor turpis ac leo. Praesent in mauris eu tortor porttitor accumsan. Nam sed tellus id magna elementum tincidunt. Fusce wisi. In sem justo, commodo ut, suscipit at, pharetra vitae, orci. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Integer imperdiet lectus quis justo. Aliquam erat volutpat.\r\n\r\nEtiam egestas wisi a erat. Proin pede metus, vulputate nec, fermentum fringilla, vehicula vitae, justo. Maecenas sollicitudin. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Donec vitae arcu. Donec iaculis gravida nulla. In convallis. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Cras pede libero, dapibus nec, pretium sit amet, tempor quis. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In enim a arcu imperdiet malesuada.\r\n\r\nMaecenas libero. Duis pulvinar. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Quisque porta. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. In enim a arcu imperdiet malesuada. Fusce wisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis bibendum, lectus ut viverra rhoncus, dolor nunc faucibus libero, eget facilisis enim ipsum id lacus. Maecenas libero. Nulla pulvinar eleifend sem. Aenean vel massa quis mauris vehicula lacinia.\r\n\r\nFusce wisi. Phasellus faucibus molestie nisl. Integer lacinia. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Integer imperdiet lectus quis justo. Etiam neque. Integer tempor. Duis pulvinar. Nullam rhoncus aliquam metus. Integer malesuada. Nullam sit amet magna in magna gravida vehicula. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Nullam eget nisl.','2019-03-11 15:52:27',NULL),(5,'Můj výlet do Athén','Adam Zacpal','Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Curabitur vitae diam non enim vestibulum interdum. Praesent in mauris eu tortor porttitor accumsan. Nulla non lectus sed nisl molestie malesuada. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Duis viverra diam non justo. Pellentesque arcu. Integer imperdiet lectus quis justo. Integer pellentesque quam vel velit. Quisque porta. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Mauris metus. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Praesent vitae arcu tempor neque lacinia pretium.\r\n\r\nDuis pulvinar. Duis bibendum, lectus ut viverra rhoncus, dolor nunc faucibus libero, eget facilisis enim ipsum id lacus. In convallis. Integer tempor. Integer malesuada. Pellentesque pretium lectus id turpis. Ut tempus purus at lorem. Duis pulvinar. Curabitur vitae diam non enim vestibulum interdum. Sed elit dui, pellentesque a, faucibus vel, interdum nec, diam. Suspendisse sagittis ultrices augue. Praesent id justo in neque elementum ultrices. Donec vitae arcu. Maecenas ipsum velit, consectetuer eu lobortis ut, dictum at dui. Duis risus. Proin in tellus sit amet nibh dignissim sagittis.\r\n\r\nPhasellus rhoncus. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Donec quis nibh at felis congue commodo. Integer malesuada. Fusce suscipit libero eget elit. Aenean vel massa quis mauris vehicula lacinia. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Fusce wisi. Proin mattis lacinia justo. Nulla pulvinar eleifend sem. Aliquam erat volutpat. Duis ante orci, molestie vitae vehicula venenatis, tincidunt ac pede. Sed ac dolor sit amet purus malesuada congue.\r\n\r\nIn sem justo, commodo ut, suscipit at, pharetra vitae, orci. Quisque porta. Suspendisse sagittis ultrices augue. Suspendisse nisl. Quisque tincidunt scelerisque libero. Phasellus faucibus molestie nisl. Duis viverra diam non justo. Pellentesque ipsum. Integer lacinia. Integer vulputate sem a nibh rutrum consequat. Fusce tellus. Et harum quidem rerum facilis est et expedita distinctio. Nam sed tellus id magna elementum tincidunt. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Etiam egestas wisi a erat. Pellentesque ipsum.\r\n\r\nSed elit dui, pellentesque a, faucibus vel, interdum nec, diam. Curabitur sagittis hendrerit ante. Etiam ligula pede, sagittis quis, interdum ultricies, scelerisque eu. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. In convallis. Praesent dapibus. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Quisque porta. Duis condimentum augue id magna semper rutrum. Phasellus rhoncus. Aliquam ornare wisi eu metus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Praesent in mauris eu tortor porttitor accumsan. Etiam dictum tincidunt diam. Nam quis nulla. Donec vitae arcu. Maecenas aliquet accumsan leo.','2019-03-11 17:34:38',NULL),(6,'Desátý článek','Adam Zacpal','<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Curabitur vitae diam non enim vestibulum interdum. Praesent in mauris eu tortor porttitor accumsan. Nulla non lectus sed nisl molestie malesuada. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Duis viverra diam non justo. Pellentesque arcu. Integer imperdiet lectus quis justo. Integer pellentesque quam vel velit. Quisque porta. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Mauris metus. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Praesent vitae arcu tempor neque lacinia pretium.</p><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Curabitur vitae diam non enim vestibulum interdum. Praesent in mauris eu tortor porttitor accumsan. Nulla non lectus sed nisl molestie malesuada. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Duis viverra diam non justo. Pellentesque arcu. Integer imperdiet lectus quis justo. Integer pellentesque quam vel velit. Quisque porta. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Mauris metus. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Praesent vitae arcu tempor neque lacinia pretium.</p>','2019-03-11 17:36:15',NULL),(7,'Maturitní práce','Adam Zacpal','Ahoj tohle je má maturitní práce. AHOOOOOOoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooj','2019-03-17 17:56:57',NULL);
/*!40000 ALTER TABLE `clanky` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(1) NOT NULL AUTO_INCREMENT,
  `jmeno` varchar(100) DEFAULT NULL,
  `prezdivka` varchar(30) DEFAULT NULL,
  `heslo` varchar(100) DEFAULT NULL,
  `register_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,NULL,NULL,NULL,'2019-03-11 12:40:59'),(2,'Adam Zacpal','adazac','$5$rounds=80000$vp5we4BpSZyo7xAN$0Q/5/Re1R868EBrYRZwsHPT3Ov5c4b3pTH3fHgjRhGC','2019-03-11 12:56:45');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-23 17:06:41
