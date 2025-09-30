import sqlite3 as sql
from store_app.models import Category


def category_data(request):
    categories = Category.objects.all()
    return {'categories': categories}
