from django.db import models
from  django.urls import reverse
# Create your models here.
class Movies(models.Model):
    Title=models.CharField(max_length=100)
    Release_Date = models.DateTimeField()
    Rating=models.FloatField()
    Director=models.CharField(max_length=100)
    Writer=models.CharField(max_length=100)
    Actor=models.CharField(max_length=100)
    Production=models.CharField(max_length=100)
    Summary=models.TextField()
    Language=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    posters=models.ImageField(upload_to='images/')
    Trailer=models.FileField(upload_to='videos/', null=True)
    def __str__(self):
        return self.Title+ ": " + str(self.Trailer)
    def get_absolute_url(self):
        return reverse('list_page_show')

