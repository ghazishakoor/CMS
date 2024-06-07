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
    path('student_subject_marks/', views.StudentSubjectMarks, name='student_subject_marks'),
    
    path('exam_marks/', views.exam_marks_view, name='exam_marks'),
    path("exam_search/", views.ExamSearchResultsView.as_view(), name="exam_search"),
    
    path("search/", views.SearchResultsView.as_view(), name="search"),
    
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
    path('contact_create/<int:pk>/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contact_update/<int:pk>', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
    path('contact_success/', views.contact_success_view, name='contact_success'),
    
    path('exam_list/', views.ExamListView.as_view(), name='exam_list'),
    path('exam_detail/<int:pk>/', views.ExamDetailView.as_view(), name='exam_detail'),
    path('exam_create/', views.ExamCreateView.as_view(), name='exam_create'),
    path('exam_update/<int:pk>', views.ExamUpdateView.as_view(), name='exam_update'),
    path('exam/<int:pk>/delete/', views.ExamDeleteView.as_view(), name='exam_delete'),
    path('exam_success/', views.exam_success_view, name='exam_success'),
    
    path('test_list/', views.TestListView.as_view(), name='test_list'),
    path('test_detail/<int:pk>/', views.TestDetailView.as_view(), name='test_detail'),
    path('test_create/', views.TestCreateView.as_view(), name='test_create'),
    path('test_update/<int:pk>', views.TestUpdateView.as_view(), name='test_update'),
    path('test/<int:pk>/delete/', views.TestDeleteView.as_view(), name='test_delete'),
    path('test_success/', views.test_success_view, name='test_success'),
    
    path('assignment_list/', views.AssignmentListView.as_view(), name='assignment_list'),
    path('assignment_detail/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment_detail'),
    path('assignment_create/', views.AssignmentCreateView.as_view(), name='assignment_create'),
    path('assignment_update/<int:pk>', views.AssignmentUpdateView.as_view(), name='assignment_update'),
    path('assignment/<int:pk>/delete/', views.AssignmentDeleteView.as_view(), name='assignment_delete'),
    path('assignment_success/', views.assignment_success_view, name='assignment_success'),
    
    path('term_list/', views.TermListView.as_view(), name='term_list'),
    path('term_detail/<int:pk>/', views.TermDetailView.as_view(), name='term_detail'),
    path('term_create/', views.TermCreateView.as_view(), name='term_create'),
    path('term_update/<int:pk>', views.TermUpdateView.as_view(), name='term_update'),
    path('term/<int:pk>/delete/', views.TermDeleteView.as_view(), name='term_delete'),
    path('term_success/', views.term_success_view, name='term_success'),
    
    path('courseclass_list/', views.CourseClassListView.as_view(), name='courseclass_list'),
    path('courseclass_detail/<int:pk>/', views.CourseClassDetailView.as_view(), name='courseclass_detail'),
    path('courseclass_create/', views.CourseClassCreateView.as_view(), name='courseclass_create'),
    path('courseclass_update/<int:pk>', views.CourseClassUpdateView.as_view(), name='courseclass_update'),
    path('courseclass/<int:pk>/delete/', views.CourseClassDeleteView.as_view(), name='courseclass_delete'),
    path('courseclass_success/', views.courseclass_success_view, name='courseclass_success'),
    
    path('teacher_courseclass_list/', views.TeacherCourseClassListView.as_view(),
         name='teacher_courseclass_list'),
    
    path('location_list/', views.LocationListView.as_view(), name='location_list'),
    path('location_detail/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('location_create/', views.LocationCreateView.as_view(), name='location_create'),
    path('location_update/<int:pk>', views.LocationUpdateView.as_view(), name='location_update'),
    path('location/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),
    path('location_success/', views.location_success_view, name='location_success'),
    
    path('exammark_list/', views.ExamMarkListView.as_view(), name='exammark_list'),
    path('exammark_detail/<int:pk>/', views.ExamMarkDetailView.as_view(), name='exammark_detail'),
    path('exammark_create/', views.ExamMarkCreateView.as_view(), name='exammark_create'),
    path('exammark_update/<int:pk>', views.ExamMarkUpdateView.as_view(), name='exammark_update'),
    path('exammark/<int:pk>/delete/', views.ExamMarkDeleteView.as_view(), name='exammark_delete'),
    path('exammark_success/', views.exammark_success_view, name='exammark_success'),
    
    path('teacher_exammark/<int:pk>/delete/', views.TeacherExamMarkDeleteView.as_view(), name='teacher_exammark_delete'),
    path('teacher_exammark_list/', views.TeacherExamMarkListView.as_view(), name='teacher_exammark_list'),
    
    path('fetch_students/', views.fetch_students, name='fetch_students'),
    
    path('exam_result/', views.exam_results, name='exam_result'),
    
    path('class_result/', views.class_results, name='class_result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
