from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    t = loader.get_template('src/index.html')
    return HttpResponse(t.render(request), content_type='application/xhtml+xml')
