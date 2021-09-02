from django.urls import path

from bookmark.views import BookmarkListView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list')
]