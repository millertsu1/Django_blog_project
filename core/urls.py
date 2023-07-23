from django.urls import path
from .views import home, post, category, author, dates
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>', category, name='category'),
    path('author/<int:author_id>', author, name='author'),
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),
    path('post/<int:post_id>', post, name='post'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)