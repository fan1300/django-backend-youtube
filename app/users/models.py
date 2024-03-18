from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
    )
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('사용자는 이메일 주소를 가져야 합니다')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique = True)
    nickname = models.CharField(max_length=255)
    is_bussiness = models.BooleanField(default = False)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    def __str__(self):
        return f'email: {self.email}, nickname: {self.nickname}'