from django.db import models
from django.db.models.base import Model

# Create your models here.



class Company(models.Model):
    logo = models.ImageField(upload_to='site_logos/')
    address = models.TextField()
    
    
class Brand(models.Model):
    image = models.ImageField(upload_to='brands/')
    
    
class Banner(models.Model):
    background_image = models.ImageField(upload_to='banner_images/')
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    
class CONTENT21_text(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='content_21_text/')
    
    
    def __str__(self):
        return self.title
    
    
class CONTENT21_obj(models.Model):
    image = models.ImageField(upload_to='content_21_obj/')
    title = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class CONTENT21_obj2(models.Model):
    image = models.ImageField(upload_to='content_21_obj2/')
    title = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.title


    
class CALL06(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='call06/')
    
    
    def __str__(self):
        return self.title
    
    
class FEATURES06_text(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='feauters_text/')
    
    
    def __str__(self):
        return self.title
    
    
class FEATURES06_obj(models.Model):
    image = models.ImageField(upload_to='feauters_obj/')
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    


class Video_introduction_title(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    
class Introduction_video(models.Model):
    video = models.FileField(upload_to='videos/')
    


class CONTENT22_SECTION1(models.Model):
    image = models.ImageField(upload_to='content22_section1/')
    title = models.CharField(max_length=150)
    text = models.TextField()
    title2 = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title
    
    
class CONTENT22_SECTION1_obj(models.Model):
    image = models.ImageField(upload_to='content22_section1_obj/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    

class CONTENT22_SECTION2(models.Model):
    image = models.ImageField(upload_to='content22_section2/')
    title = models.CharField(max_length=150)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    

class CONTENT22_SECTION2_obj(models.Model):
    image = models.ImageField(upload_to='content22_section2_obj/')
    title = models.CharField(max_length=150)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    

class CONTENT22_SECTION3(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='content22_section3/')
    
    def __str__(self):
        return self.title
    
    
class CONTENT22_SECTION3_obj(models.Model):
    image =models.ImageField(upload_to='content22_section3_obj/')
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    

class CONTENT23(models.Model):
    background_image = models.ImageField(upload_to='content23/')
    title = models.CharField(max_length=150)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    

class PORTFOLIO07(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
class PORTFOLIO07_image(models.Model):
    image = models.ImageField(upload_to='portfolio007_image/')
    
    
class PORTFOLIO07_obj(models.Model):
    image = models.ImageField(upload_to='portfolio007obj/')
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    

class TESTIMONALS(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    

class TESTIMONALS_text(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='testimonals_text/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    


class DOWNLOAD01_form_text(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='download_form_text/')
    
    
    def __str__(self):
        return self.title
    
    
class Clients(models.Model):
    name = models.TextField()
    phone_number = models.TextField()
    
    def __str__(self):
        return self.name
    

class Chat_id(models.Model):
    chat_id = models.PositiveIntegerField()
    

    