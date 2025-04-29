from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import Blog, Comment

'''def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})'''

def post_list(request):
    """View for the main blog page that shows all posts."""
    blogs = Blog.objects.all().order_by('-created_date')
    comments = Comment.objects.all().order_by('-timestamp')
    return render(request, 'posts/post_list.html', {'blogs': blogs, 'comments': comments})

def admin_login(request):
    """Handle admin login requests."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('post_list')
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions')
            return redirect('post_list')
    
    return redirect('post_list')

@login_required
def admin_logout(request):
    """Handle admin logout requests."""
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def post_comment(request):
    """Handle posting new comments."""
    if request.method == 'POST' and request.user.is_staff:
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                content=content,
                timestamp=timezone.now()
            )
            messages.success(request, 'Comment posted successfully')
        else:
            messages.error(request, 'Comment cannot be empty')
    
    return redirect('post_list')

def check_auth(request):
    """Check if user is authenticated and is staff."""
    is_authenticated = request.user.is_authenticated and request.user.is_staff
    return JsonResponse({'authenticated': is_authenticated})
