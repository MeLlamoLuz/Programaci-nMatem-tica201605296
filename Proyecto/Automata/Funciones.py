# -*- coding: utf-8 -*-

from os import popen
from django.core.files import File
from graphviz import Source
import dot2tex
import datetime

class Automata:

    def __init__(self, lenguaje = set(['0', '1'])):
        self.estados = set()
        self.estadoInicial = None
        self.aceptacion = []
        self.transiciones = dict()
        self.lenguaje = lenguaje

    @staticmethod
    def epsilon():
        return ":e:"

    def defEstadoIncial(self, estado):
        self.estadoInicial = estado
        self.estados.add(estado)

    def agregarAceptacion(self, estado):
        if isinstance(estado, int):
            estado = [estado]
        for s in estado:
            if s not in self.aceptacion:
                self.aceptacion.append(s)

    def agregarTransicion(self, estadoSal, estadoEn, inp):
        if isinstance(inp, str):
            inp = set([inp])
        self.estados.add(estadoSal)
        self.estados.add(estadoEn)
        if estadoSal in self.transiciones:
            if estadoEn in self.transiciones[estadoSal]:
                self.transiciones[estadoSal][estadoEn] = self.transiciones[estadoSal][estadoEn].union(inp)
            else:
                self.transiciones[estadoSal][estadoEn] = inp
        else:
            self.transiciones[estadoSal] = {estadoEn : inp}

    def agregarTransicionDicc(self, transiciones):
        for estadoSal, estadosEn in transiciones.items():
            for estado in estadosEn:
                self.agregarTransicion(estadoSal, estado, estadosEn[estado])

    def obtenTransiciones(self, estado, key):
        if isinstance(estado, int):
            estado = [estado]
        trestados = set()
        for st in estado:
            if st in self.transiciones:
                for tns in self.transiciones[st]:
                    if key in self.transiciones[st][tns]:
                        trestados.add(tns)
        return trestados

    def EClausura(self, encEstado):
        estadosTodos = set()
        estados = set([encEstado])
        while len(estados)!= 0:
            estado = estados.pop()
            estadosTodos.add(estado)
            if estado in self.transiciones:
                for tns in self.transiciones[estado]:
                    if Automata.epsilon() in self.transiciones[estado][tns] and tns not in estadosTodos:
                        estados.add(tns)
        return estadosTodos

    def desplegarLenguaje(self):
        return "Lenguaje: {" + ", ".join(self.lenguaje) + "}"

    def desplegarEstados(self):
        return "Estados: {" + ", ".join(map(str, self.estados)) + "}"

    def desplegarEstInicial(self):
        return "Estado inicial: " + str(self.estadoInicial)

    def desplegarEstAceptacion(self):
        return "Estados de aceptacion: {" + ", ".join(map(str, self.aceptacion)) + "}"

    def desplegarTransiciones(self):
        texto = "Trancisiones:\n"
        lineas = 5
        for estadoSal, estadosEn in self.transiciones.items():
            for estado in estadosEn:
                for car in estadosEn[estado]:
                    texto += str(estadoSal) + " -> " + str(estado) + " con '" + car + "', "
                    lineas += 1
        return texto

    def nuevoDesdeNumero(self, numini):
        traslaciones = {}
        for i in list(self.estados):
            traslaciones[i] = numini
            numini += 1
        nuevo = Automata(self.lenguaje)
        nuevo.defEstadoIncial(traslaciones[self.estadoInicial])
        nuevo.agregarAceptacion(traslaciones[self.aceptacion[0]])
        for estadoSal, estadosEn in self.transiciones.items():
            for estado in estadosEn:
                nuevo.agregarTransicion(traslaciones[estadoSal], traslaciones[estado], estadosEn[estado])
        return [nuevo, numini]

    def nuevoDesdeEstados(self, equivalente, pos):
        nuevo = Automata(self.lenguaje)
        for estadoSal, estadosEn in self.transiciones.items():
            for estado in estadosEn:
                nuevo.agregarTransicion(pos[estadoSal], pos[estado], estadosEn[estado])
        nuevo.defEstadoIncial(pos[self.estadoInicial])
        for s in self.aceptacion:
            nuevo.agregarAceptacion(pos[s])
        return nuevo

    def codigoDot(self):
        codigo = "digraph DFA {\nrankdir=LR\n"
        if len(self.estados) != 0:
            codigo += "root=s1\nstart [shape=point]\nstart->s%d\n" % self.estadoInicial
            for estado in self.estados:
                if estado in self.aceptacion:
                    codigo += "s%d [shape=doublecircle]\n" % estado
                else:
                    codigo += "s%d [shape=circle]\n" % estado
            for estadoSal, estadosEn in self.transiciones.items():
                for estado in estadosEn:
                    for car in estadosEn[estado]:
                        codigo += 's%d->s%d [label="%s"]\n' % (estadoSal, estado, car)
        codigo += "}"
        return codigo

