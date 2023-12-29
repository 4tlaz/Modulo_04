import requests

class FipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = self.get_modelos()

    def get_modelos(self):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos'
        headers = {'user-agent': 'MyStudyApp'}
        response = requests.get(url, headers=headers)
        response.raise_for_status() 

        modelos = response.json()['modelos']
        return modelos

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.modelos):
            modelo = self.modelos[self.index]
            self.index += 1
            return modelo
        else:
            raise StopIteration



marca_id_selecionada = 241  # Exemplo usado: {"codigo":"241","nome":"D2D Motors"}
iterador = FipeIterator(marca_id_selecionada)

for modelo in iterador:
    print(f"Nome: {modelo['nome']}, ID: {modelo['codigo']}")
