from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = _("Neighborhood")
        verbose_name_plural = _("Neigh  borhoods")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Neighborhood_detail", kwargs={"pk": self.pk})
    
    