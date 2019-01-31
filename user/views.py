from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from cards.models import Card
from cards.forms import CardForm

# Create your views here.

def my_user_view(request):

        if request.user.is_authenticated:


            user = User.objects.get(id = request.user.id)
            duser = UserSocialAuth.objects.get(id = request.user.id)

            cards = Card.objects.filter(user=user).order_by('-date')

            ctx = {
                'user':user,
                'cards':cards,
                'duser':duser,
                'detailed':duser
            }



            if request.method == 'POST':
                form = CardForm(request.POST)

                if form.is_valid:
                    card = form.save(commit=False)
                    card.user = User.objects.get(id = request.user.id)
                    card.save()
                    return HttpResponseRedirect("home")


            else:
                form = CardForm()

            ctx['form'] = form

            return render(request,"user/user.html", ctx)


        else:
            return HttpResponseRedirect('signup')



def user_view(request, uid):

        ctx = {}

        if request.user.is_authenticated:
            duser = UserSocialAuth.objects.get(id = request.user.id)

            ctx['duser'] = duser

        user = User.objects.get(id=uid)
        detailed_user = UserSocialAuth.objects.get(id=uid)

        if not user:
            return render(request,"errors/404.html",{})

        else:

            cards = Card.objects.filter(user=user).order_by('-date')
            ctx['detailed'] = detailed_user
            ctx['user'] = user
            ctx['cards'] = cards


            return render(request,"user/user.html", ctx)



def signup_view(request):

    return render(request, "user/signup.html", {})


def search_results(request):

    try:

        query = request.GET.get('q')

        ctx = {'query':query}

        detailed = UserSocialAuth.objects.get(id = query)

        user = User.objects.get(id=query)

        ctx['detailed'] = detailed
        ctx['user'] = user

        if request.user.is_authenticated:
            duser = UserSocialAuth.objects.get(id = request.user.id)

            ctx['duser'] = duser

        return render(request, "user/search_results.html", ctx)

    except:
        return render(request, "errors/404.html", {})
