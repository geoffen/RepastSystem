from django.shortcuts import render_to_response
# Create your views here.


def myselfweb(request):
    return render_to_response('myself.html', {'var': 'Hello world!'})

