from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path("register", views.register,name="register"),
    path("login", views.login ,name="login"),
    path("logout", views.logout ,name="logout"),
    # path("update-user/<int:id>/",views.update_user,name="update-user"),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
]
