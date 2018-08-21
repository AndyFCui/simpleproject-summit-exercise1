from django.db import models


class Uzer(models.Model):
    name        =   models.CharField(
                        max_length=32,
                    )
    phone       =   models.CharField(
                        max_length=12,
                    )
                    
    def __str__(self):
        return '%s (%s)' % (self.name, self.phone)
