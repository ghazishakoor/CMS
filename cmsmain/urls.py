from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('student_page/', views.StudentPage, name='student_page'),
    path('teacher_page/', views.TeacherPage, name='teacher_page'),
    path('admin_page/', views.AdminPage, name='admin_page'),
    path('custom_page/', views.custom_redirect, name='custom_page'),
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
    path('subject_list/', views.SubjectListView.as_view(), name='subject_list'),
    path('subject_detail/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('subject_create/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subject_update/<int:pk>', views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),
    path('subject_success/', views.subject_success_view, name='subject_success'),
    path('contact_detail/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contact_create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contact_update/<int:pk>', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
    path('contact_success/', views.contact_success_view, name='contact_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
