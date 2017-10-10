from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Personal, Details, Location, Name, Contacts, Payment, Plan, Director, Genre, Soap, Movie, Release
from .serializers import UserSerializer, PersonalSerializer, DetailsSerializer, LocationSerializer, NameSerializer, ContactsSerializer, PaymentSerializer, PlanSerializer, DirectorSerializer, GenreSerializer, SoapSerializer, MovieSerializer, ReleaseSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PersonalViewSet(ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()

class DetailsViewSet(ModelViewSet):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()

class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class NameViewSet(ModelViewSet):
    serializer_class = NameSerializer
    queryset = Name.objects.all()

class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class SoapViewSet(ModelViewSet):
    serializer_class = SoapSerializer
    queryset = Soap.objects.all()

class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class ReleaseViewSet(ModelViewSet):
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()
