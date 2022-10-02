from django.db import models

# 많이 본 뉴스
class NaverTitle(models.Model):
    create_date = models.DateField()
    name = models.CharField(max_length=50)
    link = models.TextField()
    title = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = u'NEWS_TITLE_FINAL'

    def __str__(self):
        return str(self.name)

# 댓글 많은 뉴스
class NaverComment(models.Model):
    create_date = models.DateField()
    name = models.CharField(max_length=50)
    link = models.TextField()
    title = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = u'NEWS_COMMENT_FINAL'

    def __str__(self):
        return str(self.name)