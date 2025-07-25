import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scdtestproj.settings")
import django
django.setup()

from jobs.models import Job

print("Latest active jobs:")
jobs = Job.objects.filter_latest(status="active")
for job in jobs:
    print(job.id, job.version, job.status)