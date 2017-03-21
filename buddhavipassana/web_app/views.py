from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'baseIntro.html')

def intro_web(request):
    return render(request, 'web_app/buddhavipassana_intro.html')

def ajahn(request):
    return render(request, 'web_app/AjahnTong.html')


def rolunk(request):
    return render(request, 'web_app/rolunk.html')


def oktatok(request):
    return render(request, 'web_app/oktatok.html')

def tanfolyamok(request):
    return render(request, 'web_app/tanfolyamok.html')


def technikarol(request):
    return render(request, 'web_app/technikarol.html')

def gyik(request):
    return render(request, 'web_app/gyik.html')


def kapcsolat(request):
    return render(request, 'web_app/kapcsolat.html')


def indexEng(request):
    return render(request, 'web_app/indexEng.html')

def ajahnEng(request):
    return render(request, 'web_app/ajahnEng.html')


def about(request):
    return render(request, 'web_app/about.html')


def teachers(request):
    return render(request, 'web_app/teachers.html')


def courses(request):
    return render(request, 'web_app/courses.html')


def technique(request):
    return render(request, 'web_app/technique.html')


def faq(request):
    return render(request, 'web_app/faq.html')


def contact(request):
    return render(request, 'web_app/contact.html')
