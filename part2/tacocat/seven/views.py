from django.shortcuts import render
from django.http import HttpResponse
from .forms import IntegersListForm
from .listLogic import split_str_by

def home(request):
    return render(request,'home.html')

def seven(request):
    if request.method == 'POST':
        set_list_form = IntegersListForm(request.POST)
        if set_list_form.is_valid():
            new_list = split_str_by(set_list_form.cleaned_data['integersList'],',')
            if len(new_list) > 1:                
                note = 'Set list that sum 7  %s ' %(new_list,)
                valid_set_list_form = IntegersListForm()
                return render(request,'seven.html',{'integerListForm':valid_set_list_form, 'note':note})
            else:
                note = 'Invalid integer list'
                invalid_set_list_form = IntegersListForm()
                return render(request,'seven.html',{'integerListForm':invalid_set_list_form, 'note':note})
        else:
            note = 'Invalid integer list'
            invalid_set_list_form = IntegersListForm()
            return render(request,'seven.html',{'integerListForm':invalid_set_list_form, 'note':note})
    else:
        form = IntegersListForm()
        return render(request,'seven.html',{'integerListForm':form})
