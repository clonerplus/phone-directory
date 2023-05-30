import sys
import gc

from pynput import keyboard
from multiprocessing import Process, Queue

global first_menu, phone_book, sw
sw = ""


def on_press(key):
    global first_menu, phone_book, listener, sw
    try:
        sw += key.char
        phone_book.show_related_contacts()

    except AttributeError:
        if key == keyboard.Key.backspace:
            sw = sw[:-1]
            phone_book.show_related_contacts(sw)
        if key == keyboard.Key.esc:
            if first_menu:
                listener.stop()


def on_release(key):
    # print('{0} released'.format(
    #     key))
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False
    pass


def make_listener():
    return keyboard.Listener(on_press=on_press, on_release=on_release)


def should_be_before(name, new_name):
    names = [name, new_name]
    if sorted(names) == names:
        return True

    return False


class Contact:
    def __init__(self, name, add):
        self.name = name
        self.address = add
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_end(self, name, add):
        new_node = Contact(name, add)

        if not self.head:
            self.head = new_node
            self.tail = self.head
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.tail = new_node

    def insert_to_first(self, name, add):
        new_node = Contact(name, add)

        if not self.head:
            self.head = new_node
            self.tail = self.tail
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_contact(self, new_name, new_add):
        if self.head is None:
            self.insert_to_end(new_name, new_add)
            return

        insert_to_first = True
        current = self.head
        while current is not None and should_be_before(current.name, new_name):
            current = current.next
            insert_to_first = False

        new_node = Contact(new_name, new_add)

        if insert_to_first:
            self.insert_to_first(new_name, new_add)
            return

        if current is None:
            self.insert_to_end(new_name, new_add)
            return

        current = current.prev
        if current.next:
            current.next.prev = new_node
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current
            return
        current.next = new_node
        new_node.prev = current
        self.tail = new_node

    def remove_contact(self, name):
        if self.head is None:
            print("\nThere is no contact with the entered name!")
        elif self.head.name == name:
            if self.head.next:
                self.head = self.head.next
                return

            self.head = None

        elif self.tail.name == name:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head.next
            while current is not None and current.name != name:
                current = current.next
            if current is None:
                print("\nThere is no contact with the entered name!")
                return
            current.prev.next = current.next
            current.next.prev = current.prev
            print("\nThe contact deleted successfully.")

    def show_related_contacts(self):
        if self.head is None:
            print("\nNo contact is found!")
            print("\n3- Searching for contact: ", sw, end='')
            return

        current = self.head
        related_list = DoublyLinkedList()

        while current is not None:
            if sw in current.name:
                related_list.insert_contact(current.name, current.address)
            current = current.next

        current = related_list.head
        while current is not None:
            print(current.name, current.address)
            current = current.next

        print("\n3- Searching for contact: ", sw[:-1], end='')
        return

    def show_reverse(self):
        current = self.tail
        while current is not None:
            print(current.name, end="<->")
            current = current.prev

    def show(self):
        current = self.head
        while current is not None:
            print(current.name, end="<->")
            current = current.next


def menu():
    global first_menu, phone_book, listener

    phone_book = DoublyLinkedList()

    while True:
        first_menu = True

        print("\n\nEnter your command:\n\n1- Add new contact.\n2- Delete existing contact.\n3- Search for a "
              "contact.\n4- Exit.\n\n: ", end='')

        order = input()

        if order == '1':
            print("\n1- Enter contact name and number: (e.g., Hana 09134567890)")
            name_address = input().split()
            name = name_address[0]
            address = name_address[1]
            phone_book.insert_contact(name, address)
            print("\ncontact added successfully")
            phone_book.show()

        elif order == '2':
            print("\n2- Enter the contact’s name to delete: (e.g., Hana)")
            name_to_delete = input()
            phone_book.remove_contact(name_to_delete)
            gc.collect()
            phone_book.show()

        elif order == '3':
            print("\n3- Searching for contact: ", end='')
            listener = make_listener()
            listener.start()
            listener.join()

        elif order == '4':
            exit(0)

        else:
            print("\n*** wrong option! ***")


if __name__ == '__main__':
    menu()
    # process1.terminate()
