from django.urls import path

from blog.views import index, single, contact, category, detail, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    # 👉-------------------------Pages----------------------------👈

    path('', index,name='index'),
    path('single/', single, name='single'),
    path('contact/', contact,name='contact'),
    path('category/<int:id>/', category,name='category'),

# 👉---------------------------Pages end------------------------------👈

# 👉---------------------------Deteil------------------------------👈

    path('detail/<slug:slug>',detail,name = 'detail' ),

# 👉---------------------------Deteil end------------------------------👈

# 👉---------------------------create delete update list ------------------------------👈

    path('addNews/', NewsCreateView.as_view(), name = 'addNews'),
    path('updateNews/<slug:slug>/', NewsUpdateView.as_view(), name='updateNews'),
    path('deleteNews/<slug:slug>/', NewsDeleteView.as_view(), name='deleteNews'),

# 👉---------------------------create delete update list end------------------------------👈

]