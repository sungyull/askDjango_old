#blog/models.py
import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Pblish'),
        ('w', 'Withdram')
    )

    author = models.CharField(max_length=50, verbose_name='작성자')
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text="""포스팅 제목을 입력해주세요. 최대 100자""")
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text = '위도,경도')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)























