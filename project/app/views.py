from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse

def landing(req):
    return render(req, 'landing.html')

def registration(req):

    if req.method == 'POST':

        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')

        i = req.FILES.get('image')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('resume')
        ql=req.POST.getlist('qualification[]')
        q=','.join(ql)
        g = req.POST.get('gender')
        s = req.POST.get('state')

        Employee.objects.create(
            name=n,
            email=e,
            contact=c,
            qualification=q,
            gender=g,
            state=s,
            image=i,
            audio=a,
            video=v,
            document=d
            )

        return HttpResponse('successfull')

    return render(req, 'registration.html')
