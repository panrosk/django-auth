from django.db import models

from django.contrib.auth.models import AbstractUser,PermissionsMixin, BaseUserManager
from django.utils import choices


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        if extra_fields.get('name') is None:
            user.name = ""

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)
    is_bussiness = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True )
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True )
    city = models.CharField(max_length=100, blank=True )
    state = models.CharField(max_length=100, blank=True)

    zip = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


