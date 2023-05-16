from articles import models
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": models.Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                for i in Article.objects.all():
                    if (i.title == form["title"]):
                        form['errors'] = u'Статья с таким названием уже существует'
                        return render(request, 'create_post.html', {'form': form})
                Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=Article.objects.last().id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 
            'email': request.POST["email"],
            'password': request.POST["password"]
        }
        if form["username"] and form["password"] and request.POST["email"]:
            for i in User.objects.all():
                if (i.username == form["username"]):
                    form['errors'] = u'Пользователь с таким именем уже существует'
                    return render(request, 'registration.html', {'form': form})
            User.objects.create_user(form["username"], form["email"], form["password"])
            return redirect('/')
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html')
    
def loginn(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 
            'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(username = form['username'], password = form['password'])
            if(user == None):
                form['errors'] = u'Неверный логин или пароль'
                return render(request, 'login.html', {'form': form})
            login(request, user)
            return redirect('/')
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html')
    
def logoutt(request):
    logout(request)
    return redirect('/')