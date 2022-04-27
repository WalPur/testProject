from django.db import models

from accounts.models import CustomUser


class TournamentStatuses(models.TextChoices):
    """Этапы турнира."""

    CREATED = 'CREATED'
    ACCEPTED = 'ACCEPTED'
    FINISHED = 'FINISHED'
    CANCELLED = 'CANCELLED'

class Tournament(models.Model):
    """Модель турнира."""

    name = models.CharField(max_length=128)
    status = models.CharField(
        choices=TournamentStatuses.choices,
        max_length=128,
        default=TournamentStatuses.CREATED
    )
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()
    TYPE_CHOICES = [
        ('LOCAL', 'Local'),
        ('REGION', 'Region'),
        ('RUSSIA', 'Russia'),
        ('WORLD', 'World'),
        ('ONLINE', 'Online')
    ]
    type = models.CharField(choices=TYPE_CHOICES, max_length=128)
    FORMAT_CHOICES = [
        ('PAIR', 'Pair'),
        ('TEAM', 'Team'),
        ('INDIVIDDUAL', 'Individual')
    ]
    format = models.CharField(choices=FORMAT_CHOICES, max_length=128)
    is_cancelled = models.BooleanField(default=False)
    editors = models.ManyToManyField(
        CustomUser,
        'tournaments',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
