# Домашнее задание № 1
## Чтение и запись файл, первичная обработка

Задание посвящено работе с данными содержания озона в атмосфере Земли за несколько десятилетий.
Вам нужно проанализировать данные в формате [NetCDF](https://ru.wikipedia.org/wiki/NetCDF), нарисовать график и вывести статистическую информацию в файл формата [JSON](https://ru.wikipedia.org/wiki/JSON).
Программа должна быть представлена в файле `ozon.py`, график в файле `ozon.png` и выходные результаты в файле `ozon.json`.

**Дедлайн 24 сентября в 23:55**

Вы должны сделать следующее:
- Загрузить файл с данными: <http://www.temis.nl/protocols/o3field/data/multimission/MSR-2.nc> (464 МБ). Информацию о данных смотрите на сайте <http://www.temis.nl/protocols/O3global.html>
- В таблице с успеваймостью найдите город, с которым  будете работать: <https://docs.google.com/spreadsheets/d/1qA9lkkvTUCxgc2h1mRjFH_gaZmp-YyYYFNYXhctx020/edit#gid=0>. Найдите на карте координаты города и запишите их в какую-нибудь переменную
- Программно определите ближайший координатный узел сетки к координатам вашего города.
- Постройте на одном графике разным цветом:
  * Зависимость содержания озона от времени для всего доступного интревала
  * Выберите январь каждого года и постройте график содержания озона только для этих моментов времени
  * То же для июля
- Сохраните график в файл `ozon.png`
- Для каждого из трёх наборов данных определите минимум, максимум и среднее. Запишите результат в файл `ozon.json` со следующей структурой:

```json
{
  "city": "Moscow",
  "coordinates": [37.66, 55.77],
  "jan": {
    "min": 294.0,
    "max": 357.0,
    "mean": 329.5
  },
  "jul": {
    "min": 269.0,
    "max": 298.0,
    "mean": 284.0
  },
  "all": {
    "min": 268.0,
    "max": 389.0,
    "mean": 306.7
  }
}
```
