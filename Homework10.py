from collections import UserDict


class Record:
    def __init__(self, name: str, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == "__main__":
    name = Name("Bill")
    phone1 = Phone("1234567890")
    phone2 = Phone("9876543210")

    rec = Record(name, phone1)
    rec.add_phone(phone2)

    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert isinstance(ab["Bill"].phones[1], Phone)

    edited_phone = Phone("5555555555")
    rec.edit_phone(phone1, edited_phone)

    assert ab["Bill"].phones[0].get_value() == "5555555555"

    # rec.remove_phone(phone1)
    assert len(ab["Bill"].phones) == 2

    print("All Ok")
