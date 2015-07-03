from django.shortcuts import render
from databases.models import Property
from databases.sulekha import scrap_sulekha


def index(request):
        results = scrap_sulekha()
