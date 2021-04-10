from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

CATEGORY_CHOICES = [
    ('health','Health'),
    ('tech','Technology'),
    ('food','Food'),
    ('travel','Travel'),
    ('music','Music'),
    ('lifestyle','Lifestyle')
]

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES,blank = True, null =True)
    body = RichTextField()
    views_count = models.IntegerField(default=0)
    slug = models.SlugField(blank = True, null =True)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:50])
        super(Blog, self).save(*args, **kwargs) # Call the real save() method

    def increase(self):
        self.views_count += 1
        self.save()


class Contact(models.Model):
    first_name = models.CharField(max_length = 80)
    last_name = models.CharField(max_length = 80)
    email = models.EmailField(max_length=254)
    message = RichTextField(max_length=1000)
    add_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return str(self.fname)
