import json, datetime
from note import Note

class NoteManager:
    def __init__(self):
        self.notes = []

    # Метод для добавления заметки
    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = Note(note_id, title, body, date)
        self.notes.append(note)
        return note_id

    # Метод для получения заметки по ID
    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    # Метод для получения всех заметок
    def get_all_notes(self):
        return self.notes

    # Метод для обновления заметки
    def update_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.body = body
            note.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return True
        return False

    # Метод для удаления заметки по ID
    def delete_note_by_id(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            return True
        return False

    # Метод для сохранения заметок в файле JSON
    def save_notes(self, filename):
        notes_list = []
        for note in self.notes:
            notes_list.append({'id': note.id, 'title': note.title, 'body': note.body, 'date': note.date})
        with open(filename, 'w') as file:
            json.dump(notes_list, file)

    # Метод для загрузки заметок из файла JSON
    def load_notes(self, filename):
        with open(filename) as file:
            notes_list = json.load(file)
            for note_data in notes_list:
                note = Note(note_data['id'], note_data['title'], note_data['body'], note_data['date'])
                self.notes.append(note)