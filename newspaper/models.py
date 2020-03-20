from django.db import models

# 뉴스 기사 : news_article
class news_article(models.Model):
    class Meta:
        verbose_name = '뉴스 기사'
        verbose_name_plural = '뉴스 기사들'

    def __str__(self):
        pass
    title = models.CharField(max_length=50, verbose_name='기사 제목')
    content = models.TextField(verbose_name='기사 내용')
    category = models.ForeignKey('news_category', on_delete=models.SET_NULL, null=True, blank=True)
    # author_id
    # banner_photo = models.
    video_link = models.CharField(max_length=200)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    views = models.IntegerField(default=0)


# 뉴스 카테고리 : news_category
class news_category(models.Model):
    class Meta:
        verbose_name = '뉴스 카테고리'
    
    def __str__(self):
        pass
    
    name = models.CharField(max_length=15)
    sorting = models.CharField(max_length=15)
    enabled_category = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

# 뉴스 댓글 : news_comment
class news_comment(models.Model):
    class Meta:
        verbose_name = '뉴스 댓글'
    
    def __str__(self):
        pass
    
    comment = models.TextField(verbose_name='댓글')
    comment_nickname = models.CharField(max_length=25)
    comment_password = models.CharField(max_length=8) 
    created_on = models.DateTimeField(auto_now_add=True)
