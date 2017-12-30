from django.db import models


class Board(models.Model):

    title = models.CharField(max_length=200)
    views = models.PositiveIntegerField(default=0)
    content = models.TextField()
    writer = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class Comment(models.Model):

    board = models.ForeignKey(
        'Board',
        on_delete=models.CASCADE
    )

    content = models.TextField()
    writer = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)