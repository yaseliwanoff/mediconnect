from django import forms
from datetime import date


class DateSelectForm(forms.Form):
    selected_date = forms.DateField(label='Select Date',
                                    widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['selected_date'].initial = date.today()
