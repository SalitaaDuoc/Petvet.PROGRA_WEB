from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='media/products/')
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.IntegerField()
  category = models.ForeignKey(category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
