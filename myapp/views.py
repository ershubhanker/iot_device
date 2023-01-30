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
    lockout_Details = tou_details.objects.all()
    EC_Details = ECDetails.objects.all()
    Date_and_Time = DateTimeDetails.objects.all()


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
            # _ssid = wifi_form.cleaned_data['ssid']
            _ssid = wifi_form.cleaned_data.get('ssid') if wifi_form.cleaned_data.get('ssid') else 'varian_secure'
            # _password = wifi_form.cleaned_data['password']
            _password = wifi_form.cleaned_data.get('password') if wifi_form.cleaned_data.get('password') else 'varian'
            # print("ssid:",_ssid)
            # wifi_form.save()

            #password valiadtion
            
            # ---------------
            # if len(_password)<8:
            #     messages.error(request,'The length be equal to or above 8 characters')
            #     return redirect('/')


            t = WifiDetails.objects.get(id=1)
            t.ssid = _ssid  # change SSID field
            t.password = _password  # change SSID field
            t.save() # this will update only
            messages.success(request,'Wi-Fi settings saved')
            
            val1 = serializers.serialize("json", WifiDetails.objects.all())
            # print('---------------',val1)
            res = ast.literal_eval(val1)
            json_dict['wifi'] = res
            json_object = json.dumps(json_dict, indent=4)

            # Writing to configuration.json
            with open("configuration.json", "w") as outfile:
                outfile.write(json_object)
            # messages.success(request,'Wi-Fi settings saved')
        else:
            # print(wifi_form['password'].errors)
            
            messages.error(request,wifi_form['password'].errors)
        #     return redirect('/')


    #----------------Date and Time---------------------------

    if request.method == 'POST' and 'datetime' in request.POST: 
        if datetime_form.is_valid():
                date_field = datetime_form.cleaned_data['date']
                
                time_field = datetime_form.cleaned_data['local_time']
                
                # _am_pm = datetime_form.cleaned_data['am_pm']
                _tz = datetime_form.cleaned_data['timezone']
                # datetime_form.save()
                t = DateTimeDetails.objects.get(id=1)
                t.date = date_field  # change SSID field
                t.local_time = time_field  # change SSID field
                # t.am_pm = _am_pm
                t.timezone = _tz
                messages.success(request,'Date and Time saved')
                
                t.save()
                val2 = serializers.serialize("json", DateTimeDetails.objects.all())
                res = ast.literal_eval(val2)
                json_dict['date_time'] = res
                json_object = json.dumps(json_dict, indent=4)
                # Writing to configuration.json
                with open("configuration.json", "w") as outfile:
                    outfile.write(json_object)
                # print(json_dict)
        else:
            messages.error(request,'Make sure select every field')


    #----------------lockoutDetails---------------------------      
          
    if request.method == 'POST' and 'lockout' in request.POST: 
        if lock.is_valid():
                    # int(lock.cleaned_data['weekday1'])
                # weekday1 = lock.cleaned_data.get('weekday1')
                weekday_from_1 = lock.cleaned_data.get('weekday_from_1') if lock.cleaned_data.get('weekday_from_1') else 11
                weekday_to_1 = lock.cleaned_data.get('weekday_to_1') if lock.cleaned_data.get('weekday_to_1') else 12
                weekday_from_2 = lock.cleaned_data.get('weekday_from_2') if lock.cleaned_data.get('weekday_from_2') else 11
                weekday_to_2 = lock.cleaned_data.get('weekday_to_2') if lock.cleaned_data.get('weekday_to_2') else 12

                weekend_from_1 = lock.cleaned_data.get('weekend_from_1') if lock.cleaned_data.get('weekend_from_1') else 11
                weekend_to_1 = lock.cleaned_data.get('weekend_to_1') if lock.cleaned_data.get('weekend_to_1') else 12
                weekend_from_2 = lock.cleaned_data.get('weekend_from_2') if lock.cleaned_data.get('weekend_from_2') else 11
                weekend_to_2 = lock.cleaned_data.get('weekend_to_2') if lock.cleaned_data.get('weekend_to_2') else 12

                
                if (weekday_from_1>23 or weekday_from_1<0) or (weekday_to_1>23 or weekday_to_1<0) or (weekday_from_2>23 or weekday_from_2<0) or (weekday_to_2>23 or weekday_to_2<0) :
                    messages.error(request,'Values must be between 0 and 23')
                    return redirect('/')

                elif (weekend_from_1>23 or weekend_from_1<0) or (weekend_to_1>23 or weekend_to_1<0) or (weekend_from_2>23 or weekend_from_2<0) or (weekend_to_2>23 or weekend_to_2<0):
                    messages.error(request,'Values must be between 0 and 23')
                    return redirect('/')

                elif weekday_from_1>weekday_to_1 or weekday_from_2>weekday_to_2:
                    messages.error(request,'From value must be less than To value')
                    return redirect('/')
                elif weekend_from_1>weekend_to_1 or weekend_from_2>weekend_to_2:
                    messages.error(request,'From value must be less than To value')
                    return redirect('/')
                # elif weekend1.isnumeric()>23 or weekend1<0 weekend1>23 or weekend1<0:

                #     messages.error(request,'weekend1 is either greater than 23 or less than 0')
                #     return redirect('/')
                else:
                    t = tou_details.objects.get(id=1)
                    # t = lockoutDetails.objects.filter(id=1).update(**request.data)
                    t.weekday_from_1 = weekday_from_1
                    t.weekday_to_1 = weekday_to_1
                    t.weekday_from_2 = weekday_from_2
                    t.weekday_to_2 = weekday_to_2

                    t.weekend_from_1 = weekend_from_1
                    t.weekend_to_1 = weekend_to_1
                    t.weekend_from_2 = weekend_from_2
                    t.weekend_to_2 = weekend_to_2

                    # print('=========data received===========')


                    messages.success(request,'Time-of-Use settings saved')


                    t.save()
                    val3 = serializers.serialize("json", tou_details.objects.all())
                    res = ast.literal_eval(val3)
                    json_dict['tou_hold'] = res
                    json_object = json.dumps(json_dict, indent=4)
                    # Writing to configuration.json
                    with open("configuration.json", "w") as outfile:
                        outfile.write(json_object)
                    # print(json_dict)


    #----------------Electric Configuration--------------
                
    if request.method == 'POST' and 'ec' in request.POST: 
        if ecform.is_valid():
                spr = ecform.cleaned_data['sensed_panel_rating']
                # spr = ecform.cleaned_data.get('sensed_panel_rating') if ecform.cleaned_data.get('sensed_panel_rating') else 100
                # print('------------------',ecform.cleaned_data)
                scr = ecform.cleaned_data['sensor_ct_rating']
                # scr = ecform.cleaned_data.get('sensor_ct_rating') if ecform.cleaned_data.get('sensor_ct_rating') else 50
                cba = ecform.cleaned_data['circuit_breaker_a']
                # cba = ecform.cleaned_data.get('circuit_breaker_a') if ecform.cleaned_data.get('circuit_breaker_a') else 15
                cbb = ecform.cleaned_data['circuit_breaker_b']
                # cbb = ecform.cleaned_data.get('circuit_breaker_b') if ecform.cleaned_data.get('circuit_breaker_b') else 0
                # _c1 = ecform.cleaned_data['c1']
                _c1 = ecform.cleaned_data.get('c1') if ecform.cleaned_data.get('c1') else ''
                # _cma1 = ecform.cleaned_data['max_amp1']
                _cma1 = ecform.cleaned_data.get('max_amp1') if ecform.cleaned_data.get('max_amp1') else 12
                c1_circuit = ecform.cleaned_data['c1_circuit']
                # _c1ab = ecform.cleaned_data.get('c1ab') if ecform.cleaned_data.get('c1ab') else 'A'
                # _c2 = ecform.cleaned_data['c2']
                _c2 = ecform.cleaned_data.get('c2') if ecform.cleaned_data.get('c2') else ''
                # _cma2 = ecform.cleaned_data['max_amp2']
                _cma2 = ecform.cleaned_data.get('max_amp2') if ecform.cleaned_data.get('max_amp2') else 12
                c2_circuit = ecform.cleaned_data['c2_circuit']
                # _c2ab = ecform.cleaned_data.get('c2ab') if ecform.cleaned_data.get('c2ab') else 'A'
                # _c3 = ecform.cleaned_data['c3']
                _c3 = ecform.cleaned_data.get('c3') if ecform.cleaned_data.get('c3') else ''
                # _cma3 = ecform.cleaned_data['max_amp3']
                _cma3 = ecform.cleaned_data.get('max_amp3') if ecform.cleaned_data.get('max_amp3') else 12
                c3_circuit = ecform.cleaned_data['c3_circuit']
                # _c3ab = ecform.cleaned_data.get('c3ab') if ecform.cleaned_data.get('c3ab') else 'A'
                # _c4 = ecform.cleaned_data['c4']
                _c4 = ecform.cleaned_data.get('c4') if ecform.cleaned_data.get('c4') else ''
                # _cma4 = ecform.cleaned_data['max_amp4']
                _cma4 = ecform.cleaned_data.get('max_amp4') if ecform.cleaned_data.get('max_amp4') else 12
                c4_circuit = ecform.cleaned_data['c4_circuit']
                # _c4ab = ecform.cleaned_data.get('c4ab') if ecform.cleaned_data.get('c4ab') else 'A'

                if _cma1>80 or _cma1<8 or _cma2>80 or _cma2<8 or _cma3>80 or _cma3<8 or _cma4>80 or _cma4<8:

                    messages.error(request,'Value must be between 8 and 80')
                    return redirect('/')
                else:
                
                    t = ECDetails.objects.get(id=1)
                    t.sensed_panel_rating = spr
                    t.sensor_ct_rating = scr
                    t.circuit_breaker_a = cba
                    t.circuit_breaker_b = cbb
                    t.c1 = _c1
                    t.c1_circuit = c1_circuit
                    t.max_amp1 = _cma1
                    t.c2 = _c2
                    t.c2_circuit = c2_circuit
                    t.max_amp2 = _cma2
                    t.c3 = _c3
                    t.max_amp3 = _cma3
                    t.c3_circuit = c3_circuit
                    t.c4 = _c4
                    t.max_amp4 = _cma4
                    t.c4_circuit = c4_circuit
                    t.save()
                    messages.success(request,'Electrical settings saved')

                val4 = serializers.serialize("json", ECDetails.objects.all())
                res = ast.literal_eval(val4)
                json_dict['Electrical'] = res
                
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

        return render(request,'form.html',{'wifi_form': wifi_form,'datetime_form':datetime_form,'lock':lock,'ecform':ecform, 'choice1':choice1, 'choice2':choice2, 'choice3':choice3, 'choice4':choice4, 'choice5':choice5, 'Wifi_Details':Wifi_Details,'lockout_Details':lockout_Details,'EC_Details':EC_Details,'Date_and_Time': Date_and_Time})
    return render(request,'form.html',{'wifi_form': wifi_form,'datetime_form':datetime_form,'lock':lock,'ecform':ecform, 'choice1':choice1, 'choice2':choice2, 'choice3':choice3, 'choice4':choice4, 'choice5':choice5, 'Wifi_Details':Wifi_Details,'lockout_Details':lockout_Details,'EC_Details':EC_Details,'Date_and_Time': Date_and_Time})
    

