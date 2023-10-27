from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from  .models import *
from django.core.paginator import Paginator
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    #paginator with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    #try:
        #post = Post.published.get(id=id)

    #except Post.DoesNotExist:
       # raise Http404('No Post found.')
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             #publish__year=year,
                             #publish__month=month,
                             #publish__day=day
                             )
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recommends you read " \
                        f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                        f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'stannjoroge643@gmail.com',
                      [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
