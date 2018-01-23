Regular expresion ::::::::::::::::::::::::::::::::::::::::::::::::::::

#  Регулярное выражение - это правило, задающее критерии 
# поиска нужного фраг­мента в исходной строке и, возможно, 
# манипуляции с найденным фрагментом. Оно включает собственно 
# искомые символы и некоторые знаки и их последовательно­сти, 
# имеющие специальное значение и называемые литералами. Литералы 
# регу­лярных выражений либо обозначают какое-либо подмножество 
# искомых символов, либо действие, которое нужно вьшолнить 
# над соседними указанными в выражении символами.
# Модуль re поддерживает более мощные и стандартизированные реrулярные 
# вы­ражения в стиле Perl (Perl 5), что позволяет предоставлять 
# нескольким потокам об­щий доступ к одним и тем же скомпилированным 
# объектам реrулярных выражений и поддерживать именованные подгруппы.

# документация на английском:
# https://docs.python.org/3/library/re.html

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import re

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

re.compile(pattern, flags=0)
# Компилирует шаблон регулярного выражения раttern с необязательными 
# флагами flags и возвращает объект регулярного выражения

re.match(pattern, string, flags=0)
# Предпринимает попытку сопоставить шаблон pattern со строкой string, 
# учитывая необязательные флаги flags; возвращает объект сопоставления 
# в случае успеха или значение None в случае неудачного завершения

re.search(pattern, string, flags=0)
# Выполняет поиск первого вхождения шаблона pattern в строке с учетом 
# необязательных флагов flags; возвра­щает объект сопоставления в 
# случае успеха или значение None в случае неудачного завершения

re.findall(pattern, string[,flags])
# Осуществляет поиск всех (неперекрывающихся) вхож­дений шаблона 
# pattern в строке string; возвращает список сопоставлений

re.finditer(pattern, string[,flags])
# То же, что и findall(), но вместо списка возвращает итератор; для 
# каждого сопоставления итератор возвраща­ет объект сопоставления

re.split(pattern, string, max=0)
# Проводит разбиение строки string на основе раздели­теля регулярного 
# выражения раttern и в случае успеха возвращает список полученных 
# сопоставлений, в котором содержится не более чем max фрагментов 
# (по умолчанию разбиение проводится по всем вхождениям)

re.sub(pattern, repl, string, count=0)
# Заменяет все вхождения шаблона регулярного выражения pattern в 
# строке string подстрокой repl, выполняя подстановку вместо всех 
# вхождений, если не задан параметр count (см. также функцию subn(), 
# которая, кроме этого, возвращает количество выполненных подстановок)

re.purge()
# Очищает кеш неявно скомпилированных шаблонов регу­лярного выражения

re.group(num=0)
# Возвращает все сопоставление (или конкретную подгруп­пу num)

re.groups(default=None)
# Возвращает все сопоставленные подгруппы в виде корте­жа (если 
# сопоставления отсутствуют, кортеж пуст)

re.groupdict(default=None)
# Возвращает словарь, содержащий все согласованные именованные 
# подгруппы, в котором ключами являются имена подгрупп (если 
# сопоставления отсутствуют, словарь пуст)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

re.I, re.IGNORECASE
# Сопоставление без учета регистра

re.L, re.LOCALE
# Правила сопоставления с регулярными выражениями, в которых 
# применяются специальные символы \w, \W, \Ь, \В, \э, \S, зависят 
# от региональной установки

re.M, re.MULTILINE
# Применение этого флага приводит к тому, что специаль­ные символы 
# ^ и $ соответственно сопоставляются с нача­лом и концом каждой 
# строки текста (обозначенной симво­лами конца строки) в целевой 
# строке, а не исключительно с началом и концом всей целевой строки

re.S, re.DOTALL
# Специальный символ точки (.) обычно сопоставляется с любым 
# отдельным символом, кроме \n; этот флаг указы­вает, что точка 
# должна сопоставляться также и с ним

