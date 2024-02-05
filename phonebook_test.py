import unittest

from my_phone import my_phone


class TestContactFunction(unittest.TestCase):
    def setUp(self):
        self.phone = Phone()

    def test_add_contact(self):
        self.phone.add_contact("John", "08105795528")
        self.assertEqual(self.phone.contacts["John"], "08105795528")

    def test_delete_contact(self):
        self.phone.add_contact("jane", "08106795528")
        self.phone.delete_contact("john")
        self.assertNotIn("Jane", self.phone.contacts, "Contact not deleted successfully.")


if _name_ == '_main_':
    unittest.main()