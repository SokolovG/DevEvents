from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .constants import DESCRIPTION_MAX_LENGTH, LOCATION_MAX_LENGTH, MAX_LENGTH



class CreatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Location(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=LOCATION_MAX_LENGTH, blank=True)
    city = models.CharField(max_length=MAX_LENGTH)
    country = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.name

class Category(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, unique=True)
    description = models.TextField(blank=True, max_length=DESCRIPTION_MAX_LENGTH)

    def __str__(self):
        return self.name


class Event(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.ForeignKey('users.Organizer', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    location = models.ForeignKey(
        Location,
        related_name='places',
        on_delete=models.CASCADE
    )
    is_published = models.BooleanField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    is_online = models.BooleanField()
    meeting_link = models.URLField()
    is_verify = models.BooleanField()
    max_participants = models.PositiveIntegerField(blank=True)
    registration_deadline = models.DateTimeField(blank=True)
    format = models.CharField(max_length=MAX_LENGTH)
    members = models.PositiveIntegerField(blank=True)
    photos = models.ImageField()
    you_are_member = models.BooleanField()

    class Meta:
        ordering = ['event_start_date']

    def __str__(self):
        return self.name

    def clean(self):
        if self.event_start_date < self.event_end_date:
            raise ValidationError('The end date cannot be earlier than the start date.')

        if self.registration_deadline and self.registration_deadline > self.event_start_date:
            raise ValidationError('The deadline for registration should be before the event starts.')

        if self.is_online and not self.meeting_link:
            raise ValidationError('For the online event, a link is required.')

        if not self.is_online and not self.location:
            raise ValidationError('For an offline event, the venue must be specified.')


class EventRegistration(CreatedDateModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=MAX_LENGTH)
    
    class Meta:
        unique_together = ['event', 'user']


class Comment(CreatedDateModel):
    text = models.TextField(max_length=MAX_LENGTH)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

