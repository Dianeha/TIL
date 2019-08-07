from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)  # > str '이름 저장'
    email = models.CharField(max_length=50)  # > str 'email'
    github_id = models.CharField(max_length=50)  # > str 'githubID'
    age = models.IntegerField()  # > int


class Menu(models.Model):
    # id 는 자동생성
    name = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.CharField(max_length=30)
