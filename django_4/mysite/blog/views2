from django.views.generic import ListView

class PostListView(ListView):
    """ 
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
    