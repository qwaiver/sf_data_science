# Проект 0. Угадай число

## Оглавление <a name="UP"></a>
[1. Описание проекта](#description)  
[2. Какой кейс решаем?](#keys)  
[3. Краткая информация о данных](#base)  
[4. Этапы работы над проектом](#steps)  
[5. Результат](#result)    
[6. Выводы](#conclusion) 

### Описание проекта <a name="description"></a>
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[ к оглавлению](#UP)


### Какой кейс решаем? <a name="keys"></a>
Нужно написать программу, которая угадывает рандомно задонное число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных <a name="base"></a>
Имеем генератор числа в диапазоне от 1 до 100, и цикл, который ищет это число.

  
:arrow_up:[ к оглавлению](#UP)


### Этапы работы над проектом  <a name="steps"></a>
1. Ничего не понял
2. Потом как понял
3. Получил точность 2-3 попытки
4. Снова как понял
5. Получил реальну точность 12-13
6. Исправил код, улучшил точность до 9-10 попыток

:arrow_up:[ к оглавлению](#UP)


### Результаты:  <a name="result"></a>
Имеем результат, который лучше пороговых значений в условии~ на 50%

:arrow_up:[ к оглавлению](#UP)


### Выводы:  <a name="conclusion"></a>
Немного расстроен, получилось проще, чем фантазировал изначально, изменение значений в коде
не даёт видимый разброс, для улучшения точности нужно менять подход,
главное, что бы оба значения не делились друг на друга.

 upd: Задание было возвращено, т.к. изменениям подвергалось загаданное число, после исправления кода выяснилось, что начальное значение предполагаемого числа оптимально брать в диапазоне 30-40, при данном алгоритме решения "+7 -3".

:arrow_up:[ к оглавлению](#UP)


Информация не будет интересна,  ⭐️⭐️⭐️зд не надо. Приятного {timeofday}.
