from django.db import models

class FizzBuzzRequest(models.Model):
    int1 = models.IntegerField()
    int2 = models.IntegerField()
    limit = models.IntegerField()
    str1 = models.CharField(max_length=100)
    str2 = models.CharField(max_length=100)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.int1}, {self.int2}, {self.limit}, {self.str1}, {self.str2}, hits: {self.hits}"
