from SemicolonPhase2.diary.DiaryLockedException import DiaryLockedException
from SemicolonPhase2.diary.InvalidEntryException import InvalidEntryException
from SemicolonPhase2.diary.InvalidPasswordException import InvalidPasswordException
from SemicolonPhase2.diary.entry import Entry


class Diary:
    def __init__(self, user_name, password):
        self._user_name = user_name
        self._password = password
        self.is_locked = True
        self.entries = []
        self.generate_id = 1000

    def is_diary_locked(self):
        return self.is_locked

    def create_entry(self, title, body):
        if self.is_locked is True:
            raise DiaryLockedException("Diary is locked")

        self.generate_id += 1
        new_entry = Entry(self.generate_id, title, body)
        self.entries.append(new_entry)
        return new_entry

    def get_id(self):
        return self.generate_id

    def unlocked_diary(self, pin):
        if self._password is not pin:
            raise InvalidPasswordException("Invalid password")
        self.is_locked = False
        #return self.is_locked

    def no_of_entries(self):
        return len(self.entries)

    # @property
    # def user_name(self):
    #     return self._user_name
    #
    # @user_name.setter
    # def user_name(self, username):
    #     self._user_name = username
    #
    # @property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, password):
    #     self._password = password

    # def get_entries(self):
    #     return self.entries
    #
    # def lock(self):
    #     self.is_locked = True
    #     return self.is_locked
    #
    # def find_entry(self, id_number):
    #     for entry in self.entries:
    #         if entry.id_number == id_number:
    #             return entry
    #     return None
    #
    # def delete_entry(self, id_number):
    #     entry = self.find_entry(id_number)
    #     self.entries.remove(entry)
    #
    # def update_entry(self, id_number, title, body):
    #     for entry in self.entries:
    #         if entry.id_number == id_number:
    #             entry._title = title
    #             entry._body = body
    def findEntryBy(self, identity):
        search_entry = None
        for entry in self.entries:
            if entry.get_id() == identity:
                search_entry = entry
        if search_entry is None:
            raise InvalidEntryException("Entry not found")
        return search_entry

    def lock_diary(self):
        self.is_locked = True

    def remove_entry(self, identity):
        entry_to_remove = self.findEntryBy(identity)
        if entry_to_remove is None:
            raise InvalidEntryException("Entry not found")
        self.entries.remove(entry_to_remove)

    # def update_entry(self, identity, body, password):
    #     entry_to_update = self.findEntryBy(identity)
    #     if entry_to_update is None:
    #         raise InvalidEntryException("Entry not found")
    #     entry_to_update = body


