from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.managers import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=35, blank=False,
                                unique=True)
    password = models.CharField('password', max_length=100, blank=False, null=False)

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting account.'
        ),
    )
    is_delete = models.BooleanField('delete', default=False, help_text=_(
        'Delete the user account and keep the data in the database as a deleted user'),
                                    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [username, password]
    objects = UserManager()
