import itertools
import string
import matplotlib.pyplot as plt
import numpy as np

chars = string.ascii_letters + string.digits + '!@#$%' # 67 символов

lengths_data = []
avg_tries_length_data = []

for length in range(1, 4):
    total_passwords = len(chars) ** length
    avg_tries = (total_passwords + 1) / 2
    
    lengths_data.append(length)
    avg_tries_length_data.append(avg_tries)

password_length = 3  # фиксированная длина пароля
alphabets = [
    ("цифры", string.digits),
    ("буквы (a-z)", string.ascii_lowercase),
    ("буквы (a-z) + цифры", string.ascii_lowercase + string.digits),
    ("все символы", string.ascii_letters + string.digits + '!@#$%')]

alphabet_names = []
alphabet_sizes = []
avg_tries_alphabet_data = []

for name, alphabet in alphabets:
    size = len(alphabet)
    total_passwords = size ** password_length
    avg_tries = (total_passwords + 1) / 2
    
    alphabet_names.append(name)
    alphabet_sizes.append(size)
    avg_tries_alphabet_data.append(avg_tries)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(lengths_data, avg_tries_length_data, 'bo-', linewidth=2, markersize=8)
ax1.set_xlabel('Длина пароля', fontsize=11)
ax1.set_ylabel('Среднее количество попыток', fontsize=11)
ax1.set_title('График зависимости среднего числа попыток от длины пароля\n(алфавит: 67 символов)', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_yscale('log')

for i, (x, y) in enumerate(zip(lengths_data, avg_tries_length_data)):
    ax1.annotate(f'{y:,.0f}', (x, y), xytext=(5, 5), textcoords='offset points', fontsize=8)

bars = ax2.bar(range(len(alphabet_names)), avg_tries_alphabet_data, 
               color='steelblue', alpha=0.7, edgecolor='black')
ax2.set_xlabel('Размер алфавита', fontsize=11)
ax2.set_ylabel('Среднее количество попыток', fontsize=11)
ax2.set_title(f'График зависимости среднего числа попыток от размера алфавита\n(пароль длиной {password_length} символа)', fontsize=10)
ax2.set_xticks(range(len(alphabet_names)))
ax2.set_xticklabels(alphabet_names, rotation=15, ha='right', fontsize=8)
ax2.grid(True, alpha=0.3, axis='y')

for bar, val, size in zip(bars, avg_tries_alphabet_data, alphabet_sizes):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + max(avg_tries_alphabet_data)*0.02,
             f'{val:,.0f}\n({size} симв.)', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
