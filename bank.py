class Account():
    def __init__(self,fname,lname,pan,deposit):
        self.fname=fname
        self.lname=lname
        self.pannumber=pan
        self.__amount=deposit
        self.username=self.fname+'100'
        self.password='12345'

    def get_balance(self):
        return self.__amount

    def set_balance(self,amt):
        self.amt=amt
        self.__amount=self.__amount+self.amt