# from po_29_enterpize_calc.dal.repository_csv  import RepositoryCsv
from po_29_enterpize_calc.dal.repository_sql  import RepositorySql

class Calculations:

    def __init__(self, connection_string):
        self.repository = RepositorySql(connection_string)

    def plus(self, x: int, y:int) -> int:
        result = x + y
        self.repository.add(x, y, result)
        return x + y;

    def minus(self, x: int, y: int) -> int:
        return x - y;