from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.managers import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=35, blank=False,
                                unique=True)
    password = models.CharField(_('password'), max_length=100, blank=False, null=False)
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(
        _('Admin status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
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

    class Meta:
        db_table = 'USER'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.username}"
