from rest_framework import serializers
from .models import User, Personal, Details, Location, Name, Contacts, Payment, Plan, Director, Genre, Soap, Movie, Release


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'details_id', 'location_id', 'plan_id')

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('personal_id', 'personal_gender', 'personal_dob', 'name_id', 'contact_id')

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('details_id', 'personal_id')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('location_id', 'location_city', 'location_state', 'location_name')

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('name_id', 'name_firstname', 'name_lastname', 'name_middlename')

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('contact_id', 'contact_number', 'contact_email')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id', 'payment_type', 'payment_amount')

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('plan_id', 'payment_id')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('director_id', 'director_soap', 'director_movie')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_id', 'genre_soap', 'genre_movie')

class SoapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soap
        fields = ('soap_id', 'soap_title', 'genre_id', 'director_id', 'soap_cast', 'release_id')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'movie_title', 'genre_id', 'director_id', 'movie_cast', 'release_id')

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ('release_id', 'release_soap', 'release_movie')
