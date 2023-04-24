import re

class Property_calculator():
    owner = {}

    def __init__(self, name):
        self.name = name
        self.login_name = []
        self.pas = []
        self.invesment_cost = 0
        self.income_cost = 0
        self.Roi = 0
        

    def driver(self):
        while True:
            action = input('What would you like to do? Register/Sign in/Quit \n')
            if action.lower() == 'register':
                self.register()
            elif action.lower() == 'sign in':
                self.log_in()
            elif action.lower() == 'quit':
                break
            else:
                print('Invalid input! Please provide actions following given prompt commands above.')
    
    def register(self):
        self.login_name = input('What is your email? \n')
        pattern = re.compile("([A-Za-z0-9]+)@([A-Za-z0-9]+).(com|org)$")
        self.pas = input('What is your password \n')
        if pattern.match(self.login_name) and self.pas:
            self.owner[self.login_name] = self.pas
            print('You have registered succesfully')
            # print(self.owner)
        else:
            print('Your input is not a corrected form for email, please input again')

    def log_in(self):
        sign_in = input('What is your sign-up email?')
        pas = input('Password?')
        if sign_in == (self.login_name) and pas == (self.pas):
            print('You have succesfully loged in, now you can use our tool to calculate ROI')
            self.investments_gain_loss()

    def investments_gain_loss(self):
        down_payment = int(input('What is your down payment on your property? \n'))
        closing_cost = int(input('What is your closing cost? \n'))
        rehab_budget = int(input('What is your rehab budget? \n'))
        income = int(input('What is your income in a month? from house rental, laundry, misc, etc. \n'))
        expenses = int(input('What is your expenses for a month? insurances, tax, utilities \n'))
        self.invesment_cost = down_payment + closing_cost + rehab_budget
        self.income_cost = (income - expenses) * 12
        self.Roi = (self.income_cost / self.invesment_cost) * 100
        print(f'Your property after calculation is {self.Roi}%')

    # def show(self):
    #     self.owner[self.name] = {
    #         'ROI': self.Roi

    #     }
    #     print(self.owner)

Khoa = Property_calculator('Khoa')
Khoa.driver()

    