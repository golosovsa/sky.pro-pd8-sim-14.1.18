# Полная длительность
# Представим, что мы решили пересмотреть все фильмы 2010 года,
# и нам нужно прикинуть, сколько дней отпуска нужно взять,
# чтобы совершить такой подвиг.
# Посчитайте длительность всех фильмов 2010 года,
# и выведите результат в полных часах
#
# Пример результата:
#
# Чтобы посмотреть все фильмы, нам нужно 100 часов.
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
import operator
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("""
    SELECT SUM(duration) FROM netflix
    WHERE `type` = 'Movie'
    AND `release_year` = 2010
""")  # TODO измените код запроса
cur.execute(sqlite_query)
executed_query = cur.fetchall()
# print(executed_query)
# result = sum(map(operator.itemgetter(0), executed_query)) // 60
result = f"Чтобы посмотреть все фильмы, нам нужно {executed_query[0][0] // 60} часов."
# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате
con.close()

if __name__ == '__main__':
    print(result)
