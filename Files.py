def read_poets_file(filename):
    poets = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if parts[-1].isdigit():
                name = ' '.join(parts[:-1])
                birth_year = parts[-1]
            else:
                birth_year = parts[0]
                name = ' '.join(parts[1:])
            poets[name] = birth_year
    return poets

def write_sorted_poets(poets, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        for name in sorted(poets):
            file.write(f"{name} {poets[name]}\n")

def main():
    input_filename = 'IranianPoets.txt'
    output_filename = 'HW4-Output.txt'
    poets = read_poets_file(input_filename)
    write_sorted_poets(poets, output_filename)

if __name__ == "__main__":
    main()
