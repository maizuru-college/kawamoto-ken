from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import re


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            pattern = r'\w\d\d\d\d'
            regex = re.compile(pattern)
            matches = re.findall(regex, request.POST["username"])
            if matches == []:
                err = "学籍番号を入力してください"
                return render(request, 'accounts/sign_up.html', {
                    'form': form,
                    'err': err
                })
            else:
                user = form.save()
                login(request, user)
                return redirect('/')
    else:
        form = UserCreationForm()
    err = ""
    return render(request, 'accounts/sign_up.html', {'form': form, 'err': err})
