OBS:Ferramenta está em fase de testes!!


# 💣 BOMBFORM

> Automação assíncrona de brute force em formulários HTTP  
> Asynchronous brute force automation on HTTP forms

---

## 🧠 Descrição | Description

**BOMBFORM** é uma ferramenta feita no **ódio e na lógica**, com foco em performance e automação real de brute force em formulários web.  
Funciona testando milhares/milhões de combinações de usuários e senhas de forma assíncrona, usando `httpx` + `asyncio` pra velocidade absurda.
Desenvolvida como estudo de automação ofensiva, manipulação de requisições POST e identificação de respostas via redirecionamento ou frase de erro.

---

## 🚀 Requisitos | Requirements
- Python 3.10+
- httpx

Instalação:

```bash
pip install httpx

⚙️ Como usar | How to use
    Crie um arquivo combos.txt com a estrutura:

usuario1:senha1
usuario2:senha2
...

    Rode o script:

python main.py
    Preencha as infos:
    URL do formulário (ex: http://zero.webappsecurity.com/login.html)
    Indicador de erro (ex: login_error=true ou trecho da frase de erro)

💡 Funcionamento | How it works
    Leitura assíncrona das combinações (user:pass)
    Envio massivo de POSTs com cabeçalhos e payloads configuráveis
    Detecção de erro por frase ou URL (resposta do servidor)
    Salva os logins válidos no logs.txt

🧱 Melhorias previstas

Suporte a proxy rotativo
Análise automática dos campos do form
Regex para detectar mensagens de erro
Export em CSV

⚠️ Disclaimer

    Esta ferramenta foi desenvolvida para fins educacionais e laboratoriais.
    O uso em sistemas sem autorização pode ser ilegal.
    O autor não se responsabiliza por qualquer uso indevido.

This tool is intended only for educational and research purposes.
Use without authorization may be considered illegal.
The author is not responsible for misuse.


👑 Autor | Author
Desenvolvido por @Adryanss

🔥 Powered by Adryan Underground
