#Step 2

import random
import hangmanlogo
import hangmanwords


print(hangmanlogo.logo)
stages = hangmanlogo.stages


word_list = hangmanwords.word_list
chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.')

lives = 6
display = []
word_len = len(chosen_word)

for _ in range(word_len):
    display += "_"
print(display)


while "_" in display:

    guess = input("Guess a letter: ").lower()
    if guess not in display:  
        for position in range(word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter  
        
        if guess not in chosen_word:
            print(stages[lives])
            print(f"The letter '{guess}' is not in the word")
            lives -= 1
            if lives < 0:
                break
    else:
        print("You've already used that letter!")    
        
    

    print(display)
    
if lives < 0:
    print(f"You've lost! The word was '{chosen_word}'.")

else:
    print("You've won!")
