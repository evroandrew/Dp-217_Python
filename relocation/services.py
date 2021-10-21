from .models import Housing, University, City
from django.db.models import Q


class CityService:

    @staticmethod
    def get(city_id:str):
        return City.objects.filter(id=city_id).first()


class UniversityService:

    @staticmethod
    def get(uni_id:str):
        return University.objects.filter(id=uni_id).first()


class HousingService:

    @staticmethod
    def all_in_city_for_uni(uni:University, city:City):
        q = Housing.objects.filter(city=city)
        return q.filter(Q(university=uni) | Q(university__isnull=True))

    @staticmethod
    def all_for_uni(uni:University):
        return HousingService.get_by_city(university=uni, city=uni.city)
