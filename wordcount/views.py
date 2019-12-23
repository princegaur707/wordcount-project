from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext1 =request.GET['fulltext']
    wordlist=fulltext1.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #increase counter
            worddictionary[word]+=1
        else: 
            # add to dict
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext1,'count':len(wordlist),"sortedwords":sortedwords})
def about(request):
    return render(request,'about.html')