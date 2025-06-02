import random

words = (
    'apple', 'orange', 'banana', 'grape', 'cherry', 'melon', 'peach', 'pear', 'plum', 'kiwi',
    'carrot', 'onion', 'potato', 'tomato', 'broccoli', 'cabbage', 'lettuce', 'spinach', 'radish', 'pepper',
    'pizza', 'burger', 'sushi', 'taco', 'pasta', 'noodle', 'steak', 'salmon', 'chicken', 'bacon',
    'tiger', 'lion', 'zebra', 'elephant', 'giraffe', 'monkey', 'panda', 'koala', 'bear', 'rhino',
    'cat', 'dog', 'mouse', 'rabbit', 'fox', 'wolf', 'deer', 'goat', 'horse', 'sheep',
    'car', 'truck', 'train', 'plane', 'boat', 'bicycle', 'scooter', 'bus', 'jeep', 'subway',
    'table', 'chair', 'sofa', 'bed', 'shelf', 'lamp', 'desk', 'mirror', 'clock', 'couch',
    'phone', 'laptop', 'tablet', 'camera', 'speaker', 'mouse', 'keyboard', 'monitor', 'router', 'printer',
    'doctor', 'nurse', 'teacher', 'pilot', 'driver', 'chef', 'baker', 'engineer', 'artist', 'singer',
    'city', 'village', 'forest', 'desert', 'mountain', 'valley', 'island', 'river', 'ocean', 'lake',
    'spring', 'summer', 'autumn', 'winter', 'rain', 'snow', 'cloud', 'storm', 'wind', 'fog',
    'blue', 'red', 'green', 'yellow', 'purple', 'orange', 'black', 'white', 'pink', 'brown',
    'circle', 'square', 'triangle', 'rectangle', 'hexagon', 'cube', 'sphere', 'pyramid', 'line', 'dot',
    'pen', 'pencil', 'brush', 'eraser', 'ruler', 'paper', 'book', 'notebook', 'folder', 'marker',
    'gold', 'silver', 'bronze', 'copper', 'iron', 'steel', 'plastic', 'glass', 'wood', 'stone',
    'sun', 'moon', 'star', 'planet', 'comet', 'galaxy', 'asteroid', 'rocket', 'spaceship', 'satellite',
    'ant', 'bee', 'bug', 'fly', 'moth', 'worm', 'spider', 'crab', 'shrimp', 'lobster',
    'bread', 'cake', 'cookie', 'donut', 'muffin', 'waffle', 'pancake', 'cereal', 'yogurt', 'cheese',
    'violin', 'guitar', 'piano', 'drums', 'flute', 'trumpet', 'harp', 'saxophone', 'cello', 'clarinet',
    'shirt', 'pants', 'skirt', 'dress', 'jacket', 'coat', 'shoes', 'boots', 'hat', 'gloves',
    'king', 'queen', 'prince', 'princess', 'knight', 'wizard', 'witch', 'dragon', 'castle', 'sword',
    'robot', 'alien', 'zombie', 'ghost', 'vampire', 'monster', 'ninja', 'pirate', 'giant', 'fairy',
    'happy', 'sad', 'angry', 'excited', 'bored', 'scared', 'tired', 'nervous', 'funny', 'brave',
    'jump', 'run', 'walk', 'sleep', 'eat', 'drink', 'read', 'write', 'sing', 'dance',
    'clock', 'watch', 'calendar', 'map', 'globe', 'compass', 'thermometer', 'microscope', 'telescope', 'binoculars',
    'school', 'class', 'lesson', 'homework', 'exam', 'test', 'project', 'subject', 'teacher', 'student',
    'earth', 'mars', 'venus', 'jupiter', 'saturn', 'uranus', 'neptune', 'mercury', 'pluto', 'orbit',
    'milk', 'water', 'juice', 'coffee', 'tea', 'soda', 'lemonade', 'smoothie', 'wine', 'beer',
    'movie', 'music', 'game', 'show', 'series', 'book', 'novel', 'story', 'comic', 'magazine',
    'apple', 'peach', 'grape', 'melon', 'berry', 'plum', 'fig', 'date', 'mango', 'papaya',
    'train', 'track', 'station', 'ticket', 'engine', 'cabin', 'window', 'luggage', 'seat', 'conductor'
)

# dictionary of key:
hangman_art = {0: ('    ',
                   '    ',
                   '    '), 
               1: ('  *  ',
                   '     ',
                   '     '),
               2: ('  *  ',
                   '  |  ',
                   '     '), 
               3: ('  *  ',
                   ' /|  ',
                   '     '),
               4: ('  *  ',
                   ' /|\\',
                   '     '),
               5: ('  *  ',
                   ' /|\\',
                   ' /   '),
               6: ('  *  ',
                   ' /|\\',
                   ' / \\')}

def display_man(wrong_guesses):
    print('******************************')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print('******************************')

def display_hint(hint):
    print(' '.join(hint))
def display_answer(answer):
    print(' '.join(answer))

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input('Enter a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input!')
            continue # continue говорит: "не проверяй дальше, вернись к началу цикла."

        if guess in guessed_letters:
            print(f'{guess} is already in guessed')
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]== guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print('You win!')
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print('You lose!')
            is_running = False

if __name__ == '__main__':
    main()