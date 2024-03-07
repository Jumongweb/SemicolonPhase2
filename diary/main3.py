import sys
import tkinter as display
from tkinter import simpledialog, messagebox

from SemicolonPhase2.diary.diary import Diary


class DiaryMain():
    def __init__(self):
        self.root = display.Tk()
        self.root.withdraw()
        #self.diaries: Diaries = Diaries()
        self.diary: Diary = Diary("", "")

    def landing_page(self):
        option = simpledialog.askinteger("Home page", """
        select
        1. create Diary
        2. Exit
        """)
        match option:
            case 1:
                self.create_diary()
            case 2:
                sys.exit(-1)
            case _:
                print("Select only 1 or 2")
                self.landing_page()

        def create_diary(self):
            try:
                user_name = simpledialog.askstring("Welcome to Hades Diary")
                password = simpledialog.askstring("Your secret is save with me")
                #self.diary
                Diary(user_name, password)
                #self.diaries.add(self.diary)
                messagebox.showinfo("Success", "Diary Created successfully")
                self.display_menu()
            except Exception as e:
                messagebox.showerror("Error", "Invalid username or password")
                self.create_diary()

def display_menu(self):
    try:
        print("=" * 50)
        print("""
            What would you like to do
            1. Create entry
            2. Unlock diary
            3. lock diary
            4. Find entry
            5. Delete entry
            6. Update entry
            7. Exit
            """)
        print("=" * 50)
        response = int(input("Enter your response: "))

        match response:
            case 1:
                self.create_entry()
                self.main_menu()
            # case 2: unlock_diary();
            # case 3: lock_diary();
            case 7:
                print("Goodbye!!!")
                print("Hope to see you soon")
                exit(-100)
            case _:
                print("Number should be between 1-7")
                        #self.main_menu()

    except ValueError:
        print("Select from 1 - 7")
        self.main_menu()



if __name__ == "__main__":
    main = DiaryMain()
    main.landing_page()