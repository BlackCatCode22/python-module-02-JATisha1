def computepay(hours, rate) :
    print("In computepay", hours, rate)
    if hours>40:
        reg = rate * hours
        otp = (hours - 40) * (rate * 1.5)
        pay = reg + otp
    else:
        xp=  hours * rate
    print("Returning", xp)
    return pay

sh= input("Enter Hours :")
sr= input("Enter Rate: ")
fh=float(sh)
fr= float(sr)

   
xp = computepay(fh, fr)

print("Pay: ", xp)