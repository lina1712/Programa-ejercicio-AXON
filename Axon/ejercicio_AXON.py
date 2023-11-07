import tkinter as tk
from tkinter import filedialog
import csv
import re
import copy
from tkinter import ttk

#variables globales
nueva_lista = []
capacidad_label = None
resultado_patron_text = None
arbol_tree=None
#esta funcion abre el archivo CSV y lo lee como una lista dentro de una listbox, aqui solo se van a poder leer los nombres de las señales osea la primera columna del archivo. (una nota importante es el tipo de delimitador del archivo csv)
def cargar_csv():
    global nueva_lista, frame_arbol;
    ruta_archivo = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if ruta_archivo:
        with open(ruta_archivo, newline='') as file:
            csv_reader = csv.reader(file, delimiter=';')
            nueva_lista = list(csv_reader)
        widgets_a_mantener = [cargar_btn,expresion_usuario_entry,buscar_btn,crear_btn,senal_entry,cargar_senales_btn]
        for widget in ventana.winfo_children():
            if widget not in widgets_a_mantener:
               widget.destroy()

        listbox1 = tk.Listbox(ventana)
        listbox1.grid(row=1, column=0)
        listbox1.place(x=20, y=80)

        for fila in nueva_lista:
            listbox1.insert("end", fila[0])

        listbox1.bind('<<ListboxSelect>>', mostrar_forma_arbol_seleccionado)

#en esta funcion se quiere mostrar los atributos de la señal seleccionada en la lista generada en la funcion anterior. estos atributos de muestran en forma de jerarquia

# en esta funcion se muestra el arlbol en la interface
def mostrar_forma_arbol(lista):
    arbol_tree = ttk.Treeview(ventana)
    arbol_tree.grid(row=2, column=2)
    arbol_tree.place(x=50, y=320)
    arbol_tree.heading("#0", text="Árbol de señales")
    mostrar_subarbol(lista, "", arbol_tree)

# esta funcion me permite seleccionar el elemento de mi lista anidada que quiero mostrar
def mostrar_subarbol(sublista, parent, tree):
    if isinstance(sublista, list):
        for i, subitem in enumerate(sublista):
            child = tree.insert(parent, "end", text=f"Elemento {i}")
            mostrar_subarbol(subitem, child, tree)
    else:
        tree.insert(parent, "end", text=sublista)

#en esta funcion se registra el evento del item seleccionado para poder ejecutar la funcion mostrar subarbol
def mostrar_forma_arbol_seleccionado(event):
    global arbol_tree
    if arbol_tree:
        frame_arbol.destroy()

    seleccion = event.widget.curselection()
    if seleccion:
        indice_seleccionado = int(seleccion[0])
        elemento_seleccionado = nueva_lista[indice_seleccionado]
        mostrar_forma_arbol(elemento_seleccionado)

# Función para buscar señales que coincidan con una expresión regular que el usuario ingrese
#en esta funcion recive un patron y una lista en la que poder buscar
def new_buscar (lista, patron):
    resultados = []
    for sublista in lista:
        if isinstance(sublista, list):
            resultados += new_buscar(sublista, patron)
        elif re.search(patron, sublista):
            resultados.append(lista)
    return resultados

resultados_text = None
#n esta funcion con el patron dado por el usuario mas la lista cargada en la primera funcion, se llama a la funcion new buscar para generar la busqueda y mostrar los resultados en la interface
def buscar():
    global resultados_text, capacidad_label
    patron = expresion_usuario_entry.get()
    copia_nueva_lista = copy.deepcopy(nueva_lista)

    if not resultados_text:
        resultados_text = tk.Text(ventana, height=10, width= 50)
        resultados_text.place(x=250, y=80)

    resultados_text.delete(1.0, tk.END)

    resultados = new_buscar(copia_nueva_lista, patron)
    if resultados:
        resultados_text.insert(tk.END, "Señales que coinciden con la expresión regular: \n")
        for resultado in resultados:
            for item in resultado:
                resultados_text.insert(tk.END, f"{item}\n")
    else:
        resultados_text.insert(tk.END,"No se encontraron coincidencias.")

    capacidad_text = capacidad_filtrado_expresion()

    if not capacidad_label:
        capacidad_label = tk.Label(ventana, text=capacidad_text, background='yellow')
        capacidad_label.place(x=250, y=270)
    else:
        capacidad_label.config(text=capacidad_text)

