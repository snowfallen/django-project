from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_item = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_item

