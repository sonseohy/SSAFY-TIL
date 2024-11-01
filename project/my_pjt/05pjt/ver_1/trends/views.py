from django.shortcuts import render, redirect
from .models import Keyword, Trend

from bs4 import BeautifulSoup
from selenium import webdriver

import re

import matplotlib.pyplot as plt
import io
import base64

def get_google_data(keyword, period='all'):
    url = f"https://www.google.com/search?q={keyword}"

    if period == 'year':
        url += "&tbs=qdr:y"

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    # div 태그 중 id 가 result-stats 인 요소 검색
    result_stats = soup.select_one("div#result-stats")
    driver.quit()

    return result_stats.text

def keyword(request):
    if request.method == 'POST':
        name = request.POST.get('query')
        keywords = Keyword(name=name)
        keywords.save()
    
    context = {
        'keywords': Keyword.objects.all(),
    }
    return render(request, 'trends/keyword.html', context)

def keyword_detail(request, pk):
    kw = Keyword.objects.get(pk=pk)
    kw.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()

    for kw in keywords:
        titles = get_google_data(kw.name, period='all')
        match = re.search(r'([\d,]+)', titles)
        # print(match.group(1))
        search = int(match.group(1).replace(',', ''))

    for title in titles:
        trend, created_trend = Trend.objects.get_or_create(
            name=kw.name,
            search_period="all",
            defaults={'result': search},
            )
        
    context = {
        'trends': Trend.objects.all(),
    }

    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    trends = Trend.objects.all()

    keywords = [trend.name for trend in trends]
    values = [trend.result for trend in trends]

    plt.figure(figsize=(10, 6))
    plt.bar(keywords, values)

    plt.title("Technology Trend Analysis")
    plt.ylabel("Result")
    plt.xlabel("Keyword")
    plt.grid(True)
    plt.legend(["Trends"], loc="best")
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    image_png = buf.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')

    context = {
        'graph': graph,
    }

    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()

    for kw in keywords:
        titles = get_google_data(kw.name, period='year')
        
        # 검색 결과 개수 추출
        match = re.search(r'([\d,]+)', titles)
        search = int(match.group(1).replace(',', ''))

    for title in titles:
        trend, created_trend = Trend.objects.get_or_create(
            name=kw.name,
            search_period="year",
            defaults={'result': search},
            )


    # 그래프 생성을 위한 데이터 수집
    trends = Trend.objects.filter(search_period='year')
    names = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    # 막대 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(names, results)
    plt.title("Technology Trend Analysis")
    plt.ylabel("Result")
    plt.xlabel("Keyword")
    plt.grid(True)
    plt.legend(["Trends"], loc="best")
    
    # 그래프 이미지를 메모리에 저장
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    graph = base64.b64encode(image_png).decode('utf-8')

    context = {
        'trends': trends,
        'graph': graph,
    }

    return render(request, 'trends/crawling_advanced.html', context)