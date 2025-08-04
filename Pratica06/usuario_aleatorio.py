import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        print(f"Nome: {nome}\nE-mail: {email}\nPaís: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter usuário: {e}")    

print("Gerando um usuário aletório...")
usuario = obter_usuario_aleatorio()
print(usuario)