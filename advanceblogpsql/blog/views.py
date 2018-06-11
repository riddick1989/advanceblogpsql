from django.contrib import messages
from django.shortcuts import render , Http404 ,get_object_or_404 ,HttpResponsePermanentRedirect,redirect
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from . models import Post
from .forms import Postform
# Create your views here.

def post_create(request):
    template_name ="templates\post_create.html"
    return render(request,template_name,context=locals())


            # '''Make a list of our post'''#
'' '...................................................................'''
def post_list(request):
    item = Post.objects.all()
    context = {
        "object_list":item
    }
    template_name = "templates/base.html"
    return render(request,template_name,context)

           #  '''Make single post_page '''   #
''''.................................................................'''
def post_detail(request,id= None):
    detail_list = get_object_or_404 (Post,id=id)
    context = {
            "details_list": detail_list
    }
    template_name = "templates/post-detail.html"

    return render (request, template_name, context)
'''.....................................................................'''

                #'''Make a post'''#
'''.....................................................................'''
def post_create(request):
    form = Postform(request.POST or None)
    if form.is_valid():
         instance = form.save(commit=False)
         instance.save()
         messages.success(request,"successfully created")
    context = {
        "myform":form
    }
    template_name = "templates/post_form.html"
    return render(request,template_name,context)

                # update a post #
'''......................................................................'''

def post_update(requset,id):
    instance = get_object_or_404(Post,id=id)
    form = Postform (requset.POST or None,instance=instance)
    if form.is_valid ():
        instance = form.save (commit=False)
        instance.save ()
    context = {
        "myform": form,
        "details_list": instance
    }
    template_name = "templates/post_form.html"
    return render (requset, template_name, context)

                #delet a post
'''..........................................................................'''

def post_delete(request,id):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    return redirect("blogs:base")






'''class post_deleteview(DeleteView):
    model = Post

class post_updateview(UpdateView):
    model = Post








##class post_createview(CreateView):
  ##  model = Post





class post_listview(ListView):
    model = Post

class post_detailview(DetailView):
    model = Post

'''