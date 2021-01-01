from django.shortcuts import render
from.models import aboutus,lesson,team,surfing
def about(request):
    aboutusdata=aboutus.objects.all()
    lessondata=lesson.objects.all()
    teamdata=team.objects.all()
    surfingdata=surfing.objects.all()

    context={
        'aboutus':aboutusdata,
        'lesson':lessondata,
        'team':teamdata,
        'surfing':surfingdata,
    }
    return render(request,'about.html',context)
