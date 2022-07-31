class HWSet(object): #####Class HW set which initializes the 
    def __init__(self,units): ####Initalizes the capacity, available and used
        self.capacity=units
        self.available=self.capacity
        self.used=0

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
        return self.checkout_units 

    

class DroneSet(HWSet):
    def __init__(self, units,payload):
        super().__init__(units)
        self.payload=payload

    def set_payload(self,units):
        self.payload=units

    def get_payload(self):
        return self.payload
    