from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

CHOICES = [
    ("Judge", "Judge"),
    ("Lawyer", "Lawyer"),
]

Court_Type=[
    ("SUP","Supreme Court"),
    ("HIG","High Court"),
    ("DST","District Court"),
    ("SES","Session Court"),
]

Case_type=[
    ("CIV","Civil"),
    ("CRI","Criminal"),
]
def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class UserProfile(models.Model):
    # required by the auth model
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30, choices=CHOICES)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)

class Advocate(models.Model):
    license_no = models.CharField(max_length=17, primary_key=True)
    name=models.CharField(max_length=400)
    address=models.CharField(max_length=500)
    court_type=MultiSelectField(choices=Court_Type,max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Judge(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    court_type=models.CharField(choices=Court_Type,max_length=20)
    district=models.CharField(max_length=100,blank=True,null=True)
    license_no = models.CharField(max_length=17, primary_key=True)
    
class Case(models.Model):
    advocate=models.ForeignKey(User,on_delete=models.CASCADE,related_name="advocate_user")
    name_of_applicant=models.CharField(max_length=400)
    phone_number=models.BigIntegerField()
    address=models.CharField(max_length=500)
    case_type=models.CharField(max_length=3,choices=Case_type)
    court_type=models.CharField(choices=Court_Type,max_length=3)
    subject=models.CharField(max_length=500)
    file=models.FileField(upload_to=user_directory_path, blank=True, null=True)
    cnr=models.CharField(max_length=16, unique=True, blank=True,null=True)
    fileNo=models.CharField(max_length=16, unique=True, blank=True,null=True)
    status=models.BooleanField(default=False)
    district=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,blank=True,null=True)
    name_of_respondent=models.CharField(max_length=400,null=True)
    lawyer_of_respondent=models.CharField(max_length=400,null=True)
    address_of_respondent=models.CharField(max_length=500, null=True)
    judge=models.ForeignKey(Judge,on_delete=models.CASCADE,related_name="judge_user",null=True,blank=True)

    def __str__(self):
        return self.cnr

# Create your models here.
