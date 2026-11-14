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

