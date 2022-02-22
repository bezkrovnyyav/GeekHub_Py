from django.db import models


class Askstories(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    kids = models.TextField(null=True)
    score = models.IntegerField()
    text = models.TextField()
    time = models.IntegerField()
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Showstories(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    kids = models.TextField(null=True)
    score = models.IntegerField()
    text = models.TextField()
    time = models.IntegerField()
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Jobstories(models.Model):
    by = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    score = models.CharField(max_length=200)
    text = models.TextField()
    time = models.IntegerField()
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Newstories(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    kids = models.TextField(null=True, default="--")
    score = models.CharField(max_length=200)
    time = models.IntegerField(default="--")
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default="--")
    text = models.TextField()

    def __str__(self):
        return self.title
