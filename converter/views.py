from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .utils import perform_conversion

def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        
        # 1. Save PDF to Media Folder
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        pdf_path = fs.path(filename)
        
        # 2. Run Conversion (Synchronous)
        docx_path = perform_conversion(pdf_path)
        
        if docx_path:
            # Generate download URL
            download_url = settings.MEDIA_URL + os.path.basename(docx_path)
            return render(request, 'converter/result.html', {
                'download_url': download_url,
                'filename': os.path.basename(docx_path)
            })
            
    return render(request, 'converter/upload.html')