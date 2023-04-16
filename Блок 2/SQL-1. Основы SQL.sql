SELECT /*выбор столбцов*/
    movie_title, /*столбец movie_title*/
    2020 - year, /*столбец, каждое из значений которого ровно разнице 2020 и соответствующего значения столбца year*/
    rating /*столбец rating*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/



SELECT * /*выбор всех столбцов*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/
WHERE position = 1 /*с позицией 1*/


SELECT /*выбор всех полей*/
    position, /*столбец position*/
    movie_title, /*столбец movie_title*/
    year, /*столбец year*/
    director /*столбец director*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/
WHERE year < 1984 /*при условии, что год создания меньше 1984*/


SELECT * /*выбор всех полей*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/
WHERE year <> 2000 /*если год создания не 2000*/

SELECT * /*выбор всех полей*/
FROM sql.kinopoisk /*из таблицы sqk.kinopoisk*/
WHERE year >= 1975 /*при условии, что год создания 1975 и позднее*/
    AND year <= 1985 /*и ранее 1985*/
/*или пишем*/    WHERE year BETWEEN 1975 AND 1985


SELECT * /*выбор всех полей*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/
WHERE year NOT BETWEEN 1965 AND 1980 /*при условии, что год создания не лежит в промежутке между 1965 и 1980*/


SELECT /*выбор*/
    year, /*столбец year*/
    movie_title, /*столбец movie_title*/
    director /*столбец director*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/
WHERE (rating > 8.5 AND year < 2000) /*при условии, что рейтинг больше 8.5 и год создания до 2000*/
    OR year >= 2000 /*или год создания — 2000 и позднее*/



column IN (value1, value2, value3) /*column = value1 OR column = value2 OR column = value3*/


SELECT * /*выбор всех полей*/
FROM sql.kinopoisk /*из таблицы sql.kinopoisk*/
WHERE movie_title LIKE 'А%' /*если название фильма начинается на А*/
/*Знак процента (%) в примере показывает, что после A встречается ноль и более символов. 
Вы можете использовать % в любом месте внутри строки.*/
/*Также в текстовых строках используется знак подчёркивания (_) — он заменяет ровно один любой символ.*/
