from pymssql import Connection, Cursor
import pymssql

connection: Connection
with pymssql.connect(
        server="yand.dyndns.org",
        database="AdventureWorks",
        user="northwind",
        password="northwind"
) as connection:
    sql = "SELECT Name, ListPrice FROM Production.Product"
    cursor: Cursor
    with connection.cursor() as cursor:
        cursor.execute(sql)
        products = cursor.fetchall()

    # print(products)

    # Вывести список товаров с ценами
    # for p in products:
    #     print(f"{p[0]}\t-\t{p[1]}")

    # Подсчитать количество товаров у которых не указана субкатегория
    # sql = "SELECT ProductSubcategoryID FROM Production.Product"
    # with connection.cursor() as cursor:
    #     cursor.execute(sql)
    #     categories: list[tuple] = cursor.fetchall()
    #
    # print(len(list(filter(lambda c: c[0] is None, categories))))

    sql = "SELECT COUNT(*) FROM Production.Product WHERE ProductSubcategoryID IS NULL"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()

    print(result[0])