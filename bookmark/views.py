from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from bookmark.models import Bookmark


class BookmarkListView(generic.ListView):
    model = Bookmark
    # 템플릿 속성이 없을때, '객체이름_list.html' 템플릿을 보여줌.


class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')  # 글쓰기를 완료하고 이동할 목록페이지
    # reverse_lazy: 나중에 해당 변수가 직접 호출되었을때 evalute 함.
    template_name_suffix = '_create'  # bookmark_craete.html 템플릿 파일 호출


class BookmarkDetailView(generic.DetailView):
    model = Bookmark


class BookmarkUpdateView(generic.UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
