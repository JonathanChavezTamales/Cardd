from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from cards.models import Card
# Create your views here.

def my_user_view(request):

        if request.user.is_authenticated:


            user = User.objects.get(id = request.user.id)
            detailed_user = UserSocialAuth.objects.get(id = request.user.id)
            cards = Card.objects.filter(user=user).order_by('-date')

            ctx = {
                'user':user,
                'cards':cards,
                'detailed':detailed_user
            }

            return render(request,"user/user.html", ctx)


        else:
            return HttpResponseRedirect('signup')



def user_view(request, uid):

        user = User.objects.filter(id = uid)
        
        cards = Card.objects.filter(user__in=user).order_by('-date')

        ctx = {
            'user':user,
            'cards':cards
        }


        return render(request,"user/user.html", ctx)



def signup_view(request):

    return render(request, "user/signup.html", {})
