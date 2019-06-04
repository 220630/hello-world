class BankAccount():
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
  def info(self):
    print(self.name,self.balance)
  def deposit(self):
    d=float(input("How much would you like to deposit?"))
    self.balance=self.balance+d
  def withdraw(self):
    w=float(input("How much would you like to withdraw?"))
    self.balance=self.balance-w
  def safe_withdraw(self):
    sw=float(input("How much would you like to withdraw?"))
    self.balance=self.balance-sw
    if self.balance>0:
      print(self.safe_withdraw)
    else:
      print("You don't have enough money")
def main():
  done = False
  while not done:
    print("Menu")
    print("D - Do Now")
    print("Q - Quit")
    choice = input("Choice: ")
    if choice == "D":
        b1=BankAccount("Arianna",50)
        b1.info()
        b2=BankAccount("Alejandro",100)
        b2.info()
        """b1.deposit()
        b2.deposit()
        b1.withdraw()
        b2.withdraw()"""
        b1.safe_withdraw()
        b2.safe_withdraw()
        b1.info()
        b2.info()
    elif choice == "Q":
        print("Exiting Game!")
        done = True

main()
