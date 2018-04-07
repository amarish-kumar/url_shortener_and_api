from django.db import models
from .utils import create_shortcode


# Create your models here.
class bitlyURL(models.Model):
    url         = models.CharField(max_length=220)
    shortcode   = models.CharField(max_length=15, unique=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    count       = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(bitlyURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
