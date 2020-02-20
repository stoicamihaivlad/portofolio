from django.db import models

# Create a blog model
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


#Create a migration

#Migrate

#Add to the admin
