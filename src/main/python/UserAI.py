# Tylor Lehman
# BatPi
# UserAI.py


# Initial AI for BatPi. Will try to go forward until there is something 
# 500 units in front of it.

#from PiDrive import PiDrive

def UserAI():
   #motor = PiDrive()
   #sensor= fullsweep()
   #envmap=sensor.sweep()
   #front = len(envmap)/2
   stepcount = 0 # How far user has travelled thus far.
   command=input("What should I do? (w,a,s,d,x,q)")
   while(command==("w" or "a" or "s" or "d" or "x")):
      if command=="w":
         print "w"
         #motor.forward()
      elif command=="a":
         print "a"
         #motor.turnLeft()
      elif command=="s":
         print "s"
         #motor.reverse()
      elif command=="d":
         print "d"
         #motor.turnRight()
      elif command=="x":
         print "x"
         #envmap=sensor.sweep()         
      stepcount=stepcount+1

   print "either that was an invalid command, or you are done!"
   print "I performed "+stepcount+" actions!"

UserAI()
