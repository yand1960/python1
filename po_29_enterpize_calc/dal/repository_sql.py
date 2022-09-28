from pymssql import Connection, Cursor
import pymssql
from .repository_base import RepositoryBase, datetime


class RepositorySql(RepositoryBase):

    def __init__(self, connectionString: str):
        params = connectionString.split(";")
        self.server = params[0]
        self.database = params[1]
        self.user = params[2]
        self.password = params[3]

    def add(self, x:int, y:int, result: int, timestamp: datetime = datetime.now ):

        connection: Connection
        with pymssql.connect(
                server=self.server,
                database=self.database,
                user=self.user,
                password=self.password
        ) as connection:

            # Вообще-то так нельзя: уязвимо для sql инжекции
            sql = f"INSERT INTO calcs(x,y,result,author) VALUES({x},{y},{result},'YA')"
            cursor: Cursor
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
