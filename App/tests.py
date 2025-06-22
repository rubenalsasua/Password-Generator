import unittest
import string
from App.views import generar_password


class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        min_length = 8
        max_length = 12
        password = generar_password(min_length, max_length, True, True)
        self.assertTrue(min_length <= len(password) <= max_length)

    def test_password_alphabet(self):
        min_length = 10
        max_length = 10
        password = generar_password(min_length, max_length, False, False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)


if __name__ == "__main__":
    unittest.main()
