CREATE DATABASE Cinema
GO
USE cinema

CREATE TABLE Films
(
	Id INT PRIMARY KEY IDENTITY,
	[Name] NVARCHAR(50),
	Duration INT,
	Create_year INT,
	Director NVARCHAR(50)
)