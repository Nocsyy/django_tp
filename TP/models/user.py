from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    groups = models.ManyToManyField(
            'auth.Group',
            verbose_name='groups',
            blank=True,
            help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
            related_name='tp_user_set',  # nom unique pour related_name
            related_query_name='tp_user',
        )
    user_permissions = models.ManyToManyField(
            'auth.Permission',
            verbose_name='user permissions',
            blank=True,
            help_text='Specific permissions for this user.',
            related_name='tp_user_permission_set',  # nom unique pour related_name
            related_query_name='tp_user_permission',
        )
