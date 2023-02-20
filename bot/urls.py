from django.urls import path
from . import views,admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_call_counts/', views.user_call_counts, name='user_call_counts'),
]
