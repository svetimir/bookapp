# BOOK APP
# AUTHOR: Georgy Yashin, ifi@yandex.ru
# STARTED: 21.02.2022
# VERSION: 0.0.1
# FILE LATEST REVISION: 21.02.2022 16:37

import os
import tkinter as tk
import re


class App:
    def __init__(self, root):
        root.geometry('500x500')
        root.title('BookApp')
        self.text = tk.Text(root)
        self.text.pack()


class FileList:
    def __init__(self, output):
        self.books = list()
        book = ""
        self.files = os.listdir(os.getcwd())
        i = 0
        for file in self.files:
            tmp = re.search(r"^.*((\.pdf)|(\.txt)|(\.fb2))$", "{0}".format(file))
            if tmp is not None:
                book = "{0}\n".format(tmp.group(0))
                output.text.insert(tk.INSERT, book)
                self.books.append(book)
                i += 1
        if i > 0:
            output.text.insert(tk.END, "Найдено книг: {0}".format(i))


def main():
    pass


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    books = FileList(app)
    root.mainloop()
