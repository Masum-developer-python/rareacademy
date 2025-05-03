from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ArabicAlphabet)


# class ArabicWordAdmin(admin.ModelAdmin):
#     # You can exclude in_quran from the admin if you don't want it to be manually editable
#     exclude = ('in_quran',)  # Hide the field from the admin panel (optional)
    
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "in_quran":
#             kwargs["required"] = False  # Ensure the field is not required
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
        
#     def save_model(self, request, obj, form, change):
#         # Automatically assign `in_quran` if it is not set
#         if not obj.in_quran:
#             # Look for a QuranWord instance based on the `word` field
#             quran_word = QuranWord.objects.filter(text=obj.word).first()
#             if quran_word:
#                 obj.in_quran = quran_word  # Assign the related QuranWord instance
#         obj.save()  # Save the object with the updated `in_quran` field
        
        
admin.site.register(ArabicWord)
admin.site.register(QuranWord)