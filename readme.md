# Mexican Postal Codes Database

## Abstract
This project aims to develop a simple interface in Flask for querying information about Mexican Postal Codes from a Database using SQL queries.

## Database
The data were downloaded from [Descarga de Códigos Postales](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx) and a full description is available on [Origen de los datos](https://github.com/eclipxe13/sepomexphp/blob/master/docs/DATABASE.md). The [SQL schema](./Database/Schema.sql) was created using both resource and renaming the fields (columns) with more useful and descriptive names. Only one table is used for the database because of the technical requirements for this assignment. 

## Pipeline
The database (table) was populated with a Python script which dumps the data downloaded from [Descarga de Códigos Postales](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx). Creates a connection to the database using PyMySQL which is used to insert the postal code records into. This procedure is described in [Pipeline](./Pipeline).

## Query Examples
Some interesting questions about the postal codes can be answered with simple SQL queries. Some of them are:

1. How many cities are there in Mexico? There are 645 cities.
```SQL
SELECT COUNT(DISTINCT CityName) AS `Number of Cities` FROM PostalCodes WHERE CityName != 'None';
```
2. What is the valid range of postal codes in Mexico? From 01000 to 99998
```SQL
SELECT MIN(PostalCode) as `Minimum Recorded Postal Code`, MAX(PostalCode) AS `Maximum Recorded Postal Code` FROM PostalCodes
```
3. List of locations that include "María" in their name
```SQL
SELECT LocationName AS `Location with 'María' in its Name` FROM PostalCodes WHERE LocationName LIKE '%María%';
```
4. Are there more urban or rural locations? There are more rural locations than urban locations
```SQL
SELECT DISTINCT ZoneLocation AS `Location Type`, COUNT(ZoneLocation) AS `Number of Locations` FROM PostalCodes GROUP BY ZoneLocation HAVING ZoneLocation = 'Rural' OR ZoneLocation = 'Urbano' ORDER BY `Number of Locations` DESC
```

The previous queries can be executed from MaridDB shell using the default user and `docker exec -it postal_codes_database mariadb --user user_db --password`. 

## Installation
1. Clone this repository:
```bash
git clone https://github.com/alexisuaguilaru/MexicanPostalCodes.git
```
2. Create a copy of `.env_example` and change their values (credentials) for yours:
```bash
cp .env_example .env
```
3. Start service:
```
docker compose up -d --build
```

## Technologies
* [Python](https://www.python.org/)
  * [PyMySQL](https://pymysql.readthedocs.io/en/latest/)
  * [Flask](https://flask.palletsprojects.com/en/stable/)
* [MariaDB](https://mariadb.org/)
* [Docker](https://www.docker.com/)

## Author, Affiliation and Contact
Alexis Aguilar [Student of Bachelor's Degree in "Tecnologías para la Información en Ciencias" at Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com

Project developed for the subject "Distributed Databases" for the class taught in semester 2026-1.

## License
Project under [MIT License](LICENSE)