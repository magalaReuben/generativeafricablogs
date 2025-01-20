from rest_framework import serializers
from .models import Blog, Section, SubSection, Tag, BlogImage

class BlogSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    blog_images = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_sections(self, obj):
        sections = obj.sections.all()
        if sections:
            return SectionSerializer(sections, many=True).data
        return None

    def get_blog_images(self, obj):
        blog_images = obj.blog_image.all()
        if blog_images:
            return BlogImageSerializer(blog_images, many=True).data
        return None
    
class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    subsections = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    def get_subsections(self, obj):
        subsections = obj.subsections.all()
        if subsections:
            return SubSectionSerializer(subsections, many=True).data
        return None

class SubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSection
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    blogs = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = '__all__'

    def get_blogs(self, obj):
        blogs = obj.blogs.all()
        if blogs:
            return BlogSerializer(blogs, many=True).data
        return None
