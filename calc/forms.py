from django import forms


class ResForm(forms.Form):
    CHOICES = [('Продукты', 'Продукты'), ('Бензин', 'Бензин'), ('Футбол', 'Футбол'), ('Прочее', 'Прочее')]
    cash = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Потраченная сумма'}))
    products = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-select"}), choices=CHOICES)
    commit = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Примечание'}))