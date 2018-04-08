from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shortener.models import bitlyURL
from .serializers import URLSerializer


@api_view(['GET', 'POST'])
def URLListView(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = bitlyURL.objects.all()
        serializer = URLSerializer(snippets, many=True)
        # JsonResponse-An HttpResponse subclass that helps to create a JSON-encoded response.
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def URLDetails(request, shortcode, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = bitlyURL.objects.get(shortcode=shortcode)
    except bitlyURL.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = URLSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = URLSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)