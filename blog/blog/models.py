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

    # content
    body = models.TextField()

    # publication date
    publish = models.DateTimeField(default=timezone.now)

    # creation date
    created = models.DateTimeField(auto_now_add=True)

    # date of last update
    updated = models.DateTimeField(auto_now=True)

    # status
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='brouillon')

    class Meta:
        # ordering in publication date descending order
        ordering = ('-publish',)

    def __str__(self):
        """conversion to string"""
        return self.title
