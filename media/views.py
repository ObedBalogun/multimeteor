from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView,DeleteView

from .models import Post, Media
from .forms import PostForm,GalleryForm
# from django.views.generic import
from user.forms import UserAccount
# Create your views here.

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
OTHER_FILE_TYPES = ['']
def home(request):
    context = {}
    if request.POST:
        user = request.user
        form = PostForm(request.POST)
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.author = UserAccount.objects.get(id=request.user.id)
            form_temp.save()
            form.save()
            return HttpResponseRedirect(reverse('media:homepage'))

            # return render(request,'media/index.html',context)
    else:
        form = PostForm()
        context['form'] = form
    context['posts'] = Post.objects.all()
    return render(request, 'multi/index.html', context)

def posts(request):
    context ={}
    if request.POST:
        user = request.user
        form = PostForm(request.POST)
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.author = UserAccount.objects.get(id=request.user.id)
            form_temp.save()
            form.save()
            return render(request,reverse('media:homepage'))
    else:
        form = PostForm()
        context['form'] = form
    return render(request, reverse('media:homepage'), context)


class MediaDetail(DetailView):
    model = Media
    template_name = 'multi/media.html'
    context_object_name = 'files'
    def get_object(self, queryset=None):
        queryset = Media.objects.filter(author=self.request.user)
        return queryset

def media(request):
    image_list = []
    files = Media.objects.filter()
    for file in files:
        if file.files.url.split('.')[-1] == 'png':
            image_list.append(file)
    print(image_list)
    pass

def contact(request):
    return render(request, 'multi/contact.html')


def upload(request):
    context = {}
    if request.method =='POST':
        file_object = GalleryForm(request.POST or None,request.FILES or None)
        if file_object.is_valid():
            temp = file_object.save(commit=False)
            temp.author = request.user
            temp.files = request.FILES['files']
            print(temp.files.url.split('.')[-1])
            temp.save()
            gallery_object_save = file_object.save()
            return redirect(reverse('media:media'))
    else:
        form = GalleryForm()
        context['form'] = form
    return render(request,'multi/upload.html',context)


class PostDelete(DeleteView):
    template_name = "multi/post_delete.html"

    def get_object(self,**kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse("media:homepage")
