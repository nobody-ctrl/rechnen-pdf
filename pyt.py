from fpdf import FPDF
import random

class PDF(FPDF):
     def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="Aufgaben fuer Donnerstag, 29.04", border=0)
     def texts(self,name, abstand, links):
        self.set_xy(10.0+links,20.0+abstand)    
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,name)

pdf = PDF()
pdf.add_page()
pdf.titles()
x=1
abstand = 10
while (x<25):
     zahl = str(random.randint(1, 500)) +"+"+str(random.randint(1, 500)) +"="
     pdf.texts(zahl, abstand, 0)
     abstand +=10
     x+=1
abstand = 10
x=1
while (x<25):
     zahl = str(random.randint(1, 500)) +"-"+str(random.randint(1, 500)) +"="
     pdf.texts(zahl, abstand, 40)
     abstand +=10
     x+=1
abstand = 10
x=1
while (x<25):
     zahl = str(random.randint(1, 50)) +" x "+str(random.randint(1, 50)) +"="
     pdf.texts(zahl, abstand, 80)
     abstand +=10
     x+=1
abstand = 10
x=1
while (x<25):
     first = random.randint(1, 20)
     second = random.randint(1, 20)
     third = first*second
     zahl = str(third) +" : "+str(first) +"="
     pdf.texts(zahl, abstand, 120)
     abstand +=10
     x+=1
pdf.output('Rechnen, datum.pdf','F')
