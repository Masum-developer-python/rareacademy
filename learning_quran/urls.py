from django.urls import path,include
from .views import ArabicAlphabetViewSet,ArabicWordViewSet, QuranWordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'arabic-words', ArabicWordViewSet)  # ArabicWord এর জন্য API URL
router.register(r'quran-words', QuranWordViewSet)  # ArabicWord এর জন্য API URL
router.register(r'arabic-alphabets', ArabicAlphabetViewSet)

urlpatterns = [
    path('', include(router.urls)),  # সব Router URL ইন্টারফেসে যোগ করা
    # path('arabic-alphabets/', ArabicAlphabetListCreateView.as_view(), name='arabic-alphabet-list-create'),
]
