from django.shortcuts import render, get_object_or_404
from .models import Pages


def pages(request,page_id,page_slug):
    page = get_object_or_404(Pages,id=page_id)
    #servicios = Service.objects.all()
    return render(request,'pages/sample.html',{'page':page})
# Create your views here.
