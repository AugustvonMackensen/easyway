from django.http import HttpResponse
from django.shortcuts import render
from .models import NaverTitle, NaverComment
import time


# Create your views here.
def naver_title(request):
    # result_comment_22Jul29.png
    filename = time.strftime("../../static/naver_crawling/main/title_pngfile/result_title_%y%b%d.png")
    form = {'filename': filename}
    content = {'form': form}
    return render(request, 'naver_crawling/naver_title.html',content)



def naver_comment(request):
    filename = time.strftime("../../static/naver_crawling/main/comment_pngfile/result_comment_%y%b%d.png")
    form = {'filename': filename}
    content = {'form': form}
    return render(request, 'naver_crawling/naver_comment.html', content)



def naver_crawling(request):
    navertitles = NaverTitle.objects.all()
    context = {'navertitles':navertitles}
    return render(request, 'naver_crawling/naver_crawling.html', context)


# create_date='날짜', name='언론사', title='제목'
# ['name']['link']['title']