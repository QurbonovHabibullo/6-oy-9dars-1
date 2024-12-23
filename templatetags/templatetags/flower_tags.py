from django import template
from flowers.models import Category

register = template.Library()

@register.inclusion_tag('flowers/category_list.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
