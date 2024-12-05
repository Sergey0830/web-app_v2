from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Question

# Create your views here.

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'contact_method', 'email', 'phone', 'question']

# Представлення для головної сторінки
def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Перенаправлення на сторінку подяки
    else:
        form = QuestionForm()
    return render(request, 'main/index.html', {'form': form})

# Представлення для сторінки подяки
def thank_you(request):
    return render(request, 'main/thank_you.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')

def types_work(request):
    return render(request, 'main/types_work.html')