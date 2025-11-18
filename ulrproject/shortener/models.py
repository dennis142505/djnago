import string, random
from django.utils import timezone   
from django.db import models
from django.contrib.auth.models import User

def make_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    original = models.URLField()
    short = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    
    def save(self, *args, **kwargs):
        if not self.short:
            new_short = make_short()
            while URL.objects.filter(short=new_short).exists():
                new_short = make_short()
            self.short = new_short
        super().save(*args, **kwargs)
