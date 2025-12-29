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
        p=req.POST.get('password')
        cp=req.POST.get('cpassword')
        c = req.POST.get('contact')
        i = req.FILES.get('image')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('resume')
        ql=req.POST.getlist('qualification[]')
        q=','.join(ql)
        g = req.POST.get('gender')
        s = req.POST.get('state')
        print(n,e,p,cp,c,i,a,v,d,q,g,s, end='\n')

        user=emp.objects.filter(email=e)
        if user:
            req.session['msg']=f'{e} Email already exists'
            redirect ('registration')
        else:
            if p==cp :
                Employee.objects.create(
             name=n,
             email=e,
             password=p,
             contact=c,
             qualification=q,
             gender=g,
            state=s,
            image=i,
            audio=a,
            video=v,
            document=d
             )
            else:
                
        
                

        




#         Employee.objects.create(
#             name=n,
#             email=e,
#             contact=c,
#             qualification=q,
#             gender=g,
#             state=s,
#             image=i,
#             audio=a,
#             video=v,
#             document=d
#             )

#         return HttpResponse('successfull')

#     return render(req, 'registration.html')
# def data(req):
#     # query that works on single-object
#     # data =emp.objects.get(id=1)
#     # data =emp.objects.latest('name')
#     # data =emp.objects.first()
#     # data =emp.objects.earliest('name')
#     # data =emp.objects.last()
#     # query that works on multiple-objects
#     # data = Employee.objects.all()
#     # data = Employee.objects.filter(gender='Female')
#     # data = Employee.objects.exclude(gender='Female')
#     # data = Employee.objects.order_by('name')
#     # data = Employee.objects.order_by('name')
#     # data = Employee.objects.order_by('-name')
# #     data = (
# #     Employee.objects
# #     .filter(state__in=['Delhi','Maharashtra','Karnataka'])
# #     .exclude(gender="Female")
# #     .order_by("id")
# #     .reverse()
# # )   
#     # data=Employee.objects.values()
#     data = Employee.objects.values_list('name','email','state','gender')



    
#     print(data, end='/n')
    
#     return render(req,'data.html',{'msg':data})

    


