from rest_framework import serializers
from .models import ArabicAlphabet, ArabicWord, QuranWord

class ArabicAlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArabicAlphabet
        fields = "__all__"   #['id','alphabet', 'alphabet_name']
        
        
class ArabicWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArabicWord
        fields = "__all__"
        
        
class QuranWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuranWord
        fields = ['aya', 'sura', 'position', 'text']