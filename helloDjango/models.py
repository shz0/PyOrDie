from django.db import models

class Artikel(models.Model):
    titel = models.CharField(max_length=100)
    number = models.TextField(null=True, blank=True)

    # Solution for my int/string problem!
    @property
    def number_as_int(self):
        if self.number:
            try:
                return int(self.number)
            except ValueError:
                return None
        return None

    @number_as_int.setter
    def number_as_int(self, value):
        self.number = str(value)
        if value is not None else None:     # <--
            pass

    # End of the Code for the Solution! (rewatch)