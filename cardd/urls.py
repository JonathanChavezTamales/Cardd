"""cardd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cards.views import all_cards_view, new_card_view
from user.views import my_user_view, signup_view, user_view
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('home', all_cards_view),
    path('', all_cards_view),

    #User
    path('me', my_user_view),
    path('user/<int:uid>', user_view),
    path('signup', signup_view),

    #Cards
    path('new_card', new_card_view),

    #social
    path('login', auth_views.login),
    path('logout', auth_views.logout),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
