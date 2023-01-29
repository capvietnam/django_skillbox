from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm, MultiFileForm
from .models import File


@login_required
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


@login_required
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
