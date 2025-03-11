class Inventory:
  def __init__(self):
    self.products = {}

  def productQuantityExist(self, product):
    if self.products.get(product, 0)>0:
      return True
    else False

  def addProduct(self, product, quantity):
    self.products[product] = self.products.get(product, 0) + quantity

  def reduceProduct(self, product):
    if self.productQuantityExist(product):
      self.products[product] = self.product.get(product) - 1

  def getProductQuantity(self, product):
    return self.product.get(product, 0)

  def removeProduct(self, product):
    del self.products[product]
  
