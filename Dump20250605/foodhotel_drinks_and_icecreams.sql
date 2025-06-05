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
-- Table structure for table `drinks_and_icecreams`
--

DROP TABLE IF EXISTS `drinks_and_icecreams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drinks_and_icecreams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `category` enum('drink','icecream') NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drinks_and_icecreams`
--

LOCK TABLES `drinks_and_icecreams` WRITE;
/*!40000 ALTER TABLE `drinks_and_icecreams` DISABLE KEYS */;
INSERT INTO `drinks_and_icecreams` VALUES (1,'Chocolate Icecream',45.00,'/static/drinksandicecreams/chocolate_icecream.jpg','icecream','2025-04-18 04:51:20'),(2,'Icecream Biscuit',40.00,'/static/drinksandicecreams/icecream_biscuit.jpg','icecream','2025-04-18 04:51:20'),(3,'Cup Icecream',50.00,'/static/drinksandicecreams/cupicecream.jpg','icecream','2025-04-18 04:51:20'),(4,'Strawberry With Vanilla',90.00,'/static/drinksandicecreams/strawberry_with_vanilla.jpg','icecream','2025-04-18 04:51:20'),(5,'Strawberry Icecream',80.00,'/static/drinksandicecreams/strawberry_icecream.jpg','icecream','2025-04-18 04:51:20'),(6,'Chocobar',70.00,'/static/drinksandicecreams/chocobar.jpg','icecream','2025-04-18 04:51:20'),(7,'Choco Vanilla Combo Icecream',90.00,'/static/drinksandicecreams/choco_vanilla_combo_icecream.jpg','icecream','2025-04-18 04:51:20'),(8,'FrostyFeast',75.00,'/static/drinksandicecreams/frostyfeast.jpg','icecream','2025-04-18 04:51:20'),(9,'Special Banana Icecream',60.00,'/static/drinksandicecreams/special_banana_icecream.jpg','icecream','2025-04-18 04:51:20'),(10,'Vanilla Icecream',40.00,'/static/drinksandicecreams/vanilla_icecream.jpg','icecream','2025-04-18 04:51:20'),(11,'Sugar Rush Icecream',35.00,'/static/drinksandicecreams/sugar_rush_icecream.jpg','icecream','2025-04-18 04:51:20'),(12,'Icyisland Icecream',90.00,'/static/drinksandicecreams/icyisland_icecream.jpg','icecream','2025-04-18 04:51:20'),(13,'Pepper Drink',35.00,'/static/drinksandicecreams/pepper_drink.jpg','drink','2025-04-18 04:51:20'),(14,'Lemonade',30.00,'/static/drinksandicecreams/lemonade.jpg','drink','2025-04-18 04:51:20'),(15,'Mirinda',20.00,'/static/drinksandicecreams/mirinda.jpg','drink','2025-04-18 04:51:20'),(16,'Wostok',60.00,'/static/drinksandicecreams/wostok.jpg','drink','2025-04-18 04:51:20'),(17,'Special Lemonade',60.00,'/static/drinksandicecreams/special_lemonade.jpg','drink','2025-04-18 04:51:20'),(18,'Grape Juice',70.00,'/static/drinksandicecreams/grapejuice.jpg','drink','2025-04-18 04:51:20'),(19,'Pepsi',30.00,'/static/drinksandicecreams/pepsi.jpg','drink','2025-04-18 04:51:20'),(20,'Rose Lemonade',50.00,'/static/drinksandicecreams/rose_lemonade.jpg','drink','2025-04-18 04:51:20'),(21,'Cococola',30.00,'/static/drinksandicecreams/cococola.jpg','drink','2025-04-18 04:51:20');
/*!40000 ALTER TABLE `drinks_and_icecreams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-05  6:23:20
