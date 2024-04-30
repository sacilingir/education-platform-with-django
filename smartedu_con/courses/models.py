from django.db import models

class Category(models.Model):
   name = models.CharField(max_length=50,null=True)
   slug = models.SlugField(max_length=50,unique=True,null=True)

   def __str__(self):
       return self.name
       


class Course(models.Model): #tablonun ismi Course
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,max_length=200,null=True,on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/sampleimg.png")
    date = models.DateTimeField(auto_now = True)
    available = models.BooleanField(default=True)
    #bu instancelar tabloda bulunan sütunlar 

    def __str__(self):
        return self.name