from django.db import models

class Symbol(models.Model):
    name = models.CharField(max_length=255)

class TopOfTheBook(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    best_bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    best_bid_size = models.PositiveIntegerField()
    best_offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    best_offer_size = models.PositiveIntegerField()

class Order(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    limit_price = models.DecimalField(max_digits=10, decimal_places=2)
    side = models.CharField(max_length=4)
    quantity = models.PositiveIntegerField()
    order_id = models.CharField(max_length=255)
