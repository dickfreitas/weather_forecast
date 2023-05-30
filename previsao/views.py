from django.shortcuts import render
import requests
# Create your views here.


def index(request) :
    if request.method == 'POST':
        cidade = request.POST.get('cidade')
        
        chave_api = f'b6e2542ed4c7f630684e757067a9a233'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=en"
        # USA O METODO PARA FAZER A REQUISIÇÃO
        response = requests.get(url)
        # TRANSFORMA OS DADOS OBTIDOS EM JSON
        dados = response.json()
        print(dados)
        if dados['cod'] != '404':
            temperatura = round(dados['main']['temp'])
            ventos = dados['wind']['speed']
            # Converte de Kelvin para Celsius
            
            descricao = dados['weather'][0]['description']
            descricao_capitalizada = descricao.title()
            tempo = dados['weather'][0]['main']
            humidity = dados['main']['humidity']
            print(descricao)
            nome = dados['name']
            
            icone_id = dados['weather'][0]['icon']
            # previsao = f'A previsão do tempo para {cidade} é : {descricao} com temperatura de {nova_temperatura} ºC e ventos de {ventos}km/h'
            
            infor = {
                'temperatura' : temperatura,
                'ventos' : ventos,
                'descricao' : descricao_capitalizada ,
                'icone_id' : icone_id,
                'name' : nome,
                'tempo' : tempo,
                'humidity' : humidity
            }
            
            return render(request , 'app/index.html' , {'dados' : infor})
        else:
            erro = 'Não foi possivel obter a previsão do tempo'
            context = {'erro' : erro}
            return render(request , 'app/index.html' , context)
    return render(request , 'app/index.html')