class constructorAutomata:

    @staticmethod
    def estructBasica(inp):
        estado1 = 1
        estado2 = 2
        basica = Automata()
        basica.defEstadoIncial(estado1)
        basica.agregarAceptacion(estado2)
        basica.agregarTransicion(1, 2, inp)
        return basica

    @staticmethod
    def disyuncionEstruct(a, b):
        [a, m1] = a.nuevoDesdeNumero(2)
        [b, m2] = b.nuevoDesdeNumero(m1)
        estado1 = 1
        estado2 = m2
        disyuncion = Automata()
        disyuncion.defEstadoIncial(estado1)
        disyuncion.agregarAceptacion(estado2)
        disyuncion.agregarTransicion(disyuncion.estadoInicial, a.estadoInicial, Automata.epsilon())
        disyuncion.agregarTransicion(disyuncion.estadoInicial, b.estadoInicial, Automata.epsilon())
        disyuncion.agregarTransicion(a.aceptacion[0], disyuncion.aceptacion[0], Automata.epsilon())
        disyuncion.agregarTransicion(b.aceptacion[0], disyuncion.aceptacion[0], Automata.epsilon())
        disyuncion.agregarTransicionDicc(a.transiciones)
        disyuncion.agregarTransicionDicc(b.transiciones)
        return disyuncion

    @staticmethod
    def concatenacion(a, b):
        [a, m1] = a.nuevoDesdeNumero(1)
        [b, m2] = b.nuevoDesdeNumero(m1)
        estado1 = 1
        estado2 = m2-1
        punto = Automata()
        punto.defEstadoIncial(estado1)
        punto.agregarAceptacion(estado2)
        punto.agregarTransicion(a.aceptacion[0], b.estadoInicial, Automata.epsilon())
        punto.agregarTransicionDicc(a.transiciones)
        punto.agregarTransicionDicc(b.transiciones)
        return punto

    @staticmethod
    def estrellaEstruct(a):
        [a, m1] = a.nuevoDesdeNumero(2)
        estado1 = 1
        estado2 = m1
        estrella = Automata()
        estrella.defEstadoIncial(estado1)
        estrella.agregarAceptacion(estado2)
        estrella.agregarTransicion(estrella.estadoInicial, a.estadoInicial, Automata.epsilon())
        estrella.agregarTransicion(estrella.estadoInicial, estrella.aceptacion[0], Automata.epsilon())
        estrella.agregarTransicion(a.aceptacion[0], estrella.aceptacion[0], Automata.epsilon())
        estrella.agregarTransicion(a.aceptacion[0], a.estadoInicial, Automata.epsilon())
        estrella.agregarTransicionDicc(a.transiciones)
        return estrella

    @staticmethod
    def masEstruct(a):
        [a, m1] = a.nuevoDesdeNumero(2)
        estado1 = 1
        estado2 = m1
        mas = Automata()
        mas.defEstadoIncial(estado1)
        mas.agregarAceptacion(estado2)
        mas.agregarTransicion(mas.estadoInicial, a.estadoInicial, Automata.epsilon())
        mas.agregarTransicion(mas.estadoInicial, mas.aceptacion[0], Automata.epsilon())
        mas.agregarTransicion(a.aceptacion[0], mas.aceptacion[0], Automata.epsilon())
        mas.agregarTransicion(a.aceptacion[0], a.estadoInicial, Automata.epsilon())
        mas.agregarTransicionDicc(a.transiciones)
        return mas

    def preguntaEstruct(a):
        [a, m1] = a.nuevoDesdeNumero(2)
        estado1 = 1
        estado2 = m1
        pregunta = Automata()
        pregunta.defEstadoIncial(estado1)
        pregunta.agregarAceptacion(estado2)
        pregunta.agregarTransicion(pregunta.estadoInicial, a.estadoInicial, Automata.epsilon())
        pregunta.agregarTransicion(pregunta.estadoInicial, pregunta.aceptacion[0], Automata.epsilon())
        pregunta.agregarTransicion(a.aceptacion[0], pregunta.aceptacion[0], Automata.epsilon())
        pregunta.agregarTransicion(a.aceptacion[0], a.estadoInicial, Automata.epsilon())
        pregunta.agregarTransicionDicc(a.transiciones)
        return pregunta


