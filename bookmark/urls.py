from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns =[
    path("", BookmarkListView.as_view(), name='list'),   # 클래스형 뷰 -> 함수형 뷰로 변환 : as_view()
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),      # <int:pk> url 뒤에 나오는 번호를 DB의 pK 참조하여 가져옴(INT형)
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]