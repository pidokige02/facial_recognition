from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from core.views import LandingPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),  // comment until frontend is connected

    path('api/', include('core.urls', namespace='api'))
]
