from django.shortcuts import render,redirect
from django.views import View
from store.forms import BookForm
from .models import Product

# Create your views here.
class Store(View):
  def get(self,request):
    context={}
    form=BookForm()
    context['form']=form
    products = Product.objects.all()
    context['books'] = products
    return render(request,'bookstore.html',context)
  def post(self, request):
    form = BookForm(request.POST)  
    if form.is_valid():
        book_instance=Product(
           name=form.cleaned_data['book_name'],
           author=form.cleaned_data['author_name']
        )
        book_instance.save()
    return redirect('store')
  
class Detail(View):
   def get(self,request,pk):
      book=Product.objects.get(pk=pk)
      context = {'book': book}
      return render(request,'bookdetail.html',context)
   
class Delete(View):
   def get(self,request,pk):
      book=Product.objects.get(pk=pk)
      book.delete()
      return redirect('store')

   
      

