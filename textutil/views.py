#i have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # a={'name':'tushar'}
    return render(request,'index.html')
    
def analzye(request):

    djtext=request.GET.get('text','default ')
    rs=request.GET.get('rs','default ')
    u=request.GET.get('u','default ')
    l=request.GET.get('l','default ')
    nolauc=request.GET.get('nolauc','default ')

    if rs=="on" or rs=="ON" or rs=="On":
        s=''
        for i in djtext :
            if i=="\n":
                s=s+"\n"
            if i!=' ':
                s=s+i
        a={"what":"remove spaces","original_text":djtext,"afterAnalyzing":s}
        return render(request,'analyse.html',a)

    elif u=="on" or u=="ON" or u=="On":
        s=''
        for i in djtext :
            s=s+i.upper()
        a={"what":"CONVERT TO UPPER CASE","original_text":djtext,"afterAnalyzing":s}
        return render(request,'analyse.html',a)

    elif l=="on" or l=="ON" or l=="On":
        s=''
        for i in djtext :
            s=s+i.lower()
        a={"what":"CONVERT TO LOWER CASE","original_text":djtext,"afterAnalyzing":s}
        return render(request,'analyse.html',a)
        
    elif nolauc=="on" or nolauc=="On" or nolauc=="ON":
        l=0
        u=0
        for i in djtext:
            if i.islower():
                l=l+1
            elif i.isupper():
                u=u+1
        a={"what":"Number Of Lower And Upper Case","original_text":djtext,"afterAnalyzing":"lower,upper","l":l,"u":u}
        return render(request,'analyse.html',a)

