from cloudinary_app.views import *

from django.urls import path

urlpatterns = [
    path('get-all-imgs/<str:folder>/', get_all_imgs, name="get_all_imgs"),
    path('upload-categorized-img/<str:folder>/<str:id>/', upload_categorized_img, name="upload_categorized_img"),
    path('get-img-with-effect/<str:folder>/<str:id>/', get_img_with_effect, name="download_img_with_effect")
]