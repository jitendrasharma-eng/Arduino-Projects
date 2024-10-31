/*******Creator JITENDRA SHARMA******/
import cv2
import numpy as np
import serial
import time

# Set up the serial connection (adjust the COM port and baud rate as necessary)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Use '/dev/ttyUSB0' on Linux
time.sleep(2)  # Wait for serial connection to initialize

lowerG = np.array([35, 100, 100])  # Lower bound for green
upperG = np.array([85, 255, 255])

lowerR0 = np.array([0,190,120])
upperR0 = np.array([5,255,180])
lowerR1 = np.array([175, 190, 120])
upperR1 = np.array([180, 255, 180])

lowerY = np.array([20, 100, 100])
upperY = np.array([30, 255, 255])

lowerB = np.array([88, 176, 70])
upperB = np.array([133, 255, 255])

def yellow(img):
  global yellowFlage
  imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(imghsv,lowerY,upperY)
  _,mask1 = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
  cnts,_ =cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  a=[]
  yellowFlage =False
  for c in cnts:
    x=600
    if cv2.contourArea(c)>x:
      #cv2.drawContours(img,[c], -1, (255, 0, 0), 2)
      x,y,w,h=cv2.boundingRect(c)
      a.append(x)
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
      x1 = int(x+x+w)//2
      y1 = int (y+y+h)//2
      cv2.circle(img,(x1,y1),4,(255,0,255),-2)
      cv2.putText(img,("yellow"),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
      yellowFlage=True
  p=len(a)  
  cv2.putText(img,("yellow"+str(p)),(111,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)   
     
      
def red(img):
  global redFlage
  imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  mask0 = cv2.inRange(imghsv,lowerR0,upperR0)
  mask1 = cv2.inRange(imghsv,lowerR1,upperR1)
  mask=mask0+mask1
  _,mask2 = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
  cnts,_ =cv2.findContours(mask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  a=[]
  redFlage=False
  for c in cnts:
    x=600
    if cv2.contourArea(c)>x:
      #cv2.drawContours(img,[c], -1, (255, 0, 0), 2)
      x,y,w,h=cv2.boundingRect(c)
      a.append(x)
      x1 = int(x+x+w)//2
      y1 = int (y+y+h)//2
      cv2.circle(img,(x1,y1),4,(255,0,255),-2)
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
      cv2.putText(img,("red"),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
      redFlage=True
  p=len(a)  
  cv2.putText(img,("red"+str(p)),(111,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)   
     
      
def blue(img):
  global blueFlage
  imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(imghsv,lowerB,upperB)
  _,mask1 = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
  cnts,_ =cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  a=[]
  blueFlage=False
  for c in cnts:
    x=600
    if cv2.contourArea(c)>x:
      #cv2.drawContours(img,[c], -1, (255, 0, 0), 2)
      x,y,w,h=cv2.boundingRect(c)
      a.append(x)
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      #print(x)
      #print(w)
      x1 = int(x+x+w)//2
      y1 = int(y+y+w)//2
      cv2.circle(img,(x1,y1),4,(255,0,255),-2)
      cv2.putText(img,("Blue"),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
      blueFlage=True
  p=len(a)  
  cv2.putText(img,("blue"+str(p)),(111,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)   
         
# Initialize flags
yellowFlage = False
redFlage = False
blueFlage = False

cap = cv2.VideoCapture(0)
while True:
  sucess, img = cap.read()
  img = cv2.resize(img,(640,480))
  yellow(img)
  red(img)
  blue(img)
  
 
  if yellowFlage and blueFlage and redFlage:
    arduino.write(b'7')
    print("ybr")
  elif yellowFlage and redFlage:
    arduino.write(b'6')
    print("yr")
  elif yellowFlage and blueFlage:
    arduino.write(b'5')
    print("yb")
  elif redFlage and blueFlage:
    arduino.write(b'4') 
    print("rb")   
  elif yellowFlage:
    print("Y=",yellowFlage)
    arduino.write(b'3')
  elif redFlage:
    print("R=",redFlage) 
    arduino.write(b'2')
  elif blueFlage:
    print("B=",blueFlage)
    arduino.write(b'1')

  else:
    arduino.write(b'0')
    print("nill")
     
    
  cv2.imshow("output",img)    
  if cv2.waitKey(1)&0xFF==ord('q'):
    break
    
cap.release()
cv2.destroyAllWindows()