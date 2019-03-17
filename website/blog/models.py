from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Post(models.Model):
    # article status
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    objects = models.Manager()  # The default manager.

    published = PublishedManager()  # Our custom manager

    # title
    title = models.CharField(max_length=1000)

    # slug
    slug = models.SlugField(max_length=1000,
                            unique_for_date='publish')

    # link to author
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               on_delete=models.PROTECT)

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
                              default='draft')

    def get_absolute_url(self):
        """ build canonical url """

        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        # articles are ordered in descending order
        # according the date of their publication
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    published = PublishedManager()  # Our custom manager.
