import os
import time
from Pipeline import *

if __name__ == '__main__':
    UnzipFile()
    WorksheetsPostalCodes = ReadExcelSheets()

    time.sleep(1)

    ConnectionToPostalCodesDatabase = SQLConnector(
        os.getenv('MARIADB_HOST','localhost'),
        os.getenv('MARIADB_USER','user_db'),
        os.getenv('MARIADB_PASSWORD','password_db'),
        os.getenv('MARIADB_DATABASE','PostalCodes'),
    )
    print(" Connection to Database ".center(65,'='))

    QueryInsert = """
    INSERT INTO PostalCodes (PostalCode,LocationName,LocationType,DistrictName,
    StateName,CityName,PostalCodeAdminName,StateCode,PostalCodeAdminCode,LocationTypeCode,
    DistrictCode,LocationConsecutiveCode,ZoneLocation,CityCode) VALUES (""" + ', '.join(['%s']*14) + ")"
    for dataframe_worksheet in WorksheetsPostalCodes:
        State = dataframe_worksheet.loc[0,'d_estado']
        print(f' Insert Postal Codes from {State} '.center(65,'='))
        
        dataframe_worksheet = CleanPostalCodesDataframe(dataframe_worksheet)
        try:
            ConnectionToPostalCodesDatabase(
                QueryInsert,
                dataframe_worksheet,
            )
        except Exception as e:
            print(e)