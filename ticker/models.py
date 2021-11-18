from django.db import models
from django.urls import reverse


# Create your models here.
class TickerModel(models.Model):
    ticker = models.CharField(max_length=4, help_text='Enter ticker')
    ticker_price = models.DecimalField(decimal_places=2, max_digits=10)
    subscriber_email = models.EmailField()

    class Meta:
        ordering = ['subscriber_email', 'ticker']

    def get_absolute_url(self):
        return reverse('ticker-detail', args=[str(self.id)])

    def __str__(self):
        return self.ticker
