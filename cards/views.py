from django.shortcuts import render
from .models import Card
from .forms import CardForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

# Create your views here.

def all_cards_view(request):

    ctx = {}

    if request.user.is_authenticated:
        detailed_user = UserSocialAuth.objects.get(id = request.user.id)

        ctx['detailed'] = detailed_user

    cards = Card.objects.filter(isPublic=True).order_by('-id')[:10]

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
    ctx['cards'] = cards

    return render(request, "cards/home.html", ctx)



def new_card_view(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = CardForm(request.POST)

            if form.is_valid:
                card = form.save(commit=False)
                card.user = User.objects.get(id = request.user.id)
                card.save()
                return HttpResponseRedirect("home")


        else:
            form = CardForm()

        return render(request, 'cards/new_card.html', {'form':form})

    else:
        return HttpResponseRedirect('/signup')
