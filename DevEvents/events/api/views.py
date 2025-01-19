from rest_framework  import viewsets
from django.shortcuts import get_object_or_404, get_list_or_404

from events.models import Event

from events.api.serializers import EventSerializer, CommentSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Event, id=self.kwargs.get('event_pk'))
        return get_list_or_404(post.comments.all())
