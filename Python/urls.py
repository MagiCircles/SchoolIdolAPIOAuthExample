from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.oauthtest),
    url(r'^oauthdone/$', views.oauthdone),
]
