from VendingMachineState import VendingMachineState
from Product import Product
from Coin import Coin
from Notes import Notes

class IdleState(VendingMachineState):
  def __init__(self, vendingMachine):
    self.vendingMachine = vendingMachine

  def selectProduct(self, product):
    if self.vendingMachine.inventory.productQuantityExist(product):
      self.vendingMachine.selectedProduct = product
      self.vendingMachine.setState(self.vendingMachine.readyState)
      print("Selected Product - ", product.name)
    else:
      print("Product Name not Available - ", product.name)

  def insertCoin(self, coin):
    print("Select product first")
 
  def insertNote(self, note):
    print("Select product first")

  def dispenseProduct(self):
    print("Select product and enter amount")

  def returnChange(self):
    print("No change to return")

  
