from rest_framework import serializers

from vacancies.models import Vacancy

# class VacancySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     text = serializers.CharField(max_length=2000)
#     slug = serializers.CharField(max_length=50)
#     status = serializers.CharField(max_length=6)
#     created = serializers.DateField()
#     username = serializers.CharField(max_length=100)

class VacancySerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = Vacancy
        fields = ["id", "text", "slug", "status", "created", "username"]

class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

