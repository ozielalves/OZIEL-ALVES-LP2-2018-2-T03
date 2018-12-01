# Relatório de desenvolvimento de software - Karrot
Disciplina: Linguagem de Programação II, Universidade Federal do Rio Grande do Norte ([UFRN](http://http://www.ufrn.br))

<div align="center">
  <img width="200" src="https://karrot.world/statics/carrot_logo.png">
</div>
<br>

## Sumário

+ [Objetivo](#objetivo)
+ [Resumo](#resumo)
+ [Caracterização da Empresa](#caracterização-da-empresa)
+ [Desenvolvimento do Sistema](#desenvolvimento-do-sistema)
  + [Front-end](#front-end)
    + [Tecnologias Utilizadas](#tecnologias-utilizadas)
  + [Back-end](#back-end)
    + [Tecnologias Utilizadas](#tecnologias-utilizadas)
+ [Considerações Finais](#considerações-finais)

## Objetivo
Analisar os comportamentos **objetivo** e **funcional** da estrutura do site, assim como a **orientação** e **organização** lógicas da aplicação, coadunando por fim em uma melhor compreenção do open source disponibilizado.

## Resumo
A plataforma conta com 3 repositórios, sendo estes referentes a: o código [front-end](https://github.com/yunity/karrot-frontend/), onde também está detalhada a localização central e planejamento de recursos; o código [back-end](https://github.com/yunity/karrot-backend), para lidar com as aplicações com o servidor; e o último para tratar do [blog da iniciativa](https://github.com/yunity/karrot-blog). É importante perceber que *****************

## Caracterização da Empresa
A *Karrot* é uma aplicação web que visa a organização de grupos de aproveitamento de comida no mundo todo. A iniciativa ataca diretamente o segundo objetivo de desenvolvimento sustentável da [ONU](https://nacoesunidas.org/conheca-os-novos-17-objetivos-de-desenvolvimento-sustentavel-da-onu/) porque têm como visão não só a diminuição do disperdício como também o favorecimento de indivíduos com o aproveitamento, o que aponta significativamente a importância do projeto e destaca sua necessidade de contribuição.

## Desenvolvimento do Sistema

## 1. Front-end
A interface front-end é composta por módulos e utilitários. A base contém todos os *bits* que podem ser considerados o núcleo do Karrot enquanto os utilitários sao *helpers* que podem ser reutilizados em outros módulos. Estes devem se manter pequenos, por isto é preciso criar outro módulo antes de adcioná-los.

### Tecnologias Utilizadas:
1. HTML
2. CSS
3. Java Script
4. Shell
5. Vue
 

#### Estrutura padrão:

- *Nome dos Módulos( __src__ )*
  - `routes.js`             -> Rotas para a aplicação
  - `assets/`               -> Depósito de imagens usadas no módulo
    - `apple.png`           
  - `api/`                  -> Comunicação com o back-end (XHR)
    - `pickup.js`           
    - `pickup.spec.js`      > Tests
    - ...
  - `datastore`             > Módulos e plugins do Vuex
    - `pickup.js`           
    - `pickup.spec.js`      > Tests
    - ...
  - `components/`           > Componentes Reutilizáveis
    - `PickupUser.vue`
    - `PickupUser.spec.js`  > Tests
    - `PickupUser.story.js` > 
    - ...
  - `pages/`                > Templates e instâncias
    - `PickupsManage.vue`   > Pagina conectada com o vuex-connect, o mapGetter e o mapActions, responsáveis pelas ações no mapa
    - `PickupsManageUI.vue` 

## 2. Back-end
### Tecnologias Utilizadas:
1. Python
2. Shell
3. Swagger

### Arquitetura do Projeto:

#### Teoria de Grupos:
Inicialmente tem-se um grupo modelo, permitido a criar objetos como "Foodsavers Brasil". Um grupo geralmente tem muitas lojas, como "Padaria do seu Pedro". Cada loja pode definir eventos onde *foodsavers* podem vir e aproveitar comida. Estes eventos são chamados em código `PickupDate`(Evento momentaneo) ou `PickupDateSeries`(Evento repetitivo).

#### Teoria de Usuários:
Como usuário logado é possível criar e entrar em grupos, oque o torna um membro, depois disso o usuário é habilitado a criar um `PickupDate,`o que fará dele um `collector`(Que passará a participar ativamente do *foodsaving*). 

### Aplicações importantes:
- `groups`: (Teoria de grupos).
- `users`: Dados do Usuário, reset de senha, troca de senha, etc.
- `userauth`: Login e Logout.
- `base`: a maioria dos modelos criados no site herda de modelos criados lá.
- `tests`: Densa cobertura de testes separadas em diferentes aplicações.
- `stores`: Classes para lojas e feedbacks como por exemplo `process_finished_pickup_dates`, que processa antigos eventos no histórico.
- `history`: Qualquer ação relacionada a loja.

### Notificações
As notificações, presentes no modulo `notifications`, são geradas pelo back-end assim como quando um usuário entra em um grupo, etc. O front-end carrega tudo isso via API na inicialização, se há notificações não vistas, estas serão exibidas.

## Considerações Finais
A estrutura do site segue um padrão intuitivo, ainda que de dificil acesso a documentação, o processo é facilitado após algum tempo de análise empírica e observatória.

## Autor

Relatório desenvolvido por [_Oziel Alves_](https://github.com/ozielalves) (*ozielalves@ufrn.edu.br*), 2018.2

&copy; IMD/UFRN 2018.
