from django.shortcuts import render
from django.http import HttpResponse
from rus_urban import settings

# import models
from words.models import Word

from django.contrib.auth.models import User
import os
import re
import datetime

# make_tables(db_name) # uncomment if you want to drop and create new tables

def add_records_to_db():
    with open('.\\InteractiveDictionaryWords.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word, _, definition = line.partition(':')
            word = word.strip('\s\'\"')
            definition = definition.strip()
            definition = definition.strip('"\'')
            # add new word
            Word.objects.create(word=word, definition=definition, examples='',
                                updater='eg', city='Moscow', date=datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))

def add_records_to_db_second():
    with open('.\\Definitions.txt', 'r', encoding='utf-8') as f:
        words = re.split('[0-9]{1,2}\.', f.read())[1:]
        for word in words:
            word, _, definition = word.partition('-')
            if '\n' in definition.strip():
                definition = definition.partition('\n')
            else:
                definition = definition.partition('.')
            Word.objects.create(word=re.sub(r'\(.*\)', '', word.strip()).lower().strip(), definition=definition[0].strip(), examples=definition[-1].strip(),
                                            updater='eg', city='Moscow', date=datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))

# Create your views here.
def home_view(request, *args, **kwargs):
    # до 5 последних слов из базы
    
    # add_records_to_db() # comment it after adding new records
    # add_records_to_db_second() # comment it after adding new records

    n = 5
    if Word.objects.all():
        latest_id = Word.objects.latest('id').id

        latest_words = Word.objects.all().order_by('-id')[:n]
        context = {
            'contdict': latest_words
        }
    else:
        context = {}
    return render(request, 'home.html', context)

def contacts(request, *args, **kwargs):
	contacts_context = {
        "about_title" : "Contacts",
	}
	return render(request, 'contacts.html', contacts_context)
    
def add_word_view(request, *args, **kwargs):
    form = NewWord(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }

    # db.execute('''INSERT INTO word_info (word, definition, updater)
    #               VALUES ("сычиу", "люди, которые <...>фыв", "e12g")''')

    return render(request, 'add.html', context)

def output(request, *args, **kwargs):
    word = request.GET['word'].lower().strip()
    context = list(Word.objects.filter(word=word))
    context = {
        'dict': context,
        'word': word
    }
    return render(request, 'output.html', context)

def about_view(request, *args, **kwargs):
	about_context = {}
	return render(request, 'about.html', about_context)

def login_view(request, *args, **kwargs):
	login_context = {}
	return render(request, 'login.html', login_context)
