from django.db import models
from django.contrib.auth.models import User

class MyUser(User):
  field1 = models.CharField(max_length=100)
  field2 = models.CharField(max_length=100)
  field3 = models.CharField(max_length=100)

  USERNAME_FIELD = 'email'

  def __unicode__(self):
    return self.email