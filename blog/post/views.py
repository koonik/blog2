from django.shortcuts import *
from post.models import Post, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('post/post_list.html', {'posts': posts})




def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/detail.html', {'post': post})

def error404(request):
    return render(request, 'post/404.html')


def log_in_page(request, template_name='registration/login.html', authentication_form=AuthenticationForm):
        if request.method == 'POST':
            form = authentication_form(request.POST)
            if form.is_valid():  # All validation rules pass
                form.save()
                return HttpResponseRedirect('/login/')    # Redirect after POST
        else:
                form = authentication_form()

        return render(request, template_name, {'form': form, })


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/post/')
        else:
            return HttpResponseRedirect('/account/login/', {'errors': 'user is disabled'})
    else:
        return HttpResponseRedirect('/account/login/', {'errors': 'login is not valid'})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/post/')


@login_required(login_url='/account/login/')
def blog_view(request):
    post_list = Post.objects.all()
    return render(request, 'post/blog_view.html', {'post_list': post_list})


def add_post(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = PostForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            return HttpResponseRedirect('/account/blog/')

    else:
        form = PostForm()

    return render(request, 'post/add_post.html', {'form': form, })


def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':  # If the form has been submitted...
        form = PostForm(request.POST, instance=post)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            return HttpResponseRedirect('/account/blog/')    # Redirect after POST
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_edit.html', {'form': form, 'post':post, })

