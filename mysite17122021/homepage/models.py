# from os import times, times_result
from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
  brend = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  content = models.TextField(blank=True)
  photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
  times_create = models.DateTimeField(auto_now_add=True)
  times_update = models.DateTimeField(auto_now=True)
  is_published = models.BooleanField(default=True)

  def __str__(self):
    return self.brend

  def get_absolute_url(self):
    return reverse('car', kwargs={'carid': self.pk})

# python manage.py shell


# from homepage.models import Car
# Car(brend='Mersedes', color='bleck', content='lorem ipsum asd fdfg erdf gfasdsfdf aseqwds')
# w1 = _  w1.save()

# objects ---> create, filter, order_by, get, 
# Car.objects.create(brend='Mersedes', color='bleck', content='lorem ipsum asd fdfg erdf gfasdsfdf aseqwds')

# wu =  Car.objects.get(pk=1)
# wu.brend = 'Honda'
# wu.save()

# wd =  Car.objects.get(pk=1)
# wd
# wd.delete()