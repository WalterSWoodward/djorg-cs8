from rest_framework import serializers, viewsets
from .models import Note, PersonalNote

# convention is to call the serializer after what it is serializing
# TODO CRITICAL: Disable this/Modify to only work for admin
class NoteSerializer(serializers.HyperlinkedModelSerializer): # HW - figure this out
  # 12:48 Definition: REVIEW
  class Meta:
    model = Note
    fields = ('title', 'content')

class NoteViewset(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PersonalNote
    fields = ('title', 'content')

  def create(self, validated_data):
    # import pdb; pdb.set_trace() # convention to do import and call in one line
    user = self.context['request'].user
    # ** denotes a list of key arguments
    personal_note = PersonalNote.objects.create(user=user, **validated_data) # From docs -- create is supposed to return validated data
    return personal_note

class PersonalNoteViewset(viewsets.ModelViewSet):
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.none() # In itializes an empty list of the querySet type

  def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
      return PersonalNote.objects.none()

    else:
      return PersonalNote.objects.filter(user=user)