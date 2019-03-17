from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    # article status
    STATUS_CHOICES = (
        ('brouillon', 'Brouillon'),
        ('publié', 'Publié'),
    )

    # title
    title = models.CharField(max_length=1000)

    # slug
    slug = models.SlugField(max_length=1000,
                            unique_for_date='publish')

    # link to author
    author = models.ForeignKey(User,
                               related_name='blog_posts')

    # article content
    body = models.TextField()

    # when the post was published
    publish = models.DateTimeField(default=timezone.now)

    # when the post was created
    created = models.DateTimeField(auto_now_add=True)

    # date of the last update
    updated = models.DateTimeField(auto_now=True)

    # article status
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0])

    class Meta:
        # articles are ordered in descending order
        # according the date of their publication
        ordering = ('-publish',)

    def __str__(self):
        return self.title
