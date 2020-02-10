from django import forms


class ExpenseForm(forms.Form):
    title = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)
    category = forms.CharField(required=False)
