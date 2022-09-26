from .repository_base import  RepositoryBase, datetime


class RepositoryCsv(RepositoryBase):

    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def add(self, x:int, y:int, result: int, timestamp = datetime.now()):
        with open(self.connection_string, "a", encoding="utf-8") as f:
            f.write(f"{x};{y};{result};{timestamp}\n")

if __name__ == "__main__":
    path = "../../data/calc.csv"
    repository = RepositoryCsv(path)
    repository.add(1, 2, 3)