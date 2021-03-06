from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from signups.models import AccountCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
from .forms import SignUpForm
from .forms import MakeADonationForm
from .forms import ToDoForm

def home(request):
    
    return render_to_response("home.html",
                              locals(),
                              context_instance=RequestContext(request))

def signup(request):
        
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            
            return HttpResponseRedirect('/thank-you/')
        else:
            return HttpResponseRedirect('<h1>Error creating user!</h1>')
    else:
        form = AccountCreationForm()

        return render(request, 'signup.html', {
            'form': form,
        })
    
#def signup(request):    
#    form = SignUpForm(request.POST or None)
#    
#    if form.is_valid():
#        save_it = form.save(commit=False)
#        save_it.save()
#        messages.success(request, 'Thank You For Donating!')
#        return HttpResponseRedirect('/thank-you/')
#    
#    return render_to_response("signup.html",
#                              locals(),
#                              context_instance=RequestContext(request))

def thankyou(request):
    
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def aboutus(request):
    
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))

def makeadonation(request):
    
    form = MakeADonationForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank You For Donating!')
        return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("makeadonation.html",
                              locals(),
                              context_instance=RequestContext(request))

def recipient(request):
    
    return render_to_response("recipient.html",
                              locals(),
                              context_instance=RequestContext(request))

def todo(request):
    
    form = ToDoForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank You For Donating!')
        return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("todo.html",
                              locals(),
                              context_instance=RequestContext(request))
    