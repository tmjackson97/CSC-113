FILENAME = "my-prompts.txt"

def main():
    while True:
        # 1. Show the Menu
        print("\n--- PROMPT TRACKER MENU ---")
        print("1. Add Prompt")
        print("2. View All Prompts")
        print("3. Search Prompts")
        print("4. Delete a Prompt")  
        print("5. Quit")             
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            text = input("Enter the prompt text: ")
            print("Categories: learning, creating, evaluating, other")
            category = input("Enter category: ").lower()
            note = input("Enter a short note about when to use it: ")

            # 'a' mode appends to the file so we don't lose old data
            with open(FILENAME, "a") as file:
                file.write(f"{category}|{text}|{note}\n")
            print("Prompt saved!")

        elif choice == "2": # Fixed the indentation here!
            print("\n--- YOUR SAVED PROMPTS ---")
            try:
                with open(FILENAME, "r") as file:
                    for line in file:
                        clean_line = line.strip()
                        if not clean_line:
                            continue
                        try:
                            # We split the line back into parts using the pipe
                            category, text, note = clean_line.split("|")
                            print(f"[{category.upper()}]")
                            print(f"  Prompt: {text}")
                            print(f"  Note: {note}")
                            print("-" * 25)
                        except ValueError:
                            print(f"Skipping a messy line: {clean_line}")
            except FileNotFoundError:
                print("No prompts saved yet! Add one first.")

        elif choice == "3":
            keyword = input("Enter a keyword to search for: ").lower()
            found = False
            try:
                with open(FILENAME, "r") as file:
                    for line in file:
                        if keyword in line.lower():
                            # Re-using the split logic for searching
                            parts = line.strip().split("|")
                            if len(parts) == 3:
                                category, text, note = parts
                                print(f"\nMATCH FOUND:")
                                print(f"[{category}] {text}")
                                found = True
                if not found:
                    print("No matching prompts found.")
            except FileNotFoundError:
                print("No file found to search.")

        elif choice == "4":
            try:
                # We read the whole file into a list to delete one item
                with open(FILENAME, "r") as file:
                    lines = file.readlines()
                
                if not lines:
                    print("Nothing to delete!")
                    continue
                    
                print("\nWhich prompt would you like to delete?")
                for index, line in enumerate(lines):
                    if line.strip():
                        print(f"{index + 1}. {line.strip()}")

                delete_choice = int(input("\nEnter the number to delete: "))
                
                # pop() removes the item at that specific index
                removed_item = lines.pop(delete_choice - 1)
                
                # 'w' mode overwrites the file with our new, smaller list
                with open(FILENAME, "w") as file:
                    file.writelines(lines)
                
                print(f"Successfully removed: {removed_item.strip()}")

            except FileNotFoundError:
                print("No prompts file found yet.")
            except (IndexError, ValueError):
                print("Sorry, that wasn't a valid number from the list.")

        elif choice == "5":
            print("Goodbye!")
            break 

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
