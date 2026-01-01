from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from .models import Employee as emp

def landing(req):
    return render(req, 'landing.html')

def registration(req):
    print("METHOD:", req.method)
    print("POST DATA:", req.POST)
    print("FILES:", req.FILES)

    if req.method == 'POST':

        n = req.POST.get('name')
        e = req.POST.get('email')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        c = req.POST.get('contact')
        i = req.FILES.get('image')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('resume')
        ql = req.POST.getlist('qualification[]')
        q = ','.join(ql)
        g = req.POST.get('gender')
        s = req.POST.get('state')

        print(n, e, p, cp, c, i, a, v, d, q, g, s, end='\n')

        user = emp.objects.filter(email=e)
        if user:
            req.session['msg'] = f'{e} Email already exists'
            return redirect('registration')
        else:
            if p == cp:
                emp.objects.create(
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
                req.session['msg1'] = "Registration Successfull"
                return redirect('login')
            else:
                req.session['msg'] = 'Password did not match'
                return redirect('registration')

    msg = req.session.pop('msg', None)
    return render(req, 'registration.html', {'msg': msg})

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e=='deepaknab17@gmail.com' and p=='deepakNAB@17':
            data={
                'name':'Deepak',
                'email':'deepaknab17@gmail.com',
                'contact':'9874561230',
                'password':'deepakNAB@17'}
            req.session['admin']=data
            return redirect('dashboard')
        
        else:
            
            user = emp.objects.filter(email=e)
            if not user:
                req.session['sign_up'] = f'{e} not registered'
                return redirect('registration')
            else:
                user_data = emp.objects.get(email=e)
                db_password = user_data.password
                if p == db_password:
                    req.session['user_id'] = user_data.id
                    return redirect('dashboard')

    msg = req.session.pop('msg1', None)
    return render(req, 'login.html', {'msg1': msg})

def dashboard(req):
    print("SESSION CONTENT:", dict(req.session))
    if req.session.get('admin',None):
        data=req.session.get('admin')
        return render(req,'admindashboard.html',{'data':data})
    elif req.session.get('user_id',None):
        id = req.session['user_id']
        user_data = emp.objects.get(id=id)
        return render(req, 'userdashboard.html', {'data': user_data})
    else:
        return redirect('login')
def logout(req):
    if req.session.get('user_id',None):
        req.session.flush()
    return redirect('login')




 
                

        




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
def data(req):
    # query that works on single-object
    # data =emp.objects.get(id=1)
    # data =emp.objects.latest('name')
    # data =emp.objects.first()
    # data =emp.objects.earliest('name')
    # data =emp.objects.last()
    # query that works on multiple-objects
    # data = Employee.objects.all()
    # data = Employee.objects.filter(gender='Female')
    # data = Employee.objects.exclude(gender='Female')
    # data = Employee.objects.order_by('name')
    # data = Employee.objects.order_by('name')
    # data = Employee.objects.order_by('-name')
#     data = (
#     Employee.objects
#     .filter(state__in=['Delhi','Maharashtra','Karnataka'])
#     .exclude(gender="Female")
#     .order_by("id")
#     .reverse()
# )   
    # data=Employee.objects.values()
    data = Employee.objects.values_list('name','email','state','gender')



    
    print(data, end='/n')
    
    return render(req,'data.html',{'msg':data})

    


