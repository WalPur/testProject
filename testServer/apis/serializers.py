from rest_framework import serializers

from web.models import Tournament
from accounts.models import CustomUser


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = (
            "id",
            "name",
            "status",
            "start_date",
            "finish_date",
            "description",
            "type",
            "format",
        )


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "is_mod", "is_superuser")
