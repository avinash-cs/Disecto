

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import LineItem, Invoice,Products,Orders
from .forms import LineItemFormset, InvoiceForm,addproductsForm,ordersForm
from .render import render_to_pdf


def index(request):
    return render(request,'disecto/home.html')
def buyproduct(request):
    form = ordersForm()
    if request.method == 'POST':
        form = ordersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/disecto/orders')
    context = {'form':form}
    return render(request,'disecto/buyproduct.html',context)
def addproducts(request):
    form = addproductsForm()
    if request.method == 'POST':
       # print(request.POST)
       form = addproductsForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/disecto/productlist')
    context = {'form':form}
    return render(request,'disecto/addproducts.html',context)

def updateproduct(request,pk):
    product = Products.objects.get(id=pk)
    if request.method == 'POST':
       # print(request.POST)
       form = addproductsForm(request.POST,instance=product)
       if form.is_valid():
           form.save()
           return redirect('/disecto/productlist')
    form = addproductsForm(instance=product)
    context = {'form':form}
    return render(request,'disecto/updateproduct.html',context)
def updateorders(request,pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
       # print(request.POST)
       form = ordersForm(request.POST,instance=order)
       if form.is_valid():
           form.save()
           return redirect('/disecto/orders')
    form = ordersForm(instance=order)
    context = {'form':form}
    return render(request,'disecto/updateorders.html',context)
def deleteproduct(request,pk):
    product = Products.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/disecto/productlist')
    context = {'product':product}
    return render(request,'disecto/deleteproduct.html',context)
def deleteorders(request,pk):
    order = Orders.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/disecto/orders')
    context = {'order':order}
    return render(request,'disecto/deleteorders.html',context)
def orders(request):
    order = Orders.objects.all()
    context = {'order':order}
    return render(request,'disecto/orders.html',context)

def productlist(request):
    products = Products.objects.all()
    context = {"products":products}
    return render(request,'disecto/productlist.html', context)

class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'disecto/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('disecto:invoice-list')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = LineItemFormset(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(customer=form.data["customer"],
                    customer_email=form.data["customer_email"],
                    billing_address = form.data["billing_address"],
                    date=form.data["date"],
                   
                    )
            # invoice.save()
            
        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0
            for form in formset:
                service = form.cleaned_data.get('service')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')
                if service  and quantity and rate:
                    amount = float(rate)*float(quantity)
                    total += amount
                    LineItem(customer=invoice,
                            service=service,
                            
                            quantity=quantity,
                            rate=rate,
                            amount=amount).save()
            invoice.total_amount = total
            invoice.save()
            try:
                generate_PDF(request, id=invoice.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('disecto:invoice-list')
    context = {
        "title" : "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'disecto/invoice-create.html', context)


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()

    context = {
        "company": {
            "name": "Disecto",
            "address" :"Sector xn, District, Jammu & Kashmir",
            "phone": "(818) XXX XXXX",
            "email": "contact@disecto.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "customer": invoice.customer,
        "customer_email": invoice.customer_email,
        "date": invoice.date,
        
        "billing_address": invoice.billing_address,
       
        "lineitem": lineitem,

    }
    return render(request, 'disecto/pdf_template.html', context)

def generate_PDF(request, id):
    # Use False instead of output path to save pdf to a variable
    # pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False)
    # response = HttpResponse(pdf,content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    # return response
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()

    context = {
        "company": {
            "name": "Disecto",
            "address" :"Sector xn, District, Jammu & Kashmir",
            "phone": "(818) XXX XXXX",
            "email": "contact@disecto.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "customer": invoice.customer,
        "customer_email": invoice.customer_email,
        "date": invoice.date,
        
        "billing_address": invoice.billing_address,
       
        "lineitem": lineitem,

    }
    return render_to_pdf( 'disecto/pdf_template.html', context)


def view_404(request,  *args, **kwargs):

    return redirect('disecto:invoice-list')