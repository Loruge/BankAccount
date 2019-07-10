import unittest
from bank_acc import *


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.terminal = InternetBank()
        self.terminal.enter_pin_code(333)

    def test_top_up_money(self):
        my_money = self.terminal.top_up_money(5000)
        self.assertEqual(my_money, 10000)

    def test_attempt_count_correct(self):
        self.assertEqual(self.terminal.attempts, 3)

    def test_attempts_not_0(self):
        self.assertNotEqual(self.terminal.attempts, 0)

    def test_pin_code_attempts_left(self):
        incorrect_attempt = self.terminal.enter_pin_code(546)
        self.assertEqual(self.terminal.attempts, 2)

    def test_incorrect_pin_code_attempts_left(self):
        incorrect_attempt = self.terminal.enter_pin_code(546)
        self.assertNotEqual(self.terminal.attempts, 3)

    def test_attempts_0_after_3_incorrect_pins(self):
        incorrect_at_1 = self.terminal.enter_pin_code(546)
        incorrect_at_2 = self.terminal.enter_pin_code(546)
        incorrect_at_3 = self.terminal.enter_pin_code(546)
        self.assertEqual(self.terminal.attempts, 0)
        self.assertTrue(self.terminal.user_can_get_money)

    def test_user_cant_top_up_0(self):
        #Test should be down
        my_money = self.terminal.top_up_money(0)
        self.assertEqual(my_money, 5000)

    def test_user_cant_top_up_negative(self):
        my_money = self.terminal.top_up_money(-1)
        self.assertEqual(my_money, 5000)
        #to do: symbols, symbols+numbers

    def test_user_cant_top_up_with_symbols(self):
        #Test should be down
        my_money = self.terminal.top_up_money('1q2w3e4r5t6y7u8i9o')
        self.assertEqual(my_money, 5000)
