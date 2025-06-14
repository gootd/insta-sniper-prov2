
import random
import string

def generate_random_quads(count=50):
    results = []
    for _ in range(count):
        results.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=4)))
    return results

def generate_five_letter_repeats(count=50):
    results = []
    for _ in range(count):
        c = random.choice(string.ascii_lowercase)
        results.append(c * 5)
        results.append(c * 4 + random.choice(string.digits))
        results.append(c * 3 + random.choice(string.digits) * 2)
    return results

def generate_five_letter_premium(count=50):
    patterns = []
    for _ in range(count):
        part1 = ''.join(random.choices(string.ascii_lowercase, k=3))
        part2 = ''.join(random.choices(string.digits, k=2))
        patterns.append(part1 + part2)
        patterns.append(part2 + part1)
        mix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        patterns.append(mix)
    return patterns

def generate_semi_quad_five(count=50):
    results = []
    separators = ['.', '_']
    for _ in range(count):
        part1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        sep = random.choice(separators)
        part2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=1))
        username = part1 + sep + part2
        if len(username) == 5:
            results.append(username)
    return results

def generate_all_usernames():
    return list(set(
        generate_random_quads() +
        generate_five_letter_repeats() +
        generate_five_letter_premium() +
        generate_semi_quad_five()
    ))
