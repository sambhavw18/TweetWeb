from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Tweet
from .forms import TweetForm,UserRegister

# Create your views here.
def home(request):
    tweet=Tweet.objects.all()
    print(tweet)
    return render(request,"home.html",{'tweets':tweet})

def mytweet(request):
    tweet=Tweet.objects.filter(user=request.user.id).all()
    # print(request.user.id)
    # print(tweet)
    return render(request,"mytweet.html",{'tweets':tweet})

def search(request):
    result=[]
    data=[]
    if(request.method=="POST"):
        srch=request.POST['searchbar']
        tweet=Tweet.objects.values()
        ntweet=Tweet.objects.all()
        # print(srch)
        # print(tweet)
        for i in tweet:
            # print(i['text'])
            if srch in i['text']:
                result.append(i['text'])
                print(result)
                # print(i['text'])

        data=Tweet.objects.filter(text=result[0]).all()
        print(data)

    return render(request,'search.html',{'value':srch,"tweet":tweet,"data":data,"ntweet":ntweet,"result":result})

@login_required
def create(request):
    if (request.method == "POST"):
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect("home")
    else:  
        form=TweetForm()
    return render(request,"newtweet.html",{'form':form})

@login_required
def edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tw=form.save(commit=False)
            tw.user=request.user
            tw.save()
            return redirect("home")
    else:
        form=TweetForm(instance=tweet)
    return render(request,"edit.html",{'form':form})

@login_required
def delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect("home")
    return render(request,"delete.html",{'tweet':tweet})

def register(request):
    if request.method=="POST":
        value=UserRegister(request.POST)
        if value.is_valid():
            user=value.save()
            login(request,user)
            return redirect("home")
    else:
        value=UserRegister()
    return render(request,"registration/register.html",{'value':value})
