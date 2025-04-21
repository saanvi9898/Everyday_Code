
class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()



    def menu(self):

        while True:
          user_input= input("""
                      How would you like to proceed?
                      1. enter 1 to create pin
                      2. enter 2 to check balance
                      3. enter 3 to Change pin
                      4. enter  4 to withdraw money
                      5. anything Else to Exit
                      """  )
          if user_input=="1" :
              self.create_pin() #create pin
          elif user_input== "2":
              self.check_balance() # check balance
          elif user_input=="3":
              self.change_pin() # change pin
          elif user_input=="4":
              self.withdraw_money() # withdraw money
          elif user_input=="5":
              print("Thank you for using ATM. Goodbye!")
              break

          else:
            print("Invalid option! Please try again.")

    def verify_pin(self, attempts=3):
        if self.pin=="":
           print("PIN not set yet! Please create a PIN first.")
           self.create_pin()
           
        
        while attempts>0:
          user_pin=input("Enter PIN")
          if user_pin==self.pin:
            return True
          else:
            attempts-=1
            print(f"Incorrect PIN. {attempts} attempts left.")
        return False





    def create_pin(self):
        if self.pin!="":
           print("PIN already exists! Use 'Change PIN' option.")
           return
        while True:
          user_pin=input("Set your Atm PIN: ")
          if not user_pin or not user_pin.isdigit() or not len(user_pin)==4:
            print("❌ PIN should be a 4-digit number. Please try again.")
            continue
          else:
            self.pin=user_pin
            break

        while True:
              
              try:
                user_balance=int(input("enter your balance"))
                self.balance=user_balance
                print("✅ User PIN created successfully!")
                break

              except:
                print("❌ Invalid Balance Input! Please enter a number.")
          



    def check_balance(self):
        if self.verify_pin():
          print("your current balance is: ",self.balance)
        else:
          print("Wrong PIN Error!")


    def change_pin(self):

        if self.verify_pin():
          new_pin=input("enter new pin: ")
          self.pin=new_pin
          print("pin changed successfully!")
        else :
          print("Entered Wrong PIN!!!")



    def withdraw_money(self):


       if self.verify_pin():
          try:
            amount=int(input("enter amount: "))
            if self.balance>=amount:
                self.balance=self.balance-amount
                print(f"{amount} withdrawn successfully!")
                print(f"Remaining balance: {self.balance}")
            else:
              print("Insufficient balance Error!!")
          except ValueError:
            print("Invalid amount input!")
       else:
          print("Wrong PIN!")




sbi=Atm()
