#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Todo

class Index(ListView):
    model=Todo

class Detail(DetailView):
    model=Todo


# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Todo
    # 編集対象にするフィールド
    fields = ["title", "body", "category", "confidentioal", "status", "tags","freetags"]
    #fields = ["type","title", "body", "confident", "stage", "tags","freetags"]


class Update(UpdateView):
    model = Todo
    fields = ["title", "body", "category", "confidentioal", "status", "tags","freetags"]


class Delete(DeleteView):
    model = Todo

    # 削除したあとに移動する先（トップページ）
    success_url = "/"
