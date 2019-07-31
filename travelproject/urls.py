from django.contrib import admin
from django.urls import path
import travelapp.views
import ReviewMore.views as review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', travelapp.views.home, name = "home"),
    path('TravelReview/<int:travel_id>', travelapp.views.detail, name="detail"),
    path('travel/new/', travelapp.views.new, name="new"),
    path('travel/create', travelapp.views.create, name="create"),
    path('reviewmore/', review.reviewmore, name="reviewmore"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

