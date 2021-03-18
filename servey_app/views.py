from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")


def process_form(request):
    request.session['name']= request.POST['name']
    request.session['dojo_loc_form'] = request.POST['dojoLoc']
    request.session['favLang_from_form'] = request.POST['favLang']
    request.session['gender_from_form'] = request.POST['gender']
    request.session['comment_from_form'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, "result.html")