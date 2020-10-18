from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django_countries.fields import CountryField

from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from . import choices as c


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(_('Name'), max_length=30, blank=False, null=True)
    surname = models.CharField(_('Surname'), max_length=30, blank=False, null=True)
    birthdate = models.DateField(_('Birthdate'), blank=False, null=True)
    email = models.EmailField(_('Email address'), unique=True, null=True, blank=True)
    phone = models.CharField(_('Phone'), max_length=50, null=True, blank=True)
    passport = models.CharField(_('Citizen ID'), max_length=255, unique=True, null=True, blank=True)
    language = models.CharField(choices=c.LANGUAGE_CHOICES, default=c.ENGLISH_LANG, max_length=50, null=True, verbose_name=_("Language"))
    gender = models.CharField(choices=c.GENDER_CHOICES, default=c.FEMALE_GENDER, max_length=50, null=True, verbose_name=_("Gender"))
    height = models.IntegerField(null=True, verbose_name=_("Height"))
    blood_group = models.CharField(choices=c.BLOOD_GROUP_CHOICES, default=c.A_PLUS, max_length=50, null=True, verbose_name=_("Blood Group"))
    country = CountryField(blank=False, null=True, verbose_name=_("Country"))
    city = models.CharField(_('City'), max_length=255, blank=False, null=True)
    physical_activity = models.CharField(_('Physical Activity'), choices=c.PHYSICAL_ACTIVITY_CHOICES, default=c.ACTIVITY_LOW, max_length=50, null=True)
    smoking = models.CharField(_('Smoking'), choices=c.SMOKING_CHOICES, default=c.SMOKER_NON, max_length=50, null=True)
    diabets = models.CharField(_('Diabets'), choices=c.DIABETS_CHOICES, default=c.DIABET_TYPE_NONE, max_length=50, null=True)
    ethnicity = models.CharField(_('Ethnicity'), choices=c.ETHNICITY_CHOICES, default=c.ETHNICITY_WHITE, max_length=50, null=True)
    angina_or_heart_attack = models.BooleanField(choices=c.BOOL_CHOICES, null=True, default=False, verbose_name=_("ANGINA OR HEART ATTACK IN A 1ST DEGREE RELATIVE &lt;60?"))
    menopause = models.BooleanField(_('Menopause'), choices=c.BOOL_CHOICES, null=True, default=False)
    kidney_disease = models.BooleanField(_('Kidney Disease'), choices=c.BOOL_CHOICES, null=True, default=False)
    atrial_fibrillation = models.BooleanField(_('Arterial Fibrillation'), choices=c.BOOL_CHOICES, null=True, default=False)
    pressure_treatment = models.BooleanField(choices=c.BOOL_CHOICES, null=True, default=False, verbose_name=_("DO YOU GETTING PRESSURE TREATMENT?"))
    rheumatoid_arthritis = models.BooleanField(_('Rheumatoid Arthritis'), choices=c.BOOL_CHOICES, null=True, default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'passport'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.name, self.surname)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f"{self.name} {self.surname} passport ID: {self.passport}"