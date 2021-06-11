from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from posts.models import Post
from posts.forms import PostForm
from django.core.paginator import Paginator
from django.utils.http import quote_plus

def post_list(request):
  queryset_list=Post.objects.all().order_by("-timestamp")
  paginator = Paginator(queryset_list, 3) # Show 25 contacts per page
  page_request_var="pagecode"
  page = request.GET.get(page_request_var)
  queryset = paginator.get_page(page)
  context={
   "title":"List",
   "object_list":queryset,
   "page_request_var" : page_request_var
  }
  return render(request,"post_list.html",context)

def post_detail(request,slug=None):
  instance = get_object_or_404(Post,slug=slug)
  share_string=quote_plus(instance.content)
  context={
    "title" : instance.title,
    "instance" : instance,
    "share_string": share_string,
  }
  return render(request, "post_detail.html",context)

def post_create(request):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = PostForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.user=request.user
    instance.save()
    messages.success(request,"successfully Created")
    return HttpResponseRedirect(instance.get_absolute_url())
  context = {
    "form" : form, 
  }
  return render(request, "post_form.html",context)

def post_update(request,slug=None):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  instance = get_object_or_404(Post,slug=slug)
  form=PostForm(request.POST or None, request.FILES or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    messages.success(request,"<a href='#'>Item </a>Saved",extra_tags='html_safe')
    return HttpResponseRedirect(instance.get_absolute_url())
  context={
    "title" : instance.title,
    "instance" : instance,
    "form" : form,
  }
  return render(request, "post_form.html",context)

def post_delete(request,slug=None):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  instance = get_object_or_404(Post, slug=slug)
  if request.method == "POST":
    instance.delete()
    messages.success(request, 'Data Deleted.')
    return redirect("posts:list")
  context = {"instance": instance}
  return render(request, "post_delete.html", context)


