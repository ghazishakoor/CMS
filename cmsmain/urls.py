from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('student_list/', views.StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student_create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student_update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('student_success/', views.student_success_view, name='student_success'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher_update/<int:pk>', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
    path('teacher_success/', views.teacher_success_view, name='teacher_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
