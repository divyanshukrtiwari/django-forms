from django.shortcuts import render

from .forms import PizzaForm, MultiplePizzaForm

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Your order of %s %s and %s pizza has been placed!' %(filled_form.cleaned_data['size'], 
            filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {"pizzaform": new_form, 'note':note, 'multiple_form':multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {"pizzaform": form, 'multiple_form': multiple_form})

