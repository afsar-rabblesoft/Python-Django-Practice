from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    today = datetime.datetime.now().date()
    return render(request, "index.html", {"today": today})


def viewArticle(request, page):

    return render(request, "article.html", {"page": page})


def viewArticle2(request, page, id):
    return render(request, "articleN.html", {"page": page, "id": id})
