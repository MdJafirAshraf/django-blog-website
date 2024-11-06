from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True)
    content = models.TextField(null=False,  blank=False)

    def get_absolute_url(self):
        return f"/blogpost/{self.slug}"
    
    def get_edit_url(self):
        return f"/blogpost/{self.slug}/edit"
    
    def get_delete_url(self):
        return f"/blogpost/{self.slug}/delete"