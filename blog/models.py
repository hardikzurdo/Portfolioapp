from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 300)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/' )
    tags = models.TextField(max_length = 100)


    def pub_date_cool(self):
        return self.pub_date.strftime('%b %e %Y')
