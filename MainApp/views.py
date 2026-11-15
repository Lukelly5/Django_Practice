from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'MainApp/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.all().order_by('date_added')

    context = {'topics': topics} # we need to pass topic objects to our template. the key of this dictonay is the variable name you use in the template
    
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id) # get the topic object with the id of topic_id
    entries = Entry.objects.filter(topic=topic).order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'MainApp/topic.html', context)

    