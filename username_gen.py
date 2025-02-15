import random

def generate_username(numbers, characters, min_length=8):
    username_components = []
    adjectives = ["Cool", "Happy", "Funky", "Fantastic", "Fierce", 
                  "Mysterious", "Brave", "Swift", "Clever", "Witty"]
    nouns = ["Tiger", "Lion", "Shark", "Dragon", "Panda", 
             "Eagle", "Wolf", "Phoenix", "Knight", "Wizard"]
    special_chars = "!@#$%^&*"

    username_components.append(random.choice(adjectives))
    username_components.append(random.choice(nouns))
    
    if numbers == "yes":
        number_length = random.choice([2,3])
        username_components.append(str(random.randint(10**(number_length-1), (10**number_length)-1)))
    
    if characters == "yes":
        username_components.append(random.choice(special_chars))
    
    username = ''.join(username_components)
    current_length = len(username)
    
    if current_length < min_length:
        allowed_fillers = []
        if numbers == "yes":
            allowed_fillers += [chr(i) for i in range(ord('0'), ord('9')+1)]
        if characters == "yes":
            allowed_fillers += list(special_chars)
        
        if allowed_fillers:
            while len(username) < min_length:
                username += random.choice(allowed_fillers)
        else:
            print("Username cannot be extended without numbers or special characters.")
    
    return username

def save_username(username, filename="usernames.txt"):
    try:
        with open(filename, "a") as file:
            file.write(username + "\n")
    except Exception as e:
        print(f"Error saving username to file: {e}")

def main():
    print("Welcome to the Username Generator!")
    while True:
        include_numbers = input("Do you want to include numbers? (yes/no): ").strip().lower()
        include_special = input("Do you want to include special characters? (yes/no): ").strip().lower()
        
        while True:
            min_length = input("What's the minimum length for your username? (default 8): ").strip()
            try:
                min_length = max(int(min_length), 5)
                break
            except:
                print("Please enter a valid number.")
        
        generated_username = generate_username(include_numbers, include_special, min_length)
        print(f"\nGenerated Username: {generated_username}\n")
        
        save_username(generated_username)
        
        another = input("Generate another username? (yes/no): ").strip().lower()
        if another != "yes":
            print("Thank you for using the Username Generator!")
            break

if __name__ == "__main__":
    main()