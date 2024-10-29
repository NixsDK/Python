import turtle
import math

class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__moons = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                             width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)
        
    def addMoon(self, aMoon):
        self.__moons.append(aMoon)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)
            
    def showMoons(self):
        for aMoon in self.__moons:
            print(aMoon)
            
    def movePlanets(self):
        G = 0.1
        dt = 0.001
        
        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())

            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()
          
            r = math.sqrt(rX**2 + rY**2)

            accX = G * self.__theSun.getMass() * rX/r**3
            accY = G * self.__theSun.getMass() * rY/r**3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY) 
    
    def moveMoons(self):
        G = 0.1
        dt = 0.0001
        for moon in self.__moons:
            moon.moveTo(moon.getXPos() + dt * moon.getXVel(),
                    moon.getYPos() + dt * moon.getYVel())

            rX = moon.getPlanet().getXPos() - moon.getXPos()
            rY = moon.getPlanet().getYPos() - moon.getYPos()
            
            r = math.sqrt(rX**2 + rY**2)
            
            accX = G * moon.getPlanet().getMass() * rX/r**3
            accY = G * moon.getPlanet().getMass() * rY/r**3

            moon.setXVel(moon.getXVel() + dt * accX)
            moon.setYVel(moon.getYVel() + dt * accY)

    def freeze(self):
        self.__ssScreen.exitonclick() 
        
    def displayProximity(self):
        distances = []
        for planet in self.__planets:
            distance = planet.getDistance()
            distances.append((planet.getName(), distance))

        distances.append((self.__theSun.getName(), 0))

        distances.sort(key=lambda x: x[1])

        print("Order of proximity to the sun:")
        for name, _ in distances:
            print(name)

class Sun:
   def __init__(self, iName, iRad, iM, iTemp):
       self.__name = iName
       self.__radius = iRad
       self.__mass = iM
       self.__temp = iTemp
       self.__x = 0
       self.__y = 0

       self.__sTurtle = turtle.Turtle()
       self.__sTurtle.shape("circle")
       self.__sTurtle.color("yellow")
       self.__sTurtle.shapesize(self.__radius*0.001)

   def getName(self):
       return self.__name
   
   def getMass(self):
       return self.__mass

   #other methods as before

   def getXPos(self):
       return self.__x

   def getYPos(self):
       return self.__y

class Planet:
    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy 

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")
        self.__pTurtle.shapesize(self.__radius*.001)

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()

    def getDistance(self):
        return self.__distance

    def getName(self):
        return self.__name
    
    def getMass(self):
        return self.__mass
    
    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy 

class Moon:
    def __init__(self, iName, iPlanet, iRad, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__planet = iPlanet
        self.__radius = iRad
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy 
        
        self.__x = self.__planet.getXPos() + self.__distance
        self.__y = self.__planet.getYPos()
        self.__color = iC
        
        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")
        self.__pTurtle.shapesize(self.__radius*.01)
        
        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()
        
    def getPlanet(self):
        return self.__planet
        
    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy 
        
        
def createSSandAnimate():
   ss = SolarSystem(2, 2)

   sun = Sun("Sun", 5000, 10, 5800)
   ss.addSun(sun)

   mercury = Planet("Mercury", 190.5, 1000, .25, 0, 2, "blue")
   ss.addPlanet(mercury)

   earth = Planet("Earth", 470.5, 5000, 0.3, 0, 2.0, "green")
   ss.addPlanet(earth)

   mars = Planet("Mars", 500, 9000, 0.5, 0, 1.63, "red")
   ss.addPlanet(mars)

   jupiter = Planet("Jupiter", 1000, 49000, 0.7, 0, 1, "black")
   ss.addPlanet(jupiter)

   moon = Moon("Moon", earth, 30, 0.075, 0, 81.64, "purple")
   ss.addMoon(moon)
   
   ss.displayProximity()
   
   numTimePeriods = 2000
   for aMove in range(numTimePeriods):
        ss.moveMoons()
        ss.movePlanets()
   
   ss.freeze()

createSSandAnimate()
