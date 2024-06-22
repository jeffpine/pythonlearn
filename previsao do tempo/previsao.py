import requests

def obter_previsao_tempo(cidade, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        print(f"Erro ao obter previsão do tempo para {cidade}. Código de status HTTP: {resposta.status_code}")
        return None

def mostrar_previsao(dados):
    if dados:
        cidade = dados['name']
        descricao = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        vento = dados['wind']['speed']

        print(f"Previsão do tempo para {cidade}:")
        print(f"Descrição: {descricao}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento} m/s")
    else:
        print("Não foi possível obter a previsão do tempo.")

def main():
    api_key = "9a7bf5b10a60ab0299a7d44b9a0df3cf"
    
    while True:
        print("\n=== MENU ===")
        print("1. Obter previsão do tempo")
        print("2. Sair")
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == "1":
            cidade = input("Digite o nome da cidade: ")
            dados_previsao = obter_previsao_tempo(cidade, api_key)
            mostrar_previsao(dados_previsao)
        elif escolha == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha 1 ou 2.")

if __name__ == "__main__":
    main()