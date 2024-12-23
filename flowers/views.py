from django.shortcuts import render, get_object_or_404,redirect
from .models import Flower, Category
from .forms import FlowerForm

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flower_list.html', {'flowers': flowers})


def flowers_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    flowers = Flower.objects.filter(category=category)
    return render(request, 'flowers_by_category.html', {'category': category, 'flowers': flowers})


def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flower_detail.html', {'flower': flower})

def add_flowers(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flower_list')
    else:
        form = FlowerForm()
    return render(request, 'add_flowers.html', {'form': form})