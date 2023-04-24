import unittest

from weekendproject3 import Property_calculator

class TestCal(unittest.TestCase):

    def testRegister(self):
        cal = Property_calculator('khoa')
        cal.register()
        self.assertEqual(cal.owner, {'khoatuanthai@yahoo.com' : 'khoa123'})

    def testLogin(self):
        cal = Property_calculator('khoa')
        cal.log_in()
        self.assertEqual(cal.log_in(), 'You have succesfully loged in, now you can use our tool to calculate ROI')

    def test_calculator(self):
        cal = Property_calculator('khoa')
        cal.investments_gain_loss()
        self.assertEqual(cal.investments_gain_loss, 'Your property after calculation is 20%')

if __name__ == '__main__':
    unittest.main()