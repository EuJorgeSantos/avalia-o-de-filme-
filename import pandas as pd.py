import pandas as pd

# Função principal
def main():
    try:
        # Carregar os dados
        dados = pd.read_csv('notas.csv')

        # 01 - Mostrar os 12 primeiros registros, os 6 últimos e o tamanho da massa de dados
        print("=== Análise de Dados ===\n")
        print("Os 12 primeiros registros:")
        print(dados.head(12))
        print("\nOs 6 últimos registros:")
        print(dados.tail(6))
        print(f"\nO tamanho da massa de dados é: {dados.shape[0]} registros.\n")

        # 02 - Avaliar o filme com ID=32
        print("=== Avaliação do Filme com ID=32 ===\n")
        filme_32 = dados[dados['ID'] == 32]

        if not filme_32.empty:
            nota = filme_32['nota'].iloc[0]
            nome = filme_32['nome'].iloc[0]
            if nota > 3:
                print(f"O filme '{nome}' (ID=32) é bom, pois a nota é {nota}.")
            else:
                print(f"O filme '{nome}' (ID=32) não é considerado bom, pois a nota é {nota}.")
        else:
            print("Nenhum filme com ID=32 encontrado.")
    except FileNotFoundError:
        print("Erro: O arquivo 'notas.csv' não foi encontrado. Certifique-se de que ele está no mesmo diretório do programa.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Executar o programa
if __name__ == "__main__":
    main()
