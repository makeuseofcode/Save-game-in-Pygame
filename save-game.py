import pygame
import pickle

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Save and Load System Tutorial")

# Game variables
player_x = 400
player_y = 500
num_save_slots = 3
selected_slot = 0
player_speed = 5
game_state = {
    'player_x': player_x,
    'player_y': player_y
}

# Save game state
def save_game_state(game_state, file_name):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(game_state, file)
            print("Game state saved successfully!")
    except IOError:
        print("Error: Unable to save game state.")

# Load game state
def load_game_state(file_name):
    try:
        with open(file_name, 'rb') as file:
            game_state = pickle.load(file)
            print("Game state loaded successfully!")
            return game_state
    except (IOError, pickle.UnpicklingError):
        print("Error: Unable to load game state.")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        game_state['player_x'] = player_x
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        game_state['player_x'] = player_x

    if keys[pygame.K_s]:
        save_game_state(game_state, 'save_game.pickle')
    if keys[pygame.K_l]:
        game_state = load_game_state('save_game.pickle')
        player_x = game_state['player_x']

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(window, (255, 255, 255), (player_x, player_y, 50, 50))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
