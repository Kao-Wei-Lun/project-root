from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=[
            ('digital', '數字易經諮詢'),
            ('healing', '療癒與服務'),
            ('divination', '牌卡占卜'),
            ('product', '商品販售'),
        ]
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # 如果未填入 slug，就自動使用 name 生成 slug
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Consultant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='consultants/', null=True, blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_at.strftime("%Y-%m-%d")}'