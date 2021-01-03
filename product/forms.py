
from django import forms
from django.utils.translation import ugettext_lazy as _


class MobileHealthStationOrderForm(forms.Form):
    email = forms.EmailField(label=_("Email"))
    name = forms.CharField(label=_("Name and Surname"), max_length=255)
    phone = forms.CharField(label=_('Phone'))
    address = forms.CharField(label=_('Delivery address'), widget=forms.Textarea(attrs={'style': 'height:100px'}))

    station_amount = forms.IntegerField(label=_("Number of required Mobile Medi-Lab"), required=False)
    capacity_number = forms.IntegerField(label=_("Number of required Checkup Capacity"), required=False)
    card_number = forms.IntegerField(label=_("Number of required RFID Card"), required=False)
    lancet_number = forms.IntegerField(label=_("Number of required Lancet"), required=False)
    glucose_number = forms.IntegerField(label=_("Number of required Glucose/Hematocrit strip"), required=False)
    ketone_number = forms.IntegerField(label=_("Number of required Ketone strip"), required=False)
    cholesterol_number = forms.IntegerField(
        label=_("Number of required Total Cholesterol (TC) + HDL strip + pipet (for postprandial)"),
        required = False
    )
    panel_number = forms.IntegerField(
        label=_("Number of required Lipid Panel (TC + HDL + Triglyceride) + pipet (for fasting)"),
        required=False
    )
    acid_number = forms.IntegerField(label=_("Number of required Uric Acid strip"), required = False)
    creatinine_number = forms.IntegerField(label=_("Number of required Creatinine strip"), required = False)


class SymptomCheckOrderForm(forms.Form):
    email = forms.EmailField(label=_("Email"))
    name = forms.CharField(label=_("Name and Surname"), max_length=255)
    phone = forms.CharField(label=_('Phone'))
    address = forms.CharField(label=_('Delivery address'), widget=forms.Textarea(attrs={'style': 'height:100px'}))

    symptom_check_set_amount = forms.IntegerField(label=_("Number of required Symptom Check set"))