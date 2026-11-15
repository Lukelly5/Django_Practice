from django.shortcuts import render, redirect
from .models import Topic
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'MainApp/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.all().order_by('date_added')

    context = {'topics': topics} # we need to pass topic objects to our template. the key of this dictonay is the variable name you use in the template
    
    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id) # get the topic object with the id of topic_id
    entries = Entry.objects.filter(topic=topic).order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'MainApp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid(): # is_valid makes sure user fills out all required fields of the form
            new_topic = form.save() # save the new topic to the database
            return redirect('MainApp:topics') # redirect to the topics page after saving the new topic

    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic # get the topic of the entry we got from the URL

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)
        
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'MainApp/edit_entry.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id) 

    if request.method != 'POST':
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        
        if form.is_valid(): # is_valid makes sure user fills out all required fields of the form
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic.id)

    context = {'form': form, 'topic': topic}
    return render(request, 'MainApp/new_entry.html', context)