from phonebook import Contact, Phonebook

def run_phonebook():
    file_path = "phonebook.txt"
    phonebook = Phonebook(file_path)
    phonebook.load_contacts()

    while True:
        print("\nМеню справочника: ")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Вывести все контакты")
        print("5. Редактировать контакт")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя: ")
            while True:
                phone_number = input("Введите номер телефона: ")
                if phone_number.startswith('8'):
                    phone_number = '+7' + phone_number[1:]
                if len(phone_number) == 12 and phone_number.startswith('+7'):
                    print("Номер корректный.")
                    break
                else:
                    print("Неправильный формат номера телефона. Попробуйте ещё.")
            comment = input("Добавить комментарий: ")
            contact = Contact(name, phone_number, comment)
            phonebook.add_contact(contact)
            print("Контакт добавлен.")
        elif choice == "2":
            name = input("Введите имя: ")
            if phonebook.delete_contact(name):
                print("Контакт удален.")
            else:
                print("Контакт не найден.")
        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска: ")
            found_contacts = phonebook.search_contact(keyword)
            if found_contacts:
                print("Найденные контакты:")
                for contact in found_contacts:
                    print(contact)
            else:
                print("Контакты не найдены.")
        elif choice == "4":
            phonebook.display_contacts()
        elif choice == "5":
            name = input("Поиск контакта для редактирования: ")
            if phonebook.edit_contact(name):
                print("Контакт успешно отредактирован.")
            else:
                print("Контакт не найден.")
        elif choice == "6":
            break
        else:
            print("Неправильный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    run_phonebook()