# Create your views here.

from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from event.models import EventUser
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


def eventsubscribe(request):
    try:
        user_id = request.POST['email']
        event_id = request.POST['event_id']
        if user_id == '':
            data = {'message': "Please input email address"}
            return JsonResponse(data)

        event_user = EventUser.objects.filter(user_id=user_id, event_id=event_id)
        if len(event_user) > 0:
            data = {'message': "Event already subscribed"}
            return JsonResponse(data)

        event_user = EventUser(user_id=user_id, event_id=Event.objects.get(id=event_id))
        event_user.save()
        if event_user is not None:
            data = {'message': "Event successfully subscribed."}
            return JsonResponse(data)
    except Exception as e:
        data = {'message': "Something wrong." + str(e)}
        return JsonResponse(data)


def eventunsubscribe(request):
    try:
        user_id = request.POST['email']
        event_id = request.POST['event_id']
        if user_id == '':
            data = {'message': "Please input email address"}
            return JsonResponse(data)

        event_user = EventUser.objects.filter(user_id=user_id, event_id=event_id)
        if len(event_user) == 0:
            data = {'message': "Event not subscribed yet"}
            return JsonResponse(data)

        event_user.delete()
        if len(event_user) == 0:
            data = {'message': "Event successfully Unsubscribed."}
            return JsonResponse(data)
    except Exception as e:
        data = {'message': "Something wrong." + str(e)}
        return JsonResponse(data)
