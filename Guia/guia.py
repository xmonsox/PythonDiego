estudiantes = []
estudiantes . append (('Juan ','Aguila','14000000',[]) )
estudiantes . append (('Aldo ','Verri ','14000001',[]) )
estudiantes . append (('Marıa','Pinto ','14000002',[]) )

# Agrego notas
estudiantes [0][3]. append (6.5)
estudiantes [0][3]. append (7.0)
estudiantes [0][3]. append (6.7)
estudiantes [1][3]. append (3.0)
estudiantes [1][3]. append (2.7)
estudiantes [1][3]. append (3.8)
estudiantes [2][3]. append (5.7)
estudiantes [2][3]. append (7.0)
estudiantes [2][3]. append (6.2)
# Muestro promedios
# for e in estudiantes :
#     promedio = sum( e [3]) /len( e [3])
#     print (e [1] ,"\t= >" '%0.2 f'% promedio)

class persona:
    pass

juan = persona ()
juan . nombre = 'Juan'
juan . apellido = 'Aguila'
juan . n_alumno = '14000000'
# Creo otra persona
aldo = persona ()
aldo . nombre = 'Aldo'
aldo . apellido = 'Verri'
aldo . n_alumno = '14000001'
# Creo ´u ltimo estudiante
maria = persona ()
maria . nombre = 'Marıa'
maria . apellido = 'Pinto'
maria . n_alumno = '14000002'

# Agrego estudiantes a mi lista
estudiantes = []
estudiantes . append ( juan )
estudiantes . append ( aldo )
estudiantes . append ( maria )
# Muestro los nombres
# for e in estudiantes :
#     print ( e . nombre )

# Defino el tipo de dato ( clase ) " persona "
# class persona :
# # Constructor
#     def __init__ ( self , nombre ) :
#         print (" Persona creada :", nombre )
# # Creo una persona
# j = persona (" juan ")
# j . nombre = 'Juan'
# j . apellido = 'Aguila'
# j . n_alumno = '14000000'

# class persona :
#     # Constructor
#     def __init__ ( self , nombre , apellido , n_alumno ) :
#     # Agrego atributos a persona
#         self . nombre = nombre
#         self . apellido = apellido
#         self . n_alumno = n_alumno
#         self.notas = []
# juan = persona ('Juan ', '´A guila ', '14000000 ')
# aldo = persona ('Aldo ', 'Verri ', '14000001 ')
# maria = persona ('Mar´ıa', 'Pinto ', '14000002 ')

# # Agrego notas
# juan . notas . extend ([6.5 , 7.0 , 6.7])
# aldo . notas . extend ([3.0 , 2.7 , 3.8])
# maria . notas . extend ([5.7 , 7.0 , 6.2])
# # Formo lista con los estudiantes
# estudiantes = [ juan , aldo , maria ]
# # Muestro promedios
# for e in estudiantes:
#     promedio = sum(e.notas) / len(e.notas)
#     print(e.apellido, "\t=>", "{:.2f}".format(promedio))




#ESTO NO ME DIO ---------
# Defino el tipo de dato ( clase ) " persona "
# class persona :
# # Constructor
#     def __init__ ( self , nombre , apellido , n_alumno ) :
# # Atributos de persona
#         self . nombre = nombre
#         self . apellido = apellido
#         self . n_alumno = n_alumno
#         self . notas = []
# # M´e todos
# def agregar_nota ( self , n ) :
#     self . notas . append ( n )
# def agregar_notas ( self , l ) :
#     self . notas . extend ( l )
# def get_promedio ( self ) :
#     return sum( self . notas ) / len( self . notas )

# juan = persona ('Juan ', '´A guila ', '14000000 ')
# aldo = persona ('Aldo ', 'Verri ', '14000001 ')
# maria = persona ('Mar´ıa', 'Pinto ', '14000002 ')

# juan . notas . extend ([6.5 , 7.0 , 6.7])
# aldo . notas . extend ([3.0 , 2.7 , 3.8])
# maria . notas . extend ([5.7 , 7.0 , 6.2])

# estudiantes = [juan, aldo, maria]
# for e in estudiantes:
#     print(e.apellido, "\t=>", "{:.2f}".format(e.get_promedio()))



import random
class guerrero :
    def __init__ ( self , nombre , vida , fuerza , precision ,velocidad , defensa ) :
            self . nombre = nombre ; self . vida = vida
            self . fuerza = fuerza ; self . precision = precision
            self . velocidad = velocidad ; self . defensa = defensa
    def golpear ( self , g ) :
# veo si acierto el golpe
        if( random . random () <= ( self . precision - g .
            velocidad ) / 100) :
# en caso de acertar , agrego da~no al oponente
            g . vida -= max ([( self . fuerza - g . defensa )
                + random . randrange ( -10 ,11) ,1])
            print (" Golpe certero de", self . nombre )
        else :
            print ( g . nombre , " esquiva el golpe !")
        def simular_batalla ( j1 , j2 ): #esta parte no me da
# comienza jugador m´as veloz
            golpeador , receptor = j1 , j2
            if( j1 . velocidad < j2 . velocidad ) :
                golpeador , receptor = j2 , j1
# se golpean hasta que alguno tenga vida cero
                while ( j1 . vida > 0 and j2 . vida > 0) :
                    print ("\n" + j1 . nombre , j1 . vida ,"vs", j2 . vida , j2 . nombre )
                    golpeador . golpear ( receptor )
# cambio de turnos
                    golpeador , receptor = receptor , golpeador
# fin
                    print ("\n" + j1 . nombre , j1 . vida ,"vs", j2 . vida , j2 . nombre )
                    print (" Ganador :", receptor . nombre )

# batalla de ejemplo
superman = guerrero ('Superman ' ,100 ,50 ,80 ,30 ,20)
goku = guerrero ('Gok´u' ,100 ,60 ,80 ,40 ,20)
chuck = guerrero ('Chuck Norris ' ,200 ,99 ,99 ,99 ,99)
simular_batalla ( goku , chuck )
