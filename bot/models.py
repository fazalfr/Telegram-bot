from django.db import models
from django.contrib.auth.models import User

class Joke(models.Model):
    CATEGORY_CHOICES = (
        ('stupid', 'Stupid'),
        ('fat', 'Fat'),
        ('dumb', 'Dumb'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, unique=True)

class JokeCall(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    call_count = models.IntegerField(default=0)


    # def __str__(self):
    #     return self.category

    # def __str__(self):
    #     return self.category

    def __str__(self):
        return f'{self.user.username} called {self.joke.category} {self.call_count} times'


    # def increment_call_count(self):
    #     self.call_count += 1
    #     self.save()
