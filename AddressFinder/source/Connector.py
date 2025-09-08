import time
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
        a MaridaDB Database for only querying 
        information.
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

        for _ in range(5):
            time.sleep(3)
            try:
                self._Connection = pymysql.connect(
                    **self._ConfigConnection,
                    charset = 'utf8mb4',
                    cursorclass = pymysql.cursors.DictCursor
                )
                self._Cursor = self._Connection.cursor()
                break
            except Exception as error:
                print(f"Exception/Error with creation of connection:\n{error}")
    
    def __call__(
            self,
            Query: str,
            Data,
        ):
        """
        Method for executing the query 
        """

        self._Cursor.execute(Query,Data)
        return self._Cursor.fetchone()