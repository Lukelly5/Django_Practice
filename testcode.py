import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnin_log.settings')

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

for t in topics:
    print(t.id, t.text, t.date_added)