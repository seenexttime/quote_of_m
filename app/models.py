from django.db import models

# Create your models here.

class Quote(models.Model):
    body = models.CharField(max_length=500, verbose_name="quote")
    author = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return str(self.author)
    