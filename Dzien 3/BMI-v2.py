print('##########-KALKULATOR BMI-###########')
wzrost = input('podaj swoj wzrost w m ')
masa = input('podaj ile wazysz w kg ')
BMI=round(int(masa) / float(wzrost) **2)
print("Twoje BMI to:" + BMI)
if BMI < 18:
    print("niedowaga")
    elif BMI < 25
    print("ok")
    elif BMI < 30
    print ("nadwaga")
    else  print ("otyłość")


    #16 - 18 niedowaga
    #19 - 25  ok
    #26 - 30 nadwaga
    #31 - 40 otylosc