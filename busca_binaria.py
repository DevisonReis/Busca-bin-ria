def busca_binaria(vetor, inicio, fim, elemento):
	
	while inicio <= fim:
		meio = fim + (inicio - fim) // 2
		
		if vetor[meio] == elemento:
			return meio
	
		elif vetor[meio] < elemento:
			inicio = meio + 1
		
		else:
			fim = meio - 1
			
	return - 1
	
vetor = list(range(1, 200, 4))

num = int(input('Informe um valor: '))

resultado = busca_binaria(vetor, 0, len(vetor) -1, num)

if resultado != - 1:
	print(f'Elemento encontrado no índice {resultado}.')
else:
	print('Elemento não encontrado.')