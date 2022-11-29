from django.shortcuts import render
from datetime import date
from .models import Post, Person, Persons

# Create your views here.
def homepage(request):

    # render
    # - request object
    # - template_name -> html name ('homepage.html')
    # - context -> dictionary of data
    
    all_post = Post.objects.all()
    context = {'time': date.today(), 'posts': all_post}
    return render(request, 'homepage.html', context)

def profile(request):
    
    context = {'name': 'Yoss', 'gender': 'M', 'items': ['banana','eggs','tv']}
    
    return render(request, 'user_profile.html', context)


def authors(request):

    all_authors = Person.objects.all()
    context = {'authors': all_authors}

    return render(request, 'authors.html', context)

def author_posts(request, id):

    author = Person.objects.get(id=id)
    author_posts = author.post_set.all()

    context = {'author': author, 'post': author_posts}

    return render(request, 'author_posts.html', context)

def persons(request):

    all_persons = Persons.objects.all()
    context = {'persons': all_persons}

    return render(request, 'persons.html', context)

def persons_phone_number(request):

    numbers = Persons.objects.all()
    context = {'numbers': numbers}

    return render(request, 'number.html', context)