diaI, tempoI = [int(input().split()[1]), [int(n) for n in input().split(' : ')]]
diaF, tempoF = [int(input().split()[1]), [int(n) for n in input().split(' : ')]]

horaI, minutoI, segundoI = tempoI
horaF, minutoF, segundoF = tempoF

segundosITot = diaI * 3600 * 24 + horaI * 3600 + minutoI * 60 + segundoI
segundosFTot = diaF * 3600 * 24 + horaF * 3600 + minutoF * 60 + segundoF

segundos = segundosFTot - segundosITot
dias = segundos // (3600 * 24)
horas = segundos // 3600 - dias * 24
minutos = (segundos - dias * 3600 * 24 - horas * 3600) // 60
segundos = segundos - dias * 3600 * 24 - horas * 3600 - minutos * 60

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')