class AFNDaAFD:

    def __init__(self, afnd):
        self.construirAFD(afnd)

    def obtenerAFD(self):
        return self.afd

    def construirAFD(self, afnd):
        estadosTodos = dict()
        clausura = dict()
        cuenta = 1
        estado1 = afnd.EClausura(afnd.estadoInicial)
        clausura[afnd.estadoInicial] = estado1
        afd = Automata(afnd.lenguaje)
        afd.defEstadoIncial(cuenta)
        estados = [[estado1, cuenta]]
        estadosTodos[cuenta] = estado1
        cuenta +=  1
        while len(estados) != 0:
            [estado, desIndice] = estados.pop()
            for car in afd.lenguaje:
                trestados = afnd.obtenTransiciones(estado, car)
                for s in list(trestados)[:]:
                    if s not in clausura:
                        clausura[s] = afnd.EClausura(s)
                    trestados = trestados.union(clausura[s])
                if len(trestados) != 0:
                    if trestados not in estadosTodos.values():
                        estados.append([trestados, cuenta])
                        estadosTodos[cuenta] = trestados
                        aIndice = cuenta
                        cuenta +=  1
                    else:
                        aIndice = [k for k, v in estadosTodos.iteritems() if v  ==  trestados][0]
                    afd.agregarTransicion(desIndice, aIndice, car)
        for valor, estado in estadosTodos.iteritems():
            if afnd.aceptacion[0] in estado:
                afd.agregarAceptacion(valor)
        self.afd = afd

