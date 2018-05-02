import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm


path=os.getcwd()
def home(request):
    documents = Document.objects.all()
    if request.method == "POST" and borrar in request.POST:
        for document in documents:
            document.delete()
    return render(request, 'Texto/home.html', { 'documents': documents })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        file = (request.FILES, 'r')
        if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = DocumentForm()
    else:
        form = DocumentForm()
    return render(request, 'Texto/model_form_upload.html', {
        'form': form
    })


A=0
B=1
C=2
D=3
E=4
F=5
G=6
H=7
I=8
J=9
K=10
L=11
M=12
N=13
O=14
P=15
Q=16
R=17
S=18
T=19
U=20
V=21
W=22
X=23
Y=24
Z=25
palabrasreservadas={"teorema","Matemático","Matemática", "Hilbert", "Turing","análisis","Euler","Fermat","Pitágoras","autómata","Boole","Cantor","Perelman","Experimentación","Físico","Física","Astronomía","Mecánica","Newton","Einstein","Galileo","Modelo","Tesla","Dinámica","Partículas"}
Finalizacion={',','?',' ','!', ':', ';','(',')','¿','¡'}
Digitos={'0','1','2','3','4','5','6','7','8','9'}
Letras={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á','É','Í','Ó','Ú','á','é','í','ó','ú'}
states = {A, B, C, D, E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}
accept_states = {B,E,F,L,M,O,Q,S,U,Y,Z}
alphabet = {'^', '+', '-', 'D','.','i','L'}
tf = {A:{'D':B, '-':D,'+':C,'L':Z,'i':F},
       B:{'D':E, '-':H, '+':G,'.':I, 'i':F},#Enteros
       C:{'D':B},
       D:{'D':B},
       E:{'D':E,'.':J,'i':F,'+':G,'-':H},#Enteros
       F:{'L':Z},#Complejos
       G:{'D':K},
       H:{'D':K},
       I:{'D':L},
       J:{'D':M},
       K:{'.':P,'i':O},
       L:{'-':H,'D':Q,'i':F,'+':G,'^':R},#Reales
       M:{'i':F,'D':S,'-':H,'+':G},#Reales
       N:{'D':N,'i':O,'.':P},
       O:{},#Complejos
       P:{'D':T},
       Q:{'i':F,'-':H,'D':Q,'+':G,'^':R},#Reales
       R:{'+':V,'D':U,'-':W},
       S:{'D':S,'+':G,'-':H,'i':F},#Reales
       T:{'i':O,'D':X},
       U:{'D':Y},#Notación
       V:{'D':U},
       W:{'D':U},
       X:{'D':X,'i':O},
       Y:{'D':Y},#Notación
       Z:{'L':Z}, #Palabras
       }
Complejos={F,O}
Enteros={B,E}
Palabras={Z}
Reales={L,M,Q,S}
Notacion={Y}

start_states = A
#ea=Estado Actual
#ac=Estado Aceptación
#al=Alfabeto
#ein=Estado Inicial
#ft=Función Transición
imagenes=[]
class DFA:
    ea=None
    def __init__(self,es,ac,al,ein,ft):
        self.es = es
        self.al = al
        self.ft = ft
        self.ein= ein
        self.ac = ac
        self.ea = ein
        return

    def CambioEstado(self, caracter):
        try:
            self.ea =self.ft[self.ea][caracter]
        except:
            self.ea=None
        
    def EnEstadoAceptacion(self):
        return (self.ea in self.ac, self.ea)
    
    def IrEstadoInicial(self):
        self.ea = self.ein
    
    def Aceptador(self, cadena):
        self.IrEstadoInicial()
        guardador=''
        nuevotexto='<p>'
        for caracter in cadena:
            if caracter in Finalizacion: #Complejos: Rojo, Enteros: Azul, Reales:Verde, Notación: Morado, Palabras: Gris
                if self.ea in Complejos: 
                    nuevotexto=nuevotexto+'<span style=\"color: #C0392B\">'+guardador+'</span>'+caracter
                elif self.ea in Enteros:
                    nuevotexto=nuevotexto+'<span style=\"color: #0000FF\">'+guardador+'</span>'+caracter
                elif self.ea in Reales: 
                    nuevotexto=nuevotexto+'<span style=\"color: #27AE60\">'+guardador+'</span>'+caracter
                elif self.ea in Notacion: 
                    nuevotexto=nuevotexto+'<span style=\"color: #5B2C6F\">'+guardador+'</span>'+caracter
                elif self.ea in Palabras: 
                    if guardador in palabrasreservadas:
                        nuevotexto=nuevotexto+'<span style=\"color: #808B96\">'+guardador+'</span>'+caracter
                        if guardador in imagenes:
                            pass 
                        else:
                            imagenes.append(guardador)
                    else:
                        nuevotexto=nuevotexto+guardador+caracter
                else: 
                    nuevotexto=nuevotexto+guardador+caracter
                guardador=''
                self.IrEstadoInicial() 
            elif caracter in Digitos:
                guardador=guardador+caracter
                self.CambioEstado('D')
            elif caracter=='i' and self.ea==0:
                self.CambioEstado(caracter)
                guardador=guardador+caracter
            elif caracter=='i' and self.ea==25:
                self.CambioEstado("L")
                guardador=guardador+caracter
            elif caracter=='i':
                self.CambioEstado(caracter)
                guardador=guardador+caracter
            elif caracter in Letras:
                self.CambioEstado('L')
                guardador=guardador+caracter
            else:
                self.CambioEstado(caracter)
                guardador=guardador+caracter
        if self.ea in Complejos: 
            nuevotexto=nuevotexto+'<span style=\"color: #C0392B\">'+guardador+'</span>'
            guardador=''
        elif self.ea in Enteros:
            nuevotexto=nuevotexto+'<span style=\"color: #0000FF\">'+guardador+'</span>'
            guardador=''
        elif self.ea in Reales: 
            nuevotexto=nuevotexto+'<span style=\"color: #27AE60\">'+guardador+'</span>'
            guardador=''
        elif self.ea in Notacion: 
            nuevotexto=nuevotexto+'<span style=\"color: #5B2C6F\">'+guardador+'</span>'
            guardador=''
        elif self.ea in Palabras: 
            if guardador in palabrasreservadas:
                nuevotexto=nuevotexto+'<span style=\"color: #808B96\">'+guardador+'</span>'
                if guardador in imagenes:
                    pass 
                else:
                    imagenes.append(guardador)
                    guardador=''
            else:
                nuevotexto=nuevotexto+guardador
        else: 
            nuevotexto=nuevotexto+guardador
            guardador=''
        nuevotexto=nuevotexto+'</p>'
        print self.ea
        return nuevotexto


Automata=DFA(states,accept_states,alphabet,start_states,tf)
