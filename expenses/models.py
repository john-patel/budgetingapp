from django.db import models

class Expense(models.Model):
    date = models.DateField(auto_now_add=True)
    day = models.CharField(max_length=10)
    object_name = models.CharField(max_length=100)
    object_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate the day based on the date
        self.day = self.date.strftime('%A')
        super().save(*args, **kwargs)