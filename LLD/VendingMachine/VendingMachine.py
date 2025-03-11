from Notes import Notes
from Coin import Coin
from Inventory import Inventory
from Products import Products
from IdleState import IdleState
from ReadyState import ReadyState
from DispenseState import DispenseState

class VendingMachine:
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(VendingMachine, cls).__new__(cls)
      cls.instance.inventory = Inventory()
      cls.instance.idleState = IdleState(cls.instance)
      cls.instance.readyState = ReadyState(cls.instance)
      cls.instance.dispenseState = DispenseState(cls.instance)
      cls.instance.returnChangeState = ReturnChangeState(cls.instance)
      cls.instance.currentState = cls.instance.idleState
      cls.instance.selectedProduct = None
      cls.totalPrice = 0
    return cls.instance

  def selectProduct(self, product):
    self.currentState.selectProduct(product)
  def insertCoin(self, coin):
    self.currentState.insertCoin(coin)
  def insertNote(self, note):
    self.currentState.insertNote(note)
  def dispenseProduct(self, product)
    self.currentState.dispenseProduct()
  def returnChange(self):
    self.currentState.returnChange()
  def setState(self, state):
    self.currentState = state
  def addCoin(self, coin):
    self.totalPrice += coin
  def addNote(self, note):
    self.totalPrice += note
  def resetProduct(self):
    self.selectedProduct = None
  def resetPrice(self):
    self.totalPrice = 0
  
    
