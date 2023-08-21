from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Property, Amenity
from .forms import RentingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def properties_index(request):
    properties = Property.objects.all()
    return render(request, 'properties/index.html', {
        'properties': properties
    })

def properties_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    id_list = property.amenities.all().values_list('id')
    amenities_property_doesnt_have = Amenity.objects.exclude(id__in=id_list)
    renting_form = RentingForm()
    return render(request, 'properties/detail.html', {
        'property':property,
        'renting_form': renting_form,
        'amenities': amenities_property_doesnt_have

    })

class PropertyAdd(CreateView):
    model = Property
    fields = ['title', 'address', 'suburb', 'state', 'postcode', 'details', 'price']

class PropertyUpdate(UpdateView):
  model = Property
  fields = ['title', 'address', 'suburb', 'state', 'postcode', 'details', 'price']

class PropertyDelete(DeleteView):
  model = Property
  success_url = '/properties'
    

def add_renting(request, property_id):
    form = RentingForm(request.POST)
  # validate the form
    if form.is_valid():
        new_renting = form.save(commit=False)
        new_renting.property_id = property_id
        new_renting.save()
    return redirect('detail', property_id=property_id)

class AmenityList(ListView):
  model = Amenity

class AmenityDetail(DetailView):
  model = Amenity

class AmenityCreate(CreateView):
  model = Amenity
  fields = '__all__'

class AmenityUpdate(UpdateView):
  model = Amenity
  fields = ['name']

class AmenityDelete(DeleteView):
  model = Amenity
  success_url = '/amenities'     


def assoc_amenity(request, property_id, amenity_id):
    Property.objects.get(id=property_id).amenities.add(amenity_id)
    return redirect('detail', property_id=property_id)

def unassoc_amenity(request, property_id, amenity_id):
    Property.objects.get(id=property_id).amenities.remove(amenity_id)
    return redirect('detail', property_id=property_id)