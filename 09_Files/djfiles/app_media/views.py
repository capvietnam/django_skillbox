from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm


def UploadFile(request):
    if request.method == 'POST':
        add_file_form = UploadFileForm(request.POST, request)
        if add_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        add_file_form = UploadFileForm()

    context = {
        'form': add_file_form
    }
    return render(request, 'upload_file.html', context=context)
