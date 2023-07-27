class Contact:
    def __init__(self, name, phone_number, comment):
        self.name = name
        self.phone_number = phone_number
        self.comment = comment

    def __str__(self):
        return f"Имя: {self.name}\nНомер телефона: {self.phone_number}\nКомментарий: {self.comment}"


class Phonebook:
    def __init__(self, file_path):
        self.contacts = []
        self.file_path = file_path

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()    

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.comment.lower():
                found_contacts.append(contact)
        return found_contacts

    def display_contacts(self):
        if not self.contacts:
            print("Справочник пуст.")
        else:
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Контакт найден:")
                print(contact)
                new_name = input("Введите новое имя: ")
                new_phone_number = input("Введите новый номер телефона: ")
                new_comment = input("Введите новый комментарий: ")
                contact.name = new_name
                contact.phone_number = new_phone_number
                contact.comment = new_comment
                self.save_contacts()
                # print("Контакт успешно отредактирован.")
                return True
        return False

    def save_contacts(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number},{contact.comment}\n")

    def load_contacts(self):
        self.contacts = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    if len(data) == 3:  
                        contact = Contact(data[0], data[1], data[2])
                        self.contacts.append(contact)
        except FileNotFoundError:
            pass