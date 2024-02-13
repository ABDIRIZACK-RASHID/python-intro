class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number =phone_number
    def send_money  (self,amount,receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient} successfully")
        else:
            print("insufficient money to send ")

class PersonalMpesa(Mpesa):
            def __init__(self,account_balance,phone_number,idno):
                super().__init__(account_balance,phone_number)
                self.idno = idno
            def buyairtime(self,amount):
                self.account_balance += amount
                print(f"{amount} KES airtime bought successfully")

class BussinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,bussines_name):
        super().__init__(account_balance,phone_number)
        self.bussines_name = bussines_name
    def Recievepayment(self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from customer")
personal=PersonalMpesa(2000,723054546,30595785)
personal.send_money(300,7687998)
personal.buyairtime(150)

business=BussinessMpesa(50000,7687998,"mega")
business.send_money(300,7687998)
business.Recievepayment(5000,)

