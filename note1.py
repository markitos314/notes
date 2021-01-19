# Generamos un array vacío
df_guardia = []
df_guardia.append(pd.read_excel(os.path.join(path, f"{months[0]}.xlsx")))

# Generamos un df vacío para el anual
df_guardia_anual = pd.DataFrame()

for i in range(1,11):
  # Hacemos un dataframe por mes y lo guardamos en el array
  df_guardia.append(pd.read_excel(os.path.join(path, f"{months[i]}.xlsx")))

  # Borramos la columna 'SEGURO' porque estaba combinada con la que sigue y 'UBICACION' porque no tiene nada
  df_guardia[i].drop(df_guardia[i].columns[5], axis = 1, inplace=True)
  df_guardia[i].drop(df_guardia[i].columns[9], axis = 1, inplace=True)
  df_guardia[i].drop(df_guardia[i].columns[16], axis = 1, inplace=True)

  # Bucle while para borrar las filas superiores que no tienen data
  j=0
  # Mientras la primera celda sea distinta de DNI, incrementar 'j'
  while (df_guardia[i].iloc[j,0]) != 'DNI':
    j = j + 1
    
  # Selecciona todo el df, desde la fila DNI hasta el final
  df_guardia[i] = df_guardia[i].iloc[j+2:,:]

  # Reiniciamos filas index
  df_guardia[i].reset_index(inplace=True)
  df_guardia[i].drop('index', axis = 1, inplace=True)

  # Agregamos columnas index
  df_guardia[i].columns = ['DNI', 'NHC', 'PACIENTE', 'SEXO', 'EDAD', 'SEGURO', 'FECHA HORA INGRESO', 'SERVICIO', 'SECCION', 'CAUSA DE ATENCION',
                           'ALTA MEDICA', 'MOTIVO ALTA', 'ALTA ADMINISTRATIVA', 'PROFESIONAL', 'DIAG LIBRE', 'CIE10', 'DESC CIE10', 'DIAG AL ALTA']

  # Hacemos un solo df con todo el año
  df_guardia_anual = df_guardia_anual.append(df_guardia[i])
  
  # Testeo del for
  print(f"pasó {months[i]}")
