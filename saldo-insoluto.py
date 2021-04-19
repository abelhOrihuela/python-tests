
import math

total_payments = 12
interest = .28
loan = 250000


def calculate():
    ac = math.floor(loan / total_payments)
    payments = []
    pending_ammount = loan
    payed_ammount = 0


    for i in range(total_payments):
        interest_payment = pending_ammount * interest
        pending_ammount = math.floor(pending_ammount - ac)
        payment = ac + interest_payment

        payed_ammount = payed_ammount + payment

        # balance = loan + interest_payment - payed_ammount
        print("==============================")
        print("Número de pago: {}".format(i))
        print("Saldo pendiente: {}".format(pending_ammount))
        print("Saldo pagado: {}".format(payed_ammount))
        print("Interes: {}".format(interest_payment))
        print("AC: {}".format(ac))
        print("Boleta: {}".format(payment))
        # print("Insoluto: {}".format(balance))
  

calculate()