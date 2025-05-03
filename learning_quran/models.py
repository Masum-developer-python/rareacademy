from django.db import models

# Create your models here.


class ArabicAlphabet(models.Model):
    alphabet = models.CharField(max_length=2)
    alphabet_name = models.CharField(max_length=10, blank=True)
    extra = models.BooleanField(default=False)
    alphabet_banglaname = models.CharField(max_length=20, blank=True)
    alphabet_phonetics = models.CharField(max_length=20, blank=True)
    
    
    def __str__(self):
        return f"{self.alphabet} - {self.alphabet_name}"
    
class QuranWord(models.Model):
    id = models.AutoField(primary_key=True)
    aya = models.IntegerField(null=True, blank=True)
    sura = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    verse_key = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    simple = models.TextField(null=True, blank=True)
    juz = models.IntegerField(null=True, blank=True)
    hezb = models.IntegerField(null=True, blank=True)
    rub = models.IntegerField(null=True, blank=True)
    page = models.IntegerField(null=True, blank=True)
    class_name = models.TextField(null=True, blank=True)
    line = models.IntegerField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    code_v3 = models.TextField(null=True, blank=True)
    char_type = models.TextField(null=True, blank=True)
    audio = models.TextField(null=True, blank=True)
    translation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Word {self.id} - Sura {self.sura}, Aya {self.aya} --- word {self.text}"
        
        
class ArabicWord(models.Model):
    diacritics = models.CharField(max_length=32, blank=True, default="")
    join_diacritics = models.CharField(max_length=32, blank=True, default="Words")
    letter = models.ForeignKey(ArabicAlphabet, on_delete=models.CASCADE)
    position = models.CharField(max_length=32, blank=True, default="")
    word = models.CharField(max_length=32, blank=True, default="")
    bangla = models.CharField(max_length=32, blank=True, default="")
    english = models.CharField(max_length=32, blank=True, default="")
    parts_of_speech = models.CharField(max_length=5, blank=True, default="")
    
    
    class Meta:
        unique_together = ('diacritics', 'letter', 'position')  # Enforces uniqueness across these fields
    
    def __str__(self):
        return f"{self.word}"
        
