# This is the driver code that uses the hardwareSet class that you are writing
import hardwareSet
# Create object hwSet1 of class hardwareSet with capacity of 250
hwSet1 = hardwareSet.HWSet(250)
# print initial capacity units of hardware set 1
print(f'Total capacity of units: {hwSet1.get_capacity()}')

# print number of available units of hardware set 1
print(f'Number of available units: {hwSet1.get_availability()}')

# Create a list of two test items
test = [20, 300]

# Run the test for all items in the test list
for i in test:
    err = hwSet1.check_out(i)

    # if function returns error code 0, it means we were able to check out the requested number of units,
    # else we were not able to check out the requested number of units
    if (err == 0):
        # print number of units available after checkout
        print(f'Number of units available after checking out {i} units: {hwSet1.get_availability()}')
        # print number of checked out units
        print(f'Number of total checked out units {hwSet1.get_checkedout_qty()}')
    else:
        # print number of units available after checkout
        print(f'Number of units available after checking out {i} units: {hwSet1.get_availability()}')
        # print number of checked out units
        print(f'Number of total checked out units {hwSet1.get_checkedout_qty()}')
        print('Could not check out requested number of units')

# check in 180 units
hwSet1.check_in(180)
# print number of units available after check in
<<<<<<< HEAD
print(f'Number of units available after checking in 180 units: {hwSet1.get_availability()}')
=======
print(f'Number of units available after checking in 180 units: {hwSet1.get_availability()}')
>>>>>>> f44757c9e693a957f8e2ba5fbe821bff4e72b41c
