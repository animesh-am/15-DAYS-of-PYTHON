mins = int(input('Enter minutes: '))

hour = 0
if mins > 60:
    hour = round(mins / 60)
    mins = mins - hour * 60
    if mins > 0:
        print(f"{hour} hours and {mins} minutes.")
    else:
        print(f"{hour} hours.")
else:
    print(f"{mins} minutes.")
