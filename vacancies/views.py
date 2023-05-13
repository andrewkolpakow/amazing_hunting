import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from amazing_hunting import settings
from django.contrib.auth.models import User
from django.db.models import Count, Avg
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from vacancies.models import Vacancy, Skill
from vacancies.serializers import VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer, VacancyUpdateSerializer, VacancyDestroySerializer, SkillSerializer

def hello(request):
    return HttpResponse("Hello World!")

class SkillsViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
class VacancyListView(ListAPIView):
    #model = Vacancy
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer

    def get(self, request, *args, **kwargs):
        vacancy_text = request.GET.get('text', None)
        if vacancy_text:
            self.queryset = self.queryset.filter(
                text__icontains=vacancy_text
            )

        skill_name = request.GET.get("skill", None)
        if skill_name:
            self.queryset.filter(
                skills__name__icontains=skill_name
            )

        return super().get(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     search_text = request.GET.get("text", None)
    #     if search_text:
    #         self.object_list = self.object_list.filter(text=search_text)
    #
    #     self.object_list = self.object_list.select_related("user").prefetch_related("skills").order_by("text")
    #
    #     """
    #     1 - 0:10
    #     2 - 10:20
    #     3 - 20:30
    #     """
        # total = self.object_list.count()
        # page_number = int (request.GET.get("page", 1))
        # offset = (page_number-1) * settings.TOTAL_ON_PAGE
        # if (page_number-1) * settings.TOTAL_ON_PAGE < total:
        #     self.object_list = self.object_list[offset:offset+settings.TOTAL_ON_PAGE]
        # else:
        #     self.object_list = self.object_list[offset:offset+total]

        # paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)

        # vacancies = []
        # for vacancy in page_obj:
        #     vacancies.append({
        #         "id": vacancy.id,
        #         "text": vacancy.text,
        #         "slug": vacancy.slug,
        #         "status": vacancy.status,
        #         "created": vacancy.created,
        #         "username": vacancy.user.username,
        #         "skills": list(map(str, vacancy.skills.all())),
        #     })

        # list(map(lambda x: setattr(x, "username", x.user.username if x.user else None), page_obj))
        #
        # response = {
        #     "items": VacancyListSerializer(page_obj, many=True).data,
        #     "num_pages": paginator.num_pages,
        #     "total": paginator.count
        # }


class VacancyDetailView(RetrieveAPIView):
    #model = Vacancy
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     vacancy = self.get_object()

        # return JsonResponse({
        #     "id": vacancy.id,
        #     "text": vacancy.text,
        #     "status": vacancy.status,
        #     "slug": vacancy.slug,
        #     "created": vacancy.created,
        #     "user": vacancy.user_id,
        #     })
        # ДО СЕРИАЛИЗАТОРА МОДЕЛИ

        # return JsonResponse(VacancyDetailSerializer(vacancy).data, safe=False)

#@method_decorator(csrf_exempt, name="dispatch")
class VacancyCreateView(CreateAPIView):

    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer
    # model = Vacancy
    # fields = ["user", "slug", "text", "status", "created", "skills"]
    # def post(self, request, *args, **kwargs):
    #     vacancy_data = VacancyCreateSerializer(data=json.loads(request.body))
    #     if vacancy_data.is_valid():
    #         vacancy_data.save()
    #     else:
    #         return JsonResponse(vacancy_data.errors)
    #
    #     # vacancy = Vacancy.objects.create(
    #     #     user_id=vacancy_data["user_id"],
    #     #     slug=vacancy_data["slug"],
    #     #     text=vacancy_data["text"],
    #     #     status=vacancy_data["status"]
    #     # )
    #     # vacancy.text = vacancy_data["text"]
    #     #
    #     # return JsonResponse({
    #     #     "id": vacancy.id,
    #     #     "text": vacancy.text
    #     #     })
    #     return JsonResponse(vacancy_data.data)

@method_decorator(csrf_exempt, name="dispatch")
class VacancyUpdateView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer

    # model = Vacancy
    # fields = ["slug", "text", "status", "skills"]
    # def patch(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #
    #     vacancy_data = json.loads(request.body)
    #     self.object.slug=vacancy_data["slug"]
    #     self.object.text=vacancy_data["text"]
    #     self.object.status=vacancy_data["status"]
    #
    #     for skill in vacancy_data["skills"]:
    #         try:
    #             skill_obj = Skill.objects.get(name=skill)
    #         except Skill.DoesNotExist:
    #             return JsonResponse({"error": "Skill not found"}, status=404)
    #         self.object.skills.add(skill_obj)
    #
    #     self.object.save()
    #
    #     return JsonResponse({
    #         "id": self.object.id,
    #         "text": self.object.text,
    #         "slug": self.object.slug,
    #         "status": self.object.status,
    #         "created": self.object.created,
    #         "user": self.object.user_id,
    #         "skills": list(self.object.skills.all().values_list("name", flat=True)),
    #     })
        # Не может ссылаться на ManyReltatedManager (таблица ManyToMany), поэтому выгружаем список навыков
@method_decorator(csrf_exempt, name="dispatch")
class VacancyDeleteView(DestroyAPIView):
    # model = Vacancy
    # success_url = "/"
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDestroySerializer

    # def delete(self, request, *args, **kwargs):
    #     super().delete(request, *args, **kwargs)
    #
    #     return JsonResponse({"status": "ok"}, status=200)

class UserVacancyDetailView(View):
    def get(self, request):
        user_qs = User.objects.annotate(vacancies=Count('vacancy'))

        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                "id":user.id,
                "name":user.username,
                "vacancies":user.vacancies
            })

        response = {
            "items": users,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
            "avg": user_qs.aggregate(avg=Avg("vacancies"))["avg"]
        }

        return JsonResponse(response)