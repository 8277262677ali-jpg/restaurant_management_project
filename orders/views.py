from django.shortcuts import render
from rest_framework.generics import listapiview
from.models import menucategoryserializer
class menucategorylistview(listapiview):
    queryset=menucategory.object.all()
    serializer_class=menucategoryserializer

# Create your views here.
