from VendingMachineState import VendingMachineState
from Coin import Coin
from Notes import Note
from Products import Product

class ReturnChangeState(VendingMachineState):
  def __init__(self, vendingMachine):
    self.vendingMachine = vendingMachine

  def selectProduct(self, product):
    print("Product dispensed, please collect change")

  def addCoin(self, coin):
    print("Dispensed, please collect change")

  def addNote(self, note):
    print("Dispensed, please collect change")

  def dispenseProduct(self):
    print("Dispensed, please collect change")

  def returnChange(self):
    #TODO - handle return of change with managing money in machine, as an add-on
    change = self.vendingMachine.totalPrice - self.vendingMachine.selectedProduct.price
    if change > 0:
      print("Change dispensed - ", change)
      self.vendingMachine.resetPrice()
    else:
      print("No change applicable")
    self.vendingMachine.resetProduct()
    self.vendingMachine.setState(self.vendingMachine.idleState)