re.X, re.VERBOSE
# Все пробельные символы и знак # (а также весь текст, который 
# следует за знаком # в той же строке) пропуска­ются, что позволяет 
# вводить комментарии и способствует повышению удобства для чтения. 
# Пробельные символы и знак # не исключаются, если они представлены 
# в классе символов или экранированы наклонной чертой влево


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
.
# Любой символ

\w 
# Буква, цифра или подчеркивание

\W 
# Не буква, не цифра и не подчеркивание

\d 
# Цифра

\D
# Не цифра

\s 
# Пробельный символ (пробел, табуляция, возврат каретки или 
# перевод строки)

\S
# Не пробельный символ

\b
# Начало или конец слова

\В 
# Не начало и не конец слова

^ и \А 
# Начало строки

$ и \Z 
# Конец строки

[<набор>] 
# Любой символ из набора

A|B 
# Либо символ А, либо символ В

*
# Предыдущий символ может присутствовать произвольное 
# количество раз, а может и не присутствовать вообще

+ 
# Предыдущий символ должен присутствовать в строке как 
# минимум один раз

? 
# Предыдущий символ должен либо не присутствовать в строке, 
# либо присутствовать один раз

{N} 
# Предыдущий символ должен присутствовать в строке строго 
# N раз

{M,N} 
# Предыдущий символ должен присутствовать в строке от 
# M до N раз

[...]
# Соответствует любому отдельному символу из класса символов

[..x-y..]
# Соответствует любому отдельному символу от x до y

[^...]
# Не соответствует ни одному символу из класса символов,
# включая любые диапазоны, если они заданы

(*|+|?|{})?
# Предусматривает применение "нежданных" версий приведённых
# выше знаков вхождения/повторения (*,+?,{})


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Если нам потребуется найти в строке символ, совпадающий с 
# литералом, мы вклю­чим его в регулярное выражение, предварив 
# обратным слешем (\). Например, регу­лярное выражение \? 
# найдет все символы вопросительного знака.
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::
# В регулярных выражениях мы можем создавать группы символов. 
# Они обрабаты­ваются как единое целое, а совпадающие с ними 
# фрагменты строки впоследствии могут быть извлечены для 
# обработки. 

# Форматы описание групп

(...)
# Соответствует регулярному выражению, заключённому в круглые
# скобки, и сохраняет его в памяти как подгруппу 


(Р<name>...) 
# Обычная группа, но совпадающее значение может быть извлечено 
# путем обращения к имени группы

(?Р=<имя>) 
# Задает последовательность, совпадающую со значением группы 
# с указанным параметром имя

(?=...) 
# Группа, чьим значением станет фрагмент, за которым следует 
# подстрока. Обеспечивает сопоставление, если далее следует 
# шаблон ..., без сохранения в памяти сопоставленной части 
# входной строки; эта операция именуется положительной 
# опережающей проверкой (positive lookahead assertioп)

(?!...) 
# Группа, чьим значением станет фрагмент, за которым не 
# следует подстрока. Обеспечивает сопоставление, если далее 
# не следует шаблон ..., без сохранения в памяти сопоставленной 
# части входной строки; эта операция именуется отрицательной 
# опережающей проверкой (пegative lookahead asseгtioп)

(?<=...) 
# Группа, чьим значением станет фрагмент, перед которым следует 
# подстрока. Обеспечивает сопоставление, если далее находится 
# шаблон ..., без сохранения в памяти сопоставленной части 
# входной строки; эта операция именуется положительной 
# ретроспективной проверкой (positive lookbehiпd assertioп)

(?<!...) 
# Группа, чьим значением станет фрагмент, перед которым не 
# следует подстрока. Обеспечивает сопоставление, если далее 
# не находится шаблон ..., без сохранения в памяти сопоставленной 
# части входной строки; эта операция именуется отрицательной 
# ретроспективной проверкой (positive lookЬehiпd assertioп)

(?:...) 
# Обозначает группу содержимое которой не сохраняется в памяти

(?#...)
# Задаёт примечание, всё содержимое примечание игнарируется 


(?(id/name)Y|N)
# Обеспечивает сопоставление регулярного выражения У по условию, 
# если группа с указанным идентификатором или именем существует; 
# в противном случае возвращает N; часть |N является необязательной
