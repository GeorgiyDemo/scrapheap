from django.db import models

class Article(models.Model):
    title = models.CharField("Название статьи", max_length=200)
    text = models.TextField("Текст статьи")
    pub_date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return f"title: {self.title}, text: {self.text}, pub_date: {self.pub_date}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField("Имя автора", max_length=50)
    text = models.CharField("Текст комментария", max_length=200)

    def __str__(self):
        return f"article: {self.article}, name: {self.name}, text:{self.text}"