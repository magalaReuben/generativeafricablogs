#from .models import BlogImage  # Replace 'myapp' with your actual app name
# import os
# from django.core.files.storage import default_storage

# # Fetch all blog images
# blog_images = BlogImage.objects.all()

# for blog_image in blog_images:
#     if blog_image.image:
#         # Get the image file path
#         image_path = blog_image.image.path  
        
#         # Delete the file if it exists
#         if os.path.exists(image_path):
#             os.remove(image_path)
#             print(f"Deleted: {image_path}")

# # Delete all BlogImage entries from the database
# blog_images.delete()
# print("All blog images deleted from the database.")
