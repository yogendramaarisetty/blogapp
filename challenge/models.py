from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Challenge(models.Model):
    Slug = models.SlugField()
    Title = models.CharField(max_length=120)
    Description = models.TextField(max_length=120)
    College = models.CharField(max_length=120)
    Duration = models.DurationField()
    Date = models.CharField(default="",max_length=20)
    Active = models.BooleanField()
    
    def __str__(self):
        return f'{self.Title}'
    def is_active(self):
        return f'{self.Active}'

class Question(models.Model):
    Slug = models.SlugField()
    Title = models.CharField(max_length=120)
    Type= models.CharField(max_length=120)
    Description = models.TextField(max_length=320)
    sample_inputs= models.TextField(max_length=50)
    sample_outputs= models.TextField(max_length=50)
    challenge = models.ForeignKey(Challenge,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.Title}'

class testcases(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE)
    input1 = models.TextField(default="",max_length=1000)
    input2 = models.TextField(default="",max_length=1000)
    input3 = models.TextField(default="",max_length=1000)
    input4 = models.TextField(default="",max_length=1000)
    input5 = models.TextField(default="",max_length=1000)
    output1 = models.TextField(default="",max_length=1000)
    output2 = models.TextField(default="",max_length=1000)
    output3 = models.TextField(default="",max_length=1000)
    output4 = models.TextField(default="",max_length=1000)
    output5 = models.TextField(default="",max_length=1000)
# Create your models here.

class Candidate(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(default="",max_length=24)
    rollnumber = models.CharField(default="",max_length=20)
    college = models.CharField(default="",max_length=50)
    test_name = models.ForeignKey(Challenge,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    submitted_code = models.TextField(max_length=10000)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'

class submittedcodes(models.Model):
    user = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    Challenge = models.ForeignKey(Challenge,on_delete=models.CASCADE)
    submission = models.TextField(max_length=10000)
    score = models.IntegerField(default=0)



