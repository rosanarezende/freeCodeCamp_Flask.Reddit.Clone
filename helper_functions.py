def salt_password(password):
  #Para cada 2 caracteres, insira 'Buau'
  iterations = 0
  password_array = []
  
  for char in password:
    iterations += 1
    password_array.append(char)
    if iterations % 2 == 0:
      password_array.append('Buau')
  
  return ''.join(password_array)

