import hardwareSet

hwSet1=hardwareSet.HWSet(250)

print("Total capacity of units",hwSet1.get_capacity())
print("Total number of available units", hwSet1.get_availability())

test=[20,300]

for i in test:
    err=hwSet1.check_out(i)
    if (err==0):
        print("Number of units after checking out",i, "units :",hwSet1.get_availability())
        print("Number of total checked out units", hwSet1.get_checkedout_qty())
    else:
        print("Number of units after checking out",i, "units :",hwSet1.get_availability())
        print("Number of total checked out units", hwSet1.get_checkedout_qty())
        print("Error: Could not check out",hwSet1.error_mar," number of units")
    
hwSet1.check_in(180)
print("Number of units after checking in 180 units :",hwSet1.get_availability())    
