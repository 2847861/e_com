from product.models import Items_F,Items
from django.forms import ModelForm
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context
	
def new_item(request):
    form = Items_F(request.POST)
    if request.method == 'POST':
        form = Items_F(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            photo = form.cleaned_data['photo']
            description = form.cleaned_data['description']             
            instance= form.save()
            it = get_object_or_404(Items, pk=instance.id)
            return render_to_response('product/item.html', { 'item': it }, RequestContext(request))# Redirect after POST		
	else:
         form = Items_F(request.POST) # An unbound form
    return render_to_response('product/new_item.html', {'form':form}, RequestContext(request))
	

def edit_item(request, i_id):
    it = get_object_or_404(Items, pk=i_id)
    return render_to_response('product/item.html', { 'item': it, 'list':Items.objects.all() })    
	
def all(request):
    return render_to_response('product/all_items.html', { 'list': Items.objects.all() } )
	
def home(request):
    return render_to_response('product/home.html', { 'list': Items.objects.all() } )