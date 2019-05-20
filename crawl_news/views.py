from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    if request.method=="POST":
        input_word=request.POST.get('input_word')

        URL="https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
        fullURL = URL+input_word
        data = requests.get(fullURL).text

        soup=BeautifulSoup(data, 'html.parser')

        news_titles = soup.find_all(class_='_sp_each_title')
      

        title_array=[]
        for title in news_titles:
            title_array.append({'url': title.get('href'), 'title': title.get('title')})
        
        return render(request, 'result.html', {'title_array':title_array})
    else :
        return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')