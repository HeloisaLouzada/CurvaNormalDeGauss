import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def producao_macas(num_pes):
    # Média desejada
    media_desejada = 600  # Média ajustada para o intervalo desejado

    # Desvio padrão ajustado para garantir que a maioria dos valores fique dentro do intervalo desejado
    desvio_padrao = 150

    # Gerar valores com média e desvio padrão ajustados
    valores = np.random.normal(media_desejada, desvio_padrao, num_pes)

    # Arredondar os valores para inteiros entre 100 e 1200
    producao_por_pe = np.round(np.clip(valores, 100, 1200))

    return producao_por_pe

def plot_distribuicao_reduzida(producao_por_pe):
    plt.figure(figsize=(10, 6))
    #histograma
    n, bins, patches = plt.hist(producao_por_pe, density=True, bins=30, alpha=0.75, color='blue', edgecolor='black')

    # Média e desvio padrão da produção
    media = np.mean(producao_por_pe)
    desvio_padrao = np.std(producao_por_pe)

    # Distribuição normal
    dist = norm(media, desvio_padrao)
    x = np.linspace(media - 4*desvio_padrao, media + 4*desvio_padrao, 1000)
    plt.plot(x, dist.pdf(x), color='red', linestyle='-', linewidth=2)

    plt.xlabel('Produção de Maçãs por Pé')
    plt.ylabel('Densidade de Probabilidade')
    plt.title('Distribuição Reduzida da Produção de Maçãs por Pé')
    plt.grid(True)
    plt.legend(['Distribuição Normal', 'Distribuição Reduzida'], loc='best')
    plt.xlim(0, 1200)  # Definindo os limites do eixo x
    plt.show()


def main():
    graficos = []
    while True:
        print("\nMenu:")
        print("1. Gerar gráfico")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("Saindo...")
            break
        elif escolha == '1':
            num_pes = int(input("Digite o número de pés de macieira na plantação: "))
            producao_por_pe = producao_macas(num_pes)
            graficos.append(producao_por_pe)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    for i, producao_por_pe in enumerate(graficos, start=1):
        print(f"\nGráfico {i}:")
        print("Desvio Padrão:", np.std(producao_por_pe))
        print("Média:", np.mean(producao_por_pe))
        plot_distribuicao_reduzida(producao_por_pe)


main()
