
class HWSet(object):
    def __init__(self,units):
        self.capacity=units
        self.available=self.capacity
        self.used=0

    def get_availability(self):
        return self.available

    def get_capacity(self):
        return self.capacity
    
    def check_out(self,checkout_units):
        if checkout_units>self.available:
            self.used=self.capacity
            #self.available=0   ###Error with code?? Ask and verify?
            self.error_checkout=-1
            #self.checkout_units=self.capacity   ###It should be checkedout
            self.checkout_units=self.available
            self.error_mar=checkout_units-self.available
            self.available=0

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
        return self.checkout_units 

    

