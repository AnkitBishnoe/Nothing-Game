import time
import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    """Print game title"""
    print("=" * 50)
    print("         NOTHING GAME")
    print("=" * 50)
    print("\nWelcome to the most interactive game ever!")
    print("Instructions: Just... play.\n")

def play_nothing_game():
    """The main nothing game loop"""
    clear_screen()
    print_title()
    
    score = 0
    level = 1
    
    while True:
        print(f"Level: {level} | Score: {score}")
        print("\nWhat would you like to do?")
        print("1. Do nothing")
        print("2. Do absolutely nothing")
        print("3. Do literally nothing")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n✨ You did nothing... ✨")
            score += 0
            level += 1
            time.sleep(1)
        elif choice == "2":
            print("\n🎯 You did absolutely nothing! Great job!")
            score += 0
            level += 1
            time.sleep(1)
        elif choice == "3":
            print("\n🏆 You literally did nothing! Perfect!")
            score += 0
            level += 1
            time.sleep(1)
        elif choice == "4":
            print("\n👋 Thanks for playing... or not playing... NOTHING GAME!")
            print(f"Final Score: {score} | Final Level: {level}")
            print("You did nothing brilliantly! 🎉\n")
            break
        else:
            print("\n❌ Invalid choice. Try doing nothing instead.\n")
            time.sleep(1)
        
        clear_screen()
        print_title()

if __name__ == "__main__":
    try:
        play_nothing_game()
    except KeyboardInterrupt:
        print("\n\n👋 You quit by doing... nothing special. Goodbye!")


