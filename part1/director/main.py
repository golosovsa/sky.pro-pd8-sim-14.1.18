# Без повторов
# Запросите список всех режиссеров, которые
# находятся в этой базе.
# Режиссеры должны быть представлены без повторов
#
# Пример результата:
#
# +----------------------+
# |       director       |
# +----------------------+
# |  Jorge Michel Grau   |
# |     Gilbert Chan     |
# |     Shane Acker      |
# +----------------------+
#
# Напиши запрос и выведи режиссеров.
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query: str = ("""
    SELECT DISTINCT director
    FROM netflix
""")  # TODO измените код запроса
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

my_table = prettytable.from_db_cursor(result)
my_table.max_width = 30


if __name__ == '__main__':
    print(my_table)
