from django.shortcuts import render
from .models import Word
from .forms import NewWord


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