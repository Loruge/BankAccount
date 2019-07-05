class InternetBank(object):
    balance = 5000
    attempts = 3
    user_can_get_money = False

    def top_up_money(self, my_money):
        return self.balance + my_money

    def enter_pin_code(self, pin_code):
        correct_pin_code = 333
        if self.attempts == 0:
            return 'Account Blocked'
        if pin_code != correct_pin_code:
            self.attempts = self.attempts - 1
            return 'Access Denied. Wrong pin'
        if pin_code == correct_pin_code:
            self.user_can_get_money = True
            return True, 'Access Allowed'
