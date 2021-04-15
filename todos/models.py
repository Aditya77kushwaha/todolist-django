from django.db import models
from django.forms import ModelForm

# Create your models here.


class MyModel(models.Model):
    """model for database"""
    task = models.CharField(max_length=1000)

    def __str__(self):
        return self.task


class MyForm(ModelForm):
    """form for respective model"""

    class Meta:
        model = MyModel
        fields = ['task']
