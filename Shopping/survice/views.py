from django.shortcuts import render
from.models import survice
def surviceus(request):
    survicedata=survice.objects.all()
    context={
        'survice':survicedata
    }


    return render(request,'survice.html',context)
