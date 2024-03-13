def compute_wage(WorkHours, PayRate):
    if WorkHours > 40:
        regular_pay = 40 * PayRate
        
        overtime_hours = WorkHours - 40
        overtime_rate =  1.25 * PayRate
        overtime_pay = overtime_hours * overtime_rate
        
        total_pay = regular_pay + overtime_pay
    
    else:
        total_pay = WorkHours * PayRate
        
    
    return total_pay        

print("Your total wage is:", compute_wage(60, 20))
