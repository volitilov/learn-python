TabStop :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Отдельная вкладка перестает применяться к абзацу или стилю. 
# Доступ к использованию семантики списка в его содержимом 
# объекта TabStops.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта font
paragraph = Document(docx_file).paragraphs[0]
tab_stop = paragraph.tabstops[0]

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

alignment
#

leader
#

position
#
