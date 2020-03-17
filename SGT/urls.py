# Django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import re_path
import notifications.urls
from django.urls import reverse_lazy

urlpatterns = [
                  path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
                  path('archivo/', include(('file.urls', 'file'), namespace='archivo')),
                  path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
                  path('prueba',
                       TemplateView.as_view(template_name='prueba.html')
                       ),
                  path('reset/password_reset', PasswordResetView.as_view(
                      template_name='registration/password_reset_form.html',
                      email_template_name="registration/password_reset_email.html"),
                       name='password_reset'),
                  path('reset/password_reset_done',
                       PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
                       name='password_reset_done'),
                  re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$',
                          PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
                          name='password_reset_confirm'),
                  path('reset/done',
                       PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
                       name='password_reset_complete')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
