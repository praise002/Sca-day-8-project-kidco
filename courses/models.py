from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from . fields import OrderField


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
    
class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
    
    
class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    order = OrderField(blank=True, for_fields=['course']) #ordering of a module is based on the course
    
    def __str__(self):
        return f'{self.order}. {self.title}'
    
    #Default ordering for both models
    class Meta:
        ordering = ['order']
    
    
class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, 
                                    on_delete=models.CASCADE,
                                    limit_choices_to={'model__in':(  #model__in: to filter query
                                        'text',
                                        'video',
                                        'image',
                                        'file'
                                    )})  #limit_choices is used for d generic relationship
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')  #it combines the two previous fields
    #The item allows you to retrieve or set the related object directly and its functionality is built
    #on top of the other two fields
    
    order = OrderField(blank=True, for_fields=['module'])  #module contents need to follow an order
    
    #Default ordering for both models
    class Meta:
        ordering = ['order']
    
    
class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title
    

class Text(ItemBase):  #to store text content
    content = models.TextField()

class File(ItemBase):  #to store files such as pdfs
    file = models.FileField(upload_to='files')

class Image(ItemBase):  #to store image files
    image = models.FileField(upload_to='images')

class Video(ItemBase):  # to store videos
    url = models.URLField()  #to embed the video