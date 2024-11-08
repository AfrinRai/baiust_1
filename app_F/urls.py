from django.urls import path

#from cbv
from .views.cbv_views import BookListView

#from fbv
from .views.fbv_views import book_list

urlpatterns = [
    # path('admin/', admin.site.urls),
    #from cbv
    path('cbv/', BookListView.as_view(), name='book_list'),  # URL for viewing the book list

    #from fbv
    path('fbv/', book_list)
]

