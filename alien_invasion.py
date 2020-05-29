import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
 
def run_game():
	#Initialize pygame,settings, and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasions")
	
	#Make the play button.
	play_button = Button(ai_settings, screen, "Play")
	
	#Create an instance to store the game statistics.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	icon = pygame.image.load('images/rocket.bmp')
	pygame.display.set_icon(icon)
	
	# Set the background color.
	bg_color = (230, 230, 230) 
	
	# Make a ship, group of bullets ad a group of aliens.
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
			aliens, bullets)
	
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship,
				aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
				bullets)
			
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
			bullets, play_button)
		
run_game()
