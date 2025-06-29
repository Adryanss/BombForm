OBS:Ferramenta está em fase de testes!!

---

💣 JohnPass

> Brute force assíncrono para formulários HTTP com foco em performance e personalização
Asynchronous brute-force automation on HTTP login forms




---

🧠 Descrição | Description

JohnPass é uma ferramenta de brute-force web criada com foco em performance, estrutura limpa e lógica ofensiva realista.
Trabalha testando combinações massivas de usuário e senha em formulários HTTP via requisições assíncronas (httpx + asyncio).
Desenvolvido como parte de estudo de automação ofensiva e como prova de conceito para análise de respostas HTTP em ambientes de laboratório.

> Feita no ódio, café e lógica. Refinada com leitura de código, erros e tentativas.




---

🚀 Requisitos | Requirements

Python 3.10 ou superior

httpx (pip install httpx)



---

⚙️ Como Usar | How to Use

1. Execute o script:



python main.py

2. Siga o assistente interativo:

Digite os comandos url, user, passw, headers, emsg etc.

Ou use o modo DEBUG para preencher com configurações padrão (ideal pra testes locais).



3. Inicie o ataque:



>> start

4. Resultados possíveis:

Resposta HTTP 302 (redirecionamento)

Ausência da frase de erro → possível sucesso

Credenciais válidas salvas em logs.txt





---

🧠 Funcionalidades | Features

Teste assíncrono de múltiplas combinações de user:pass

Detecção de sucesso por:

Redirecionamento (302 Found)

Ausência de mensagem de erro configurável


Headers personalizados (User-Agent, Content-Type)

Wordlists customizadas ou padrão (fallback)

Portas configuráveis

Suporte a arquivos door.txt, loginspad.txt, senhaspad.txt



---

💡 Funcionamento Interno

Lê campos de usuário/senha do HTML manualmente ou por entrada do usuário

Permite testes com wordlists personalizadas ou automáticas

Dispara centenas de requisições POST simultâneas usando httpx.AsyncClient

Identifica potenciais sucessos com base no conteúdo da resposta

Salva hits em logs.txt para revisão posterior



---

🧱 Melhorias Futuras

Integração com proxies e rotação automática

Análise de formulários com parsing HTML (BeautifulSoup ou lxml)

Detecção automática de campos de login/senha

Regex para identificar respostas variadas

Exportação em CSV e relatório resumido

Modo CLI com argparse



---

⚠️ Aviso Legal | Legal Notice

> Esta ferramenta foi desenvolvida para fins educacionais e laboratoriais.
O uso em sistemas sem autorização prévia pode ser considerado ilegal.
O autor não se responsabiliza por qualquer uso indevido.



This tool is intended only for educational and research purposes.
Use without authorization may be considered illegal.
The author is not responsible for any misuse or abuse.


---

👑 Autor | Author

Desenvolvido por @Adryanss
🔥 Powered by Adryan Underground
🎯 Alvo: Transição de carreira para Segurança da Informação


---
