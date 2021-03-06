from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=50, help_text="Username", unique=True)
    password = models.CharField(max_length=50, help_text="Password")

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    RESEARCHER = "RESEARCHER"
    TAKER = "SURVEY TAKER"
    BOTH = "BOTH"
    MTYPE_CHOICES = (
    (RESEARCHER, "Researcher"),
    (TAKER, "Survey Taker"),
    (BOTH, "Both"),
    )    
    memberType = models.CharField(max_length=20, choices=MTYPE_CHOICES, help_text="Member Type",)

    WHITE = "WHITE"
    AM = "AFRICAN AMERICAN"
    ASIAN = "ASIAN"
    NA = "NATIVE AMERICAN"
    PI = "PACIFIC ISLANDER"
    RACE_CHOICES = (
    (WHITE, "White"),
    (AM, "African American"),
    (ASIAN, "Asian"),
    (NA, "Native American"),
    (PI, "Pacific Islander"),
    ) 
    race = models.CharField(max_length=20, choices=RACE_CHOICES, help_text="Race", null=True, blank=True)

    MALE = "MALE"
    FEMALE = "FEMALE"
    GENDER_CHOICES = (
    (MALE, "Male"),
    (FEMALE, "Female"),
    ) 
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, help_text="Gender", null=True, blank=True)

    country = models.CharField(max_length=50, help_text="Country", null=True, blank=True)
    city = models.CharField(max_length=50, help_text="City", null=True, blank=True)
    state = models.CharField(max_length=50, help_text="State", null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (self.user.username + "'s profile")