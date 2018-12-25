from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    class Meta:
        db_table = 'student'
        verbose_name = u'学生信息'

    def __str__(self):
        return self.name
        
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)
    password = models.IntegerField()
    class Meta:
        db_table = 'user'
        verbose_name = u'前台用户管理'

    def __str__(self):
        return self.name

class File(models.Model):
    fileName = models.CharField(max_length = 30)
    uploadFile = models.FileField(upload_to = 'disk/upload/')

    class Meta:
        db_table = 'file'
        
    def __str__(self):
        return self.fileName