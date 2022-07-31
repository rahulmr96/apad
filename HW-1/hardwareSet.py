
<<<<<<< HEAD
class HWSet(object): #####Class HW set which initializes the 
    def __init__(self,units): ####Initalizes the capacity, available and used
=======
class HWSet(object):
    def __init__(self,units):
>>>>>>> f44757c9e693a957f8e2ba5fbe821bff4e72b41c
        self.capacity=units
        self.available=self.capacity
        self.used=0

<<<<<<< HEAD
    def get_availability(self):  ###Returns the available quantity in stock
        return self.available

    def get_capacity(self):###Returns the initial capacity that was declared at __init__
        return self.capacity
    
    def check_out(self,checkout_units):   #####Checkouts the quantity mentioned by the user. 
        if checkout_units>self.available:  ###If checkout units is greater than the existing quantity, it allocates all remaining resources
            self.used=self.capacity
            self.available=0   
            self.checkout_units=self.capacity   
            return -1                       #####Returns an error code of -1
        else:                               ###Subtracting checkout units from available units
            self.available-=checkout_units
            self.used+=checkout_units       
            self.checkout_units=checkout_units
            return 0                        ####Return 0 which tells it the checkout hapened properly

    def check_in(self,checkin_units):       ####Checks in resources to the available pool 
        self.available+=checkin_units

    def get_checkedout_qty(self):           ###Indicates the number of units that was checked out
=======
    def get_availability(self):
        return self.available

    def get_capacity(self):
        return self.capacity
    
    def check_out(self,checkout_units):
        if checkout_units>self.available:
            self.error_mar=checkout_units-self.available
            self.used=self.capacity
            self.available=0   ###Error with code?? Ask and verify?
            self.error_checkout=-1
            self.checkout_units=self.capacity   ###It should be checkedout

            
            return self.error_checkout
        else:
            self.available-=checkout_units
            self.used+=checkout_units
            self.checkout_units=checkout_units
            self.error_checkout=0
            return self.error_checkout

    def check_in(self,checkin_units):
        self.available+=checkin_units
        self.capacity=self.available+self.used

    def get_checkedout_qty(self):
>>>>>>> f44757c9e693a957f8e2ba5fbe821bff4e72b41c
        return self.checkout_units 

    

