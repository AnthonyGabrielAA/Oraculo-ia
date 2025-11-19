import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

chave_secreta = os.getenv("MINHA_CHAVE_API")

# Verifica se a chave foi carregada corretamente
if not chave_secreta:
    print("ERRO: Chave não encontrada! Verifique se criou o arquivo .env")
    exit()

# 3. Configura o Gemini com a chave
genai.configure(api_key=chave_secreta)

# --- FUNÇÕES ---

def consultar_oraculo(pergunta):
    """
    Envia a pergunta para o Gemini com uma instrução de personalidade.
    """
    try:
        # Escolhendo o modelo (o Flash é rápido e gratuito para testes)
        modelo = genai.GenerativeModel('gemini-2.0-flash')
        
        # O Prompt define QUEM é a IA. Aqui definimos a personalidade sarcástica.
        prompt_sistema = "Aja como um sábio muito antigo, mas que é extremamente sarcástico e sem paciência. Responda a pergunta abaixo de forma curta e irônica."
        
        # Enviando para a IA
        resposta = modelo.generate_content(f"{prompt_sistema}\n\nPergunta do mortal: {pergunta}")
        
        return resposta.text
    except Exception as erro:
        return f"O Oráculo está dormindo (Erro na API): {erro}"

def main():
    print("\n🔮 --- BEM-VINDO AO ORÁCULO SARCÁSTICO --- 🔮")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta_usuario = input("O que desejas saber, mortal? > ")

        if pergunta_usuario.lower() == "sair":
            print("Já vai tarde... 👋")
            break
        
        if not pergunta_usuario:
            continue

        print("\n🤔 O Oráculo está pensando...")
        
        # Chama a função que fala com a IA
        resposta_ia = consultar_oraculo(pergunta_usuario)
        
        print("-" * 40)
        print(f"🗣️  Oráculo: {resposta_ia}")
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()