from rest_framework import serializers
from .models import Blog, Section, SubSection, Tag

class BlogSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_sections(self, obj):
        sections = obj.sections.all()
        if sections:
            return SectionSerializer(sections, many=True).data
        return None

    # def get_tags(self, obj):
    #     tags = obj.tags.all()
    #     if tags:
    #         return TagSerializer(tags, many=True).data
    #     return None

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
