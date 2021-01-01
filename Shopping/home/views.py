from django.shortcuts import render
from.models import destinate,destination,destin,destin1,destin2,destin3,destin4,destin5
def home(request):
    destinatedata=destinate.objects.all()
    destinationdata=destination.objects.all()
    destindata=destin.objects.all()
    destin1data=destin1.objects.all()
    destin2data=destin2.objects.all()
    destin3data=destin3.objects.all()
    destin4data=destin4.objects.all()
    destin5data=destin5.objects.all()

    dests={
        'destinate':destinatedata,
        'destination':destinationdata,
        'destin':destindata,
        'destin1':destin1data,
        'destin2':destin2data,
        'destin3':destin3data,
        'destin4':destin4data,
        'destin5':destin5data,
        

        }
        
    return render(request,'home.html',dests)