from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include([
        path('about', views.about, name='about'),
        path('contact', views.contact, name='contact'),
        path('registration/', views.registration_request, name='registration'),
        path('login/', views.login_request, name='login'),
        path('logout/', views.logout_request, name='logout'),
        path('', views.get_dealerships, name='index'),
        path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
        path('dealer/<int:dealer_id>/add-review/', views.add_review, name='add_review'),
    ])),
    path('', TemplateView.as_view(template_name='index.html')),
]
