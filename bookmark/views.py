from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from bookmark.models import Bookmark


class BookmarkListView(generic.ListView):
    model = Bookmark


class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') # 글쓰기를 완료하고 이동할 목록페이지
    # reverse_lazy: 나중에 해당 변수가 직접 호출되었을때 evalute 함.
    template_name_suffix = '_create'