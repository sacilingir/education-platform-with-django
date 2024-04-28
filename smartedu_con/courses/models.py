from django.db import models


class Course(models.Model): #tablonun ismi Course
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/sampleimg.png")
    date = models.DateTimeField(auto_now = True)
    available = models.BooleanField(default=True)
    #bu instancelar tabloda bulunan sütunlar 

    def __str__(self):
        return self.name