from django.db import models

class newRecipe(models.Model):
     recipeimage = models.ImageField(upload_to = 'pics/')
     recipename = models.CharField(max_length = 20)
     recipedesc = models.TextField()
     ingredients = models.TextField()
     procedure = models.TextField()

class entry(models.Model):
     title = models.CharField(max_length = 50)
     content = models.TextField()

     def __str__(self):
        return self.data
     
class ent(models.Model):
     title = models.CharField(max_length = 50)
     content = models.TextField()
     entry_time = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.data
     

