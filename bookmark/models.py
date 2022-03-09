from django.db import models
from django.urls import reverse

# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 데이터를 객체화해서 다루기 위함
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값 = 레코드의 컬럼 데이터 값


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항 (몇글자까지?)
    # 3. Form의 종류
    # 4. Form에서 제약사항

    def __str__(self):
        return f'{self.site_name} : {self.url}'

    def get_absolute_url(self):     # 장고에서 제공하는 기능, object 하나하나에 대한 url
        return reverse('detail', args=[self.id])       # urls.py에서 설정한 URL의 name이나, viewname을 통해서 URL로 돌려받을 수 있다.


# 모델을 만들었다 => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
# 마이그레이션(migrate) => 데이터베이스에 모델의 내용을 반영(테이블 생성)
# makemigrations => 모델의 변경사항을 추적해서 기록