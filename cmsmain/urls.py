from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('student_list/', views.StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student_create/', views.StudentCreateView.as_view(), name='student_create'),
    path('success/', views.my_success_view, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
