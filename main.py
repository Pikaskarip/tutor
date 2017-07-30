import time
import tutor

com_exit = 0
while com_exit == 0:
    orig_com = input(">>>: ")
    command = orig_com.lower()
    if command == "time":
        print(time.strftime("{} %H:%M:%S").format("Сейчас"))
    elif command[0:4] == "add ":
        anime_name = orig_com[4:]
        if len(anime_name) > 0:
            tutor.list_write(anime_name)
            print(anime_name, "было успешно добавлено!")
        else:
            print("Пустая строка! Ничего не было добавлено")
    elif command == "list":
        [print(c) for c in tutor.list_read()]
    elif command == "html":
        result = tutor.gen_html()
        if result:
            print("HTML файл сгенерирован успешно!")
        else:
            print("HTML файл не был сгенерирован! Ваш список пуст")
    elif command == "exit":
        print("Bye-bye!")
        com_exit = True
    elif command[0:7] == "remove ":
        anime_name = orig_com[7:]
        if anime_name:
            result = tutor.list_remove(anime_name)
            if result:
                print(anime_name, "было успешно удалено!")
            else:
                print(anime_name, "не было найдено!")
        else:
            print("Укажите название аниме для удаления!")
    elif command == "help":
        scr_help = """Привет! Ты используешь скрипт великого гладиатора Влада
    Доступные комманды:
    - help                  - вызывает данное сообщение
    - time                  - покажет текущее время
    - exit                  - выйти из скрипта
    - add {название_аниме}  - добавить аниме в список
    - list                  - просмотреть список аниме в консоли
    - html                  - получить список аниме в html файле
    - remove                - удалить аниме из списка
    - edit                  - изменить объект"""
        print(scr_help)
    else:
        print('Unknown command! Type help to get help.')

# Test for git
