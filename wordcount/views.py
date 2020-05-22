from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return HttpResponse('home')
def homepage(request):
    return render(request, 'home.html')
def count(request):
    fulltext= request.GET['fulltext']
    # print(len(fulltext))
    wordlist= fulltext.split()
    word_dic= {}
    # x=len(fulltext)
    for word in wordlist:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1
    # sortedwords={}
    sortedwords=sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'word_dic': word_dic})
# def eggs(request):
#     return HttpResponse('eggs are great')
def intro(request):
    return render(request,'intro.html')