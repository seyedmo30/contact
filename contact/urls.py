
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from phone import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/<int:grp_id>/',views.contacts ,name='contacts'),
    path('contacts/', views.contacts_all,name='contacts_all'),
    path('contacts/<int:grp_id>/delete/<int:contact_id>/',views.delete ,name='delete'),
    path('contacts//delete/<int:contact_id>/',views.delete_a ,name='delete_a'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('add/', views.add,name='add'),
    path('contacts/update/<int:contact_id>/',views.update ,name='update'),
    path('add_grp/', views.add_grp,name='add_grp'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
