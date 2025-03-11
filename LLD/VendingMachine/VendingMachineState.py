from abc import ABC, abstractmethod
class VendingMachineState(ABC):
  def __init__(self, vendingMachine):
    self.vendingMachine = vendingMachine

  @abstractmethod
  def selectProduct(self, product):
    pass
  
  @abstractmethod
  def insertCoin(self, coin):
    pass
 
  @abstractmethod
  def insertNote(self, note):
    pass

  @abstractmethod
  def dispenseProduct(self):
    pass

  @abstractmethod
  def returnChange(self):
    pass
