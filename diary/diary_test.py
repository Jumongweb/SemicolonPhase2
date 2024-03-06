import unittest

from SemicolonPhase2.diary.DiaryLockedException import DiaryLockedException
from SemicolonPhase2.diary.InvalidEntryException import InvalidEntryException
from SemicolonPhase2.diary.InvalidPasswordException import InvalidPasswordException
from SemicolonPhase2.diary.diary import Diary
from SemicolonPhase2.diary.entry import Entry


class TestDiaryFunctions(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("user_name", "password")
        self.assertTrue(self.diary.is_diary_locked())

    def test_thatIHaveADiaryAndItIsLocked(self):
        self.diary = Diary("username", "password")
        self.assertTrue(self.diary.is_diary_locked())

    def test_thatDiaryIsLocked_unlockDiary(self):
        self.diary = Diary("username", "password")
        self.assertTrue(self.diary.is_diary_locked())
        self.diary.unlocked_diary("password")
        self.assertFalse(self.diary.is_diary_locked())

    def test_thatNoOfEntriesIsZeroByDefault(self):
        self.diary = Diary("user_name", "password")
        self.assertEqual(0, self.diary.no_of_entries())

    def test_create_entry(self):
        self.assertTrue(self.diary.is_diary_locked())
        self.diary.unlocked_diary("password")
        self.assertFalse(self.diary.is_diary_locked())
        self.assertEqual(0, self.diary.no_of_entries())
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.assertEqual(1, self.diary.no_of_entries())

    def test_thatICannotCreateEntryWhenDiaryIsLocked(self):
        self.assertTrue(self.diary.is_diary_locked())
        with self.assertRaises(DiaryLockedException):
            self.diary.create_entry("title", "This is my fourth entry but it will throw an exception")

    def test_DiaryCanAcceptMultipleEntries(self):
        self.diary.unlocked_diary("password")
        self.assertEqual(0, self.diary.no_of_entries())
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.diary.create_entry("title", "Hello diary. This is my first entry")
        self.assertEqual(3, self.diary.no_of_entries())

    def test_ThatDiaryCanBeSearchForUsingId(self):
        self.diary.unlocked_diary("password")
        self.assertFalse(self.diary.is_diary_locked())
        self.assertEqual(0, self.diary.no_of_entries())
        diary_one = self.diary.create_entry("title", "Hello diary. This is my second entry")
        self.assertEqual(1, self.diary.no_of_entries())
        self.assertEqual(diary_one, self.diary.findEntryBy(1001))

    def test_thatDiaryThrowExceptionIfDiaryThatDoesNotExistIsSearchFor(self):
        self.assertTrue(self.diary.is_diary_locked())
        self.diary.unlocked_diary("password")
        self.assertFalse(self.diary.is_diary_locked())
        diary_one = self.diary.create_entry("title", "Hello diary. This is the third entry")
        self.assertEqual(1, self.diary.no_of_entries())
        self.assertEqual(diary_one, self.diary.findEntryBy(1001))
        with self.assertRaises(InvalidEntryException):
            self.diary.findEntryBy(1002)

    def test_DiaryCannotBeUnlockedWithWrongPassword(self):
        self.diary = Diary("user_name", "password")
        self.assertTrue(self.diary.is_diary_locked())
        with self.assertRaises(InvalidPasswordException) as e:
            self.diary.unlocked_diary("wrong_password")

    def test_thatMyDiaryCanBeLockedWithLockedFunction(self):
        self.assertTrue(self.diary.is_diary_locked())
        self.diary.unlocked_diary("password")
        self.assertFalse(self.diary.is_diary_locked())
        self.diary.create_entry("title", "Body of diary")
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_diary_locked())

    def test_thatMyDiaryCanDeleteEntry(self):
        self.assertTrue(self.diary.is_diary_locked())
        self.diary.unlocked_diary("password")
        self.diary.create_entry("title", "Body of diary")
        self.assertEqual(1, self.diary.no_of_entries())
        self.diary.remove_entry(1001)
        self.assertEqual(0, self.diary.no_of_entries())

    def test_thatMyDiaryThrowExceptionIfUserTryToDeleteEntryThatDoesntExist(self):
        self.diary = Diary("user_name", "password")
        self.assertTrue(self.diary.is_diary_locked())
        self.diary.unlocked_diary("password")
        self.diary.create_entry("title", "Body of diary")
        self.assertEqual(1, self.diary.no_of_entries())
        self.diary.remove_entry(1001)
        with self.assertRaises(InvalidEntryException):
            self.diary.findEntryBy(1001)

    # def test_thatMyDiaryCanUpdateEntry(self):
    #     self.diary.unlocked_diary("password")
    #     self.diary.create_entry("title", "Body of diary")
    #     self.assertEqual(1, self.diary.no_of_entries())
    #     diary = self.diary.update_entry(1001, "Hello diary, am to be added to the body", "password")
    #     print(diary.findEntryBy(1001))



if __name__ == '__main__':
    unittest.main()
