from vizinho_mais_proximo import VizinhoMaisProximo

sequencia = [0,1,3,2,9,1,14,15,1,2,2,10,7]
amostra = 4

vizinhoMaisProximo = VizinhoMaisProximo(sequencia, amostra)

vizinhoMaisProximo.buscar_vetor_do_vizinho_mais_proximo()

vizinhoMaisProximo.exibir_matriz_de_distancias()

vizinhoMaisProximo.exibir_vetor_de_similaridade()
