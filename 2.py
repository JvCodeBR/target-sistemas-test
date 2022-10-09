fibonacci_seq = [0, 1]

user_input = int(input())

while user_input > fibonacci_seq[len(fibonacci_seq) - 1]:
    f_number = fibonacci_seq[len(fibonacci_seq) - 1] + fibonacci_seq[len(fibonacci_seq) - 2]
    fibonacci_seq.append(f_number)

if user_input in fibonacci_seq:
    print(f'O número {user_input} pertence a sequencia de Fibonacci')
else:
    print(f'O número {user_input} NÃO pertence a sequencia de Fibonacci')
    
print(fibonacci_seq)
