PyAutoGUI :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Кросс-платформенная автоматизация графического интерфейса для 
# людей. Способен посылать сигналы виртуальных нажатий клавиш и 
# щелчков мышью операционным системам Windows, Linux, OSX. 

# документация на английском:
# https://pyautogui.readthedocs.io/en/latest/

# установка:
pip install python-xlib pyautogui

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import pyautogui as pg

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.size()
# возвращает кортеж из двух целых чисел, представляющих ширину и 
# высоту экрана в пикселях

pg.position()
# возвращает кортеж из двух целых чисел, представляющих координаты
# текущей позиции указателя

pg.onScreen(x, y)
# возвращает True если x и y находятся в пределах экрана


# мышь ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.moveTo(x, y, duration)
# немедленно перемещает указатель в указанную позицию на экране
# x и y координаты. Необязательный именнованный аргумент duration
# в виде целого или вещественного числа задаёт (в секундах) 
# длительность перемещения указателя в конечную точку. Если его не
# указывать, то duration присваивается значение 0, что приводит к
# мгнавенному перемещению указателя.

pg.moveRel(x, y, duration)
# перемещает указатель мыши относительно его текущей позиции
# x,y перемещение указателя вправо по горизонтали и вниз по 
# вертикали, отрицатильные значения задают обратный направления

pg.click(x, y, button)
# отправить компьютеру виртуальный щелчок мышью, по умолчанию
# предпологается что это щелчок левой кнопкой мыши, в месте 
# текущего указателя мыши. Необязательные аргументы x и y указывают
# где вызвать щелчок. 
# Необязательный именнованный аргумент button указывает какой 
# кнопкой происходит нажатие, могут быть следующие значения
# left, right, middle

pg.mouseDown(x, y, button)
# соответствует лишь нажатие кнопки

pg.mouseUp(x, y, button)
# соответствует лишь отжатие кнопки

pg.doubleClick(x, y)
# выполняет двойной щелчок левой кнопки мыши

pg.rightClick(x, y)
# выполняет нажатие правой кнопки мыши

pg.middleClick(x, y)
# выполняет нажатие средней кнопки мыши

pg.dragTo(x, y, duration)
# перетаскивает нажатый указатель мыши в новое место

pg.dargRel(x, y, duration)
# перетаскивает нажатый указатель мыши в местоположение 
# относительно текущего.

pg.scroll(200)
# принимает целочисленный аргумент, определяющий количество единиц 
# прокрутки в направлении вверх или вниз. Прокрутка осуществляется 
# в текущей позиции курсора. Положительное значение означает 
# прокртку вверх, отрицательное вниз.