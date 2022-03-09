from django.urls import path
from .views import BookmarkListView

urlpatterns =[
    path("", BookmarkListView.as_view(), name='list'),   # 클래스형 뷰 -> 함수형 뷰로 변환 : as_view()
]