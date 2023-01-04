from django.db import models
from user.models.profile import Profile


class BaseEmployeeMixin(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
