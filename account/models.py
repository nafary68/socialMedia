from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from account.manager import UserManager



class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField("email address", unique=True, null=False)
    gender = models.CharField(choices=(('F', 'Female'), ('M', 'Male')), default='d', max_length=1,null=True, blank=True)
    slug = AutoSlugField(populate_from=['email'], unique=True, )
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    phone = models.PositiveIntegerField(null=True, blank=True)
    website_link = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=500,null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('MyUser')
        verbose_name_plural = _('MyUsers')
        app_label = 'account'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


#
# def save_profile(sender, **kwargs):
#     if kwargs['created']:
#         p1 = Profile(user=kwargs['instance'])
#         p1.save()
#
#
# post_save.connect(save_profile, sender=User)


class Relation(models.Model):
    from_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='follower')
    to_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'
