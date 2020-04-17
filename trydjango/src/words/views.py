from django.shortcuts import render
from .models import Word
from .forms import NewWord
from django.http import HttpResponse


def add_word_view(request, *args, **kwargs):
    form = NewWord(request.POST or None)
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'Anonymous'
    #form.updater = username
    if form.is_valid():
        newform = Word()
        newform.word = form.cleaned_data['word']
        newform.definition = form.cleaned_data['definition']
        newform.examples = form.cleaned_data['examples']
        newform.updater = username
        newform.city = form.cleaned_data['city']
        newform.date = form.cleaned_data['date']
        newform.save()
    context = {
    'form' : form,
    'username' : username
    }
    return render(request, 'add.html', context)


def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['word']
    likes = 0
    if cat_id:
        cat = Word.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)


def dislike_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['word']
    dislikes = 0
    if cat_id:
        cat = Word.objects.get(id=int(cat_id))
        if cat:
            dislikes = cat.dislikes + 1
            cat.dislikes = dislikes
            cat.save()
    return HttpResponse(dislikes)
