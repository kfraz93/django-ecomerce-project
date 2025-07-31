from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        """
        To show the plural of the Model name
        """
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        """
        To return the name of the items inside model
        :return:
        """
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items',  on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
