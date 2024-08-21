import random
from datetime import datetime, timedelta

def generate_random_date(start_year=2000, end_year=2024):
    """Gera uma data aleatória entre dois anos fornecidos no formato YYYY-MM-DD."""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')

def generate_passwords(num_passwords):
    """Gera uma lista de senhas compostas apenas por datas aleatórias."""
    passwords = set()  # Usar um conjunto para evitar duplicatas
    while len(passwords) < num_passwords:
        date_str = generate_random_date()
        passwords.add(date_str)
    return list(passwords)

def save_passwords_to_file(passwords, filename='passwords.txt'):
    """Salva a lista de senhas em um arquivo de texto."""
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(f"{password}\n")

if __name__ == "__main__":
    num_passwords = 5000
    passwords = generate_passwords(num_passwords)
    save_passwords_to_file(passwords)
    print(f"Gerado {num_passwords} senhas e salvo em passwords.txt")

