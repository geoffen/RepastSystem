from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from Books.models import *


class BookListView(ListView):
    model = Book
    queryset = Book.objects.filter(title__icontains='django')
    template_name = 'booklist.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context
