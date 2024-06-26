from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps
from django.utils.decorators import method_decorator


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=None):
    if allowed_roles == None:
        allowed_roles = []
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
                
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    @wraps(view_func)
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'student' or group == 'teacher':
            return redirect('custom_page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_function
            

def teacher_only(view_func):
    @wraps(view_func)
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student' or group == 'admin':
            return redirect('custom_page')
        if group == 'teacher':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def student_only(view_func):
    @wraps(view_func)
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin' or group == 'teacher':
            return redirect('custom_page')
        if group == 'student':
            return view_func(request, *args, **kwargs)

    return wrapper_function
