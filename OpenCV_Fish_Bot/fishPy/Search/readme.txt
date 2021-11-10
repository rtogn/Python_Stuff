This is a fishing bot for a certain MMO game.
Dependencies: OpenCV2 and pyautogui

Note: THIS WILL CONTROLL MOUSE AND KEY MOVEMENTS 
You may need to adjust color settings in the graphics tab. I noticed the reclections on max settings for water caused issues, turn it to low or medium.
This is not a robust algorithm for detection.


How it works: 
	On loop:
		1) Cast rod (set to a specific key from hotbar in game)
		2) Scans middle sclice of screen top to bottom for the darkest color in green channel (almost always the bobber if no terrain in way)
		3) Move mouse to found location
		4) Calculate average change of pixel color until it reaches a certain threshold (splash animation for 'fish on line' causes
						a mostly white array of pixels which reduces the overall average color significantly)
		5) Click on bobber to collect item caught
	repeat!
	
Requirements for use:
	1) Stand near water and zoom in camera to first person. Hide UI (alt + Z)
	2) Angle viewpoint straight ahead in such a way that there arent other game objects on the screen besides water.
	3) Run program and alt tab back to game
	4) make sure it is finding the bobber and recognizing the change
	5) If it worked, walk away, it can run for as long as desired
	
Pros: Never been caught or banned by system with reasonable use. I think the lack of perfection helps, it will miss clicks once and awhile.
Cons: Awkward to use, color settings can cause issues, just doesn't work in certain areas, pretty slow pixel by pixels scan. 

I was going to make this really pattern match the bobber in the future but to be honest it worked so well I didn't have much incentive to 
update anything. I also no longer play this game so it would serve little purpose.

-RT
	
