from VendingMachineState import VendingMachineState
from Coin import Coin
from Notes import Note
from Products import Product

class DispenseState(VendingMachineState):
  def __init__(self, vendingMachine):
    self.vendingMachine = vendingMachine

  def selectProduct(self, product):
    print("Product selected, please collect")

  def addCoin(self, coin):
    print("Paid, please collect")

  def addNote(self, note):
    print("Paid, please collect")

  def dispenseProduct(self):
    self.vendingMachine.setState(self.vendingMachine.readyState)
    product = self.vendingMachine.product
    self.vendingMachine.inventory.reduceProduct(product)
    print("Product dispensed - ", product.name)
    self.vendingMachine.setState(self.vendingMachine.ReturnChangeState)

  def returnChange(self):
    print("Please collect product before change")
