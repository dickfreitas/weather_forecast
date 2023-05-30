# Projeto de Previsão do Tempo utilizando Django e a biblioteca Requests do Python

## Descrição do Projeto
Projeto Previsão do Tempo onde o objetivo principal foi desenvolver uma aplicação web usando o framework Djanfo e a biblioteca Requests do Python, a aplicação permitira que os usuarios visualizem a previsão do tempo atual. 


## Funcionalidades Principais
1. **Página de Início:** A página inicial da aplicação tem um input onde o usuário poderá inserir o nome da cidade para a qual deseja obter a previsão do tempo. Após confirmar, a aplicação fará uma requisição à API OpenWeaterMap usando a biblioteca Requests para obter os dados necessários.

2. **Exibição da Previsão do Tempo:** A aplicação exibirá as informações de previsão do tempo da cidade solicitada. Isso incluirá dados como temperatura, condições climáticas, umidade, velocidade do vento, entre outros. Essas informações serão apresentadas de forma clara e organizada para o usuário.

3. **Erro ao não achar a cidade:** Caso a cidade solicitada pelo usuario não esteja ou não seja encontrada no banco de dados, ira retornar uma mensagem de erro

4. **Responsividade** : O projeto conta com responsividade para desktop e para alguns dispositivos moveis.

## Tecnologias Utilizadas
- Django: Framework web em Python que facilita o desenvolvimento rápido e eficiente de aplicativos web.
- Requests: Biblioteca do Python para fazer requisições HTTP e acessar APIs externas.
- HTML, CSS e JavaScript: Linguagens utilizadas para criar a interface do usuário e interações na aplicação web.


## Benefícios e Aprendizados Esperados
- Aprofundar os conhecimentos em Django, um framework web popular e poderoso do Python.
- Aprender a fazer requisições HTTP usando a biblioteca Requests para acessar APIs externas.
- Aprender a integrar diferentes tecnologias e APIs para fornecer uma experiência aprimorada aos usuários.
- Adquirir conhecimentos sobre o desenvolvimento de aplicativos voltados para dados em tempo real, como a previsão do tempo.

Esse projeto proporcionará uma oportunidade de aplicar e aprofundar os conhecimentos em Django e na biblioteca Requests do Python, além de fornecer uma base sólida para o desenvolvimento de aplicativos web com foco em dados em tempo real.

## O Futuro do Projeto

4. **Sistema de Login e Autenticação:** Adicionar um sistema de login para o usuario, onde  aplicação permitirá que os usuários criem uma conta e façam login para personalizar sua experiência. Os usuários autenticados poderão salvar suas cidades favoritas e receber atualizações automáticas da previsão do tempo para essas cidades.

5. **Integração com API de Mapas:** Para melhorar a experiência do usuário, a aplicação poderá ser integrada com uma API de mapas, permitindo que os usuários visualizem a localização da cidade em um mapa interativo.

## Ilustrações
Segue algumas imagens de como o projeto pronto ficou!!!
![clearsky](../previsao_tempo/imagens/clearsky.png)
![Recife](../previsao_tempo/imagens/recife.png)
![error](../previsao_tempo/imagens/error.png)
