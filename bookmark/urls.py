from django.urls import path
from .views import BookmarkListView, BookmarkCreateView

urlpatterns =[
    path("", BookmarkListView.as_view(), name='list'),   # 클래스형 뷰 -> 함수형 뷰로 변환 : as_view()
    path("add/", BookmarkCreateView.as_view(), name='add'),
]