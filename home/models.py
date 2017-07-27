from django.core.urlresolvers import reverse
from django.db import models


class Bike(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bike_images')
    description = models.TextField()
    daily_rent = models.IntegerField()

    is_available = models.BooleanField()

    def get_absolute_url(self):
        return reverse('bike-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Booking(models.Model):
    bike = models.ForeignKey(Bike)

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone_number = models.TextField()

    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    booking_message = models.TextField()

    is_approved = models.BooleanField()