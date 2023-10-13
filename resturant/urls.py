#import of the views at resturant app and url paths
from django.urls import path
from resturant import views

# Url paths for all the pages in the site
urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu_page/', views.menu_page, name='menu_page'),
    path('make_reservation/', views.make_reservation, name='make_reservation'),
    path('view_reservation/', views.view_reservation, name='view_reservation'),
    path('edit_or_delete_reservation/<int:reservation_id>/', views.edit_or_delete_reservation, name='edit_or_delete_reservation'),
    path('contact_page', views.contact_page, name='contact_page'),
    path('search_reservation/', views.search_reservation, name='search_reservation')
]