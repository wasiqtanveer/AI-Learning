# property decorator

import pygame
import random
import sys
import os
import math
from pygame.math import Vector2
from enum import Enum

# Add numpy import at the top level
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

class Direction(Enum):
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)

class SnakeGame:
    def __init__(self, width=800, height=600, cell_size=40):
        pygame.init()
        pygame.mixer.init()  # Initialize sound mixer
        
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        
        # Try to set a game icon
        try:
            icon = pygame.Surface((32, 32))
            icon.fill((0, 200, 0))
            pygame.draw.rect(icon, (0, 100, 0), (8, 8, 16, 16))
            pygame.display.set_icon(icon)
        except:
            pass  # If icon setting fails, just continue
            
        self._clock = pygame.time.Clock()
        self._game_over = False
        self._score = 0
        self._high_score = 0
        self._font = pygame.font.SysFont("Arial", 20, bold=True)
        self._big_font = pygame.font.SysFont("Arial", 40, bold=True)
        
        # Animation variables
        self._food_animation = 0
        self._snake_animation = 0
        
        # Background grid
        self._grid_visible = True
        
        # Initial snake (3 body parts)
        self._snake = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self._direction = Direction.RIGHT
        self._new_direction = Direction.RIGHT
        
        # Food
        self._food = self._generate_food_position()
        self._rainbow_colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), 
                               (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
        self._current_color_index = 0
        
        # Colors
        self._bg_color = (15, 35, 15)
        self._grid_color = (30, 50, 30)
        self._snake_colors = [(0, 180, 0), (0, 200, 0), (0, 220, 0)]  # Multiple green shades
        self._food_color = (200, 0, 0)
        self._text_color = (220, 220, 220)
        
        # Particle effects for food collection
        self._particles = []
        
        # Load sounds
        self._load_sounds()
        
        # Game states
        self._paused = False
        self._intro_screen = True
        
    def _load_sounds(self):
        self._sounds = {}
        try:
            # Create a sounds directory if it doesn't exist
            sounds_dir = "sounds"
            if not os.path.exists(sounds_dir):
                os.makedirs(sounds_dir)
                
            # Define sound paths
            eat_sound_path = os.path.join(sounds_dir, "eat.wav")
            crash_sound_path = os.path.join(sounds_dir, "crash.wav")
            game_over_path = os.path.join(sounds_dir, "game_over.wav")
            
            # Create empty sounds if they don't exist
            self._create_default_sound(eat_sound_path)
            self._create_default_sound(crash_sound_path)
            self._create_default_sound(game_over_path)
            
            # Load sounds
            self._sounds["eat"] = pygame.mixer.Sound(eat_sound_path)
            self._sounds["crash"] = pygame.mixer.Sound(crash_sound_path)
            self._sounds["game_over"] = pygame.mixer.Sound(game_over_path)
            
            # Set volumes
            self._sounds["eat"].set_volume(0.5)
            self._sounds["crash"].set_volume(0.4)
            self._sounds["game_over"].set_volume(0.6)
            
        except Exception as e:
            print(f"Sound loading error: {e}")
            # Create empty sounds dictionary if loading fails
            self._sounds = {
                "eat": None,
                "crash": None,
                "game_over": None
            }
    
    def _create_default_sound(self, path):
        # Create a simple sound file if it doesn't exist
        if not os.path.exists(path):
            try:
                sound_name = os.path.basename(path)[:-4]  # Remove .wav extension
                
                if not NUMPY_AVAILABLE:
                    print(f"NumPy not available, cannot generate sound: {path}")
                    return
                
                # Use pygame to create a simple sound
                sample_rate = 44100
                duration = 0.2  # seconds
                
                if sound_name == "eat":
                    # Create rising tone for eat sound
                    buf = self._generate_rising_tone(sample_rate, duration)
                elif sound_name == "crash":
                    # Create noise burst for crash
                    buf = self._generate_noise_burst(sample_rate, duration)
                elif sound_name == "game_over":
                    # Create descending tone for game over
                    buf = self._generate_descending_tone(sample_rate, duration * 2)
                else:
                    buf = self._generate_simple_tone(sample_rate, duration)
                
                # Make sure buf is not None before proceeding
                if buf is not None:
                    # Save the sound to a file - using a different method since .save() is not available
                    sound = pygame.sndarray.make_sound(buf)
                    # Write WAV file using pygame's mixer
                    pygame.mixer.Sound.play(sound)
                    pygame.mixer.Sound.stop(sound)
                else:
                    print(f"Could not generate sound buffer for {path}")
                
                # Alternative approach for creating sound files, using system functions
                if sys.platform.startswith('win'):
                    # Windows-specific code to create a simple sound file
                    try:
                        import winsound
                        if sound_name == "eat":
                            winsound.Beep(880, 100)
                        elif sound_name == "crash":
                            winsound.Beep(220, 100)
                        elif sound_name == "game_over":
                            winsound.Beep(440, 300)
                    except ImportError:
                        pass
            except Exception as e:
                print(f"Error creating sound {path}: {e}")
    
    def _generate_simple_tone(self, sample_rate, duration):
        # Generate a simple sine wave
        if not NUMPY_AVAILABLE:
            return None
            
        samples = int(sample_rate * duration)
        buf = np.zeros((samples, 2), dtype=np.int16)
        frequency = 440  # A4 tone
        
        for i in range(samples):
            t = i / sample_rate
            value = int(32767 * 0.5 * math.sin(2 * math.pi * frequency * t))
            buf[i][0] = value
            buf[i][1] = value
            
        return buf
    
    def _generate_rising_tone(self, sample_rate, duration):
        # Generate a rising tone
        if not NUMPY_AVAILABLE:
            return None
            
        samples = int(sample_rate * duration)
        buf = np.zeros((samples, 2), dtype=np.int16)
        start_freq = 220
        end_freq = 880
        
        for i in range(samples):
            t = i / sample_rate
            # Linear interpolation between frequencies
            freq = start_freq + (end_freq - start_freq) * (i / samples)
            value = int(32767 * 0.5 * math.sin(2 * math.pi * freq * t))
            # Apply fade out
            amplitude = 1.0 - (i / samples) ** 2
            buf[i][0] = int(value * amplitude)
            buf[i][1] = int(value * amplitude)
            
        return buf
    
    def _generate_descending_tone(self, sample_rate, duration):
        # Generate a descending tone
        if not NUMPY_AVAILABLE:
            return None
            
        samples = int(sample_rate * duration)
        buf = np.zeros((samples, 2), dtype=np.int16)
        start_freq = 660
        end_freq = 220
        
        for i in range(samples):
            t = i / sample_rate
            # Linear interpolation between frequencies
            freq = start_freq + (end_freq - start_freq) * (i / samples)
            value = int(32767 * 0.5 * math.sin(2 * math.pi * freq * t))
            buf[i][0] = value
            buf[i][1] = value
            
        return buf
    
    def _generate_noise_burst(self, sample_rate, duration):
        # Generate a noise burst
        if not NUMPY_AVAILABLE:
            return None
            
        samples = int(sample_rate * duration)
        buf = np.zeros((samples, 2), dtype=np.int16)
        
        for i in range(samples):
            # Random noise with fade out
            amplitude = 1.0 - (i / samples)
            value = int(32767 * 0.7 * random.uniform(-1, 1) * amplitude)
            buf[i][0] = value
            buf[i][1] = value
            
        return buf

    @property
    def score(self):
        return self._score
    
    @property
    def game_over(self):
        return self._game_over
    
    @property
    def grid_width(self):
        return self._width // self._cell_size
    
    @property
    def grid_height(self):
        return self._height // self._cell_size
    
    def _generate_food_position(self):
        while True:
            position = Vector2(
                random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_height - 1)
            )
            if position not in self._snake:
                return position
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._handle_key_press(event.key)
    
    def _handle_key_press(self, key):
        # Game controls
        if key == pygame.K_p:
            self._paused = not self._paused
            
        if key == pygame.K_g:
            self._grid_visible = not self._grid_visible
            
        if self._intro_screen and key == pygame.K_RETURN:
            self._intro_screen = False
            
        # Can't move in the opposite direction
        if key == pygame.K_UP and self._direction != Direction.DOWN:
            self._new_direction = Direction.UP
        elif key == pygame.K_DOWN and self._direction != Direction.UP:
            self._new_direction = Direction.DOWN
        elif key == pygame.K_LEFT and self._direction != Direction.RIGHT:
            self._new_direction = Direction.LEFT
        elif key == pygame.K_RIGHT and self._direction != Direction.LEFT:
            self._new_direction = Direction.RIGHT
    
    def _move_snake(self):
        # Update direction
        self._direction = self._new_direction
        
        # Move snake by adding new head and removing tail
        head = self._snake[0] + self._direction.value
        self._snake.insert(0, head)
        
        # Check if snake ate food
        if self._snake[0] == self._food:
            self._food = self._generate_food_position()
            self._score += 1
            if self._score > self._high_score:
                self._high_score = self._score
            
            # Play eat sound
            if self._sounds["eat"]:
                self._sounds["eat"].play()
                
            # Add particles
            self._create_food_particles()
        else:
            self._snake.pop()
    
    def _create_food_particles(self):
        # Create particle effects when food is eaten
        food_pos_x = self._food.x * self._cell_size + self._cell_size // 2
        food_pos_y = self._food.y * self._cell_size + self._cell_size // 2
        
        for _ in range(15):  # Create 15 particles
            speed = random.uniform(1, 3)
            angle = random.uniform(0, 2 * math.pi)
            velocity = [speed * math.cos(angle), speed * math.sin(angle)]
            size = random.randint(2, 5)
            color = random.choice(self._rainbow_colors)
            life = random.randint(20, 40)  # Particle lifetime in frames
            
            self._particles.append({
                "pos": [food_pos_x, food_pos_y],
                "velocity": velocity,
                "size": size,
                "color": color,
                "life": life
            })
    
    def _update_particles(self):
        # Update all particles and remove dead ones
        i = 0
        while i < len(self._particles):
            p = self._particles[i]
            p["pos"][0] += p["velocity"][0]
            p["pos"][1] += p["velocity"][1]
            p["life"] -= 1
            
            if p["life"] <= 0:
                self._particles.pop(i)
            else:
                i += 1
    
    def _draw_particles(self):
        # Draw all active particles
        for p in self._particles:
            # Fade out particles as they age
            alpha = int(255 * (p["life"] / 40))
            color = p["color"][:3] + (alpha,)
            
            pygame.draw.circle(
                self._screen, 
                color, 
                (int(p["pos"][0]), int(p["pos"][1])), 
                p["size"]
            )
    
    def _check_collision(self):
        # Check if snake hit the wall
        if (self._snake[0].x < 0 or self._snake[0].x >= self.grid_width or
                self._snake[0].y < 0 or self._snake[0].y >= self.grid_height):
            if not self._game_over:
                self._handle_game_over()
        
        # Check if snake hit itself
        if self._snake[0] in self._snake[1:]:
            if not self._game_over:
                self._handle_game_over()
    
    def _handle_game_over(self):
        self._game_over = True
        # Play crash and game over sounds
        if self._sounds["crash"]:
            self._sounds["crash"].play()
        if self._sounds["game_over"]:
            pygame.time.delay(300)  # Small delay before game over sound
            self._sounds["game_over"].play()
    
    def _draw_background(self):
        # Fill background
        self._screen.fill(self._bg_color)
        
        # Draw grid if enabled
        if self._grid_visible:
            for x in range(0, self._width, self._cell_size):
                pygame.draw.line(self._screen, self._grid_color, (x, 0), (x, self._height))
            for y in range(0, self._height, self._cell_size):
                pygame.draw.line(self._screen, self._grid_color, (0, y), (self._width, y))
    
    def _draw_snake(self):
        # Draw snake with gradient and animated effect
        for i, segment in enumerate(self._snake):
            # Choose color - head is brightest, tail gradually darker
            color_idx = min(i % len(self._snake_colors), len(self._snake_colors) - 1)
            color = self._snake_colors[color_idx]
            
            # Base rectangle
            rect = pygame.Rect(
                segment.x * self._cell_size,
                segment.y * self._cell_size,
                self._cell_size, self._cell_size
            )
            
            # Round corners for the head
            if i == 0:  # Head
                pygame.draw.rect(self._screen, color, rect, border_radius=10)
                
                # Draw eyes
                eye_size = self._cell_size // 8
                eye_offset = self._cell_size // 4
                
                # Position eyes based on direction
                if self._direction == Direction.RIGHT:
                    left_eye = (rect.right - eye_offset, rect.top + eye_offset)
                    right_eye = (rect.right - eye_offset, rect.bottom - eye_offset)
                elif self._direction == Direction.LEFT:
                    left_eye = (rect.left + eye_offset, rect.top + eye_offset)
                    right_eye = (rect.left + eye_offset, rect.bottom - eye_offset)
                elif self._direction == Direction.UP:
                    left_eye = (rect.left + eye_offset, rect.top + eye_offset)
                    right_eye = (rect.right - eye_offset, rect.top + eye_offset)
                else:  # DOWN
                    left_eye = (rect.left + eye_offset, rect.bottom - eye_offset)
                    right_eye = (rect.right - eye_offset, rect.bottom - eye_offset)
                
                pygame.draw.circle(self._screen, (255, 255, 255), left_eye, eye_size)
                pygame.draw.circle(self._screen, (255, 255, 255), right_eye, eye_size)
                
                # Draw pupils
                pupil_size = eye_size // 2
                pygame.draw.circle(self._screen, (0, 0, 0), left_eye, pupil_size)
                pygame.draw.circle(self._screen, (0, 0, 0), right_eye, pupil_size)
                
            else:  # Body
                # Determine if this segment is a corner
                is_corner = False
                if i > 0 and i < len(self._snake) - 1:
                    prev_dir = self._snake[i-1] - self._snake[i]
                    next_dir = self._snake[i] - self._snake[i+1]
                    is_corner = prev_dir.x != next_dir.x and prev_dir.y != next_dir.y
                
                # Draw body segments, corners with slightly rounded edges
                if is_corner:
                    pygame.draw.rect(self._screen, color, rect, border_radius=5)
                else:
                    pygame.draw.rect(self._screen, color, rect)
                
                # Inner segment for 3D effect
                inner_size = 8
                inner_rect = pygame.Rect(
                    segment.x * self._cell_size + inner_size // 2,
                    segment.y * self._cell_size + inner_size // 2,
                    self._cell_size - inner_size,
                    self._cell_size - inner_size
                )
                
                # Lighten the inner color
                inner_color = tuple(min(c + 40, 255) for c in color)
                pygame.draw.rect(self._screen, inner_color, inner_rect, 
                               border_radius=5 if is_corner else 0)
    
    def _draw_food(self):
        # Rainbow animated food
        self._food_animation = (self._food_animation + 0.1) % 360
        self._current_color_index = (self._current_color_index + 0.05) % len(self._rainbow_colors)
        
        # Interpolate between colors
        idx1 = int(self._current_color_index)
        idx2 = (idx1 + 1) % len(self._rainbow_colors)
        t = self._current_color_index - idx1
        
        c1 = self._rainbow_colors[idx1]
        c2 = self._rainbow_colors[idx2]
        
        color = tuple(int(c1[i] * (1-t) + c2[i] * t) for i in range(3))
        
        # Pulsing effect
        size_mod = math.sin(self._food_animation) * 4
        
        # Draw the food
        center = (
            int(self._food.x * self._cell_size + self._cell_size // 2),
            int(self._food.y * self._cell_size + self._cell_size // 2)
        )
        
        # Draw an apple shape
        apple_radius = self._cell_size // 2 - 4 + size_mod
        pygame.draw.circle(self._screen, color, center, apple_radius)
        
        # Apple stem
        stem_color = (34, 139, 34)  # Forest green
        stem_points = [
            (center[0], center[1] - apple_radius),
            (center[0] - 3, center[1] - apple_radius - 7),
            (center[0] + 3, center[1] - apple_radius - 7),
        ]
        pygame.draw.polygon(self._screen, stem_color, stem_points)
        
        # Small shine on the apple
        shine_pos = (center[0] + apple_radius // 3, center[1] - apple_radius // 3)
        pygame.draw.circle(self._screen, (255, 255, 255, 128), shine_pos, apple_radius // 4)
    
    def _draw_score(self):
        # Draw score and high score
        score_text = self._font.render(f"Score: {self._score}", True, self._text_color)
        high_score_text = self._font.render(f"High Score: {self._high_score}", True, self._text_color)
        self._screen.blit(score_text, (10, 10))
        self._screen.blit(high_score_text, (self._width - high_score_text.get_width() - 10, 10))
        
        # Draw instructions
        if not self._game_over and not self._intro_screen:
            instructions = self._font.render("P: Pause   G: Toggle Grid", True, self._text_color)
            self._screen.blit(instructions, (self._width // 2 - instructions.get_width() // 2, 10))
            
        # Draw paused message
        if self._paused and not self._game_over:
            paused_text = self._big_font.render("PAUSED", True, self._text_color)
            text_rect = paused_text.get_rect(center=(self._width // 2, self._height // 2))
            
            # Draw semi-transparent background
            s = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
            s.fill((0, 0, 0, 128))
            self._screen.blit(s, (0, 0))
            
            self._screen.blit(paused_text, text_rect)
            
            resume_text = self._font.render("Press P to Resume", True, self._text_color)
            resume_rect = resume_text.get_rect(center=(self._width // 2, self._height // 2 + 50))
            self._screen.blit(resume_text, resume_rect)
        
        # Draw game over message
        if self._game_over:
            # Semi-transparent overlay
            s = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
            s.fill((0, 0, 0, 180))
            self._screen.blit(s, (0, 0))
            
            game_over_text = self._big_font.render("GAME OVER", True, (255, 50, 50))
            text_rect = game_over_text.get_rect(center=(self._width // 2, self._height // 2 - 40))
            self._screen.blit(game_over_text, text_rect)
            
            final_score = self._font.render(f"Your Score: {self._score}", True, self._text_color)
            score_rect = final_score.get_rect(center=(self._width // 2, self._height // 2 + 10))
            self._screen.blit(final_score, score_rect)
            
            restart_text = self._font.render("Press R to Restart", True, self._text_color)
            restart_rect = restart_text.get_rect(center=(self._width // 2, self._height // 2 + 50))
            self._screen.blit(restart_text, restart_rect)
    
    def _draw_intro_screen(self):
        # Draw intro/title screen
        self._screen.fill(self._bg_color)
        
        # Draw animated title
        title_color = (0, 200, 0)
        title_pulse = math.sin(pygame.time.get_ticks() * 0.005) * 20 + 235
        title_color_pulsed = (0, min(255, int(title_pulse)), 0)
        
        title_font = pygame.font.SysFont("Arial", 60, bold=True)
        title_text = title_font.render("SNAKE GAME", True, title_color_pulsed)
        title_rect = title_text.get_rect(center=(self._width // 2, self._height // 3))
        self._screen.blit(title_text, title_rect)
        
        # Draw instructions
        instructions = [
            "Use Arrow Keys to move",
            "Eat food to grow",
            "Don't hit walls or yourself",
            "P: Pause game",
            "G: Toggle grid",
            "R: Restart after game over"
        ]
        
        y_offset = self._height // 2
        for instruction in instructions:
            text = self._font.render(instruction, True, self._text_color)
            rect = text.get_rect(center=(self._width // 2, y_offset))
            self._screen.blit(text, rect)
            y_offset += 30
        
        # Start button
        y_pos = self._height * 3 // 4
        start_text = self._big_font.render("Press ENTER to Start", True, self._text_color)
        start_rect = start_text.get_rect(center=(self._width // 2, y_pos))
        
        # Blinking effect
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            self._screen.blit(start_text, start_rect)
    
    def _draw(self):
        if self._intro_screen:
            self._draw_intro_screen()
        else:
            self._draw_background()
            self._draw_snake()
            self._draw_food()
            self._draw_particles()
            self._draw_score()
        
        pygame.display.update()
    
    def _restart(self):
        self._snake = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self._direction = Direction.RIGHT
        self._new_direction = Direction.RIGHT
        self._food = self._generate_food_position()
        self._score = 0
        self._game_over = False
        self._particles = []
    
    def run(self):
        while True:
            self._handle_events()
            
            # Handle restart
            keys = pygame.key.get_pressed()
            if self._game_over and keys[pygame.K_r]:
                self._restart()
            
            # Update game state if not paused, game over, or intro screen
            if not self._paused and not self._game_over and not self._intro_screen:
                self._move_snake()
                self._check_collision()
                
            # Always update animations and particles
            self._update_particles()
            
            self._draw()
            self._clock.tick(10)  # Controls game speed

if __name__ == "__main__":
    game = SnakeGame()
    game.run()