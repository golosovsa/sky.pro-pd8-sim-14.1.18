# Болливуд
#
# Индийские фильмы одно время были очень популярны.
# Давайте проверим, как это отразилось на Нетфликсе!
# Нам нужно посчитать, сколько индийских фильмов и сериалов есть на платформе.
#
# Пример результата:
#
# фильмы: 50 шт
# сериалы: 10 шт
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

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
# sqlite_query = ("""
#     SELECT
#     (
#         SELECT COUNT(`type`)
#         FROM netflix
#         WHERE `country` LIKE '%India%'
#         AND `type` = 'TV Show'
#     ),
#     (
#         SELECT COUNT(`type`)
#         FROM netflix
#         WHERE `country` LIKE '%India%'
#         AND `type` = 'Movie'
#     )
# """)  # TODO измените код

sqlite_query = ("""
    SELECT `type`, COUNT(*) FROM netflix
    where `country` LIKE '%India%'
    GROUP BY `type`
""")

cur.execute(sqlite_query)
executed_query = cur.fetchall()

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате

result = f"фильмы: {executed_query[0][1]} шт\nсериалы: {executed_query[1][1]} шт"

con.close()

if __name__ == '__main__':
    print(result)
