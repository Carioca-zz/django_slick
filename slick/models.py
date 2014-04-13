from django.db import models
from django.template import Context
from django.template.loader import get_template

# Create your models here.

class Slick(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Element(models.Model):
    gallery = models.ForeignKey(Slick)
    content = models.TextField()
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['ordering']

class Image(Element):
    image = models.ImageField(upload_to='slick')

    @classmethod
    def content(self):
        t = get_template('image.html')
        return t.render(Context({'image': self.image}))