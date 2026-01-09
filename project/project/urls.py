"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('data/',views.data,name='data'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/add_emp/',views.add_emp,name='add_emp'),
    path('dashboard/add_dept/',views.add_dept,name='add_dept'),
    path('dashboard/show_dept/',views.show_dept,name='show_dept'),
    path('dashboard/show_emp/',views.show_emp,name='show_emp'),
    path('userdashboard/profile/',views.profile,name='profile'),
    path('userdashboard/query/edit/<int:pk>/',views.edit,name='edit'),
    path('userdashboard/query/update/<int:pk>/',views.update,name='update'),
    path('query/delete_query/<int:id>/',views.delete_query,name='delete_query'),
    path('admindashboard/reply/<int:id>/',views.reply,name='reply'),
    path('dashboard/query/',views.query,name='query'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    path('userdashboard/query_status/',views.query_status,name='query_status'),
    path('show_query/',views.show_query,name='show_query'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('logout/',views.logout,name='logout'),

    # path('register_data',views.register_data,name='register_data')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
