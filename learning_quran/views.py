from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from .models import ArabicAlphabet, ArabicWord, QuranWord
from .serializers import ArabicAlphabetSerializer, ArabicWordSerializer, QuranWordSerializer

class ArabicAlphabetViewSet(viewsets.ModelViewSet):
    queryset = ArabicAlphabet.objects.all()
    serializer_class = ArabicAlphabetSerializer
    pagination_class = None

    # def create(self, request, *args, **kwargs):
    #     print("Received Data:", request.data)  # Debugging
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     print("Errors:", serializer.errors)  # Log errors
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArabicWordViewSet(viewsets.ModelViewSet):
    queryset = ArabicWord.objects.all()  # সব ArabicWord দেখাবে
    serializer_class = ArabicWordSerializer
    pagination_class = None
    
    @action(detail=False, methods=['get'])
    def filter_by_diacritics(self, request):
        diacritic = request.query_params.get('diacritic', None)
        
        if not diacritic:
            return Response({"error": "diacritic parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        word = ArabicWord.objects.filter(diacritics = diacritic)
        serializer = self.get_serializer(word, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class QuranWordViewSet(viewsets.ModelViewSet):
    queryset = QuranWord.objects.all()  # সব ArabicWord দেখাবে
    serializer_class = QuranWordSerializer
    pagination_class = None
    
    
    @action(detail=False, methods=['get'])
    def filter_by_arabic_words(self, request):
        arabic_words = ArabicWord.objects.values_list('word', flat=True)
        filtered_quran_words = QuranWord.objects.filter(text__in=arabic_words)

        serializer = self.get_serializer(filtered_quran_words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'])
    def filter_by_word(self, request):
        word = request.query_params.get('word', None)  # Get 'word' from the request

        if not word:
            return Response({"error": "Word parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        filtered_quran_words = QuranWord.objects.filter(text=word)  # Filter by the word

        serializer = self.get_serializer(filtered_quran_words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)