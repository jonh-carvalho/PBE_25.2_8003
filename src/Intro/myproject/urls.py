from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),  # URLs tradicionais
    path('api/', include('myapp.api_urls')),  # URLs da API
]
