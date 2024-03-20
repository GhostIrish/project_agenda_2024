from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# id (primary key)
# first_name (string), last_name (string), phome(string)
# email (email), created_date (date), description (text)[a diferença entre texto é
# que quando passa de 255 caracteres, a string é considerada um text]

# category (foreign key), show (boolean), picture (imagem)
# faremos depois:
# owner (foreign key),

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
    
class Contact(models.Model):
    #decide ate quantas caracteres pode ter o nome
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
                                 )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True
                                 )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    