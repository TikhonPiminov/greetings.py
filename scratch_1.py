note_name = input("Название заметки: ")#имя заметки .дата создания заметки и на какое число ставится заметка
description_of_the_note = input("Описание заметки: ")
day = input("День оповещения о заметке : ")
month = input(",месяц: ")
years = input(",год: ")
notification_date= day+"-"+ month+"-"+ years
print(f"Запланированное оповещение: {notification_date}")