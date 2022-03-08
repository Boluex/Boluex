from django.shortcuts import render,redirect
from PyDictionary import PyDictionary
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        check=PyDictionary()
        word = request.POST['text']
        antonyms=check.antonym(word)
        meaning=check.meaning(word)
        synonyms=check.synonym(word)
        print(synonyms)
        print(antonyms)
        context = {
            'word':word,
            'antonyms':antonyms,
            'meaning':meaning['Noun'][0],
            'synonyms':synonyms,
        }
        messages.success(request,f'You search for {word} and here are your results')
        return render(request,'books/search.html',context)
    else:
        return render(request, 'books/search.html', {})
