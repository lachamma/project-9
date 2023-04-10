from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=30,blank=True)
    date=models.DateField(auto_now=True)
    body=models.TextField()
    # lang=[['kannada','kannada'],['tamil','tamil'],['hindi','hindi']]
    # language=models.CharField(max_length=15,choices=lang,default='')
    # gen=[['male','male'],['female','female']]
    # gender=models.CharField(max_length=15,choices=gen,default='')

    def __str__(self):
        return self.title

class Review(models.Model):
    ratings=[[1,1],[2,2],[3,3],[4,4],[5,5]]
    rating=models.PositiveIntegerField(choices=ratings,default=None)
    date=models.DateField(auto_now=True)
    reviewarea=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)