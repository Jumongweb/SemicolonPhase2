import unittest

from SemicolonPhase2.diary.InvalidPasswordException import InvalidPasswordException
from SemicolonPhase2.diary.diary import Diary
from SemicolonPhase2.diary.entry import Entry


class TestDiaryFunctions(unittest.TestCase):
    # def setUp(self):
    #     self.diary = Diary("user_name", "password")
    #     self.assertTrue(self.diary.is_locked)


    def test_thatNoOfEntriesIsZeroByDefault(self):
        self.diary = Diary("user_name", "password")
        self.assertEqual(0, self.diary.no_of_entries())

    def test_create_entry(self):
        self.diary = Diary("user_name", "password")
        self.assertEqual(0, self.diary.no_of_entries())
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.assertEqual(1, self.diary.no_of_entries())

    def test_DiaryCanAcceptMultipleEntries(self):
        self.diary = Diary("user_name", "password")
        self.assertEqual(0, self.diary.no_of_entries())
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.assertEqual(3, self.diary.no_of_entries())

    
    # def test_DiaryCannotBeUnlockedWithWrongPassword(self):
    #     self.diary = Diary("user_name", "password")
    #     with self.assertRaises(InvalidPasswordException) as e:
    #         self.diary.unlocked("wrong_password")
    #
    # def test_IhaveADiaryAndItIsLocked(self):
    #     self.diary = Diary("user_name", "password")
    #     self.assertTrue(self.diary.is_locked)
    #
    # def test_DiaryIsLocked_UnlockDiary(self):
    #     self.diary = Diary("user_name", "password")
    #     self.assertTrue(self.diary.is_locked)
    #     self.diary.unlocked("password")
    #     self.assertFalse(self.diary.is_locked)
    #
    # def test_set_up_diary(self):
    #     self.diary.unlocked("password")
    #     self.assertFalse(self.diary.is_locked)
    #
    # def test_enter_wrong_password_diary_remains_locked(self):
    #     self.diary.unlocked("incorrect_password")
    #     self.assertTrue(self.diary.is_locked)
    #
    # def test_that_diary_can_be_lock(self):
    #     self.diary.lock()
    #     self.assertTrue(self.diary.is_locked)
    #
    # def test_find_entry_by_id(self):
    #     self.diary.unlocked("password")
    #     self.assertFalse(self.diary.is_locked)
    #
    #     self.diary.create_entry("title", "body")
    #     found_entry = self.diary.find_entry(101)
    #     self.assertEqual(101, found_entry.id_number)
    #
    # def test_delete_entry(self):
    #     self.diary.unlocked("password")
    #     self.assertFalse(self.diary.is_locked)
    #
    #     self.diary.create_entry("title", "body")
    #     self.diary.find_entry(101)
    #     self.assertEqual(len(self.diary.get_entries()), 1)
    #
    #     self.diary.delete_entry(101)
    #     self.assertEqual(len(self.diary.get_entries()), 0)
    #
    # def test_update_entry(self):
    #     self.diary.unlocked("password")
    #     self.assertFalse(self.diary.is_locked)
    #
    #     self.diary.create_entry("title", "body")
    #     self.diary.update_entry(101, "new_title", "new_body")
    #     found_diary = self.diary.find_entry(101)
    #     self.assertEqual("new_title", found_diary.title)
    #     self.assertEqual("new_body", found_diary.body)


if __name__ == '__main__':
    unittest.main()
