from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰(제네릭 뷰), 함수형 뷰 두 종류 
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 어떤 내용을 추가할 것인지? 없으면 오류(ImproperlyConfigured)!
    success_url = reverse_lazy('list')    # 전송 요청 성공 시 리로드 되는 페이지
    template_name_suffix = '_create' # 기본적으로 CreateView, UpdateView의 템플릿 이름은 ..._form인데 이걸 임의로 바꿔줌

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'