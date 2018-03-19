http ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# представляет собой пакет, который собирает несколько модулей для работы с 
# протоколом передачи HyperText.

# документация на английском:
# https://docs.python.org/3/library/http.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import http

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

http.client
# является клиентом протокола низкого уровня HTTP; для открытия URL-адресов 
# высокого уровня используйте urllib.request
# смотреть 'client/'

http.server
# содержит базовые классы HTTP-сервера на основе socketserver
# смотреть 'server/'

http.cookies
# содержит утилиты для рабаты с кукисами
# смотреть 'cookies/'

http.cookiejar
# обеспечивает сохранение файлов cookie
# смотреть 'cookiejar/'


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

http.HTTPStatus
# содержит список кодов состояния с их описанием