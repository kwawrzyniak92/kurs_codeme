# Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45]
# itp. W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
import sys

list=[2,0,12.5,"kot",x]
for i in list:
    try:
        dzielenie = int(i)/10
    except ZeroDivisionError:
        print ('ZeroDivision')
    except ValueError:
        print ('Value')
    except Exception:
        print(sys.exc_info()[0])
    else:
        print("Wynik to ",dzielenie)
