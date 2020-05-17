#funkcja oblicza BMI

def bmi_counter(masa, wzrost):
    BMI=round(int(masa) / float(wzrost) **2)
    print("Twoje BMI to:" + BMI)

#Funkcja porównuje wyniki
def bmi_result(BMI):
    if BMI < 18:
        print("niedowaga")
    elif BMI < 25:
        print("ok")
    elif BMI < 30:
        print ("nadwaga")
    else:
        1,print ("otyłość")

#kod
print('##########-KALKULATOR BMI-###########')
wzrost = input('podaj swoj wzrost w m ')
masa = input('podaj ile wazysz w kg ')
result = bmi_counter(masa, wzrost)
bmi_result(result)
