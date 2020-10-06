# Create your views here.

from django.views.generic import ListView, DetailView

from eviteapi.models import Event


# home view for Event. Event are displayed in a list
class IndexView(ListView):
    template_name = 'event/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all().order_by('start_time')


class EventSignUp(DetailView):
    model = Event
    template_name = 'event/event-signup.html'
