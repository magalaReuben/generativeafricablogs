from django.db import models

# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    introduction = models.TextField()
    course_image = models.ImageField(upload_to='images/')
    course_link = models.URLField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200, blank=True, null=True)
    section_image = models.ImageField(upload_to='images/', null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.blog.title} : " + self.title


class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subsections')
    title = models.CharField(max_length=200, blank=True, null=True)
    sub_section_image = models.ImageField(upload_to='images/', null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.section.blog.title}-" + f"{self.section.title} : " + self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    blogs = models.ManyToManyField(Blog, related_name='tags')

    def __str__(self):
        return self.name
