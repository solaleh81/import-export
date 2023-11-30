from django.shortcuts import render
from .forms import CsvModelForm

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    return render(request, 'csvs/upload.html', context={'form': form})