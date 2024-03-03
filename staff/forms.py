from django import forms


class DateSelectForm(forms.Form):
    selected_date = forms.DateField(label='Select Date', widget=forms.DateInput(attrs={'type': 'date'}))
