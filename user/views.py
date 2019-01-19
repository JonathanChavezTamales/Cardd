from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from cards.models import Card
from .forms import CreateUserForm
# Create your views here.

def my_user_view(request):

        if request.user.is_authenticated:


            user = User.objects.get(id = request.user.id)
            detailed_user = UserSocialAuth.objects.get(id = request.user.id)
            cards = Card.objects.filter(user=user)

            ctx = {
                'user':user,
                'cards':cards,
                'detailed':detailed_user
            }

            print(dir(detailed_user))
            return render(request,"user/user.html", ctx)


        else:
            return HttpResponseRedirect('signup')



def user_view(request, uid):


        user = User.objects.filter(id = uid)
        cards = Card.objects.filter(user__in=user)

        ctx = {
            'user':user,
            'cards':cards
        }


        return render(request,"user/user.html", ctx)



def signup_view(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/home')

    else:
        form = CreateUserForm()

    return render(request, "user/signup.html", {'form':form})
