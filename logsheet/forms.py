from django import forms

class GenerateReportForm(forms.Form):
    sumDate = forms.CharField(label='Enter Date')

    