#en esta funcion se busca medir la capacidad de filtrado de una expresion, con el numero de coincidencias de la busqueda. entre menos coincidencia mas exacto es el patrón
def capacidad_filtrado_expresion():
    patron2 = expresion_usuario_entry.get()
    copia2_nueva_lista = copy.deepcopy(nueva_lista)
    resultado_buscar = new_buscar(copia2_nueva_lista, patron2)
    capacidad = len([sublista for sublista in resultado_buscar
                if isinstance(sublista,list)])
    print(capacidad)
    return(f" La capacidad de filtrado de esta expresion {patron2}: es {capacidad} coincidencias")

#aqui se define una funcion que va a permitir al usuario ingresar una notacion MMSPATH, y como resultado va obtener una expresion regular unica para su busqueda
def creacion_patron():
    global resultado_patron_text
    senal = senal_entry.get()
    senal_str = senal
    patron_A = re.compile (r'[/]\w')
    patron_B = re.compile (r'\w(?=\$)')
    resultadoA = patron_A.findall(senal_str)
    resultadoB = patron_B.findall(senal_str)
    cadena_resultado = resultadoA + resultadoB
    cadena_u = '.+'.join(cadena_resultado)

    if not resultado_patron_text:
        resultado_patron_text = tk.Text(ventana, height=4, width=30)
        resultado_patron_text.place(x=400, y=360)
    resultado_patron_text.delete(1.0, tk.END)
    resultado_patron_text.insert(tk.END, f"Este seria su patrÓn: \n{cadena_u}")
#esta funcion genera una expresion regular para una determinada señal pasada como parametro
def molde_patron(senal):
    senal_str = senal
    patron_A = re.compile (r'[/]\w')
    patron_B = re.compile (r'\w(?=\$)')
    resultadoA = patron_A.findall(senal_str)
    resultadoB = patron_B.findall(senal_str)
    cadena_resultado = resultadoA + resultadoB
    return '.+'.join(cadena_resultado)

#aqui se configura para cargar un archivo que contenga señales en una version csv, para generar sus expresiones regulares
def cargar_lista_senales():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if ruta_archivo:
        with open(ruta_archivo, newline='') as file:
            csv_reader = csv.reader(file, delimiter=';')
            new_lista = list(csv_reader)
            patrones = creacion_patrones_lista(new_lista)
            mostrar_patrones(patrones)

#funcion para crear las expresiones regulares de una lista ya cargada con anteioridad
def creacion_patrones_lista(lista):
    patrones = [molde_patron(senal[1]) for senal in lista]
    return patrones

resultado_patron_text= None

#funcion para mostrar al usuario las expresiones regulares que se generaron para la lista de señales csv cargada anteriormente
def mostrar_patrones(patrones):
    global resultado_patron_text

    resultados_patrones_text = tk.Text(ventana, height=10, width= 47)
    resultados_patrones_text.place(x=270, y=480)
    resultados_patrones_text.delete(1.0, tk.END)
    if patrones:
        resultados_patrones_text.insert(tk.END, "Esta es una lista de posibles patrones para cada senal: \n")
        for patron in patrones:
            resultados_patrones_text.insert(tk.END, f"{patron}\n")
    else:
        resultados_patrones_text.insert(tk.END,"No se pudo genera un patrón")



#aqui se crea la ventana de visualizacion para el usuario
ventana = tk.Tk()
ventana.geometry('680x680')
ventana.title("Ejercicio AXON")
#se crea el boton para poder cargar el archivo desde la interface
cargar_btn = tk.Button(ventana, text= "Cargar Archivo CSV", command=cargar_csv)
cargar_btn.grid(row=0, column=0, sticky="w")
cargar_btn.place(x=20, y=30)
#se crea el cuadro de entrada de informacion del usuario desde la interface
expresion_usuario_entry = tk.Entry(ventana)
expresion_usuario_entry.place(x=250, y=30)
#se crea el boton para buscar por expresion regular en la lista desde la interface
buscar_btn = tk.Button(ventana, text= "Buscar", command=buscar)
buscar_btn.place(x=380, y= 30)
#se crea el cuadro de entrada de informacion del usuario desde la interface para escribir una señal que se quiera pasar a expresion regular
senal_entry = tk.Entry(ventana)
senal_entry.place(x=400, y=320)
#se crea el boton para crear la expresion regular
crear_btn = tk.Button(ventana, text="Crear patrón", command=creacion_patron)
crear_btn.place(x=550, y=320)
#se crea el boton para poder cargar el archivo desde la interface
cargar_senales_btn = tk.Button(ventana, text="Cargas lista de señales", command=cargar_lista_senales)
cargar_senales_btn.place(x=400, y=450)




ventana.mainloop()
