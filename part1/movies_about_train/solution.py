import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT `title` "
                "FROM netflix "
                "WHERE title LIKE '%train%' "
                "AND `type`='Movie'")
result = cur.execute(sqlite_query)
my_table = prettytable.from_db_cursor(result)
my_table.max_width = 30

if __name__ == '__main__':
    print(my_table)
