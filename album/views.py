from django.urls import reverse_lazy 
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Author, Publisher, Book

from rest_framework import viewsets
from album.serializers import AuthorSerializer, PublisherSerializer, BookSerializer

# Create your views here.

class AuthorListView(ListView):
    model = Author

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'album/author_form.html'  # Ajustar la ruta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operacion'] = 'Editar Autor'  # Cambiar este valor según sea necesario
        return context

    def get_success_url(self):
        return reverse_lazy('author-list')

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'album/author_form.html'  # Ajustar la ruta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operacion'] = 'Crear Autor'  # Cambiar este valor según sea necesario
        return context

    def get_success_url(self):
        return reverse_lazy('author-list')

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

class PublisherListView(ListView):
    model = Publisher

class PublisherUpdate(UpdateView):
    model = Publisher
    fields = '__all__' 
    template_name = 'album/publisher_form.html'  # Ajustar la ruta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operacion'] = 'Editar Editorial'  # Cambiar este valor según sea necesario
        return context

    def get_success_url(self):
        return reverse_lazy('publisher-list')

class PublisherCreate(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'album/publisher_form.html'  # Ajustar la ruta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operacion'] = 'Crear Editorial'  # Cambiar este valor según sea necesario
        return context

    def get_success_url(self):
        return reverse_lazy('publisher-list')

class PublisherDelete(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher-list')

class BookListView(ListView):
    model = Book

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__' 
    template_name = 'album/book_form.html'  # Ajustar la ruta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operacion'] = 'Editar Libro'  # Cambiar este valor según sea necesario
        return context

    def get_success_url(self):
        return reverse_lazy('book-list')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'album/book_form.html'  # Ajustar la ruta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operacion'] = 'Crear Libro'  # Cambiar este valor según sea necesario
        return context

    def get_success_url(self):
        return reverse_lazy('book-list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

def dashboard(request):
    return render(request, 'album\dashboard.html')

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer