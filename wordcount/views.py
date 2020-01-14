from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # http response must be returned
    #return (HttpResponse("Hello there!"))
    return render(request,'home.html', {'textKey' : 'Good!!'})

def count(request):
    fulltext = request.GET['fulltext']
    print('text entered by user = '+fulltext)
    wordlist = fulltext.split()
    worddictionary = None ## Issue here , pls fix it later

    for word in wordlist:
         if word in worddictionary:
             worddictionary[word] += 1
         else:
             worddictionary[word] = 1

    return render(request, 'count.html', {'userinput': fulltext , 'wordcount' : len(words), 'worddictionary' : worddictionary })

def home2(request):
    return (HttpResponse("Good morning, You are great!! <br> click <a href onClick=#> here </a>"))
