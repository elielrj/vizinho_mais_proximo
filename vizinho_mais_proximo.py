import math

class VizinhoMaisProximo:

    matriz = []

    def __init__(self, sequencia, amostra):
        self.sequencia = sequencia
        self.amostra = amostra

    def buscar_vetor_do_vizinho_mais_proximo(self):

        matriz_linha = []

        for i in range(0, len(self.sequencia),1):
            subsequencia_1 = self.sequencia[i:i+self.amostra]

            if(len(subsequencia_1) >= self.amostra):

                for j in range(0, len(self.sequencia),1):
                    subsequencia_2 = self.sequencia[j:j+self.amostra]

                    if(len(subsequencia_2) >= self.amostra):
                        valor = self.calcular_distancia_euclidiana(subsequencia_1,subsequencia_2)

                        matriz_linha.append(valor)

                self.matriz.append(matriz_linha)
                matriz_linha = []

    def calcular_distancia_euclidiana(self, subsequencia_1, subsequencia_2):

        total = float(0.0)

        for index in range(0, self.amostra):
            subatracao_t1_t2 = subsequencia_1[index] - subsequencia_2[index]
            valor_ao_quadrado = math.pow(subatracao_t1_t2,2)
            total += valor_ao_quadrado

        total = math.sqrt(total)
        return f"{total:.1f}"

    def exibir_matriz_de_distancias(self):

        matriz_de_distancias = ''

        for i in range(len(self.matriz)):

            for j in self.matriz[i]:

                matriz_de_distancias += j + '   '

            matriz_de_distancias += '\n'

        print(matriz_de_distancias)

    def exibir_vetor_de_similaridade(self):

        vetor_de_similaridade = []

        for i in range(len(self.matriz)):
            lista = self.matriz[i]
            self.ordenar_lista(lista)
            vizinho_mais_proximo = lista[1]
            vetor_de_similaridade.append(vizinho_mais_proximo)

        print(vetor_de_similaridade)

    def ordenar_lista(self,lista):

        quantidade = len(lista)

        for i in range(0, quantidade):
            for j in range(0, quantidade - 1):
                if float(lista[j + 1]) < float(lista[j]):
                    menor = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = menor