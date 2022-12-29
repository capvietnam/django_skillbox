# from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm, MultiFileForm
# from .models import Avatar
from django.contrib.auth.models import User

from .models import File


def UploadFile(request):
    if request.method == 'POST':
        add_file_form = UploadFileForm(request.POST, request.FILES)
        if add_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        add_file_form = UploadFileForm()

    context = {
        'form': add_file_form
    }
    return render(request, 'upload_file.html', context=context)


def UploadFiles(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for file in files:
                instans = File(file=file)
                instans.save()
            return redirect('/blog')
    else:
        form = MultiFileForm()
    return render(request, 'upload_file.html', {'form': form})

# def UploadAvatar(request):
#     if request.method == 'POST':
#         form = AvatarForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('/blog')
#     else:
#         form = AvatarForm(instance=request.user)
#
#     return render(request, 'upload_avatar.html', {'form': form})
#

# def UploadAvatar(request):
#     if request.method == 'POST':
#         form = AvatarForm(request.POST)
#         if form.is_valid():
#             avatar = form.cleaned_data.get('avatar')
#             request.user.objects.filter(request.user).create(avatar=avatar)
#             return redirect('news-list')
#     else:
#         form = AvatarForm()
#     return render(request, 'app_users/user-register.html', {'form': form})
