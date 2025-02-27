from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import home, recipes, base, delete_recipe, update_recipe, login_page, register_page , logout_page
from vege.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Home page
    path("recipes/", recipes, name="recipes"),  # Recipes page
    path("base/", base, name="base"),  # Base page
    path("delete_recipe/<int:id>/", delete_recipe, name="delete_recipe"),  # Fixed delete route
    path("update_recipe/<int:id>/", update_recipe, name="update_recipe"),  # Update route
    path("login/", login_page, name="login_page"),  # Login page
    path("register/", register_page, name="register_page"),  # Register page
    path("logout/", logout_page, name="logout_page"),  # Logout page
    
    # path("students/", get_students , name="get_students"), 
    # path("see-marks/<student_id>", see_marks , name="see_marks"), 



]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files
urlpatterns += staticfiles_urlpatterns()
