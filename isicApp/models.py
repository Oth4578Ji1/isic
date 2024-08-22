# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('responsable', 'Responsable'),
        ('etudiant', 'Etudiant'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    CIN = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username

class Competition(models.Model):
    BACHELOR = 'L'
    MASTER = 'M'
    COMPETITION_TYPES = [
        (BACHELOR, 'License'),
        (MASTER, 'Master'),
    ]

    FIELD_CHOICES = [
        ('Communication Politique', 'Communication Politique'),
        ('Journalisme Sportif', 'Journalisme Sportif'),
        ('Innovation et Production de Contenus Audiovisuels et Numérique', 'Innovation et Production de Contenus Audiovisuels et Numérique'),
    ]

    type = models.CharField(max_length=1, choices=COMPETITION_TYPES)
    field = models.CharField(max_length=150, choices=FIELD_CHOICES, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_type_display()} - {self.field}'

class Application(models.Model):
    ARRIVED = 'Arrivée'
    UNDER_PROCESSING = 'En cours'
    ACCEPTED = 'Accepté'
    REJECTED = 'Rejetée'
    STATUS_CHOICES = [
        (ARRIVED, 'Arrivée'),
        (UNDER_PROCESSING, 'En cours'),
        (ACCEPTED, 'Accepté'),
        (REJECTED, 'Rejetée'),
    ]

    BACCALAUREATE_CHOICES = [
        ('Sciences', 'Sciences'),
        ('Littéraire', 'Littéraire'),
        ('Economie/Gestion', 'Economie/Gestion'),
    ]

    DIPLOMA_CHOICES = [
        ('Diplome d`ISIC', 'Diplome d`ISIC'),
        ('License Fondamentale', 'License Fondamentale'),
        ('License Professionnelle', 'License Professionnelle'),
    ]

    DIPLOMA_GRADE_CHOICES = [
        ('Passable', 'Passable'),
        ('A-Bien', 'A-Bien'),
        ('Bien', 'Bien'),
        ('T-Bien', 'T-Bien'),
    ]

    LANGUAGE_CHOICES = [
        ('Anglais', 'Anglais'),
        ('Francais', 'Francais'),
        ('Arabe', 'Arabe'),
    ]
    T_LANGUAGE_CHOICES = [
        ('Anglais', 'Anglais'),
        ('Espagnole', 'Espagnole'),
        ('Allemand', 'Allemand'),
        ('Autre', 'Autre'),
    ]

    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    CNE= models.CharField(max_length=24, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ARRIVED)
    baccalaureate_category = models.CharField(max_length=35, choices=BACCALAUREATE_CHOICES, default='Littéraire')
    baccalaureate_grade = models.FloatField(null=True)
    diploma_category = models.CharField(max_length=60, choices=DIPLOMA_CHOICES, blank=True)
    diploma_year = models.IntegerField(null=True, blank=True)
    diploma_grade = models.CharField(max_length=20, choices=DIPLOMA_GRADE_CHOICES, blank=True)
    license_field_name = models.CharField(max_length=200,null=True, blank=True)
    université = models.CharField(max_length=200, null=True, blank=True)
    troisieme_lng =models.CharField(max_length=25, null=True, blank=True, choices= T_LANGUAGE_CHOICES)
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICES)
    semester_1_grade = models.FloatField(null=True, blank=True)
    semester_2_grade = models.FloatField(null=True, blank=True)
    semester_3_grade = models.FloatField(null=True, blank=True)
    semester_4_grade = models.FloatField(null=True, blank=True)
    semester_5_grade = models.FloatField(null=True, blank=True)
    semester_6_grade = models.FloatField(null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student} - {self.competition} - {self.status}'