from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from uuid import uuid4
from tinymce.models import HTMLField


def dir_path(instance, file_name):
    """
        The path where the cover is stored.
        Like This:
            media/images/user_xxx/2021-11-17-uuid4.fmt #file format
    """

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    user = instance.author
    unique = uuid4().hex
    fmt = file_name.split(".")[-1]

    path = f"images/user_{user}/{year}-{month}-{day}-{unique}.{fmt}"
    return path


class Post(models.Model):

    STATUS_CHOICES = (
        ("Publish", "publish ✅"),
        ("Draft", "draft ❌")
    )
	
	# < Main >
    author = models.ForeignKey(
        to=User,
        related_name="blog_post",
        on_delete=models.CASCADE,
        default="admin")
  
    title = models.CharField(
        max_length=120,
        null=True)

    slug = models.SlugField(
        max_length=150,
        unique=True)

    body = HTMLField()
 
    summary = models.CharField(
        max_length=250,
        blank=True,
        null=True)
    
    avatar = models.ImageField(upload_to=dir_path)

    # < Date >
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(auto_now_add=False)
    update_date = models.DateTimeField(auto_now=True) 

    # < Metadata >
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    status = models.CharField(
        max_length=40, 
        choices=STATUS_CHOICES, 
        default="Draft")

    likes = models.ManyToManyField(
        to=User,
        blank=True,
        related_name="psot_like",
        default="0")

    views = models.PositiveIntegerField(
        null=True,
        blank=True, 
        default=0)

    tags = models.ManyToManyField(
        "Tag",
        blank=True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Blog Post'


    def __str__(self):
        return self.title
   

    def total_likes(self):
        return self.likes.count()


    def total_comments(self):
        return self.post_comment.count()
   

    def user_can_like(self, user):
        """
            Get all posts and send query to check 
            current user(request.user) can like or not!
		"""
        liked_posts = []
        for post in self.objects.all():
            if not post.likes.filter(username=user):
                liked_posts.append(post.id)
        return liked_posts


    def get_absolute_url(self):
        date = self.publish_date 
        return reverse("Posts:post", args=[date.year, date.month, date.day, self.id, self.slug])
    

    def thumbnail_preview(self):
        from django.utils.html import format_html
        return format_html(f'<img src="{self.avatar.url}" width="150" height="100" style="border-radius:5px;"/>')

 
class Comment(models.Model):
    """ """
    author = models.ForeignKey(
        to=User, 
        related_name="user_comment", 
        on_delete=models.CASCADE)

    post = models.ForeignKey(
        to=Post,
        related_name="post_comment",
        on_delete=models.CASCADE)

    reply = models.ForeignKey(
        to="self",
        related_name="blog_reply_comment",
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    body = models.TextField()
    is_replay = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True)

    slug = models.SlugField(
        max_length=60,
        default="no-slug",
        blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Tag"
        verbose_name_plural = verbose_name


class Category(models.Model):
    pass

