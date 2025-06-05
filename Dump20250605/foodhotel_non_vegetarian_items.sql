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
-- Table structure for table `non_vegetarian_items`
--

DROP TABLE IF EXISTS `non_vegetarian_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `non_vegetarian_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non_vegetarian_items`
--

LOCK TABLES `non_vegetarian_items` WRITE;
/*!40000 ALTER TABLE `non_vegetarian_items` DISABLE KEYS */;
INSERT INTO `non_vegetarian_items` VALUES (1,'Chicken Dum Biryani',180.00,'/static/images/Hyderbad_chicken_biriyani.jpg','2025-04-18 04:50:13'),(2,'Chicken Noodles',90.00,'/static/images/chicken_noodles.jpg','2025-04-18 04:50:13'),(3,'Chicken Fried Rice',120.00,'/static/images/chicken_friedrice.jpg','2025-04-18 04:50:13'),(4,'Mutton Curry',350.00,'/static/images/mutton_curry.jpg','2025-04-18 04:50:13'),(5,'Shawarma',100.00,'/static/images/shawarma.jpg','2025-04-18 04:50:13'),(6,'Japanese Ramen',250.00,'/static/images/japanese_ramen.jpg','2025-04-18 04:50:13'),(7,'Mutton Paya Soup',350.00,'/static/images/mutton_payasoup.jpg','2025-04-18 04:50:13'),(8,'Thandoori',450.00,'/static/images/thandoori.jpg','2025-04-18 04:50:13'),(9,'Chicken Wings',220.00,'/static/images/chickenwings.jpg','2025-04-18 04:50:13'),(10,'Chicken Nuggets',230.00,'/static/images/chicken_nuggets.jpg','2025-04-18 04:50:13');
/*!40000 ALTER TABLE `non_vegetarian_items` ENABLE KEYS */;
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
