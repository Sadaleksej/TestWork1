import json
import datetime

notes = []

def create_note():
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes()

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def read_notes():
    with open('notes.json', 'r') as file:
        notes = json.load(file)
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
            print(note['body'])
            print()

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            break
    else:
        print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes()
            break
    else:
        print("Заметка с таким ID не найдена.")

def filter_notes_by_date():
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == filter_date.date()]
        for note in filtered_notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
            print(note['body'])
            print()
    except ValueError:
        print("Некорректный формат даты.")

def note_taking_app():
    while True:
        print("\nМеню:\n1. Создать заметку\n2. Просмотреть заметки\n3. Редактировать заметку\n4. Удалить заметку\n5. Поиск заметок по дате\n6. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

note_taking_app()