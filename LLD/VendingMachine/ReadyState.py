from VendingMachineState import VendingMachineState
from Coin import Coin
from Notes import Notes

class ReadyState(VendingMachineState):
  def __init__(self, vendingMachine):
    self.vendingMachine = vendingMachine

  def selectProduct(self, product):
    print("Product selected, please pay")
 
  def insertCoin(self, coin):
    self.vendingMachine.addCoin(coin)
    print("Coin added - ", coin.name)
    self.checkPaymentStatus()

  def insertNote(self, note):
    self.vendingMachine.addNote(note)
    print("Note added - ", note.name)
    self.checkPaymentStatus()

  def dispenseProduct(self):
    print("Please complete payment")

  def returnChangeState(self):
    print("Please complete payment")

  def checkPaymentStatus(self):
    if self.vendingMachine.totalPrice >= self.selectedProduct.price:
      self.vendingMachine.setState(self.vendingMachine.dispenseState)
 
    
