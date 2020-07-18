"""elder_gurder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from elder_gurder_service import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    # users
    path('',views.homepage),
    path('registration',views.registration),
   
    #
    # path('people_list',views.people_list), 
    # path('people_detail',views.people_detail),
    # path('add_visit',views.add_visit),
    # path('add_visit_permission',views.add_visit_permission),
    # path('visit_detail',views.visit_detail),
    # path('edit_visit',views.edit_visit),
    # path('delete_visit',views.delete_visit),
    
    path('converstions_ideas' , views.converstions_ideas),
    
    # lonely
    path('create_loenly' , views.CreateLonely.as_view()),
    path('lonely_peoples', views.LonelyPeoples.as_view(), name='lonely_peoples'),
    path('lonely/<int:pk>', views.LonelyDetails.as_view() , name='lonely'), 
    path('delete_lonely/<int:pk>', views.DeleteLonelyView.as_view(), name='delete_lonely'),
    path('update_lonely/<int:pk>', views.UpdateLonelyView.as_view(), name='update_lonely'),
    #visits
    path('create_visit', views.CreateVisit.as_view(), name='create_visit'),
    path('list_view_visits/<int:loneny_id>', views.ListViewVisits.as_view(), name='list_view_visits'),
    path('detail_view_visit/<int:pk>', views.DetailViewVisit.as_view(), name='detail_view_visit'),
    path('update_view_visit/<int:pk>', views.UpdateViewVisit.as_view(), name='update_view_visit'),
    path('delete_view_visit/<int:pk>/<int:loneny_id>', views.DeleteViewVisit.as_view() , name='delete_view_visit'),
]
                            