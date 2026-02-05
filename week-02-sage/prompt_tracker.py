# prompt-tracker.py

# prompt-tracker.py

FILENAME = "my-prompts.txt"

def main():
    while True:
        print("\n--- PROMPT TRACKER MENU ---")
        print("1. Add Prompt")
        print("2. View All Prompts")
        print("3. Search Prompts")
        print("4. Delete a Prompt") # NEW OPTION
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # (Same as before: Append a new line)
            text = input("Enter the prompt text: ")
            category = input("Enter category (learning/creating/evaluating/other): ").lower()
            note = input("Enter a short note: ")

            with open(FILENAME, "a") as file:
                file.write(f"{category}|{text}|{note}\n")
            print("Prompt saved!")

        elif choice == "2":
            # (Same as before: Read and print)
            print("\n--- YOUR SAVED PROMPTS ---")
            try:
                with open(FILENAME, "r") as file:
                    for line in file:
                        category, text, note = line.strip().split("|")
                        print(f"[{category.upper()}] Prompt: {text}")
            except FileNotFoundError:
                print("No prompts saved yet.")

        elif choice == "3":
            # (Same as before: Search)
            keyword = input("Enter keyword: ").lower()
            try:
                with open(FILENAME, "r") as file:
                    for line in file:
                        if keyword in line.lower():
                            print(f"MATCH: {line.strip()}")
            except FileNotFoundError:
                print("No file found.")

        elif choice == "4":
            # --- DELETE A PROMPT ---
            try:
                # Step 1: Read all prompts into a list
                with open(FILENAME, "r") as file:
                    lines = file.readlines()
                
                if not lines:
                    print("Nothing to delete!")
                    continue

                # Step 2: Show prompts with a number so the user can pick one
                print("\nWhich prompt would you like to delete?")
                for index, line in enumerate(lines):
                    # enumerate gives us a count (0, 1, 2...) as we loop
                    print(f"{index + 1}. {line.strip()}")

                delete_choice = int(input("\nEnter the number to delete: "))
                
                # Step 3: Remove the chosen item from our list
                # We subtract 1 because lists start at index 0, but we showed 1 to the user
                removed_item = lines.pop(delete_choice - 1)
                
                # Step 4: Write the remaining list back to the file
                # Using "w" mode overwrites the file entirely
                with open(FILENAME, "w") as file:
                    file.writelines(lines)
                
                print(f"Deleted: {removed_item.strip()}")

            except (FileNotFoundError, IndexError, ValueError):
                print("Invalid selection or file not found.")

        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()