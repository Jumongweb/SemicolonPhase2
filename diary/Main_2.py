# import time
#
# from SemicolonPhase2.diary import *
# from tkinter import simpledialog, messagebox
#
# from SemicolonPhase2.diary.TitleLengthException import TitleLengthException
# from SemicolonPhase2.diary.diary import Diary
# from SemicolonPhase2.diary.entry import Entry
#
#
# class DiaryMain:
#
#     def main_menu(self):
#         try:
#             print("=" * 50)
#             print("""
#                 What would you like to do
#                 1. Create entry
#                 2. Unlock diary
#                 3. lock diary
#                 4. Find entry
#                 5. Delete entry
#                 6. Update entry
#                 7. Exit
#             """)
#             print("=" * 50)
#             response = int(input("Enter your response: "))
#
#             match response:
#                 case 1:
#                     self.create_entry()
#                     self.main_menu()
#                 # case 2: unlock_diary();
#                 # case 3: lock_diary();
#                 case 7:
#                     print("Goodbye!!!")
#                     print("Hope to see you soon")
#                     exit(-100)
#                 case _:
#                     print("Number should be between 1-7")
#                     self.main_menu()
#
#         except ValueError:
#             print("Select from 1 - 7")
#             self.main_menu()
#
#     def prompt_user(self):
#         print("Welcome to Hades Diary")
#         print("Your secret is save with me")
#         user_name = input("Enter your username: ")
#         password = input("Enter your password: ")
#         Diary(user_name, password)
#
#     def create_entry(self):
#         title = simpledialog.askstring("Enter your title: ")
#         body = simpledialog.askstring("write something here: ")
#         # title = input("Enter your title: ")
#         # password = input("Enter your password: ")
#         diary.create_entry(title, body)
#         self.create_entry(title, body)
#
#         print("Entry successfully created")
#
#     # user_name = input("Enter Your User_name: ")
#     # password = input("set password: ")
#     # diary = Diary(user_name, password)
#     # print(f"Welcome {user_name} your diary has been created successfully")
#     # return diary
#
#
# if __name__ == '__main__':
#     # DiaryMain().prompt_user()
#     diary = DiaryMain
#     diary.main_menu()
