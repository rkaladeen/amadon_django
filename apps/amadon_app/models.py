from django.db import models

class ProdManager(models.Manager):
  def prod_available(self, requestedProd, onHand):
    error = ""
    if requestedProd > onHand:
      error = "We are sorry we do not have sufficient amount of product in-stock"
    return error

class Product(models.Model):
  item_name = models.CharField(max_length=45)
  price = models.FloatField()
  qty_in_stock = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ProdManager()