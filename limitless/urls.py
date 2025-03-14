"""
URL configuration for limitless project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path

from limitless.api_urls import router
from users.views import ProfileAppView

urlpatterns = [
    path("", ProfileAppView.as_view(), name="index"),
    path("api/", include(router.urls), name="api"),
    path("admin/", admin.site.urls),
]

# Media URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Catch-all URL pattern to be able to handle all frontend URLs
urlpatterns += [re_path(r"^.*/$", ProfileAppView.as_view(), name="catch-all")]
