
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from phone import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/<int:grp_id>/',views.contacts ,name='contacts'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('add/', views.add,name='add'),
    path('add_grp/', views.add_grp,name='add_grp'),
    path('contacts/', views.contacts_all,name='contacts_all'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
