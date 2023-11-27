from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categories = models.ManyToManyField('Categorias')
    featured = models.BooleanField(default=False)
    pub_date =models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("blogs:post", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["-date_created"]
        
    def __str__(self):
        return self.title
    

class Categorias(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categorias'

    def get_absolute_url(self):
        return reverse("blogs:categorias", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title  
    
    
