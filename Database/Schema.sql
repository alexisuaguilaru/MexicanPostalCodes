CREATE TABLE PostalCodes (
    PostalCode CHAR(5) PRIMARY KEY, -- d_codigo
    LocationName TEXT, -- d_asenta
    LocationType VARCHAR(255), -- d_tipo_asenta
    DistrictName TEXT, -- D_mnpio
    StateName VARCHAR(255), -- d_estado
    CityName TEXT, -- d_ciudad
    PostalCodeAdminName CHAR(5), -- d_CP , Postal Administration name
    StateCode INTEGER, -- c_estado
    PostalCodeAdminCode CHAR(5), -- c_oficina , Postal Administration code
    LocationTypeCode INTEGER, -- c_tipo_asenta
    DistrictCode INTEGER, -- c_mnpio
    LocationConsecutiveCode INTEGER, -- id_asenta_cpcons , Unique location identifier (in district)
    ZoneLocation VARCHAR(255), -- d_zona , type of zone location
    CityCode INTEGER -- c_cve_ciudad
);