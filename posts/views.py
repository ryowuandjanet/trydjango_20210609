from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from posts.models import Post
from posts.forms import PostForm
from django.core.paginator import Paginator

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

def post_detail(request,id=None):
  instance = get_object_or_404(Post,id=id)
  context={
    "title" : instance.title,
    "instance" : instance,
  }
  return render(request, "post_detail.html",context)

def post_create(request):
  form = PostForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance=form.save(commit=False)
    print(form.cleaned_data.get("title"))
    instance.save()
    messages.success(request,"successfully Created")
    return HttpResponseRedirect(instance.get_absolute_url())
  context = {
    "form" : form, 
  }
  return render(request, "post_form.html",context)

def post_update(request,id=None):
  instance = get_object_or_404(Post,id=id)
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

def post_delete(request,id=None):
  instance = get_object_or_404(Post, id=id)
  if request.method == "POST":
    instance.delete()
    messages.success(request, 'Data Deleted.')
    return redirect("posts:list")
  context = {"instance": instance}
  return render(request, "post_delete.html", context)


