"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include # Make sure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_writer.urls')), # Assuming you have this for your app's views
    # Add other paths as needed
]

# Add this section to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Note: While STATIC_ROOT is often used here, for development serving
    # from STATICFILES_DIRS is more direct. However, the standard pattern
    # uses STATIC_URL and lets Django's staticfiles finders handle it,
    # which should work with your STATICFILES_DIRS setting.
    # If the above doesn't work, ensure STATICFILES_DIRS is correctly defined.
    # A more explicit alternative for development might be needed in complex cases,
    # but try the standard pattern first.

    # An alternative often seen (might be needed if the above fails with STATICFILES_DIRS):
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) # If only one dir
