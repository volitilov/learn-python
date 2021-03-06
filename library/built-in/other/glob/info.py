glob ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Этот модуль находит все пути, совпадающие с заданным шаблоном в 
# соответствии с правилами, используемыми оболочкой Unix. 

# документация на английском:
# https://docs.python.org/3/library/glob.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from glob import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

* # любое количество символов

? # любой одиночный символ

[abc] # совподает с символами a, b или c

[!abc] # совподает со всеми символами кроме a, b, c


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

glob(pathname, *, recursive=False)
# возвращение список (возможно, пустой) путей, соответствующих шаблону 
# pathname. Путь может быть как абсолютным 
# (например, /usr/src/Python-1.5/Makefile) или относительный 
# (как ../../Tools/*/*.gif). 

iglob(pathname, *, recursive=False)
# возвращает итератор, дающий те же значения, что и glob.glob

escape(pathname)
# экранирует все специальные символы для glob ("?", "*" и "["). Специальные 
# символы в имени диска не экранируются (так как они там не учитываются), 
# то есть в Windows escape("//?/c:/Quo vadis?.txt") возвращает 
# "//?/c:/Quo vadis[?].txt". 
