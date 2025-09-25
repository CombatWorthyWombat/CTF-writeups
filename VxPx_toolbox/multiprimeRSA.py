# RSA decryption using multiple primes
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main():
    # User input
    n = int(input("Enter the value of n: "))
    e = int(input("Enter the value of e: "))
    c = int(input("Enter the ciphertext c: "))

    print("Enter the prime factors of n one by one. Type 'done' when finished:")
    primes = []
    while True:
        prime_input = input("Enter a prime factor: ")
        if prime_input.lower() == 'done':
            break
        try:
            prime = int(prime_input)
            primes.append(prime)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if not primes:
        print("No primes provided. Exiting.")
        return

    # Step to calculate d for each prime factor
    ds = [modinv(e, p - 1) for p in primes]

    # Initialize variables for Chinese Remainder Theorem
    ts = []
    xs = []

    m = primes[0]
    for i in range(1, len(primes)):
        ts.append(modinv(m % primes[i], primes[i]))
        m *= primes[i]

    for i in range(len(primes)):
        xs.append(pow(c % primes[i], ds[i], primes[i]))

    # Combine results using CRT
    x = xs[0]
    m = primes[0]

    for i in range(1, len(primes)):
        x += m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
        m *= primes[i]

    # Convert the result to hexadecimal and decode it
    decrypted_message = hex(x % n)[2:]
    try:
        print("Decrypted message:")
        print(bytes.fromhex(decrypted_message).decode('utf-8'))
    except ValueError:
        print("Decrypted result is not valid UTF-8 text.")
        print(f"Hexadecimal result: {decrypted_message}")

if __name__ == "__main__":
    main()
