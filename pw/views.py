from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Contact
from .forms import CommentForm, ContactForm

# Create your views here.
def index_page_view(request):
    games = ['League of Legends', 'World of Warcraft', 'Dota2', 'CS-GO', 'Pokémon', 'Overwatch', 'etc...']

    context = {
        list: games
    }
    return render(request, 'pw/index.html', context)

def about_page_view(request):
    return render(request, 'pw/about.html')

def lol_page_view(request):
    return render(request, 'pw/League_of_Legends.html')

def wow_page_view(request):
    return render(request, 'pw/World_of_Warcraft.html')

def contact_page_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('proj2:contact'))

    context = {'form': form}
    return render(request, 'pw/contact.html', context)

def Comment_page_view(request):
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('proj2:comments'))

    context = {'form': form}
    return render(request, 'pw/Comment.html', context)

def quizz_page_view(request):
    return render(request, 'pw/quizz.html')

def start_page_view(request):
    return render(request, 'pw/start.html')