from django.db import models
from django.urls import reverse

# User < AbstractUser < AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from faker import Faker
f = Faker()

class User(AbstractUser):
    # fans = models.ManyToManyField(self, related_name='stars')
    # fans = models.ManyToManyField('accounts.User', related_name='stars') 도 가능하지만
    # settings에서 AUTH_USER_MODEL 적어두고 변수처리 하는 것이다 언제든 갈아낄 수 있다.
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')

    def __str__(self):
        return self.username
    
    @classmethod
    def dummy(cls, n):
        for i in range(n):
            u = cls()
            u.username = f.first_name()
            u.set_password('4321rewq')
            u.save()

    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})
    