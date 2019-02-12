
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from phone import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',views.contacts,name='contacts'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
