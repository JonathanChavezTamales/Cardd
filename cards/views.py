from django.shortcuts import render
from .models import Card
from .forms import CardForm
from django.http import HttpResponseRedirect
# Create your views here.

def all_cards_view(request):

    cards = Card.objects.filter(isPublic=True).order_by('-id')[:10]


    return render(request, "cards/home.html", {'cards':cards})



def new_card_view(request):

    if request.method == 'POST':
        form = CardForm(request.POST)

        if form.is_valid:
            card = form.save(commit=False)
            card.save()
            return HttpResponseRedirect("home")


    else:
        form = CardForm()

    return render(request, 'cards/new_card.html', {'form':form})
