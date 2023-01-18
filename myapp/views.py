from django.shortcuts import render,redirect
import json
from .forms import *
from .models import *
from django.core import serializers
from django.contrib import messages
import ast 
# https://stackoverflow.com/questions/37840839/get-json-representation-of-django-model
#

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }



json_dict = {'wifi':'','date_time':'','lockout':'','Electrical Config':''}
def index(request):
    
    wifi_form = wifiForm(request.POST)
    datetime_form = DateTimeForm(request.POST)
    lock = LockoutForm(request.POST)
    ecform = EcForm(request.POST)

    if request.method == 'POST' and 'wifi' in request.POST:
        if wifi_form.is_valid():
            _ssid = wifi_form.cleaned_data['ssid']
            _password = wifi_form.cleaned_data['password']
            # print("ssid:",_ssid)
            # wifi_form.save()
            t = WifiDetails.objects.get(id=1)
            t.ssid = _ssid  # change SSID field
            t.password = _password  # change SSID field
            t.save() # this will update only
            val1 = serializers.serialize("json", WifiDetails.objects.all())
            # print(val1)
            res = ast.literal_eval(val1)
            json_dict['wifi'] = res
            json_object = json.dumps(json_dict, indent=4)

            # Writing to configuration.json
            with open("configuration.json", "w") as outfile:
                outfile.write(json_object)
            messages.success(request,'Wifi Details Saved Successfully')
        else:
            # print(wifi_form['password'].errors)
            messages.error(request,wifi_form['password'].errors)
            return redirect('/')

    if request.method == 'POST' and 'datetime' in request.POST: 
        if datetime_form.is_valid():
                date_field = datetime_form.cleaned_data['_date']
                time_field = datetime_form.cleaned_data['_time']
                
                # _am_pm = datetime_form.cleaned_data['am_pm']
                _tz = datetime_form.cleaned_data['timezone']
                # datetime_form.save()
                t = DateTimeDetails.objects.get(id=1)
                t._date = date_field  # change SSID field
                t._time = time_field  # change SSID field
                # t.am_pm = _am_pm
                t.timezone = _tz
                messages.success(request,'Date Time Saved Succesfully')
                
                t.save()
                val2 = serializers.serialize("json", DateTimeDetails.objects.all())
                res = ast.literal_eval(val2)
                json_dict['date_time'] = res
                json_object = json.dumps(json_dict, indent=4)
                # Writing to configuration.json
                with open("configuration.json", "w") as outfile:
                    outfile.write(json_object)
                # print(json_dict)
                
    if request.method == 'POST' and 'lockout' in request.POST: 
        if lock.is_valid():
                weekday1 = int(lock.cleaned_data['weekday1'])
                weekday2 = int(lock.cleaned_data['weekday2'])
                weekend1 = int(lock.cleaned_data['weekend1'])
                weekend2 = int(lock.cleaned_data['weekend2'])
                if weekday1>23 or weekday1<0:

                    messages.error(request,'Weekday1 is either greater than 23 or less than 0')
                    return redirect('/')
                elif weekday2>23 or weekday2<0:

                    messages.error(request,'Weekday2 is either greater than 23 or less than 0')
                    return redirect('/')
                elif weekend2>23 or weekend2<0:

                    messages.error(request,'weekend2 is either greater than 23 or less than 0')
                    return redirect('/')
                elif weekend1>23 or weekend1<0:

                    messages.error(request,'weekend1 is either greater than 23 or less than 0')
                    return redirect('/')
                
                elif weekday1>weekday2:

                    messages.error(request,'Weekday From value should be less than To value ')
                    return redirect('/')
                
                elif weekend1>weekend2:

                    messages.error(request,'Weekend From value should be less than To value ')
                    return redirect('/')
                
                # elif weekend1.isnumeric()>23 or weekend1<0 weekend1>23 or weekend1<0:

                #     messages.error(request,'weekend1 is either greater than 23 or less than 0')
                #     return redirect('/')
                else:
                    t = lockoutDetails.objects.get(id=1)
                    t.weekday1 = weekday1
                    t.weekday2 = weekday2
                    t.weekend1 = weekend1
                    t.weekend2 = weekend2

                    t.save()
                    val3 = serializers.serialize("json", lockoutDetails.objects.all())
                    res = ast.literal_eval(val3)
                    json_dict['lockout'] = res
                    json_object = json.dumps(json_dict, indent=4)
                    # Writing to configuration.json
                    with open("configuration.json", "w") as outfile:
                        outfile.write(json_object)
                    # print(json_dict)

                # print("day1:",weekday1)
                # print("day2:",weekday2)
                # print("end1:",weekend1)
                # print("end2:",weekend2)

                
    if request.method == 'POST' and 'ec' in request.POST: 
        if ecform.is_valid():
                spr = ecform.cleaned_data['sensed_panel_rating']
                scr = ecform.cleaned_data['sensor_ct_rating']
                cba = ecform.cleaned_data['circuit_breaker_a']
                cbb = ecform.cleaned_data['circuit_breaker_b']
                _c1 = ecform.cleaned_data['c1']
                _cma1 = ecform.cleaned_data['max_amp1']
                _c1ab = ecform.cleaned_data['c1ab']
                _c2 = ecform.cleaned_data['c2']
                _cma2 = ecform.cleaned_data['max_amp2']
                _c2ab = ecform.cleaned_data['c2ab']
                _c3 = ecform.cleaned_data['c3']
                _cma3 = ecform.cleaned_data['max_amp3']
                _c3ab = ecform.cleaned_data['c3ab']
                _c4 = ecform.cleaned_data['c4']
                _cma4 = ecform.cleaned_data['max_amp4']
                _c4ab = ecform.cleaned_data['c4ab']

                if _cma1>80 or _cma1<8 or _cma2>80 or _cma2<8 or _cma3>80 or _cma3<8 or _cma4>80 or _cma4<8:

                    messages.error(request,'Value Should be between 8 to 80')
                    return redirect('/')
                else:
                
                    t = ECDetails.objects.get(id=1)
                    t.sensed_panel_rating = spr
                    t.sensor_ct_rating = scr
                    t.circuit_breaker_a = cba
                    t.circuit_breaker_b = cbb
                    t.c1 = _c1
                    t.c1ab = _c1ab
                    t.max_amp1 = _cma1
                    t.c2 = _c2
                    t.c2ab = _c2ab
                    t.max_amp2 = _cma2
                    t.c3 = _c3
                    t.max_amp3 = _cma3
                    t.c3ab = _c3ab
                    t.c4 = _c4
                    t.max_amp4 = _cma4
                    t.c4ab = _c4ab
                    t.save()
                    messages.success(request,'Value Saves be Successfully')

                val4 = serializers.serialize("json", ECDetails.objects.all())
                res = ast.literal_eval(val4)
                json_dict['Electrical Config'] = res
                
                # Serializing json
                json_object = json.dumps(json_dict, indent=4)
                
                # Writing to configuration.json
                with open("configuration.json", "w") as outfile:
                    outfile.write(json_object)
             
    else:
        wifi_form = wifiForm()
        datetime_form = DateTimeForm()
        lock = LockoutForm()
        ecform = EcForm()
        # ccaform = CcAssignmentForm()

        return render(request,'form.html',{'wifi_form': wifi_form,'datetime_form':datetime_form,'lock':lock,'ecform':ecform})
    return render(request,'form.html',{'wifi_form': wifi_form,'datetime_form':datetime_form,'lock':lock,'ecform':ecform})
    

