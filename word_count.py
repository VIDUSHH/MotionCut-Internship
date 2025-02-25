def count_words():
    while True:
        # Prompt user to enter a sentence
        sentence = input("Enter a sentence (or type 'exit' to quit): ")
        
        # Exit condition to break the loop
        if sentence.lower() == 'exit':
            print("Exiting the program...")
            break
        
        # Check if the input is empty
        if not sentence.strip():
            print("Please enter a sentence.")
            continue
        
        # Split sentence into words
        words = sentence.split()
        print("Words in the sentence:", words)
        
        # Filter words containing only alphabets
        filtered_words = [word for word in words if word.isalpha()]
        print("Filtered words (only alphabets):", filtered_words)
        
        # Count the valid words
        word_count = len(filtered_words)
        print("Word count:", word_count)

# Call the function to run the word counting program
count_words()
