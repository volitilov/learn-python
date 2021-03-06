tarfile :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# В отличие от файлов ZIP, архивы формата ТAR не используют сжатие. Обычно 
# такие архи­вы дополнительно сжимаются другим архиватором: GZIP, BZIP2 или 
# LZMA. Однако­ и в этом состоит их другое отличие от ZIР-файлов - они могут 
# включать в свой состав не только файлы, но и папки, хранящие как файлы, 
# так и другие папки. Python поддерживает работу с архивами ТAR - как 
# несжатыми, так и сжатыми.

# документация на английском:
# https://docs.python.org/3/library/tarfile.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from tarfile import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)
# Открываемый файл может быть задан либо в виде имени (параметр name), либо 
# в виде фай­лового объекта (параметр fileobj).
# Параметр mode задает режим открытия и алгоритм сжатия файла. Его значение 
# указывается в виде строки в формате: 'Режим открытия:Алгоритм сжатия'
	'r' or 'r:*'
	# открыть существующий файл для чтения. Если файл не существует, будет 
	# возбуж­дено исключение
	'r:'
	#
	'r:gz'
	#
	'r:bz2'
	# чтение, сжатие BZIP2
	'r:xz'
	#
	'x' or 'x:'
	#
	'x:gz'
	#
	'x:bz2'
	#
	'x:xz'
	# запись, сжатие LZMA
	'a' or 'a:'
	# открыть существующий файл для записи. Если файл не существует, он 
	# будет соз­дан. Если файл существует, новое содержимое будет добавлено 
	# в его конец, а старое со­держимое сохранится. В этом режиме можно 
	# открывать лишь несжатые файлы
	'w' or 'w:'
	# открыть существующий файл для записи. Если файл не существует, будет 
	# возбуж­дено исключение. Если файл существует, он будет перезаписан
	'w:gz'
	#
	'w:bz2'
	#
	'w:xz'
	#
# Параметр compresslevel задает степень сжатия и доступен лишь при указании 
# какого-либо алгоритма сжатия.
# Параметр format указывает формат архива TAR. Для него доступны четыре 
# значения:
	tarfile.USTAR_FORМAT
	# формат POSIX.1-1988 (ustar);
	tarfile.GNU_FORМAT
	# формат GNU;
	tarfile.PAX_FORМAT
	# формат POSIX.1-2001 (рах);
	tarfile.DEFAULT_FORМAT
	# формат по умолчанию, на данный момент - GNU (tarfile.GNU_FORМAT).

# Если параметр dereference имеет значение True, при добавлении в архив 
# символической или жесткой ссылки на самом деле будет добавлен файл или 
# папка, на которую указывает эта ссылка. Если же задать для него значение 
# False (это, кстати, значение по умолчанию), то в архив будет добавлен сам 
# файл ссылки.



TarFile(name=None, mode='r', fileobj=None, format=DEFAULT_FORMAT, 
	tarinfo=TarInfo, dereference=False, ignore_zeros=False, 
	encoding=ENCODING, errors='surrogateescape', pax_headers=None, 
	debug=0, errorlevel=0)
#

# методы объекта tarfile:
	
	getmember(name)
	# возвращает объект класса TarInfо, представляющий хра­нящийся в архиве 
	# элемент с указанным именем.

	getmembers()
	# возвращает сведения обо всех содержащихся в архиве элементах в виде
	# списка объектов класса TarInfo. Отметим, что возвращаются, в том числе, 
	# все файлы и папки, хранящиеся в присутст­вующих в архиве папках

	getnames()
	# возвращает список с именами хранящихся в архиве элементов

	list(verbose=True, *, members=None)
	#

	next()
	# возвращает следующий элемент из находящихся в архиве. Если элементов
	# больше нет, возвращается None

	extractall(path=".", members=None, *, numeric_owner=False)
	# распаковывает сразу несколько или даже все элементы из архива. Параметр 
	# memЬers задает список элементов, представленных объектами класса TarFile, 
	# которые должны быть распакованы, - если он не указан, будут распакованы 
	# все элементы.

	extract(member, path="", set_attrs=True, *, numeric_owner=False)
	# распаковывает указанный эле­мент, который может быть задан в виде имени 
	# или объекта класса TarInfo. Параметр path сообщает архиватору путь, по 
	# которому должен быть распакован элемент, - если он не указан, элемент 
	# будет сохранен там же, где находится сам архив. Если задать для 
	# параметра set_attrs значение False, время последнего изменения элемента 
	# и права дос­тупа для распаковываемого элемента задаст сама операционная 
	# система, если же его значение - Truе (как по умолчанию), эти сведения 
	# будут взяты из архива.

	extractfile(member)
	# открывает для чтения хранящийся в архиве элемент-файл, заданный именем 
	# или объектом класса TarFile. В качестве результата возвращается объект 
	# класса ExFileObject, поддерживающий методы read(), readline(), 
	# readlines(), и итерационный протокол.

	add(name, arcname=None, recursive=True, exclude=None, *, filter=None)
	# добавляет в архив элемент (файл, папку, символи­ческую или жесткую 
	# ссылку) с указанным именем. Параметр arcname задает имя, кото­рое 
	# элемент примет, будучи помещенным в архив. По умолчанmо это изначальное 
	# имя элемента. Если параметру recursive присвоить значение False, папки 
	# будут добавляться в архив без содержащихся в них папок и файлов. По 
	# умолчанюо они добавляются вместе с содержимым.
	# Параметру exclude можно присвоить функцию, которая будет принимать один 
	# пара­метр - имя очередного добавляемого в архив элемента - и возвращать 
	# логическую ве­личину. Если она равна True, элемент не будет добавлен в 
	# архив, если False - то будет. Причем этот элемент может как добавляться 
	# непосредственно в вызове метода add(), так и находиться в добавляемой 
	# папке.

	addfile(tarinfo, fileobj=None)
	#

	gettarinfo(name=None, arcname=None, fileobj=None)
	#

	close()
	# закрывает архивный файл

	pax_headers
	#




TarInfo(name="")
# методы объектов класса TarInfo:

	frombuf(buf, encoding, errors)
	#

	fromtarfile(tarfile)
	#

	tobuf(format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape')
	#

	name
	# имя элемента (файла, папки, жесткой или символической ссылки)

	size
	# размер элемента в байтах

	mtime
	# время последнего изменения элемента

	mode
	# права доступа к элементу

	type
	#

	linkname
	# путь, на который указывает жесткая или символическая ссылка. Доступно 
	# только для элементов-ссылок

	uid
	#

	gid
	#

	uname
	#

	gname
	#

	pax_headers
	#

	isfile() or isreg()
	# возвращают True, если элемент является файлом

	isdir()
	# возвращает тrue, если элемент является папкой

	issym()
	# возвращает тrue, если элемент является символической ссылкой

	islnk()
	# возвращает тrue, если элемент является жесткой ссылкой

	ischr()
	#

	isblk()
	#

	isfifo()
	#

	isdev()
	#



is_tarfile(name)
# возвращает True, если файл с переданным ей именем является архивом TAR.

ENCODING
#

USTAR_FORMAT
#

GNU_FORMAT
#

PAX_FORMAT
#

DEFAULT_FORMAT
#




# exceptions :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

TarError
# базовый класс для всех последующих классов исключений

ReadError
# либо архив поврежден, либо это вообще не архив ТAR

CompressionError
# заданный алгоритм сжатия не поддерживается, или данные по ка­кой-то 
# причине не могут быть сжаты

StreamError
# ошибка обмена данными с файлом архива

ExtractError
# при распаковке данных возникла некритическая ошибка

HeaderError
#