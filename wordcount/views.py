from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token


def home(request):
  return render(request, 'home.html')

def egg(request):
  return HttpResponse("Eggs are eggs")

@requires_csrf_token
def count(request):
  full = request.POST['full-text']
  # print(full)
  word_list = full.split()

  word_dict = {}

  for word in word_list:
    if word in word_dict:
      #increase
      word_dict[word] += 1
    else:
      #add to dict
      word_dict[word] = 1
  return render(request, 'count.html', {'fulltext': full, 'count': len(word_list), 'word_dict': word_dict})
