from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView
from manager.models import Purchase,Inventory,Orders,OrderItem
from manager.forms import LoginForm,PurchaseForm
from django.urls import reverse_lazy

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect


class ManagerHomeView(TemplateView):
    template_name = "home.html"







def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manager_home')
        else:
            return render(request, 'managerlogin.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'managerlogin.html')




class PurchaseView(CreateView):
    model = Purchase
    template_name = "purchase.html"
    fields = ['medicine_id', 'medicine_name', 'quantity', 'purchase_amount']
    success_url = reverse_lazy('manager_home')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Get the Purchase object and its data
        purchase = form.save(commit=False)
        medicine_id = purchase.medicine_id
        quantity = purchase.quantity

        # Update the Stock object or create a new one if it doesn't exist
        stock, created = Inventory.objects.get_or_create(product_id=medicine_id,expiry_date=purchase.expiry_date)
        stock.medicine_name = purchase.medicine_name
        stock.quantity += quantity
        stock.save()

        return response



class StockView(ListView):
    model = Inventory
    context_object_name = "Stocks"
    template_name = "stock.html"

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders.html', {'orders': orders})

# create a new order
# order = Orders.objects.create(cut_name='John Smith')
#
 # create some order items and associate them with the order
# item1 = OrderItem.objects.create(order=order, medicine_name='Aspirin', quantity=2)
# item2 = OrderItem.objects.create(order=order, medicine_name='Ibuprofen', quantity=3, prescription='Take with food')





