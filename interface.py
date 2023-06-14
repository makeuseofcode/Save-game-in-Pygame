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
# Game variables
save_slots = ['Slot 1', 'Slot 2', 'Slot 3']
selected_slot = None
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Show save slots
                selected_slot = None
                for i, slot in enumerate(save_slots):
                    print(f"Save Slot {i+1}: {slot}")
                print("Choose a slot to save the game.")

            if event.key == pygame.K_l:
                # Show save slots
                selected_slot = None
                for i, slot in enumerate(save_slots):
                    print(f"Save Slot {i+1}: {slot}")
                print("Choose a slot to load the game.")

            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                # Save or load game based on the selected slot
                slot_index = event.key - pygame.K_1
                selected_slot = save_slots[slot_index]
                
                save_game_state(game_state, f"{selected_slot}.pickle")
                print(f"Game saved in {selected_slot}!")

            if event.key in [pygame.K_a, pygame.K_b, pygame.K_c]: 
                print("Select Slot:- a - Slot 1 , b - Slot 3, c - Slot 3")
                slot_index = event.key - pygame.K_a
                selected_slot = save_slots[slot_index] 
                game_state = load_game_state(f"{selected_slot}.pickle")
                player_x = game_state['player_x']
                print(f"Game loaded from {selected_slot}!")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        game_state['player_x'] = player_x
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        game_state['player_x'] = player_x

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(window, (255, 255, 255), (player_x, player_y, 50, 50))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
