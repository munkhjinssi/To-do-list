from django.db import models

#taskiin model 
class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True) 
  created_at = models.DateField(auto_now_add=True)  
      
  def __str__(self):
    return self.title 
