from django.contrib import admin
from django.urls import path
from engine import views  # Import your new engine app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # The UI Home Page
    path('api/process/', views.process_prompt, name='process_api'),  # The Logic Endpoint
]