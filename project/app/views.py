from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from .models import Employee as emp

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
def data(req):
    # query that works on single-object
    # data =emp.objects.get(id=1)
    # data =emp.objects.latest('name')
    # data =emp.objects.first()
    # data =emp.objects.earliest('name')
    # data =emp.objects.last()
    # query that works on multiple-objects
    


    print(data.name,data.email,data.contact)
    return render(req,'data.html', {'msg': data})

