from note_manager import NoteManager

def start():
    # Создаем экземпляр класса управления заметками
    note_manager = NoteManager()

    # Загружаем заметки из файла (если он существует)
    filename = 'notes.json'
    try:
        note_manager.load_notes(filename)
    except:
        pass

    # Основной цикл программы
    while True:
        print('Выберите действие:')
        print('1 - Добавить заметку')
        print('2 - Просмотреть заметку по ID')
        print('3 - Просмотреть все заметки')
        print('4 - Редактировать заметку')
        print('5 - Удалить заметку')
        print('6 - Сохранить заметки в файл')
        print('7 - Выйти из программы')
        choice = input('Введите номер действия: ')

        # Обработка выбранного действия
        if choice == '1':
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            note_id = note_manager.add_note(title, body)
            print(f'Заметка успешно добавлена. ID заметки: {note_id}')
        elif choice == '2':
            note_id = input('Введите ID заметки: ')
            note = note_manager.get_note_by_id(int(note_id))
            if note:
                print(f'ID заметки: {note.id}')
                print(f'Заголовок заметки: {note.title}')
                print(f'Текст заметки: {note.body}')
                print(f'Дата создания или последнего изменения: {note.date}')
            else:
                print('Заметка с таким ID не найдена')
        elif choice == '3':
            notes = note_manager.get_all_notes()
            if notes:
                for note in notes:
                    print(f'ID заметки: {note.id}')
                    print(f'Заголовок заметки: {note.title}')
                    print(f'Текст заметки: {note.body}')
                    print(f'Дата создания или последнего изменения: {note.date}')
            else:
                print('Заметок пока нет')
        elif choice == '4':
            note_id = input('Введите ID заметки: ')
            note = note_manager.get_note_by_id(int(note_id))
            if note:
                title = input('Введите новый заголовок заметки: ')
                body = input('Введите новый текст заметки: ')
                if note_manager.update_note(int(note_id), title, body):
                    print('Заметка успешно обновлена')
                else:
                    print('Не удалось обновить заметку')
            else:
                print('Заметка с таким ID не найдена')
        elif choice == '5':
            note_id = input('Введите ID заметки: ')
            if note_manager.delete_note_by_id(int(note_id)):
                print('Заметка успешно удалена')
            else:
                print('Не удалось удалить заметку')
        elif choice == '6':
            note_manager.save_notes(filename)
            print('Заметки успешно сохранены в файл')
        elif choice == '7':
            break
        else:
            print('Некорректный выбор действия')
