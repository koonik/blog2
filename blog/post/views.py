from django.shortcuts import *
from post.models import Post


def index(request):
    post_list = Post.objects.all()[:50]
    template = loader.get_template('post/post_list.html')
    context = RequestContext(request, {
        'post_list': post_list,
    })
    return HttpResponse(template.render(context))


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/detail.html', {'post': post})

def error404(request):
    return render(request, 'post/404.html')



