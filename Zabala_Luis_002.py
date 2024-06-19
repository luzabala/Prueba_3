import csv
def eliminar(id_listita):
 for x in listita:
    if id_e==x[0]:
        listita.remove(x)
        print("Producto eliminado correctamente...")
        break
lista=[]
#FUNCIONES#

while (True):
    print(".-.-.-.-.MENU.-.-.-.-.-.")
    print("1.-Agregar equipo")
    print("2.-Listar equipo")
    print("3.-Actualizar nombre de equipo por id")
    print("4.-Generar BBDD")
    print("5.- Cargar BBDD")
    print("6.- Estadisticas")
    print("0.- Salir")
    op=int(input("Ingrese una opcion : "))
    if op==1:
        print("AGREGAR EQUIPO")
        print("")
        id=int(input("Ingrese id : "))
        nombre=(input("Ingrese nombre : "))
        puntos=int(input("Ingrese puntaje : "))
        diccionario={"id":id,"nombre": nombre,"puntos":puntos}
        if puntos==0>40:
            print("Categoria asignada : Amateur")
        elif puntos>80:
            print("Categoria asignada : Principiante")
        elif puntos>120:
            print("Categoria asignada : Avanzado")
        elif puntos>120:
            print("Categoria asignada : IDOLO")
            equipo=[id,nombre,puntos,categoria]
            lista.append(equipo)
        
    elif op==2:
        print("LISTADO DE EQUIPOS")
        for x in lista:
            print(f"id:{x[0]} nombre:{x[1]} puntos: {x[2]}

    elif op==3:
        print (".-.-.-.-.-Actualizar nombre del equipo.-.-.-.-.-")
        for x in lista:
            if ac==x["id"]:
                nom_nuevo=input("Ingrese nuevo nombre del equipo")
                print(f"Actualizar nombre del equipo(x{[nombre]} a {nom_nuevo}")
                resp=input(" Confirme que desea modificar el nombre (si/no)").lower()
                if resp=="si":
                    x["nombre"]=nom_nuevo
                    print ("Nombre actualizado correctamente")
                    print (nombre)
                    break
                if resp=="no":
                    print("No se ha modificado el nombre")
                    break
                else:
                    print("ingrese una opcion valida")
    elif op==4:
        print("GENERAR BBDD")
        with open ('bbdd_equipos.csv','w',newline='') as bbdd_equipo:
            escritor_csv=csv.writer(bbdd_equipo)
            escritor_csv.writerow(bbdd_equipo)
            escritor_csv.writerows(lista)
            print("Archivo generado correctamente")
    elif op==5:
        print("CARGAR BBDD")
        print("")
        lista.clear()
        cont=0
        with open ('bbdd_equipos.csv','w',newline='') as bbdd_equipo:
            lector_csv=csv.reader(bbdd_equipo)
            for fila in lector_csv:
                if cont==0:
                    cont+1
                    continue
                x=int(fila[0])
                n=fila[1]
                p=int(fila[2])
                lista_chica=[i,n,p]
                lista.append(lista_chica)        
        
    elif op==6:
        acum=0
        print(".-.-.--.-.Estadisticas.-.-.-.-.-.-")
        print("")
        cant=len(lista)
        if cant>0:
            for x in lista:
                acum=acum+x[2]
                prom=acum/cant
                print("Equipos   :",cant)
    elif op==0:
        print("Adios.....")
    else:
        ("Ingrese una opcion valida")
        
        
    
