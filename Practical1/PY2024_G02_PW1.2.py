Hours = 50
Rate = 15
additional_rate = 1.25

if Hours > 40:
    total_rate = (40 * Rate) + (((Hours - 40)*Rate) * additional_rate)

else:
    total_rate = Hours * Rate

print(total_rate)    