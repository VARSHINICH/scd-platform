from django.db import models
from django.db.models import Max, OuterRef, Subquery

class SCDQuerySet(models.QuerySet):
    def latest_versions(self):
        sub = self.model.objects.values('id').annotate(
            max_version=Max('version')
        ).filter(id=OuterRef('id')).values('max_version')
        return self.filter(version=Subquery(sub))

    def filter_latest(self, **kwargs):
        return self.latest_versions().filter(**kwargs)

class SCDManager(models.Manager):
    def get_queryset(self):
        return SCDQuerySet(self.model, using=self._db)

    def latest_versions(self):
        return self.get_queryset().latest_versions()

    def filter_latest(self, **kwargs):
        return self.get_queryset().filter_latest(**kwargs)