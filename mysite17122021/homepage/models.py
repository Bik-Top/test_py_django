# from os import times, times_result
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Car(models.Model):
  brend = models.CharField(max_length=50, verbose_name='Бренд')
  color = models.CharField(max_length=50, verbose_name="Цвет")
  content = models.TextField(blank=True, verbose_name="Описание")
  photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Логотип")
  times_create = models.DateTimeField(auto_now_add=True, verbose_name="Создание запист")
  times_update = models.DateTimeField(auto_now=True, verbose_name="Обновление записи")
  is_published = models.BooleanField(default=True, verbose_name="Опубликованно")

  def __str__(self):
    return self.brend

  def get_absolute_url(self):
    return reverse('car', kwargs={'carid': self.pk})


  class Meta:
    verbose_name = 'Машина'
    verbose_name_plural = 'Машины'
    ordering = ['-times_create']

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