# Урок 14
Для начала работы скопируйте репозиторий на локальную машину:
c помощью команды в терминале

`https://github.com/skypro-008/lesson14-and-tests.git`

Откройте склонированный репозиторий в PyCharm.

### Cоздайте виртуальное окружение, для этого:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson15)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значек ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК
#### Настройка виртуального окружения завершена!

### Далее необходимо установить зависимости для корректной работы тренажера
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

### Порядок выполнения заданий
### Этот урок разделён на 2 части:
#### Часть 1:

- part1/director
- part1/movies_about_train
- part1/movies_year
- part1/old_new
- part1/where_plays
- part1/where_plays_2

#### Часть 2:
- part2/full_long
- part2/how_many_seasons
- part2/india
- part2/long_film
- part2/new_film

Задачи описаны в комментариях в файле main.py
Вам будет необходимо составить запросы на SQL
После того, как вы составили запрос попробуйте запустить фаил main.py.
Вы можете это сделать кликнув на него правой кнопкой мыши в окне проекта.

Если Ваш запрос сработал корректно и ошибок не возникло, проверьте правильность
его составления, запустив таким же образом фаил tests.py который находится
в той же директории, что и фаил с заданием.

*Обращаем ваше внимание, что для каждого задания предусмотрены свои тесты
и запускать нужно именно те тесты, которые находятся в папке с заданием*

