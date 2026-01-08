from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Employee as emp,Employee1 as emp1, Department as dept,Query


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
            # print("Saving to DB")
            # return redirect('registration')
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
                'name':'Sony',
                'email':'deepaknab17@gmail.com',
                'contact':'9874561230',
                'password':'deepakNAB@17'}
            req.session['admin']=data
            return redirect('dashboard')
        
        else:
            
            user = emp1.objects.filter(email=e)
            if not user:
                print("No user :", req.session)
                req.session['sign_up'] = f'{e} is not an user employee'
                return redirect('login')
            else:
                user_data = emp1.objects.get(email=e)
                db_password = user_data.password
                if p == db_password:
                    req.session['user_id'] = user_data.id
                    return redirect('dashboard')
                else:
                    req.session['msg1'] = 'Incorrect password'
                    return redirect('login')

    msg = req.session.pop('msg1', None)
    sign=req.session.pop('sign_up',None)
    return render(req, 'login.html', {'msg1': msg,'sign_up':sign})

def dashboard(req):
    print("SESSION CONTENT:", dict(req.session))
    if req.session.get('admin',None):
        data=req.session.get('admin')
        return render(req,'admindashboard.html',{'data':data})
    elif req.session.get('user_id',None):
        id = req.session['user_id']
        user= emp1.objects.get(id=id)
        return render(req, 'userdashboard.html', {'user':user})
    else:
        return redirect('login')
def userdashboard(req):
    if 'user_id' not in req.session:
        return redirect('login')
def add_emp(req):

    if 'admin' in req.session:
        print('admin is here')

        data = req.session.get('admin')

        if req.method == 'POST':

            n = req.POST.get('name')
            e = req.POST.get('email')
            c = req.POST.get('contact')
            p = req.POST.get('password')
            cp = req.POST.get('cpassword')
            img = req.FILES.get('profile')
            dep = req.POST.get('department')
            dep_data= dept.objects.get(id=dep)
            d_name=dep_data.name
            d_code=dep_data.code
            d_des=dep_data.description

            print(n, e, c, p,dep,dep_data)

            user = emp1.objects.filter(email=e)

            if user:
                req.session['msg'] = f'{e} Email already exists'
                return redirect('add_emp')
            else:
                if p == cp:
                    emp1.objects.create(
                        name=n,
                        email=e,
                        contact=c,
                        password=p,
                        profile=img,
                        department=d_name,
                        d_code=d_code,
                        d_des=d_des
                    )
                    send_mail("User id and Password from admin",
                              f'your user_id is {e} and password is {p}',
                              'deepaknab17@gmail.com',
                              [e],
                              fail_silently=False)
                    req.session['message'] = 'employee added successfully and user_id sent to mail'
                    return redirect('add_emp')
                
                else:
                    req.session['msg'] = 'Password did not match'
                    return redirect('add_emp')
        
        msg = req.session.pop('msg', None)
        message = req.session.pop('message', None)
        all_dept=dept.objects.all()
        return render(req, 'admindashboard.html', {
            'data': data,
            'add_emp': True,
            'msg': msg,
            'message': message,
            'all_dept':all_dept})  
def add_dept(req):
    if 'admin' in req.session:
        print("Dept")
        if req.method=='POST':
            n=req.POST.get('name')
            c=req.POST.get('code')
            d=req.POST.get('description')
            print(n,c,d)
            depart=dept.objects.filter(code=c)
            if depart:
                req.session['msg']='department already exists'
            else:
                dept.objects.create(
                    name=n,
                    code=c,
                    description=d)
                req.session['message']='Department created successfully'
                return redirect('add_dept')
        msg = req.session.pop('msg', None)
        message = req.session.pop('message', None)   
        return render(req,'admindashboard.html',{'add_dept':True,'msg':msg,'message':message})                                           
def show_emp(req):
    if 'admin' not in req.session:
        return redirect('login')
    data=req.session.get('admin')
    employees=emp1.objects.all()
    return render(req,'admindashboard.html',{'data':data,'employees':employees,'show_emp':True})                                    
def show_dept(req):
    if 'admin' not in req.session:
        return redirect('login')
    # data=req.session.get('admin')
    departments=dept.objects.all()
    return render(req,'admindashboard.html',{'departments':departments,'show_dept':True})
def delete(req,id):
    if 'admin' not in req.session:
        return redirect('login')
    else:
        data = emp1.objects.get(id=id)
        data.delete()
        return redirect('show_emp')
def delete_query(req,id):
    data = Query.objects.get(id=id)
    data.delete()
    all_query = Query.objects.all()
    return render(req,'userdashboard.html',{'query':all_query})
def show_query(req):
    if 'admin' not in req.session:
        return redirect('login')

    all_query = Query.objects.all()
    return render(req, 'admindashboard.html', {'query': all_query})

def query(req):
    print("query form is open")
    if req.method == "POST":
        n= req.POST.get('name')
        e= req.POST.get('email')
        s=req.POST.get('subject')
        q = req.POST.get('query')
        print(n,e,s,q)
        Query.objects.create(
            name=n,
            email=e,
            subject=s,
            query=q,
        )
        messages.success(req, 'Query submitted successfully!')
        return redirect('dashboard')
    id=req.session['user_id']
    user= emp1.objects.get(id=id)
    return render(req, 'userdashboard.html',{'query':True,'user':user})
def query_status(req):
    user_id = req.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = emp1.objects.get(id=user_id)
    queries = Query.objects.filter(email=user.email)

    return render(req, 'userdashboard.html', {
        'user': user,
        'query_status': True,
        'queries': queries
    })
def reply(req,id):
    if 'admin' not in req.session:
        return redirect('login')
    if req.session.get('admin',None):
        data=req.session.get('admin')
        if req.method=='POST':
            print('reply page')
            r=req.POST.get('reply')
            querydata=Query.objects.get(id=id)
            if len(r)>1:
                querydata.solution=r
                querydata.status="Done"
                querydata.save()
                queries=Query.objects.all().order_by('created_at')
                req.session['mess']='Reply Sent'
                mess=req.session.pop('mess',None)
                return render(req,'admindashboard.html',{'data':data,'queries':queries,'mess':mess,'id':id})
        else:
            return render(req, 'admindashboard.html', {'data': data,'reply':True,'id':id})
            

    
    

def profile(req):

    user_id = req.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = emp1.objects.get(id=user_id)
    print("PROFILE FIELD IN VIEW:", user.profile)
    return render(req, 'userdashboard.html', {'user': user,'profile':True})

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

    


