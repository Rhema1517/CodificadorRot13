def rot13():
    a='abcdefghijklmnopqrstuvwxyzabcdefghijklm'
    l2=''
    message = input('Escribe el mensaje a codificar: ')
    for n in range(len(message)):
        if message[n] == (message[n]).upper() and not a.find(message.lower()[n]) == -1:
            l2 += (a[a.find(message.lower()[n])+13]).upper()#LOWER pasa todo a minuscula para que encuentre el caracter ya que todo en a esta en minuscula
            continue
        elif a.find(message[n]) == -1:
            l2 += message[n]
            continue
        l2 += a[a.find(message[n])+13]
    print('Resultado: ', l2)
rot13()