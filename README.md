# Criando o App Baralho Mágico com Streamlit

O jogo ***Baralho Mágico*** é uma atividade lúdica que utiliza um ***truque de mágica*** com cartas para introduzir e explorar conceitos matemáticos, em especial as funções logarítmicas. No jogo, um participante escolhe uma carta, e através de uma série de perguntas sobre a posição da carta escolhida, o truque consegue identificá-la. A ***mágica*** por trás desse processo está fundamentada em um ***algoritmo matemático*** que reduz progressivamente o número de possibilidades, baseando-se na propriedade de crescimento logarítmico. Assim, o jogo não apenas entretém, mas também demonstra como conceitos matemáticos aparentemente complexos, como os ***logaritmos***, podem ser aplicados de maneira prática e divertida.

Utilizei ***Python*** em conjunto com o Streamlit para criar um aplicativo web que materializa o jogo ***Baralho Mágico***. Através do Python, desenvolvi a lógica por trás do truque de mágica, aplicando funções para manipulação das cartas e execução do ***algoritmo logarítmico*** que identifica a carta escolhida. Com o ***Streamlit***, fui capaz de transformar essa lógica em uma ***interface*** interativa e amigável, permitindo que os usuários joguem diretamente no navegador. O Streamlit facilitou a criação de um aplicativo Web, onde as cartas são ***distribuídas visualmente*** e as escolhas dos usuários são processadas em tempo real, proporcionando uma experiência fluida e intuitiva.

> ***IMPORTANTE:*** O app funciona de maneira fluida quando acessado via navegador, que é o meio mais indicado.

<!--
https://www.youtube.com/@renato-coelho

# Apresentação em vídeo

<p align="center">
  <a href="https://www.youtube.com/@renato-coelho" target="_blank"><img src="thumbnail/Streamlit-Baralho-Magico.png" alt="Vídeo de apresentação"></a>
</p>
-->

### Requisitos

+ ![Docker](https://img.shields.io/badge/Docker-23.0.3-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-1.25.0-E3E3E3)

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)

## Deploy do App

+ Clonando o repositório
```bash
git clone https://github.com/Renatoelho/streamlit-baralho-magico.git streamlit-baralho-magico
```

+ Acessando o diretório clonado
```bash
cd streamlit-baralho-magico/
```

+ Ativando App
```bash
docker compose -p baralho_magico -f docker-compose.yaml up -d --build
```

## Acessando o App Local

Para acessar o App local clique aqui: [http://0.0.0.0:8100](http://0.0.0.0:8100)

## Acessando o App Online

Caso queira acessar a versão online que fiz o deploy em "Produção" acesse aqui: [https://baralhomagico.com.br](https://baralhomagico.com.br)

> ***IMPORTANTE:*** O app funciona de maneira fluida quando acessado via navegador, que é o meio mais indicado.

# Referências

API reference, **Streamlit.** Disponível em: <https://docs.streamlit.io/develop/api-reference>. Acesso em: 09 ago. 2024.

Guia do professor - Experimento, **Baralho mágico.** Disponível em: <https://m3.ime.unicamp.br/arquivos/998/TELA-baralho_magico---guia_do_professor.pdf>. Acesso em: 09 ago. 2024.
