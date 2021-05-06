from django.db import models


class BadWordQuerySet(models.query.QuerySet):
    def is_forbidden(self, text: str):
        return self.filter(bad_word__in=text.split(' ')).exists()


class BadWordManager(models.Manager):
    def get_queryset(self):
        return BadWordQuerySet(self.model, using=self._db)

    def is_forbidden(self, text: str):
        return self.get_queryset().is_forbidden(text)


class BadWord(models.Model):
    bad_word = models.CharField(max_length=255, null=False, unique=True)

    objects = BadWordManager()

    def __str__(self):
        return self.bad_word
