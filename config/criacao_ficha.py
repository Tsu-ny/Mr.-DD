import json
import os

class CriarFichaDePersonagem:
    def __init__(self, nome, classe):
        self.nome = str(nome.title())
        self.classe = str(classe.title())
        self._hp = 100

    def criar_json(self):
        '''
        Cria um arquivo JSON com os atributos do personagem.
        '''
        os.makedirs('./config/fichas_salvas', exist_ok=True) # Garante que o diretório exista

        path = os.path.join('./config/fichas_salvas', f'ficha_{self.nome}.json') # Define o caminho do arquivo JSON

        with open(path, 'w', encoding="UTF-8") as arquivo_json:
            json.dump(self.__dict__, arquivo_json, ensure_ascii=False, indent=4)

# p = CriarFichaDePersonagem("Aragorn", "Guerreiro")
# print(p.__dict__)