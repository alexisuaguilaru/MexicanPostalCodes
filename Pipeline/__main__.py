import os
from Pipeline import *

if __name__ == '__main__':
    UnzipFile()
    WorksheetsPostalCodes = ReadExcelSheets()

    ConnectionToPostalCodesDatabase = SQLConnector(
        os.getenv('MARIADB_HOST','localhost'),
        os.getenv('MARIADB_USER','user_db'),
        os.getenv('MARIADB_PASSWORD','password_db'),
        os.getenv('MARIADB_DATABASE','PostalCodes'),
    )

    QueryInsert = "INSERT INTO PostalCodes VALUES (" + ', '.join(['%s']*14) + ")"
    for dataframe_worksheet in WorksheetsPostalCodes:
        for record_postal_code in CleanPostalCodesDataframe(dataframe_worksheet):
            # Convert np.NaN values into Python None 
            nan_values = (record_postal_code != record_postal_code)
            record_postal_code[nan_values] = None

            ConnectionToPostalCodesDatabase(
                QueryInsert,
                tuple(record_postal_code)
            )