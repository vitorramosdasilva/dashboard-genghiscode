from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path


urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler50x = 'dashboard.views.error_500'
handler404 = 'dashboard.views.error_404'
# handler403 = 'dashboard.views.error_403'
# handler400 = 'dashboard.views.error_400'


