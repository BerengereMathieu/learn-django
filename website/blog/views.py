from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """ display a list of post"""

    # get full list of posts
    object_list = Post.published.all()

    # display 3 posts by pages
    paginator = Paginator(object_list, 3)

    # get page
    page = request.GET.get('page')

    try:
        # display the page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # the page is not an integer: deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # page is out of range: deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, slug):
    """ display a single post"""

    post = get_object_or_404(Post, slug=slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
