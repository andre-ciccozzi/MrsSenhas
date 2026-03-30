import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    print(f"[LOG] Gerando senha: tamanho={length}, maiúsculas={use_upper}, minúsculas={use_lower}, números={use_digits}, símbolos={use_symbols}")
    
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        return "Erro: Selecione ao menos um tipo de caractere!"
    
    return ''.join(random.choice(chars) for _ in range(length))

