from django.db import models


class User(models.Model):
    """
    Netflix Model
    Defines the attributes of a Netflix Movie
    """
    user_id = models.IntegerField(primary_key = True)
    details_id = models.ForeignKey('Details', on_delete = models.CASCADE)
    location_id = models.ForeignKey('Location', on_delete = models.CASCADE)
    plan_id = models.ForeignKey('Plan', on_delete = models.CASCADE)

    # def get_genre(self):
    #     return self.name + ' belongs to ' + self.genre + ' genre.'
    #
    # def __repr__(self):
    #     return self.name + ' is added.'

class Personal(models.Model):
    personal_id = models.IntegerField(primary_key = True)
    personal_gender = models.CharField(max_length = 50)
    personal_dob = models.DateTimeField()
    name_id = models.ForeignKey('Name', on_delete = models.CASCADE)
   

class Details(models.Model):
    details_id = models.IntegerField(primary_key = True)
    personal_id = models.ForeignKey('Personal', on_delete = models.CASCADE)

class Location(models.Model):
    location_id = models.IntegerField(primary_key = True)
    location_city = models.CharField(max_length = 50)
    location_state = models.CharField(max_length = 50)
    location_name = models.CharField(max_length = 50)

class Name(models.Model):
    name_id = models.IntegerField(primary_key = True)
    name_firstname = models.CharField(max_length = 50)
    name_lastname = models.CharField(max_length = 50)
    name_middlename = models.CharField(max_length = 50)

class Contacts(models.Model):
    contact_id = models.IntegerField(primary_key = True)
    contact_number = models.IntegerField()
    contact_email = models.CharField(max_length = 50)

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key = True)
    payment_type = models.CharField(max_length = 50)
    payment_amount = models.IntegerField()

class Plan(models.Model):
    plan_id = models.IntegerField(primary_key = True)
    payment_id = models.ForeignKey('Payment', on_delete = models.CASCADE)

class Director(models.Model):
    director_id = models.IntegerField(primary_key = True)
    director_soap = models.CharField(max_length = 50)
    director_movie = models.CharField(max_length = 50)

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key = True)
    genre_soap = models.CharField(max_length = 50)
    genre_movie = models.CharField(max_length = 50)

class Soap(models.Model):
    soap_id = models.IntegerField(primary_key = True)
    soap_title = models.CharField(max_length = 50)
    genre_id = models.ForeignKey('Genre', on_delete = models.CASCADE)
    director_id = models.ForeignKey('Director', on_delete = models.CASCADE)
    soap_cast = models.CharField(max_length = 50)
    release_id = models.ForeignKey('Release', on_delete = models.CASCADE)

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key = True)
    movie_title = models.CharField(max_length = 50)
    genre_id = models.ForeignKey('Genre', on_delete = models.CASCADE)
    director_id = models.ForeignKey('Director', on_delete = models.CASCADE)
    movie_cast = models.CharField(max_length = 50)
    release_id = models.ForeignKey('Release', on_delete = models.CASCADE)

class Release(models.Model):
    release_id = models.IntegerField(primary_key = True)
    release_soap = models.DateTimeField()
    release_movie = models.DateTimeField()
