from django import forms


class MobileHealthStationOrderForm(forms.Form):
    email = forms.EmailField(label="Email")
    name = forms.CharField(label="Name and Surname", max_length=255)
    phone = forms.CharField(label='Phone')
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'style': 'height:100px'}))

    station_amount = forms.IntegerField(label="Number of required Mobile Health Station")
    capacity_number = forms.IntegerField(label="Number of required Checkup Capacity")
    card_number = forms.IntegerField(label="Number of required RFID Card")
    lancet_number = forms.IntegerField(label="Number of required Lancet")
    glucose_number = forms.IntegerField(label="Number of required Glucose / Hematocrit strip")
    ketone_number = forms.IntegerField(label="Number of required Ketone strip")
    cholesterol_number = forms.IntegerField(
        label="Number of required Total Cholesterol (TC) + HDL strip + pipet (for postprandial)"
    )
    panel_number = forms.IntegerField(
        label="Number of required Lipid Panel (TC + HDL + Triglyceride) + pipet (for fasting)"
    )
    acid_number = forms.IntegerField(label="Number of required Uric Acid strip")
    creatinine_number = forms.IntegerField(label="Number of required Creatinine strip")
