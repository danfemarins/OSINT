from googlesearch import search

def find_sites_using_email(email):
    results = []
    
    # Exemplo de pesquisa no Google por "email" + "site:"
    query = f'"{email}" site:'
    
    try:
        # Realizando a pesquisa no Google
        for url in search(query, num=10, stop=10, pause=2):  # Limitando a 10 resultados
            results.append(url)
                
    except Exception as e:
        print('Erro ao fazer a pesquisa:', e)
    
    return results

def find_sites_using_name(name):
    results = []
    
    # Exemplo de pesquisa no Google pelo nome completo
    query = f'"{name}"'
    
    try:
        # Realizando a pesquisa no Google
        for url in search(query, num=10, stop=10, pause=2):  # Limitando a 10 resultados
            results.append(url)
                
    except Exception as e:
        print('Erro ao fazer a pesquisa:', e)
    
    return results

def main():
    print("Selecione o tipo de pesquisa:")
    print("1. Pesquisar pelo e-mail")
    print("2. Pesquisar pelo nome completo")
    choice = input("Escolha 1 ou 2: ")
    
    if choice == '1':
        email = input('Digite o e-mail para pesquisar: ')
        sites = find_sites_using_email(email)
        print('\nSites onde o e-mail foi encontrado:')
    elif choice == '2':
        name = input('Digite o nome completo para pesquisar: ')
        sites = find_sites_using_name(name)
        print('\nSites onde o nome foi encontrado:')
    else:
        print('Escolha inválida. Por favor, escolha 1 ou 2.')
        return
    
    for site in sites:
        print(site)

if __name__ == '__main__':
    main()
