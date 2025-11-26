import json
import os

class CriarFichaDePersonagem:
    def __init__(self, nome, classe, hp):
        self.nome = str(nome)
        self.classe = str(classe)
        self.hp = int(hp)

    def criar_json(self):
        '''
        Cria um arquivo JSON com os atributos do personagem.
        '''
        os.makedirs('./config/fichas_salvas', exist_ok=True) # Garante que o diretório exista

        path = os.path.join('./config/fichas_salvas', f'ficha_{self.nome}.json') # Define o caminho do arquivo JSON

        with open(path, 'w', encoding="UTF-8") as arquivo_json:
            json.dump(self.__dict__, arquivo_json, ensure_ascii=False, indent=4)

