
tarea = ['🏦 sacar dinero del banco.',
          '🧺hacer la colada.',
            '🌳dar un paseo',
          '💈cortarse el cabello',
            '☕preparar un té.',
              '💻terminar capitulos.',
              '☎llamar a la mamá',
              '📺ver my hero academy']

indice = tarea.index('💈cortarse el cabello')
print("error al buscar el indice:", indice)

tarea[1] = "Entregar la tarea"
#desbloquear la primera msion
print(tarea[1])
#encontrar la segunda mision
print(tarea[2])
#obtener el subconjunto de tareas usando slicing
print(tarea[2:8])
#intentar acceder a un indice enexistente
print(indice)
#imprimit la lista
print(tarea)