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
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `dateAndtime` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('mahendra22','1234','2025-04-04 13:08:47'),('mahendra22','1234','2025-04-04 13:13:43'),('mahendra22','1234','2025-04-04 13:23:00'),('mahendra22','1234','2025-04-04 14:23:00'),('mahendra22','1234','2025-04-04 15:24:46'),('mahendra22','1234','2025-04-04 15:33:58'),('mahendra22','1234','2025-04-04 15:43:14'),('mahendra22','1234','2025-04-04 15:46:51'),('mahendra22','1234','2025-04-04 16:07:33'),('mahendra22','1234','2025-04-04 16:10:11'),('mahendra22','1234','2025-04-04 16:31:33'),('mahendra22','1234','2025-04-04 16:32:22'),('mahendra22','1234','2025-04-04 16:36:17'),('mahendra22','1234','2025-04-04 16:51:38'),('mahendra22','1234','2025-04-06 18:20:35'),('mahendra22','1234','2025-04-06 18:30:08'),('mahendra22','1234','2025-04-06 18:36:02'),('mahendra22','1234','2025-04-06 18:53:56'),('mahendra22','1234','2025-04-06 19:02:16'),('MahiChowdary','1234','2025-04-06 19:12:29'),('manasa22','A1234@','2025-04-06 20:39:19'),('mahendra22','1234','2025-04-07 16:08:16'),('manasa22','A1234@','2025-04-07 16:11:09'),('mahendra22','1234','2025-04-07 16:12:16'),('manasa22','A1234@','2025-04-07 16:13:40'),('mahendra22','1234','2025-04-08 22:59:04'),('manasa22','A1234@','2025-04-08 23:01:11'),('mahendra22','1234','2025-04-09 21:45:25'),('mahendra22','1234','2025-04-09 21:56:50'),('manasa22','A1234@','2025-04-09 21:57:13'),('Mukesh22','A123456@','2025-04-12 08:58:05'),('Mukesh22','A123456@','2025-04-12 09:03:47'),('mahendra22','1234','2025-04-12 09:04:31'),('mahendra22','1234','2025-04-18 15:40:45'),('mahendra22','1234','2025-04-18 15:46:51'),('mahendra22','1234','2025-04-18 15:51:08'),('mahendra22','1234','2025-04-18 15:57:34'),('mahendra22','1234','2025-04-18 15:58:48'),('mahendra22','1234','2025-04-18 16:03:33'),('mahendra22','1234','2025-04-18 16:05:01'),('mahendra22','1234','2025-04-18 16:06:00'),('mahendra22','1234','2025-04-18 16:07:01'),('mahendra22','1234','2025-04-18 16:08:16'),('mahendra22','1234','2025-04-21 11:26:10'),('mahendra22','1234','2025-04-21 19:39:46'),('mahendra22','1234','2025-04-21 19:49:49'),('Mukesh22','A123456@','2025-04-21 19:52:17'),('mahendra22','1234','2025-04-21 19:55:00'),('mahendra22','1234','2025-04-21 20:05:57'),('manasa22','A1234@','2025-04-27 10:49:04'),('mahendra22','1234','2025-04-30 16:02:51'),('mahendra22','1234','2025-04-30 16:05:31'),('mahendra22','1234','2025-04-30 16:10:10'),('mahendra22','1234','2025-04-30 16:15:53'),('mahendra22','1234','2025-04-30 16:17:06'),('mahendra22','1234','2025-04-30 16:22:13'),('mahendra22','1234','2025-04-30 16:28:45'),('mahendra22','1234','2025-04-30 16:30:14'),('mahendra22','1234','2025-04-30 16:34:13'),('mahendra22','1234','2025-04-30 16:36:02'),('mahendra22','1234','2025-05-01 10:37:34'),('mahendra22','1234','2025-05-01 10:39:31'),('mahendra22','1234','2025-05-01 10:44:15'),('mahendra22','1234','2025-05-01 10:46:46'),('mahendra22','1234','2025-05-01 10:50:01'),('mahendra22','1234','2025-05-01 10:52:16'),('mahendra22','1234','2025-05-04 17:50:56'),('Mukesh22','A123456@','2025-05-04 17:53:52'),('Mukesh22','A123456@','2025-05-04 22:35:23'),('Mukesh22','A123456@','2025-05-06 20:38:59'),('mahendra22','1234','2025-05-06 20:41:28'),('Mukesh22','A123456@','2025-05-06 20:41:49'),('Mukesh22','A123456@','2025-05-06 20:43:06'),('Mukesh22','A123456@','2025-05-07 15:56:00'),('Mukesh22','A123456@','2025-05-07 15:56:52'),('mahendra99','newpass123','2025-05-07 20:35:37'),('mahendra99','newpass123','2025-05-13 16:18:59'),('Mukesh22','A123456@','2025-05-13 16:19:22'),('Mukesh22','A123456@','2025-05-17 13:42:14'),('Mukesh22','A123456@','2025-05-28 18:09:59'),('mahendra22','1234','2025-05-28 18:20:20'),('mahendra22','1234','2025-05-28 18:23:37'),('mahendra22','1234','2025-05-28 18:35:58'),('mahendra22','1234','2025-06-01 10:19:53'),('mahi22','A1234','2025-06-02 17:33:23'),('mahendra22','1234','2025-06-02 18:34:30'),('mahendra22','1234','2025-06-02 18:36:23'),('mahendra22','1234','2025-06-04 07:56:45'),('mahendra22','1234','2025-06-04 08:03:33'),('mahendra22','1234','2025-06-04 08:06:21'),('mahendra22','1234','2025-06-04 08:06:57'),('mahendra22','1234','2025-06-04 08:08:19'),('mahi22','A1234','2025-06-04 08:08:38'),('mahi22','A1234','2025-06-04 17:24:08'),('mahendra22','1234','2025-06-04 17:25:18'),('mahendra22','1234','2025-06-04 17:27:17'),('mahendra22','1234','2025-06-04 17:27:58'),('mahendra22','1234','2025-06-04 17:29:12'),('mahendra22','1234','2025-06-04 17:33:27'),('mahendra22','1234','2025-06-04 17:36:25'),('mahendra22','1234','2025-06-04 17:37:16');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
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
