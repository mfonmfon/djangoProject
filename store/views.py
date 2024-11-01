from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product, Collection
from store.serializer import ProductSerializer, CollectionSerializer


# Create your views here.

#localhost:8080/store/products
#localhost:8080/store/products/1

@api_view()
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True , context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.isvalid(request_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def collection_display(request):
    collection = Collection.objects.all()
    serializer = CollectionSerializer(collection)
    return Response(serializer.data, status=status.HTTP_200_OK)
