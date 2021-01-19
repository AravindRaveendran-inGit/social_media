# from django.db import models
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile
#
#
# class Profile(models.Model):
#     first_name = models.CharField(max_length=25,blank=True)
#     last_name = models.CharField(max_length=25,blank=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     email = models.EmailField(blank=True)
#     bio = models.TextField(default="no bio...",max_length=250)
#     country = models.CharField(max_length=25,blank=True)
#     profile_pic = models.ImageField(default='avatar.png',upload_to='avatar/')
#     friends = models.ManyToManyField(User,blank=True,related_name='friends')
#     slug = models.SlugField(unique=True,blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#
# @receiver(post_save, sender=User)
# def post_create_profile(sender, instance, created, **kwargs):
#     print('sender', sender)
#     print('instance', instance)
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print('sender', sender)
#     print('instance', instance)
#     instance.profile.save()