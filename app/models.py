from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(null=False,max_length=20)
    # tel=models.CharField(null=False,max_length=20)
    
    def __str__(self):
        return self.name