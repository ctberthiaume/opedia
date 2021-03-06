USE [master]
GO

/****** Object:  Database [Opedia]    Script Date: 12/5/2017 2:39:00 PM ******/
CREATE DATABASE [Opedia]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Opedia', FILENAME = N'D:\opediaDB\Opedia.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%), 
 FILEGROUP [FG1] 
( NAME = N'Opedia_fg1', FILENAME = N'C:\opediaDB\Opedia_fg1.ndf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%), 
 FILEGROUP [FG2] 
( NAME = N'Opedia_fg2', FILENAME = N'E:\opediaDB\Opedia_fg2.ndf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%), 
 FILEGROUP [FG3] 
( NAME = N'Opedia_fg3', FILENAME = N'F:\opediaDB\Opedia_fg3.ndf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%), 
 FILEGROUP [FG4] 
( NAME = N'Opedia_fg4', FILENAME = N'H:\opediaDB\Opedia_fg4.ndf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
 LOG ON 
( NAME = N'Opedia_log', FILENAME = N'D:\opediaDB\Opedia_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO

ALTER DATABASE [Opedia] SET COMPATIBILITY_LEVEL = 140
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Opedia].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [Opedia] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [Opedia] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [Opedia] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [Opedia] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [Opedia] SET ARITHABORT OFF 
GO

ALTER DATABASE [Opedia] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [Opedia] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [Opedia] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [Opedia] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [Opedia] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [Opedia] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [Opedia] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [Opedia] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [Opedia] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [Opedia] SET  DISABLE_BROKER 
GO

ALTER DATABASE [Opedia] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [Opedia] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [Opedia] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [Opedia] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [Opedia] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [Opedia] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [Opedia] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [Opedia] SET RECOVERY SIMPLE 
GO

ALTER DATABASE [Opedia] SET  MULTI_USER 
GO

ALTER DATABASE [Opedia] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [Opedia] SET DB_CHAINING OFF 
GO

ALTER DATABASE [Opedia] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [Opedia] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [Opedia] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [Opedia] SET QUERY_STORE = OFF
GO

USE [Opedia]
GO

ALTER DATABASE SCOPED CONFIGURATION SET IDENTITY_CACHE = ON;
GO

ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO

ALTER DATABASE [Opedia] SET  READ_WRITE 
GO


