# Mexican Postal Codes Database

## Abstract
This project aims to develop a simple interface in Flask for querying information about Mexican Postal Codes from a Database using SQL queries.

## Database
The data were downloaded from [Descarga de Códigos Postales](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx) and a full description is available on [Origen de los datos](https://github.com/eclipxe13/sepomexphp/blob/master/docs/DATABASE.md). The [SQL schema](./Database/Schema.sql) was created using both resource and renaming the fields (columns) with more useful and descriptive names. Only one table is used for the database because of the technical requirements for this assignment.

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
docker compose up -d
```

## Technologies
* [Python](https://www.python.org/)
  * [Flask](https://flask.palletsprojects.com/en/stable/)
* [MariaDB](https://mariadb.org/)
* [Docker](https://www.docker.com/)

## Author, Affiliation and Contact
Alexis Aguilar [Student of Bachelor's Degree in "Tecnologías para la Información en Ciencias" at Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com

Project developed for the subject "Distributed Databases" for the class taught in semester 2026-1.

## License
Project under [MIT License](LICENSE)