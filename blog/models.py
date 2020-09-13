from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
             self).get_queryset()\
                          .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    picture = models.ImageField(blank=True, null=True,
                                upload_to='blog/%Y/%m/%d')
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.was_status = self.status

    def save(self, *args, **kwargs):
        if self.status == 'published' and self.status != self.was_status:
            self.publish = timezone.now()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
               args=[self.publish.year,
               self.publish.month,
               self.publish.day,
               self.slug])

    def get_change_url(self):
        link = reverse('admin:blog_post_change', args=(self.id,))
        return link

    def next_published(self):
        next_post = (Post.objects
                    .filter(status='published', publish__gt=self.publish)
                    .exclude(id=self.id)
                    .order_by('publish')
                    .first())
        return next_post

    def prev_published(self):
        prev_post = (Post.objects
                    .filter(status='published', publish__lt=self.publish)
                    .exclude(id=self.id)
                    .order_by('-publish')
                    .first())
        return prev_post
