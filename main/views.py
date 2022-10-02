from django.shortcuts import render , redirect
from .models import Post
from .form import FileUploadForm
from .models import  FileUpload

def index(request):
    return render(request, 'main/index.html')

# def blog(request):
#     postlist = Post.objects.all()
#     return render(request, 'main/blog.html', {'postlist':postlist})

def blog(request):
    postlist = FileUpload.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

# def posting(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'main/posting.html', {'post':post})

def posting(request, pk):
    post = FileUpload.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post':post})

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title=title,
            content=content,
            imgfile=img,
        )
        fileupload.save()
        return redirect('main:blog')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'main/fileupload.html', context)

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('main:blog')
    return render(request, 'main/new_post.html')

# Create your views here.
