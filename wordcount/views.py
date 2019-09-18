from django.http import HttpResponse
from django.shortcuts import render
import operator
def about(request):
    return render(request,'about.html')
def Home(request):
    return render(request,'home.html')
def count(request):
    data=request.GET['full_textarea']#Fetch Data From Home.html
    word_list=list(data.split())
    length=len(word_list)
    worddict={ }
    for word in word_list:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sortedlist=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'id':data,'length':length,'worddict':sortedlist})
     