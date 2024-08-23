class Item:
   def __init__(self,name,quantity,unitPrice,location): 
        self.name = name
        self.quantity= quantity
        self.unitPrice = unitPrice
        self.location = location
#----------------------------------------------------------------------------
#                          GENERALCATEGORIES
#----------------------------------------------------------------------------
class Instrument(Item):
    def __init__(self,name,quantity,price,description,location):
        super().__init__(name,quantity,price)
        self.name = name
        self.package = description

class Component(Item):
    def __init__(self,name,quantity,price,package,location):
        super().__init__(name,quantity,price,location)
        self.name = name
        self.package = package
#----------------------------------------------------------------------------
#                                  TRANSISTORS
#----------------------------------------------------------------------------

class BJT(Component):
    def __init__(self,name, quantity,price,package,type,Icmax, beta,location):
        super().__init__(name,quantity,price,package,location)
        self.type = type
        self.Icmax = Icmax
        self.beta = beta

class MOSFET(Component):
    def __init__(self,name, quantity,price,package,type,VT,location):
        super().__init__(name,quantity,price,package,location)
        self.type = type
        self.VT = VT
#----------------------------------------------------------------------------
#                                  DIODES
#----------------------------------------------------------------------------
class Diode(Component):
    def __init__(self,name, quantity,price,package,VD,location):
        super().__init__(name,quantity,price,package,location)
        self.VD = VD

class Led(Diode):
    def __init__(self,name, quantity,price,package,VD,color,location):
        super().__init__(name,quantity,price,package,VD,location)
        self.color=color

class Zener(Diode):
    def __init__(self,name, quantity,price,package,VD,location,VZ):
        super().__init__(name,quantity,price,package,VD,location)
        self.VZ = VZ

class GraetzBridge(Diode):
    def __init__(self,name, quantity,price,package,VD,location,Imax):
        super().__init__(name,quantity,price,package,VD,location)
        self.Imax = Imax
#----------------------------------------------------------------------------
#                        INTEGRATED CIRCUITS
#----------------------------------------------------------------------------
class IC(Component):
    def __init__(self,name, quantity,price,package,location, pinout):
        super().__init__(self,name, quantity,price,package,location)
        self.pinout=pinout

class OPAMP(IC):
    def __init__(self,name, quantity,price,package,location, pinout,CMRR):
        super().__init__(self,name, quantity,price,package,location, pinout)
        self.CMRR=CMRR

class Timer(IC):
    def __init__(self,name, quantity,price,package,location, pinout):
        super().__init__(self,name, quantity,price,package,location, pinout)

class Logic(IC):
    def __init__(self,name, quantity,price,package,location, pinout,logicFunciton):
        super().__init__(self,name, quantity,price,package,location, pinout)
        self.logicFunciton =logicFunciton

class Microcontroller(IC):
    def __init__(self,name, quantity,price,package,location, pinout,family,SRAM):
        super().__init__(self,name, quantity,price,package,location, pinout)
        self.family =family
        self.SRAM =SRAM

#----------------------------------------------------------------------------
#                        PASSIVE COMPONENTS
#----------------------------------------------------------------------------
class Resistor(Component):
    def __init__(self,name, quantity,price,package,R,location):
        super().__init__(self,name, quantity,price,package,location)
        self.R=R

class Capacitor(Component):
    def __init__(self,name, quantity,price,package,C,location):
        super().__init__(self,name, quantity,price,package,location)
        self.C=C

class Inductor(Component):
    def __init__(self,name, quantity,price,package,L,location):
        super().__init__(self,name, quantity,price,package,location)
        self.L=L