from django import template
from django.db.models import Count, Q
from django.utils.safestring import mark_safe
import markdown
from ..models import Post, Comment




register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments',
                                                        filter=Q(comments__active=True))) \
        .exclude(total_comments=0).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def post_by_user(username):
    return Post.objects.filter(author=username).count()

@register.simple_tag
def comments_by_user(email):
    return Comment.objects.filter(email=email).count()