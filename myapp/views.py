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
    
    Wifi_Details = WifiDetails.objects.all()
    lockout_Details = lockoutDetails.objects.all()
    EC_Details = ECDetails.objects.all()



    choice1 = time_stamp
    choice2 = channel
    choice3 = sensed_panel_rating_choice
    choice4 = circuit_breaker
    choice5 = TIME_ZONE_CHOICES



    wifi_form = wifiForm(request.POST)
    datetime_form = DateTimeForm(request.POST)
    lock = LockoutForm(request.POST)
    # form = LockoutForm(initial={'weekday2': 12})
    ecform = EcForm(request.POST)


    #----------------Custom Wi-Fi SSID--------------------- 

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


    #----------------Date and Time---------------------------

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


    #----------------Date and Time---------------------------      
          
    if request.method == 'POST' and 'lockout' in request.POST: 
        if lock.is_valid():
                    # int(lock.cleaned_data['weekday1'])
                # weekday1 = lock.cleaned_data.get('weekday1')
                weekday1 = lock.cleaned_data.get('weekday1') if lock.cleaned_data.get('weekday1') else 11
                # print('-------------',lock.cleaned_data)
                # weekday2 = lock.cleaned_data.get('weekday2')
                weekday2 = lock.cleaned_data.get('weekday2') if lock.cleaned_data.get('weekday2') else 12
                # print('----------->',weekday2)
                # weekend1 = lock.cleaned_data.get('weekend1')
                weekend1 = lock.cleaned_data.get('weekend1') if lock.cleaned_data.get('weekend1') else 11
                # weekend2 = lock.cleaned_data.get('weekend2')
                weekend2 = lock.cleaned_data.get('weekend2') if lock.cleaned_data.get('weekend2') else 12

                # if not weekday2:
                #     weekday2 = 12
                #     print(weekday2)
                # if not weekend2:
                #     weekend2 = 12
                #     print(weekend2)
                
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
                    # t = lockoutDetails.objects.filter(id=1).update(**request.data)
                    t.weekday1 = weekday1
                    t.weekday2 = weekday2
                    t.weekend1 = weekend1
                    t.weekend2 = weekend2

                    # print('=========data received===========')

                    messages.success(request,'Lockout Details Saved Succesfully')


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


    #----------------Electric Configuration--------------
                
    if request.method == 'POST' and 'ec' in request.POST: 
        if ecform.is_valid():
                spr = ecform.cleaned_data['sensed_panel_rating']
                # spr = ecform.cleaned_data.get('sensed_panel_rating') if ecform.cleaned_data.get('sensed_panel_rating') else 50
                # print('------------------',ecform.cleaned_data)
                scr = ecform.cleaned_data['sensor_ct_rating']
                # scr = ecform.cleaned_data.get('sensor_ct_rating') if ecform.cleaned_data.get('sensor_ct_rating') else 50
                cba = ecform.cleaned_data['circuit_breaker_a']
                # cba = ecform.cleaned_data.get('circuit_breaker_a') if ecform.cleaned_data.get('circuit_breaker_a') else 15
                cbb = ecform.cleaned_data['circuit_breaker_b']
                # cbb = ecform.cleaned_data.get('circuit_breaker_b') if ecform.cleaned_data.get('circuit_breaker_b') else 0
                # _c1 = ecform.cleaned_data['c1']
                _c1 = ecform.cleaned_data.get('c1') if ecform.cleaned_data.get('c1') else 12
                # _cma1 = ecform.cleaned_data['max_amp1']
                _cma1 = ecform.cleaned_data.get('max_amp1') if ecform.cleaned_data.get('max_amp1') else 12
                _c1ab = ecform.cleaned_data['c1ab']
                # _c1ab = ecform.cleaned_data.get('c1ab') if ecform.cleaned_data.get('c1ab') else 'A'
                # _c2 = ecform.cleaned_data['c2']
                _c2 = ecform.cleaned_data.get('c2') if ecform.cleaned_data.get('c2') else 12
                # _cma2 = ecform.cleaned_data['max_amp2']
                _cma2 = ecform.cleaned_data.get('max_amp2') if ecform.cleaned_data.get('max_amp2') else 12
                _c2ab = ecform.cleaned_data['c2ab']
                # _c2ab = ecform.cleaned_data.get('c2ab') if ecform.cleaned_data.get('c2ab') else 'A'
                # _c3 = ecform.cleaned_data['c3']
                _c3 = ecform.cleaned_data.get('c3') if ecform.cleaned_data.get('c3') else 12
                # _cma3 = ecform.cleaned_data['max_amp3']
                _cma3 = ecform.cleaned_data.get('max_amp3') if ecform.cleaned_data.get('max_amp3') else 12
                _c3ab = ecform.cleaned_data['c3ab']
                # _c3ab = ecform.cleaned_data.get('c3ab') if ecform.cleaned_data.get('c3ab') else 'A'
                # _c4 = ecform.cleaned_data['c4']
                _c4 = ecform.cleaned_data.get('c4') if ecform.cleaned_data.get('c4') else 12
                # _cma4 = ecform.cleaned_data['max_amp4']
                _cma4 = ecform.cleaned_data.get('max_amp4') if ecform.cleaned_data.get('max_amp4') else 12
                _c4ab = ecform.cleaned_data['c4ab']
                # _c4ab = ecform.cleaned_data.get('c4ab') if ecform.cleaned_data.get('c4ab') else 'A'

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
                    messages.success(request,'Value Saved Successfully')

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

        return render(request,'form.html',{'wifi_form': wifi_form,'datetime_form':datetime_form,'lock':lock,'ecform':ecform, 'choice1':choice1, 'choice2':choice2, 'choice3':choice3, 'choice4':choice4, 'choice5':choice5, 'Wifi_Details':Wifi_Details,'lockout_Details':lockout_Details,'EC_Details':EC_Details})
    return render(request,'form.html',{'wifi_form': wifi_form,'datetime_form':datetime_form,'lock':lock,'ecform':ecform, 'choice1':choice1, 'choice2':choice2, 'choice3':choice3, 'choice4':choice4, 'choice5':choice5, 'Wifi_Details':Wifi_Details,'lockout_Details':lockout_Details,'EC_Details':EC_Details})
    

