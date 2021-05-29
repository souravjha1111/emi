from django import forms

class LoanForm(forms.Form):
    Loan_amount = forms.IntegerField(max_value=9999999,min_value=100)
    Down_Payment = forms.IntegerField()
    Interest_rate = forms.FloatField()
    Loan_tenure = forms.IntegerField( max_value=100000,min_value=1)
    class Meta:
        fields = ['Loan_amount', 'Down_Payment','Interest_rate','Loan_tenure']
