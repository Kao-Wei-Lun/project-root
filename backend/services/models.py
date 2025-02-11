# services/models.py
from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('digital', '數字易經諮詢'),
        ('healing', '療癒與服務'),
        ('divination', '牌卡占卜'),
        ('product', '商品販售'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.name