class regexAafnd:

    def __init__(self, regex):
        self.estrella = '*'
        self.disyuncion = '|'
        self.punto = '.'
        self.pregunta = '?'
        self.mas = '+'
        self.parentesisA = '('
        self.parentesisB = ')'
        self.operadores = [self.disyuncion, self.punto]
        self.regex = regex
        self.alfabeto = [chr(i) for i in range(65,91)]
        self.alfabeto.extend([chr(i) for i in range(97,123)])
        self.alfabeto.extend([chr(i) for i in range(48,58)])
        self.construirAFND()

    def obtenerAFND(self):
        return self.afnd

    def construirAFND(self):
        lenguaje = set()
        self.stack = []
        self.automata = []
        previo = "::e::"
        for car in self.regex:
            if car in self.alfabeto:
                lenguaje.add(car)
                if previo != self.punto and (previo in self.alfabeto or previo in [self.parentesisB,self.estrella]):
                    self.operadorAstack(self.punto)
                self.automata.append(constructorAutomata.estructBasica(car))
            elif car  ==  self.parentesisA:
                if previo != self.punto and (previo in self.alfabeto or previo in [self.parentesisB,self.estrella]):
                    self.operadorAstack(self.punto)
                self.stack.append(car)
            elif car  ==  self.parentesisB:
                if previo in self.operadores:
                    return "Error procesando '%s' después '%s'" % (car, previo)
                while(1):
                    if len(self.stack) == 0:
                        return "Error procesando '%s'. Stack vacío" % car
                    o = self.stack.pop()
                    if o == self.parentesisA:
                        break
                    elif o in self.operadores:
                        self.procesarOperador(o)
            elif car == self.estrella:
                if previo in self.operadores or previo == self.parentesisA or previo == self.estrella:
                    return "Error procesando '%s' después '%s'" % (car, previo)
                self.procesarOperador(car)
            elif car in self.operadores:
                if previo in self.operadores or previo == self.parentesisA:
                    return "Error procesando '%s' después '%s'" % (car, previo)
                else:
                    self.operadorAstack(car)
            else:
                return "El símbolo '%s' no está permitido" % car
            previo = car
        while len(self.stack) != 0:
            op = self.stack.pop()
            self.procesarOperador(op)
        if len(self.automata) > 1:
            return "La expresión regular no pudo ser preocesada correctamente."
        self.afnd = self.automata.pop()
        self.afnd.lenguaje = lenguaje

    def operadorAstack(self, car):
        while(1):
            if len(self.stack) == 0:
                break
            top = self.stack[len(self.stack)-1]
            if top == self.parentesisA:
                break
            if top == car or top == self.punto:
                op = self.stack.pop()
                self.procesarOperador(op)
            else:
                break
        self.stack.append(car)

    def procesarOperador(self, operador):
        if len(self.automata) == 0:
            return "Error procesando el operador '%s'. El stack está vacío" % operador
        if operador == self.estrella:
            a = self.automata.pop()
            self.automata.append(constructorAutomata.estrellaEstruct(a))
        elif operador in self.operadores:
            if len(self.automata) < 2:
                return "Error procesando el operador '%s'. Operandos inadecuados" % operador
            a = self.automata.pop()
            b = self.automata.pop()
            if operador == self.disyuncion:
                self.automata.append(constructorAutomata.disyuncionEstruct(b,a))
            elif operador == self.punto:
                self.automata.append(constructorAutomata.concatenacion(b,a))

def dibujarGrafoD(automata, filename):
    now = datetime.datetime.now()
    nombre = now.strftime("%Y-%m-%d_%H-%M")
    directorio = "Grafos"
    grafo = Source(automata.codigoDot(), filename=filename, directory=directorio, format='png')
    grafo.render('%s.gv' %(nombre + filename), view=False)

def dibujarLatex(regex, automata, filename):
    now = datetime.datetime.now()
    nombre = now.strftime("%Y-%m-%d_%H-%M")
    path = "Grafos\%s.txt" %(nombre + filename)
    figura = automata.codigoDot()
    codigo = "\documentclass{article}\n\usepackage[utf8]{inputenc}\n\usepackage{dot2texi}\n\usepackage{tikz}\n\usetikzlibrary{shapes, arrows}\n\%s{" %'title' + regex + "}\n\%s{document}\maketitle\n\%s{dot2tex}[dot, options = -tmath]\n" %('begin', 'begin') + figura + "\end{dot2tex}\n\end{document}"
    archivo = open(path, 'w')
    f = File(archivo)
    f.write(codigo)
    f.close()

def codigoLatex(regex, automata):
    figura = automata.codigoDot()
    return "\documentclass{article}\n\usepackage[utf8]{inputenc}\n\usepackage{dot2texi}\n\usepackage{tikz}\n\usetikzlibrary{shapes, arrows}\n\%s{" % 'title' + regex + "}\n\%s{document}\maketitle\n\%s{dot2tex}[dot, options = -tmath]\n" % (
    'begin', 'begin') + figura + "\end{dot2tex}\n\end{document}"


expresion = "01*"
afndObj = regexAafnd(expresion)
afnd = afndObj.obtenerAFND()
afdObj = AFNDaAFD(afnd)
afd = afdObj.obtenerAFD()
#dibujarGrafoD(afnd, "afnd")
dibujarLatex(expresion, afnd, "prueba")