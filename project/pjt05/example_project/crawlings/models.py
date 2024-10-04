from django.db import models

class Article(models.Model):
    query = models.TextField()
    title = models.TextField()


# 하나의 query로 여러 개의 게시글을 검색할 수 있음
# class Query(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#     name = models.TextField()