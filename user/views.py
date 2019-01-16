from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from cards.models import Card
from .forms import CreateUserForm
# Create your views here.

def user_view(request):


        user = User.objects.get(id=request.GET['id'])
        cards = Card.objects.filter(user=user)

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
