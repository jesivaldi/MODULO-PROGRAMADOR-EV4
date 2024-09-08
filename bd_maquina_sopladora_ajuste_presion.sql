-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: bd_maquina_sopladora
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `ajuste_presion`
--

DROP TABLE IF EXISTS `ajuste_presion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ajuste_presion` (
  `id_ajuste` int NOT NULL AUTO_INCREMENT,
  `id_maquina` int DEFAULT NULL,
  `presion_actual` float NOT NULL,
  `nuevo_ajuste` float NOT NULL,
  `fecha_ajuste` datetime NOT NULL,
  PRIMARY KEY (`id_ajuste`),
  KEY `fk_maquina_sopladora` (`id_maquina`),
  CONSTRAINT `fk_maquina_sopladora` FOREIGN KEY (`id_maquina`) REFERENCES `maquina_sopladora` (`id_maquina`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ajuste_presion`
--

LOCK TABLES `ajuste_presion` WRITE;
/*!40000 ALTER TABLE `ajuste_presion` DISABLE KEYS */;
INSERT INTO `ajuste_presion` VALUES (5,250,100,105,'2024-09-21 13:00:00'),(6,250,90,95,'2024-09-21 13:30:54'),(7,250,80,85,'2024-09-21 13:54:20'),(8,250,85,80,'2024-09-21 14:24:20'),(9,250,80,75,'2024-09-21 14:55:14'),(10,250,75,70,'2024-09-21 15:23:10');
/*!40000 ALTER TABLE `ajuste_presion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-08 20:22:23
