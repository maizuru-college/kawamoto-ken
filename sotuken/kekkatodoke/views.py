from django.shortcuts import render, redirect
from .models import Notification, Student
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NoteForm


# Create your views here.
def top(request):  # トップページの表示
    return render(request, 'top.html')


@login_required
def new(request):  # 投稿作成ページへ移動
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kekkatodoke:show')
    else:
        form = NoteForm
    return render(request, 'new.html', {'form': form})


def about(request):  # 概要ページの表示
    return render(request, 'about.html')


def detail(request):  # 投稿詳細ページへ移動
    return render(request, 'detail.html')


@login_required
def show(request):  # 一覧表示
    d = {'absent_list': Notification.objects.all()}
    return render(request, 'show.html', d)
