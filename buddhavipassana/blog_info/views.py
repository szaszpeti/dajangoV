
from django.shortcuts import render, get_object_or_404
from .models import Category, Document


# Create your views here.
def index(request):
    all_category = Category.objects.all()
    return render(request, 'blog_info/blog_index.html', {'all_category':all_category})

def details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    documentId = Category.objects.get(pk=category_id)
    document = documentId.document_set.all()
    return render(request, 'blog_info/blog_details.html', {'category':category, 'document':document})

def read(request, document_id):
    return render(request, 'blog_info/blog_read.html')