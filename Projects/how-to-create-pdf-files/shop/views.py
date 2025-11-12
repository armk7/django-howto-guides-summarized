from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, FileResponse

import io
from reportlab.pdfgen import canvas

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def download_pdf(request: HttpRequest) -> FileResponse:

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
