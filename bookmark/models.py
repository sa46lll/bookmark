from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):  # 수정이 완료된 후 이동할 페이지 설정(success_url, get_absolute_url)
        return reverse('detail', args=[str(self.id)])
