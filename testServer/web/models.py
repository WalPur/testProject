from django.db import models

from accounts.models import CustomUser


class TournamentStatuses(models.TextChoices):
    """Этапы турнира."""

    CREATED = 'CREATED'
    ACCEPTED = 'ACCEPTED'
    FINISHED = 'FINISHED'
    CANCELLED = 'CANCELLED'


class TypeChoices(models.TextChoices):
    """Типы турниров"""

    LOCAL = "LOCAL"
    REGION = "REGION"
    RUSSIA = "RUSSIA"
    WORLD = "WORLD"
    ONLINE = "ONLINE"


class FormatChoices(models.TextChoices):
    """Форматы турниров"""

    PAIR = "PAIR"
    TEAM = "TEAM"
    INDIVIDDUAL = "INDIVIDDUAL"


class Tournament(models.Model):
    """Модель турнира."""

    name = models.CharField(max_length=128)
    status = models.CharField(
        choices=TournamentStatuses.choices,
        max_length=128,
        default=TournamentStatuses.CREATED,
    )
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()
    type = models.CharField(
        choices=TypeChoices.choices,
        max_length=128,
        default=TypeChoices.LOCAL,
    )
    format = models.CharField(
        choices=FormatChoices.choices,
        max_length=128,
        default=FormatChoices.PAIR,
    )
    editors = models.ManyToManyField(
        CustomUser,
        'tournaments',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
