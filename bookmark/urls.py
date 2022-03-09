from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView

urlpatterns =[
    path("", BookmarkListView.as_view(), name='list'),   # 클래스형 뷰 -> 함수형 뷰로 변환 : as_view()
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
]