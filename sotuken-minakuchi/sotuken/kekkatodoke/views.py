from django.shortcuts import render, redirect
from .forms import KekkaForm
from .models import Kekka
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'kekkatodoke/index.html')


def about(request):
    return render(request, 'kekkatodoke/index.html')


def show(request):
    return render(request, 'kekkatodoke/index.html')

@login_required
def detail(request, subject):
    kekkas = Kekka.objects.all().filter(student_code=request.user.username).filter(subject=subject)
    return render(request, 'kekkatodoke/detail.html',{'kekkas':kekkas})

@login_required
def new(request):
    if request.method == 'POST':
        form = KekkaForm(request.POST)
        if request.POST["student_code"] != request.user.username:
            err = "自分の学籍番号を入力してください"
            return render(request, 'kekkatodoke/new.html', {
                'form': form,
                'err': err
            })

        if form.is_valid():
            form.save()
            return redirect('kekkatodoke:index')
    else:
        form = KekkaForm
        err = ""
    return render(request, 'kekkatodoke/new.html', {'form': form, 'err': err})