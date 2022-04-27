from rest_framework import serializers

from web.models import Tournament

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ("id", "name", "status", "start_date", "finish_date", "description", "type", "format")