from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import TemperatureForm, PinsForm, ZonesForm
from .models import Temperature, Pins, Zones


#########################TEMPERATURES####################

def get_temperature(request):
    if request.method == "POST":
        form = TemperatureForm(request.POST)
        if form.is_valid():
            fuel = form.cleaned_data['fuel']
            termfuel = form.cleaned_data['termfuel']
            clad = form.cleaned_data['clad']
            tube = form.cleaned_data['tube']
            t = Temperature(fuel=fuel,
                            termfuel=termfuel,
                            clad=clad,
                            tube=tube, )
            t.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = TemperatureForm()

    return render(request, 'temperatures.html', {'form': form})


#########################################################
#########################THANKS##########################

def get_thanks(request):
    return HttpResponse("Thanks! Your data saved into Database.")


#########################################################
#########################PINS############################

def get_pins(request):
    if request.method == "POST":
        form = PinsForm(request.POST)
        if form.is_valid():
            pin1_void1 = form.cleaned_data['pin1_void1']
            pin1_fuel = form.cleaned_data['pin1_fuel']
            pin1_void2 = form.cleaned_data['pin1_void2']
            pin1_clad = form.cleaned_data['pin1_clad']

            pin2_termfuel = form.cleaned_data['pin2_termfuel']
            pin2_clad = form.cleaned_data['pin2_clad']

            p = Pins(pin1_void1=pin1_void1,
                     pin1_fuel=pin1_fuel,
                     pin1_void2=pin1_void2,
                     pin1_clad=pin1_clad,
                     pin2_termfuel=pin2_termfuel,
                     pin2_clad=pin2_clad, )
            p.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = PinsForm()

    return render(request, 'pins.html', {'form': form})

#########################################################
#########################ZONES###########################

def get_zones(request):
    if request.method == "POST":
        form = ZonesForm(request.POST)
        if form.is_valid():
            zone1_x = form.cleaned_data['zone1_x']
            zone1_y = form.cleaned_data['zone1_y']
            zone1_d = form.cleaned_data['zone1_d']

            zone2_x = form.cleaned_data['zone2_x']
            zone2_y = form.cleaned_data['zone2_y']
            zone2_d = form.cleaned_data['zone2_d']

            zone3_x = form.cleaned_data['zone3_x']
            zone3_y = form.cleaned_data['zone3_y']
            zone3_d = form.cleaned_data['zone3_d']

            zone4_x = form.cleaned_data['zone4_x']
            zone4_y = form.cleaned_data['zone4_y']
            zone4_d = form.cleaned_data['zone4_d']

            z = Zones(zone1_x=zone1_x,
                      zone1_y=zone1_y,
                      zone1_d=zone1_d,
                      zone2_x=zone2_x,
                      zone2_y=zone2_y,
                      zone2_d=zone2_d,
                      zone3_x=zone3_x,
                      zone3_y=zone3_y,
                      zone3_d=zone3_d,
                      zone4_x=zone4_x,
                      zone4_y=zone4_y,
                      zone4_d=zone4_d,
                     )
            z.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ZonesForm()

    return render(request, 'zones.html', {'form': form})

#########################################################
#########################INDEX###########################

def index(request):
    return render(request, 'index.html')