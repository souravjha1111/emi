from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import LoanForm
import math

def cal(p, r, t): 
    # for one month interest
    r = r/(12*100)  
    # for one month period
    t = t*12 
    emi = (p*r*pow(1+r,t))/(pow(1+r,t)-1) 
    return emi 

def loanCalculate(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            d =  form.cleaned_data['Down_Payment']
            p =  form.cleaned_data['Loan_amount']
            r =  form.cleaned_data['Interest_rate']
            t =  form.cleaned_data['Loan_tenure']

    # for one month period
            emi = cal(p,r,t)
    
            context = {
                'loan_emi':emi,

            }

            return render(request, 'loan_api/result_page.html', context)
    else:
        form = LoanForm()
        return render(request, 'loan_api/loan_page.html', {'form': form})

