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
-- Table structure for table `menu_items`
--

DROP TABLE IF EXISTS `menu_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `category` enum('vegetarian','non-vegetarian','drink','icecream') NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_items`
--

LOCK TABLES `menu_items` WRITE;
/*!40000 ALTER TABLE `menu_items` DISABLE KEYS */;
INSERT INTO `menu_items` VALUES (1,'Veg Noodles',80.00,'/static/images/veg_noodles.jpg','vegetarian','2025-04-18 04:53:04'),(2,'Veg Fried Rice',70.00,'/static/images/veg_friedrice.jpg','vegetarian','2025-04-18 04:53:04'),(3,'Chapathi',40.00,'/static/images/chapathi.jpg','vegetarian','2025-04-18 04:53:04'),(4,'Butter Naan',80.00,'/static/images/buter_nans.jpg','vegetarian','2025-04-18 04:53:04'),(5,'Kajju Tomato Curry',180.00,'/static/images/kajju_tomato_curry.jpg','vegetarian','2025-04-18 04:53:04'),(6,'Pulka\'s',10.00,'/static/images/pulka\'s.jpg','vegetarian','2025-04-18 04:53:04'),(7,'Cheese Cake',40.00,'/static/images/chesecake.jpg','vegetarian','2025-04-18 04:53:04'),(8,'Paneer Butter Masala Curry',230.00,'/static/images/paneer_butter_masala.jpg','vegetarian','2025-04-18 04:53:04'),(9,'Momo\'s',130.00,'/static/images/momos.jpg','vegetarian','2025-04-18 04:53:04'),(10,'Chicken Dum Biryani',180.00,'/static/images/Hyderbad_chicken_biriyani.jpg','non-vegetarian','2025-04-18 04:53:04'),(11,'Chicken Noodles',90.00,'/static/images/chicken_noodles.jpg','non-vegetarian','2025-04-18 04:53:04'),(12,'Chicken Fried Rice',120.00,'/static/images/chicken_friedrice.jpg','non-vegetarian','2025-04-18 04:53:04'),(13,'Mutton Curry',350.00,'/static/images/mutton_curry.jpg','non-vegetarian','2025-04-18 04:53:04'),(14,'Shawarma',100.00,'/static/images/shawarma.jpg','non-vegetarian','2025-04-18 04:53:04'),(15,'Japanese Ramen',250.00,'/static/images/japanese_ramen.jpg','non-vegetarian','2025-04-18 04:53:04'),(16,'Mutton Paya Soup',350.00,'/static/images/mutton_payasoup.jpg','non-vegetarian','2025-04-18 04:53:04'),(17,'Thandoori',450.00,'/static/images/thandoori.jpg','non-vegetarian','2025-04-18 04:53:04'),(18,'Chicken Wings',220.00,'/static/images/chickenwings.jpg','non-vegetarian','2025-04-18 04:53:04'),(19,'Chicken Nuggets',230.00,'/static/images/chicken_nuggets.jpg','non-vegetarian','2025-04-18 04:53:04'),(20,'Pepper Drink',35.00,'/static/drinksandicecreams/pepper_drink.jpg','drink','2025-04-18 04:53:04'),(21,'Lemonade',30.00,'/static/drinksandicecreams/lemonade.jpg','drink','2025-04-18 04:53:04'),(22,'Mirinda',20.00,'/static/drinksandicecreams/mirinda.jpg','drink','2025-04-18 04:53:04'),(23,'Wostok',60.00,'/static/drinksandicecreams/wostok.jpg','drink','2025-04-18 04:53:04'),(24,'Special Lemonade',60.00,'/static/drinksandicecreams/special_lemonade.jpg','drink','2025-04-18 04:53:04'),(25,'Grape Juice',70.00,'/static/drinksandicecreams/grapejuice.jpg','drink','2025-04-18 04:53:04'),(26,'Pepsi',30.00,'/static/drinksandicecreams/pepsi.jpg','drink','2025-04-18 04:53:04'),(27,'Rose Lemonade',50.00,'/static/drinksandicecreams/rose_lemonade.jpg','drink','2025-04-18 04:53:04'),(28,'Cococola',30.00,'/static/drinksandicecreams/cococola.jpg','drink','2025-04-18 04:53:04'),(29,'Chocolate Icecream',45.00,'/static/drinksandicecreams/chocolate_icecream.jpg','icecream','2025-04-18 04:53:04'),(30,'Icecream Biscuit',40.00,'/static/drinksandicecreams/icecream_biscuit.jpg','icecream','2025-04-18 04:53:04'),(31,'Cup Icecream',50.00,'/static/drinksandicecreams/cupicecream.jpg','icecream','2025-04-18 04:53:04'),(32,'Strawberry With Vanilla',90.00,'/static/drinksandicecreams/strawberry_with_vanilla.jpg','icecream','2025-04-18 04:53:04'),(33,'Strawberry Icecream',80.00,'/static/drinksandicecreams/strawberry_icecream.jpg','icecream','2025-04-18 04:53:04'),(34,'Chocobar',70.00,'/static/drinksandicecreams/chocobar.jpg','icecream','2025-04-18 04:53:04'),(35,'Choco Vanilla Combo Icecream',90.00,'/static/drinksandicecreams/choco_vanilla_combo_icecream.jpg','icecream','2025-04-18 04:53:04'),(36,'FrostyFeast',75.00,'/static/drinksandicecreams/frostyfeast.jpg','icecream','2025-04-18 04:53:04'),(37,'Special Banana Icecream',60.00,'/static/drinksandicecreams/special_banana_icecream.jpg','icecream','2025-04-18 04:53:04'),(38,'Vanilla Icecream',40.00,'/static/drinksandicecreams/vanilla_icecream.jpg','icecream','2025-04-18 04:53:04'),(39,'Sugar Rush Icecream',35.00,'/static/drinksandicecreams/sugar_rush_icecream.jpg','icecream','2025-04-18 04:53:04'),(40,'Icyisland Icecream',90.00,'/static/drinksandicecreams/icyisland_icecream.jpg','icecream','2025-04-18 04:53:04');
/*!40000 ALTER TABLE `menu_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-05  6:23:19
