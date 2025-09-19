rating=float(input('Enter a Decimal Number:'))
if rating>=4.5:
    print('ExtraOrdinary')
elif rating>=4.0:
    print('Excellent')
elif rating>=3.0:
    print('Good')
elif rating>=2.0:
    print('Fair')
else:
    print('Poor')