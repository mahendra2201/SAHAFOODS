-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: foodhotel
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vegetarian_items`
--

DROP TABLE IF EXISTS `vegetarian_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vegetarian_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vegetarian_items`
--

LOCK TABLES `vegetarian_items` WRITE;
/*!40000 ALTER TABLE `vegetarian_items` DISABLE KEYS */;
INSERT INTO `vegetarian_items` VALUES (1,'Veg Noodles',80.00,'/static/images/veg_noodles.jpg','2025-04-18 04:49:05'),(2,'Veg Fried Rice',70.00,'/static/images/veg_friedrice.jpg','2025-04-18 04:49:05'),(3,'Chapathi',40.00,'/static/images/chapathi.jpg','2025-04-18 04:49:05'),(4,'Butter Naan',80.00,'/static/images/buter_nans.jpg','2025-04-18 04:49:05'),(5,'Kajju Tomato Curry',180.00,'/static/images/kajju_tomato_curry.jpg','2025-04-18 04:49:05'),(6,'Pulka\'s',10.00,'/static/images/pulka\'s.jpg','2025-04-18 04:49:05'),(7,'Cheese Cake',40.00,'/static/images/chesecake.jpg','2025-04-18 04:49:05'),(8,'Paneer Butter Masala Curry',230.00,'/static/images/paneer_butter_masala.jpg','2025-04-18 04:49:05'),(9,'Momo\'s',130.00,'/static/images/momos.jpg','2025-04-18 04:49:05');
/*!40000 ALTER TABLE `vegetarian_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-05  6:23:21
