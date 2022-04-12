from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Beans(models.Model):
  name = models.CharField(max_length=100)
  pub_date = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)

  def __str__(self):
    return self.name