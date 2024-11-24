Dynamic Reactions Mod para Battle for Wesnoth
Visão Geral

O Dynamic Reactions Mod é uma modificação para o jogo Battle for Wesnoth que adiciona reações dinâmicas ao jogo. Quando uma unidade é eliminada no campo de batalha, unidades próximas exibem reações geradas por uma inteligência artificial (IA). Essas reações aparecem no log do jogo e no chat para melhorar a imersão.
Funcionalidades

    Reações Contextuais: Unidades próximas à que morreu têm suas reações registradas no log do jogo.
    Integração com IA: Utiliza uma API Flask para gerar falas dinâmicas e contextuais com base no evento.
    Aplicação Global: Funciona em qualquer cenário ou campanha sem necessidade de configurações adicionais.

Estrutura do Mod

O mod segue a estrutura recomendada para modificações do Wesnoth:

TCC-MG-BoW/
├── _main.cfg
├── _modifications.cfg
├── utils/
│   └── ia_reactions.cfg
└── images/
    └── icons/
        └── your_icon.png

    _main.cfg: Configuração principal que inclui os eventos.
    _modifications.cfg: Registra o mod como uma modificação global.
    utils/ia_reactions.cfg: Contém os eventos e o código Lua que aciona as reações.
    images/icons/your_icon.png: Ícone representando o mod no menu de modificações.

Como Funciona

    Quando uma unidade morre:
        Informações sobre a unidade morta e as unidades próximas são coletadas.
        O evento dispara uma chamada para a API Flask, enviando um contexto do evento.
    A API retorna uma reação gerada, que é exibida no log do jogo.
    Mensagens no formato "IA Reação" aparecem no chat do jogo.

Instalação

    Baixe o Mod: Extraia os arquivos para a pasta de add-ons do Wesnoth:
        No Windows: Documents/My Games/Wesnoth1.x/data/add-ons/
        No Linux: ~/.local/share/wesnoth/1.x/data/add-ons/
        No macOS: ~/Library/Application Support/Wesnoth_1.x/data/add-ons/
    Ative o Mod: No menu principal do Wesnoth, vá em Modificações e ative o Dynamic Reactions Mod.
    API Flask:
        Certifique-se de que o Flask API está rodando localmente.
        Execute o Flask com:

        python flask_api.py

Requisitos

    Battle for Wesnoth: Compatível com a versão 1.14 ou superior.
    Python: Necessário para rodar a API Flask.
    Dependências:
        Instale as dependências necessárias no ambiente Python:

        pip install flask transformers

Customização

    Raio de Detecção: O raio em que as unidades próximas reagem pode ser ajustado no arquivo ia_reactions.cfg. O padrão é radius=2.
    Temperatura e Comprimento do Texto: Altere os parâmetros temperature e max_length no flask_api.py para ajustar o estilo das respostas da IA.

Exemplo de Funcionamento

    Evento: Uma unidade é eliminada.
    Contexto Criado: "A unidade Soldado foi morta perto de Arqueiro."
    Mensagem no Log:

    IA Reação: Arqueiro reagiu: "Essa foi uma grande perda. Precisamos nos proteger melhor!"

Notas

    Certifique-se de que a API Flask está funcionando antes de iniciar o jogo.
    Caso a conexão com a API falhe, mensagens de erro serão exibidas no log do jogo para depuração.

Contribuição

Se desejar contribuir ou relatar problemas:

    GitHub: https://github.com/gihwho/ANALISE-E-CRIACAO-DE-DIALOGOS-BASEADO-EM-SENTIMENTO-PARA-JOGOS-DIGITAIS
    Contato: RA00297621@pucsp.edu.br
