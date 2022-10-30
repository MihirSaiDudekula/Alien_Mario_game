import pygame
from sys import exit

def display_score():
	current_time=pygame.time.get_ticks() 
	shown_time=current_time-start_time
	score_surf=text_font.render(f"{show_time}",False,"Green")
	score_rect=score_surf.get_rect(center=(400,50))
	screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
player_gravity=0
game_active=True
start_time=0

text_font=pygame.font.Font("E:\\coding\\Developed Games\\UltimatePygameIntro\\Pixeltype.ttf",50)
sky_surface=pygame.image.load("E:\\coding\\Developed Games\\UltimatePygameIntro\\Sky.png").convert()
ground_surface=pygame.image.load("E:\\coding\\Developed Games\\UltimatePygameIntro\\ground.png").convert()
# score_surf=text_font.render("MY GAME",False,"Green")
# score_rect=score_surf.get_rect(center=(400,50))
snail_surface=pygame.image.load("E:\\coding\\Developed Games\\UltimatePygameIntro\\snail1.png").convert_alpha()
snail_rect=snail_surface.get_rect(midbottom=(600,300))
player_surf=pygame.image.load("E:\\coding\\Developed Games\\UltimatePygameIntro\\player_walk_1.png").convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80,300))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		# if event.type== pygame.MOUSEMOTION:
		# 	print(event.pos)
		# if event.type== pygame.MOUSEBUTTONDOWN:
		# 	print("you clicked")
		# if event.type== pygame.MOUSEMOTION:
		# 	if 	player_rect.collidepoint(event.pos):
		# 		print("collision")

	if game_active:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and player_rect.bottom>=300:
			player_gravity=-20
	else:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			start_time=current_time
			game_active=True
			snail_rect.left=800
			

	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		# pygame.draw.rect(screen,"Black",score_rect)
		# pygame.draw.rect(screen,"Black",score_rect,10)
		# pygame.draw.line(screen,"Gold",(0,0),pygame.mouse.get_pos(),5)
		# pygame.draw.ellipse(screen,"Gold",pygame.Rect(50,200,100,100))
		#pygame.Rect(xcoord,ycoord,width,height)
		# screen.blit(score_surf,score_rect)
		display_score()
		snail_rect.left=snail_rect.left-4
		if snail_rect.left<-15:
			snail_rect.left=815
		screen.blit(snail_surface,snail_rect)
		screen.blit(player_surf,player_rect)
		#player_rect.left=player_rect.left+1
		player_gravity+=1
		player_rect.y+=player_gravity
		if player_rect.bottom >=300:
			player_rect.bottom=300
		if snail_rect.colliderect(player_rect)==1:
			game_active=False

	else:
		screen.fill("Yellow")
	#player_rect.y--->y coordinate -----> increases
	# if player_rect.colliderect(snail_rect)==1:
	# 	print("collision")
	# mouse_pos=pygame.mouse.get_pos()
	# if 	player_rect.collidepoint((mouse_pos)):
	# 	print("collision")
	
	pygame.display.update()
	clock.tick(60)

