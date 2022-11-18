from django.shortcuts import render
from django.http import Http404
from django.views.generic import (
    View,
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)


from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        main = Restaurant.objects.all().order_by('id')[:4]
        store = Store.objects.all()
        store_menu = Store_menu.objects.all()
        star = []
        for i in main.values():
            try:
                num = int(i['res_stars'])
                point = float(i['res_stars']) - num
                ls = [1 for _ in range(num)]
                if (point >= 0.25) and (point < 0.99):
                    ls.append(2)
                elif point < 0.25:
                    ls.append(0)
                if len(ls) != 5:
                    for _ in range(5-len(ls)):
                        ls.append(0)
                star.append({'name': i['id'], 'star': ls})
            except:
                star.append({'name': i['id'], 'star': [0, 0, 0, 0, 0]})


        context = {'main': main, 'star': star,'store':store,'store_menu':store_menu}
        return render(request, 'place/index.html', context)

class PlaceDetailView(View):
    def get(self, request, restaurant_id, *args, **kwargs):
        try:
            place = Restaurant.objects.get(id=restaurant_id)
            menu = Menu.objects.get(id=restaurant_id)

        except Restaurant.DoesNotExist:
            raise Http404('장소가 존재하지 않아요')

        return render(request, 'place/place_detail.html', context={'place':place, 'menu':menu})
    # def get(self, request, *args, **kwargs):
    #     menu = Menu.object.get(id=restaurant_id)

    # def book_detail_view(request, primary_key):
    # try:
    #     book = Book.objects.get(pk=primary_key)
    # except Book.DoesNotExist:
    #     raise Http404('Book does not exist')

    # return render(request, 'catalog/book_detail.html', context={'book': book})