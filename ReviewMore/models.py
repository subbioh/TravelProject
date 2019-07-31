from django.db import models

class Reviewmore(models.Model):
    title = models.CharField(max_length = 255)
    title1 = models.CharField(max_length = 255, blank=True, default='')#이제 되겠죠?
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return self.title1 title이 또 필요한가요?
        

# Create your models here.
