import pymysql

class SQLConnector:
    def __init__(
            self,
            Host: str,
            User: str,
            Password: str,
            Database: str,
            Port: int = 3306,
        ):
        """
        Class for managing the connection to 
        a MaridaDB Datbase for only insert 
        values into tables.
        """

        self._ConfigConnection = {
            'host': Host,
            'user': User,
            'password': Password,
            'database': Database,
            'port': Port,
        }

        self._Connection = None
        self.CreateConnection()

    def CreateConnection(self):
        """
        Method for creating a 
        connection to the database.
        """

        try:
            self._Connection = pymysql.connect(
                **self._ConfigConnection,
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
            self._Cursor = self._Connection.cursor()
        except Exception as error:
            print(f"Exception/Error with creation of connection:\n{error}")
    
    def __call__(
            self,
            Query: str,
            Data: dict = None
        ):
        """
        Method for executing the query 
        of insert values into the database.
        """

        self._Cursor.executemany(Query,Data)
        self._Connection.commit()