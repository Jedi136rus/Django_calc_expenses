from django.shortcuts import render, redirect
from .models import Expense, Wallet

from calc.forms import ResForm


def calc(request):
    objects = Expense.objects.all()
    error = ''
    wallet = Wallet.objects.latest('id')
    if request.method == 'POST':
        form = ResForm(request.POST)
        if form.is_valid():
            cash = int(request.POST['cash'])
            cat = request.POST['products']
            commit = request.POST['commit']
            wallet.exp_wallet -= cash
            wallet.save()
            element = Expense(exp_cat=cat, exp_sum=cash, exp_text=commit, exp_ostan=wallet.exp_wallet)
            element.save()
            return redirect('home')
        else:
            error = "Форма заполнена непправильно"
    form = ResForm()
    date = {
        'objects': objects,
        'form': form,
        'error': error,
    }
    return render(request, './base.html', date)


