
class my1stClass:
    def printMe( self, x ):
        print("x=", x)

class myChildClass(my1stClass):
    def printMe( self, x ):
        print("X => ", x)

monObjet = myChildClass()
monObjet.printMe( 'hello' ) 
