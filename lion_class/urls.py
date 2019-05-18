from django.contrib import admin
from django.urls import path, include
import blog.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('post/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]
