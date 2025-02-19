from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CustomPasswordValidator:

    def __init__(self, min_length=6):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(_('Your password must contain at least %(min_length)d characters.') % {'min_length': self.min_length})

    def get_help_text(self):
        return _("Your password must contain at least %(min_length)d characters.") % {'min_length': self.min_length}