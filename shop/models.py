from django.db import models
from django.urls import reverse


class Products(models.Model):
    product_name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    information = models.TextField(max_length=2048)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={'pk': self.pk})