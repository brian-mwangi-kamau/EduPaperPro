from django.db import models



class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    file = models.FileField(upload_to='files/')
    LEVEL_CHOICES = [
        ('primary-school', 'Primary School'),
        ('high-school', 'High School'),
        ('tertiary', 'Tertiary Institutions'),
    ]
    level_of_education = models.CharField(max_length=50, choices=LEVEL_CHOICES)

    SUBJECT_CHOICES = [
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
    ]

    COURSE_CHOICES = [
        ('Architecture', 'Architecture'),
        ('Medicine', 'Medicine'),
    ]

    subjects = models.CharField(max_length=100, choices=SUBJECT_CHOICES, blank=True)
    courses = models.CharField(max_length=100, choices=COURSE_CHOICES, blank=True)

    FORM_CHOICES = [
        ('Form one', 'Form One'),
        ('Form two', 'Form Two'),
        ('Form three', 'Form Three'),
    ]

    YEAR_CHOICES = [
        ('First year', 'First year'),
        ('Second year', 'Second year'),
        ('Third year', 'Third year'),
    ]

    form = models.CharField(max_length=100, choices=FORM_CHOICES, blank=True)
    year = models.CharField(max_length=100, choices=YEAR_CHOICES, blank=True)
    is_free = models.BooleanField(default=False)
    # timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class DownloadRecord(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    