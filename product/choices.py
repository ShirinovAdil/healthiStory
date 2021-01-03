from django.utils.translation import ugettext_lazy as _
ENGLISH_LANG = 'en'
RUSSIAN_LANG = 'ru'
TURKISH_LANG = 'tr'
AZERBAIJANI_LANG = 'az'
LANGUAGE_CHOICES = [
    (ENGLISH_LANG, _('English')),
    (RUSSIAN_LANG, _('Russian')),
    (TURKISH_LANG, _('Turkish')),
    (AZERBAIJANI_LANG, _('Azerbaijan')),
]