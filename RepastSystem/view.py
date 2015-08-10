from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
import datetime


# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)


# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('current_time.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_time.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render_to_response('hours_ahead.html', locals())


def hello(request):
    return HttpResponse("Hello world")
