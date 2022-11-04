from pickle import TRUE
import time
from time import sleep
import pyfirmata
from pyfirmata import Arduino, SERVO

board = pyfirmata.Arduino('COM4')
board.digital[7].mode = SERVO
board.digital[12].mode = SERVO
board.digital[11].mode = SERVO 
board.digital[10].mode = SERVO
board.digital[9].mode = SERVO
board.digital[8].mode = SERVO


def newfunc(te):
    if te =="":
    
        print("Didn't find any String in File")
        exit
    else:
        print(te)
        def rotateServo(pin, angle):
            board.digital[pin].write(angle)
            sleep
        
    
    while TRUE:
        for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    rotateServo(10,i)      
                    rotateServo(9,i)      
                    rotateServo(8,i)      
                    time.sleep(.2)  
        
        for cha in te :
            char=ord(cha)
            
            if (char==46):
                return
                

            
               
               
            if char >=48 and char<=57:
                 print("This is number")
                 for i in range(0,90,+80):
                    rotateServo(12,i)      
                    rotateServo(10,i)      
                    rotateServo(9,i)      
                    rotateServo(8,i)      
                    time.sleep(.2)   
                    
            if char>=65 and char<=91:
                 print("capital ")
                 for i in range(0,90,+80):
                    rotateServo(8,i) 
                    time.sleep(.2)
                
            if char == 32:
                 print('space')
            
            elif char == 69 or char == 101 or char == 53: # E e 5
                 print(" e / 5 ")
                 for i in range(0,90,+80):
                    rotateServo(7,i)
                    rotateServo(10,i)
                    sleep(.2)
        
            elif char == 84 or char == 116: # T t 
                print(" t ")
                for i in range(0,90,+80):
                    rotateServo(12,i)
                    rotateServo(11,i)
                    rotateServo(10,i)
                    rotateServo(9,i)
                    sleep(.2)			

            elif char == 65 or char == 97 or char == 49: # a A 49
                print(" a / 1 ")
                for i in range(0,90,+80):
                    rotateServo(7,i)
                    sleep(.2) 
                    
            elif char == 73 or char == 105 or char == 57: # I i 9 3
                print(" i ")
                for i in range(0,90,+80):
                    rotateServo(12,i)
                    rotateServo(11,i)
                    sleep(.2)        
            elif char == 78 or char == 110 : #N 4
                print(" n ")
                for i in range(0,90,+80):
                    rotateServo(7,i)
                    rotateServo(12,i)
                    rotateServo(10,i)
                    rotateServo(9,i)
                    sleep(.2)
            elif char == 79 or char == 111 : #o 5
                print(" o ")
                for i in range(0,90,+80):
                    rotateServo(7,i)
                    rotateServo(10,i)
                    rotateServo(9,i)
                    sleep(.2)      
            elif char == 83 or char == 115 or char == 53: #s 6
                print(" s / ")
                for i in range(0,90,+80):
                    rotateServo(12,i)
                    rotateServo(11,i)
                    rotateServo(9,i)
                    sleep(.2)       
            elif char == 72 or char == 104 or char == 56: # h 8
                print(" h ")
                for i in range(0,90,+80):
                    rotateServo(7,i)
                    rotateServo(11,i)
                    rotateServo(10,i)
                    sleep(.2)
            elif char == 82 or char == 114 : #r
                print(" r ")
                for i in range(0,90,+80):
                    rotateServo(7,i)
                    rotateServo(11,i)
                    rotateServo(10,i)
                    rotateServo(9,i)
                    sleep(.2)

            elif char == 68 or char == 100 or char == 52: # d
                print(" d ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(10,i)  
                    sleep(.2)    
                
            elif char == 76 or char == 108 : #L: #11
                print(" l ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(11,i)      
                    rotateServo(9,i)     
                    sleep(.2) 
                
            elif char == 85 or char == 117 : # u
                print(" u ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(9,i)     
                    rotateServo(8,i)     
                    sleep(.2) 

            elif char == 67 or char == 99 or char == 51: # c
                print(" c ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)    
                    sleep(.2)      
                        
            elif char == 77 or char == 109 : # m
                print(" m ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(9,i)      
                    sleep(.2)    
                            
            elif char == 70 or char == 102 or char == 54: # e E 5: #f
                print(" f ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    sleep(.2)
                            
            elif char == 87 or char == 119: # e E 5: #w
                print(" w ")
                for i in range(0,90,+80):
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    rotateServo(10,i)      
                    rotateServo(8,i)      
                    sleep(.2)
                                    
            elif char == 89 or char == 121 : # e E 5: #y
                print(" y ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(10,i)      
                    rotateServo(9,i)      
                    rotateServo(8,i)      
                    sleep(.2)
                        
            elif char == 71 or char == 103 or char == 55: # g
                print(" g ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    rotateServo(10,i)      
                    sleep(.2)
                                        
            elif char == 82 or char == 112: # e E 5: #p
                print(" p ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    rotateServo(9,i)      
                    sleep(.2)

            elif char == 66 or char == 98 or char == 50: #20
                print(" b ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(11,i)    
                    sleep(.2)  
                
            elif char == 86 or char == 118: # e E 5: #v
                print(" v ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(11,i)      
                    rotateServo(9,i)       
                    rotateServo(8,i)      
                    sleep(.2)
                                        
            elif char == 75 or char == 107 : # e E 5: #22
                print(" K")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(9,i)      
                    sleep(.2)
                                        
            elif char == 81 or char == 17 : # e E 5: #q
                print(" q ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    rotateServo(10,i)      
                    rotateServo(9,i) 
                    sleep(.2)     
                        
            elif char == 74 or char == 106 or char == 48: # e E 5: #j
                print(" j ")
                for i in range(0,90,+80):
                    rotateServo(12,i)      
                    rotateServo(11,i)      
                    rotateServo(10,i)      
                    sleep(.2)
                        
            elif char == 88 or char == 120: # e E 5: #x
                print(" x ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(12,i)      
                    rotateServo(9,i)      
                    rotateServo(8,i)      
                    sleep(.2)
                        
            elif char == 90 or char == 122 : # e E 5: #z
                print(" z ")
                for i in range(0,90,+80):
                    rotateServo(7,i)      
                    rotateServo(10,i)      
                    rotateServo(9,i)      
                    rotateServo(8,i)      
                    sleep(.2)
                    
