class Customer():
    def __init__(self, name):
        self.name=name

def greet(customer):
    customer.name="meera"
    return f"hello {customer.name}"

# cust=Customer("Shanvi")
# print(cust.name)

# print(greet(cust))
# print(cust.name)






class Atm():
    # static/ class variable
    counter=1
    def __init__(self):
        self.sno=Atm.counter
        Atm.counter=Atm.counter+1
        print(id(self))

sbi=Atm()
hdfc=Atm()
axis=Atm()
print(sbi.sno)
print(hdfc.sno)
print(axis.sno)
print(sbi.counter)
print(hdfc.counter)
print(axis.counter)






