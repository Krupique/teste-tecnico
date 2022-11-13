from django.db import models

# Create your models here.

class Noticia(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Comentario(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField()

    noticia = models.ForeignKey(Noticia, null=False, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

