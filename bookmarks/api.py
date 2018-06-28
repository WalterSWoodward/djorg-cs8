from rest_framework import serializers, viewsets
from .models import Bookmark

class BookmarkSerializer(serializers.HyperlinkedModelSerializer): # HW - figure this out
  # 12:48 Definition: REVIEW
  class Meta:
    model = Bookmark
    fields = ('title', 'description', 'url')

class BookmarkViewset(viewsets.ModelViewSet):
  serializer_class = BookmarkSerializer
  queryset = Bookmark.objects.all()