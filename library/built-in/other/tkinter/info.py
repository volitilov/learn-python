tkinter :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# это предусмотренная по умолчанию библиотека графического 
# пользо­вательского интерфейса Python. Средства разработки графи­ческого 
# пользовательского интерфейса с применением Tk являются переносимыми и
# гибкими, а также обеспечивают возможносrь применения простого языка 
# сценариев.

# документация на английском:
# https://docs.python.org/3/library/tkinter.html
# http://www.tkdocs.com/index.html
# http://effbot.org/tkinterbook/

# полезно:
# для получения полноценного графического пользовательского ин­терфейса 
# необходимо сделать пять основных шагов.

	# Импортировать модуль Tkinter (для этого применяется конструкция 
	# from Tkinter import *)

	# Создать объект для работы с окнами верхнего уровня, который 
	# содержит всё приложение с графическим пользовательским 
	# интерфейсом.

	# Сформировать все компоненты графического пользовательского 
	# интерфейса (вместе с функциональными средствами) в качестве 
	# надстройки (или вложе­ния) к объекту работы с окнами верхнего 
	# уровня.

	# Подключить эти компоненты графического пользовательского 
	# интерфейса к основному коду приложения.

	# Войти в основной цикл обработки событий.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from tkinter import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Tk(screenName=None, baseName=None, className='Tk', useTk=1)
# создаёт окно верхнего уровня (фундамент, корневое окно)

Tcl(screenName=None, baseName=None, className='Tk', useTk=0)
#

scrolledtext
#

colorchooser
#

commondialog
#

filedialog
#

font
#

messagebox
#

simpledialog
#

dnd
#

turtle
#


# tk widjets ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Frame
# Выполняет исключительно роль контейнера для других графических 
# элементов

Label
# Используется для размещения текста или изображений

Listbox
# Предоставляет пользователю список вариантов, из которых может быть 
# вы­бран только один вариант

Labelframe
# Сочетание метки и рамки, но с дополнительными атрибутами метки

Button
# Аналогичен Label, но предоставляет дополнительные функциональные 
# воз­можности обработки операций наведения курсора, нажатия и отпускания 
# кно­пок мыши, а также действий/событий, связанных с клавиатурой

Canvas
# Обеспечивает возможность рисовать фигуры (линии, овалы, 
# многоугольники, прямоугольники); может содержать изображения, в том 
# числе битовые

Checkbutton
# Набор флажков, любые из которых могут быть установлены (по аналогии 
# с элементом checkЬox языка HTML)

Radiobutton
# Набор кнопок, из которых может быть нажата только одна (по аналогии 
# с эле­ментом ввода radio языка НТМL)

Entry
# Однострочное поле ввода, в котором можно вводить символы с клавиатуры
# (по аналогии с элементом ввода текста языка HTML)

Combobox
#

Menu
# Список команд элемента Menubutton, из которого пользователь может 
# вы­брать только одну команду

Menubutton
# Предоставляет инфраструктуру для создания меню (ниспадающих, 
# каскадных и т.д.)

Message
# Аналогичен Label, но отображает многострочный текст

Scrollbar
# Предоставляет функциональные возможности прокрутки для графических 
# эле­ментов, поддерживающих эту операцию, таких как Text, Canvas, Listbox 
# и Entry

Sizegrip
#

Scale
# Линейный графический элемент ползунка, позволяющий устанавливать 
# точное значение заданного параметра; могут быть установлены начальное 
# и конечное значения

Spinbox
# Элемент, представляющий собой сочетание поля ввода с кнопкой, который 
# по­зволяет задавать корректируемое значение

Separator
#

Text
# Многострочное поле ввода, позволяющее собирать (или отображать) текст,
# вводимый пользователем (по аналогии с элементом textarea языка HTML)

Toplevel
# Аналогичен Frame, но предоставляет отдельный контейнер окна

Progressbar
#

Panedwindow
# Контейнерный графический элемент, с помощью которого можно 
# управлять размещением других графических элементов, которые 
# укладываются в нем

Notebook
#
