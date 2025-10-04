import Levenshtein

# "event_name": (total_choices, selected_choice) # "choice1 description", "choice 2 description", and so on.
EVENT_DATABASE = {
# [SUPPORTS]
# Mejiro Ryan
    "(❯) Flustered Afternoon Tea!": (2,1), # "Energy +10 Mood +1", "Wit +10 Skill points +15 Pace Chaser Savvy ○ hint +3"
    "My Muscles and Me, Onward to Tomorrow!": (2,2), # "Energy -10 Power +15 Mejiro Ryan bond +5", "Maximum Energy +4 Power +5 Mejiro Ryan bond +5"
    "It's Not Like I Like Romance!": (2,2), # "Pace Strategy hint +1 Mejiro Ryan bond +5", "Energy +30 Mejiro Ryan bond +5"

# Seiun Sky
    "(❯) Sudden Murder Mystery! Part 1": (2,2), # "Wit +5 Skill points +10 Seiun Sky bond +5", "Energy +10 Seiun Sky bond +5"
    "(❯❯) Sudden Murder Mystery! Part 2": (2,2), # "Wit +5 Frenzied Pace Chasers hint +1 Seiun Sky bond +5", "Energy +5 Skill points +10 Seiun Sky bond +5"
    "(❯❯❯) Sudden Murder Mystery! Part 3": (2,2), # "Wit +5/+10 Vanguard Spirit hint +1/+3 Seiun Sky bond +5", "Energy +10 Stamina +10 Skill points +15"
    "Recruiting Cat Catchers": (2,1), # "Energy +10 Wit +5 Seiun Sky bond +5", "Energy -10 Speed +15 Stamina +5 Seiun Sky bond +5"
    "Recruiting Advisors": (2,1), # "Wit +15 Seiun Sky bond +5", "Keeping the Lead hint +1 Seiun Sky bond +5"
    "(❯) Be Strategic ☆": (2,1), # "Energy +10 Wit +5 Seiun Sky bond +5", "Skill points +30 Second Wind hint +1 Seiun Sky bond -5 Event chain ended"

# King Halo
    "(❯) A Captivating Invitation": (2,2), # "Power +10 King Halo bond +5", "Guts +10 King Halo bond +5"
    "(❯❯) Dancer's Pride": (2,2), # "Energy -5 Stamina +10 Power +5 Skill points +5 King Halo bond +5", "Energy +15 Skill points +5 King Halo bond +5"
    "You May Socialize With Me!": (2,1), # "Energy -20 Speed +10 Power +10 Wit +5 King Halo bond +5", "Mood -1 Guts +25 King Halo bond +5"
    "You May Advise Me!": (2,1), # "Guts +10 Wit +5 King Halo bond +5", "Homestretch Haste hint +1 King Halo bond +5"

# Gold Ship
    "(❯) Raising the Uma Lord's Castle": (2,1), # "Maximum Energy +4 Gold Ship bond +5", "Speed +10 Gold Ship bond +5"
    "(❯❯❯) Assembling the Uma Lord's Minions": (2,2), # "Randomly either ---------- Energy -10 Speed +5 Stamina +5 Inside Scoop hint +3 Gold Ship bond +5 ---------- Energy -10 Speed +10 Stamina +10 Innate Experience hint +3 Gold Ship bond +5", "Energy +10 Maverick ○ hint +1"
    "Revive the Brand! Golshi's Yakisoba": (2,1), # "Mood +1 Stamina +5", "Hanshin Racecourse ○ hint +1 Gold Ship bond +5"
    "Adventurer Gold Ship": (2,2), # "Stamina +15 Gold Ship bond +5", "Guts +10 Skill points +15 Gold Ship bond +5"

# Bamboo Memory
    "(❯❯) No One Is Above Discipline!": (3,1), # "Randomly either ---------- Maximum Energy +4 Energy -10 Stamina +10 Power +10 Guts +5 Homestretch Haste hint +1 Bamboo Memory bond +5 ---------- Energy -20 Stamina +10 Power +10 Guts +5 Bamboo Memory bond +5 ---------- Energy -20 Stamina +10 Guts +10 Obtain Running Idle skill", "Energy -10 Mood +1 Stamina +5 Power +5 Bamboo Memory bond +5", "Energy +30 Hesitant Late Surgers hint +1 Event chain ended"
    "Overthrow the Rival!": (2,2), # "Guts +10 Bamboo Memory bond +5", "Maximum Energy +4 Energy -5 Bamboo Memory bond +5"
    "Tons of Trouble!": (2,1), # "Stamina +5 Guts +5 Bamboo Memory bond +5", "Energy -10 Standard Distance ○ hint +5 Bamboo Memory bond +5"

# Kawakami Princess
    "(❯) Modestly! Boldly!": (2,1), # "Mood +1 Speed +5 Kawakami Princess bond +5", "Skill points +10 Tether hint +1 Kawakami Princess bond +5"
    "(❯❯❯) Hit It! Princess Road!": (2,2), # "Speed +15 Guts +15 Center Stage hint +1 Kawakami Princess bond +5", "Energy +25 Skill points +25"
    "Princess Punch!": (2,1), # "Guts +10 Kawakami Princess bond +5", "Mood +1 Kawakami Princess bond +5"
    "Princess Escape!": (2,1), # "Energy +10 Kawakami Princess bond +5", "Steadfast hint +1 Kawakami Princess bond +5"

# Hishi Akebono
    "(❯❯) Let's Go... Buono ☆": (2,1), # "Energy +30 Guts +5 Hishi Akebono bond +5 (random) Get Slow Metabolism status", "Stamina +5 Power +5 Hishi Akebono bond +5"
    "Eat Up ♪": (2,1), # "Energy +10 Hishi Akebono bond +5", "Energy -5 Power +15 Hishi Akebono bond +5"
    "Leave It to Me ♪": (2,1), # "Stamina +10 Hishi Akebono bond +5", "Energy -15 Sprinting Gear hint +2 Hishi Akebono bond +5"

# Mejiro Dober
    "(❯) One Step Forward": (2,2), # "Energy -10 Skill points +15/+45 Mejiro Dober bond +5", "Guts +5 Wit +5 Mejiro Dober bond +5"
    "Give It a Try": (2,1), # "Energy +15 Mejiro Dober bond +5", "Mood +1 Skill points +15 Mejiro Dober bond +5"
    "Hope She'll Like It...": (2,1), # "Skill points +45 Mejiro Dober bond +5", "Unyielding Spirit hint +1 Mejiro Dober bond +5"

# Sakura Chiyono O
    "(❯❯) Blooming Hope!": (2,2), # "Randomly either ---------- Stamina +15 Heal a negative status effect Sakura Chiyono O bond +5 ---------- Energy -10 Guts +15 Sakura Chiyono O bond +5", "Energy +10 Mood +1 Sakura Chiyono O bond +5"
    "(❯❯❯) Someday, I'll Bloom!": (2,1), # "Randomly either ---------- Energy -15 Stamina +20 Skill points +10 Speed Star hint +3 Sakura Chiyono O bond +5 ---------- Energy -15 Stamina +10 Skill points +5 Prepared to Pass hint +3 Sakura Chiyono O bond +5", "Speed +5 Stamina +10 Power +5 Skill points +30 Sakura Chiyono O bond +5"
    "Until I Bloom...": (2,1), # "Energy +5 Stamina +5 Sakura Chiyono O bond +5", "Spring Runner ○ hint +1 Sakura Chiyono O bond +5"
    "Today's Words of Wisdom!": (2,2), # "Energy -10 Power +20 Sakura Chiyono O bond +5", "Energy +5 Skill points +10 Sakura Chiyono O bond +5"

# Yaeno Muteki
    "(❯❯) A Reasonable Diet vs. an Explosive Diet": (2,1), # "Energy +10 Skill points +10 Yaeno Muteki bond +5", "Energy +10 Wit +10 Skill points +10 Playtime's Over! hint +3 Event chain ended"
    "Firm and Plain, Yet Close to Virtue": (2,1), # "Speed +10", "Mood +1 Power +5"
    "The Will to Protect!": (2,1), # "Stamina +10 Power +10", "Medium Corners ○ hint +1"

# Winning Ticket
    "Full-Power Muscles!": (2,1), # "Stamina +5 Skill points +15 Winning Ticket bond +5", "Mood +1 Skill points +15 Winning Ticket bond +5"
    "Full-Power Racing!": (2,1), # "Late Surger Corners ○ hint +1 Winning Ticket bond +5", "Skill points +30 Winning Ticket bond +5"

# Yukino Bijin
    "(❯) Cozy Memories of Wanko Soba": (2,2), # "Mood +1 Yukino Bijin bond +5", "Maximum Energy +4 Yukino Bijin bond +5"
    "(❯❯) The Class Rep's Intense Crash Course": (2,2), # "Mood +1 Power +5 Yukino Bijin bond +5", "Power +3 Guts +3 Wit +3 Yukino Bijin bond +5"
    "(❯❯❯) I Wanna Win!": (2,2), # "Mood +1 No Stopping Me! hint +1 Yukino Bijin bond +5", "Power +3 Guts +3 Wit +3 No Stopping Me! hint +1 Yukino Bijin bond +5"
    "For a Spiffy Concert": (2,1), # "Guts +10 Yukino Bijin bond +5", "Energy -10 Guts +15 Yukino Bijin bond +5"
    "Aiming for the City Spots": (2,1), # "Energy -10 Mood +1 Guts +10 Yukino Bijin bond +5", "Corner Acceleration ○ hint +1 Yukino Bijin bond +5"

# Kitasan Black
    "(❯❯) Paying It Forward": (2,1), # "Energy +10 Mood +1 Kitasan Black bond +5", "Speed +5/+10 Straightaway Adept hint +1/+3 Kitasan Black bond +5"
    "Ah, Friendship": (2,2), # "Mood +1 Power +5 Kitasan Black bond +5", "Energy +10 Kitasan Black bond +5"
    "Ah, Home Sweet Home": (2,1), # "Speed +5 Power +10 Kitasan Black bond +5", "Get Practice Perfect ○ status Kitasan Black bond +5"

# Satono Diamond
    "(❯❯) Diamond Fixation": (2,2), # "Wit +10 Satono Diamond bond +5", "Randomly either ---------- Energy +15 Stamina +10 Satono Diamond bond +5 ---------- Mood -1 Guts +20"
    "(❯❯❯) Only for You": (2,2), # "Energy -20 Stamina +30 Iron Will hint +1 Satono Diamond bond +5", "Energy +5 Guts +5 Iron Will hint +1 Satono Diamond bond +5"
    "I Love New Things!": (2,1), # "Guts +10 Satono Diamond bond +5", "Energy -10 Stamina +20 Satono Diamond bond +5"
    "I Love Complicated Things!": (2,1), # "Stamina +5 Guts +10 Satono Diamond bond +5", "Hesitant Front Runners hint +1 Satono Diamond bond +5"

# Matikanetannhauser
    "(❯) Seeking Uniqueness!": (2,2), # "Mood +1 Matikanetannhauser bond +5", "Energy +10/+30 Matikanetannhauser bond +5"
    "Just Your Typical Hard Work!": (2,1), # "Speed +10 Matikanetannhauser bond +5", "Power +10 Matikanetannhauser bond +5"
    "Just A Typical Accident?!": (2,1), # "Stamina +5 Guts +10 Matikanetannhauser bond +5", "Subdued Front Runners hint +1 Matikanetannhauser bond +5"

# Mejiro Palmer
    "(❯) Run Away to First Base": (2,1), # "Energy -15 Stamina +10 Guts +10 Mejiro Palmer bond +5", "Energy -15 Guts +10 Wit +10 Mejiro Palmer bond +5"
    "(❯❯) Runaway Romance": (2,2), # "Energy +10 Guts +5 Wit +5 Mejiro Palmer bond +5", "Energy +10 Front Runner Savvy ○ hint +1 Mejiro Palmer bond +5"
    "(❯❯❯) Optimistic Escapism: Never Give Up!": (2,2), # "Energy -20 Stamina +5 Guts +5 Vanguard Spirit hint +3 or Keeping the Lead hint +1/+3 Mejiro Palmer bond +5", "Energy +10 Lone Wolf hint +1"
    "An Inescapable Choice?": (2,1), # "Energy -15 Guts +20 Mejiro Palmer bond +5", "Power +5 Skill points +15 Mejiro Palmer bond +5"
    "Optimistic Escapism": (2,1), # "Guts +15 Mejiro Palmer bond +5", "Wet Conditions ○ hint +1 Mejiro Palmer bond +5"

# Twin Turbo
    "(❯) I'm Not Afraid!": (2,1), # "Randomly either ---------- Speed +10 Twin Turbo bond +5 ---------- Energy -10 Speed +10 Event chain ended", "Energy +20 Event chain ended"
    "(❯❯) Can't Catch Me!": (2,1), # "Randomly either ---------- Speed +15 Leader's Pride hint +3 Twin Turbo bond +5 ---------- Energy -10 Speed +10 Event chain ended", "Energy +25 Event chain ended"
    "(❯❯❯) Turbo Is Strong!": (2,2), # "Randomly either ---------- Energy -10 Speed +5 Early Lead hint +3 ---------- Energy -10 Speed +25 Taking the Lead hint +3 Twin Turbo bond +5", "Energy +15 Watchful Eye hint +1"
    "Just Start Running!": (2,1), # "Mood -1 Speed +20", "Energy -10 Power +20"
    "I'm All Fired Up!": (2,1), # "Energy +15 Twin Turbo bond +5", "Early Lead hint +1 Twin Turbo bond +5"

# Oguri Cap
    "(❯❯) How Should I Respond?": (2,1), # "Power +5 Skill points +10 Stamina to Spare hint +1 Oguri Cap bond +5", "Stamina +5 Skill points +10 Outer Swell hint +1 Oguri Cap bond +5"
    "(❯❯❯) What I Want to Say": (2,2), # "Randomly either ---------- Power +10 Guts +5 Skill points +10 Oguri Cap bond +5 Furious Feat hint +1 ---------- Power +15 Guts +10 Skill points +15 Oguri Cap bond +5 Furious Feat hint +3", "Energy +30"
    "Conquering the Crowds": (2,1), # "Power +5 Skill points +15", "Nakayama Racecourse ○ hint +1"
    "How Should I Respond?": (2,1), # "Energy +5 Power +5", "Energy -10 Guts +15"

# Special Week
    "(❯❯) Just a Little Closer": (3,1), # "Energy -10 Speed +15 Special Week bond +5", "Energy -10 Skill points +20 Special Week bond +5", "Energy -10 Shake It Out hint +1 Special Week bond +5"
    "Watch Where You're Going!": (2,2), # "Extra Tank hint +1 Special Week bond +5", "Guts +15 Special Week bond +5"
    "So Many Options!": (2,1), # "Energy +10 Mood +1 Special Week bond +5", "Energy -10 Stamina +15 Skill points +15 Special Week bond +5"
    "(❯❯) A Roller Coaster of Feelings!": (2,1), # "Energy -10 Speed +5 Stamina +5 Guts +10 Special Week bond +5", "Energy +20 Wit +10 Special Week bond +5 Event chain ended"

# Silence Suzuka
    "On and On": (2,1), # "Speed +10 Stamina +5 Silence Suzuka bond +5", "Speed +15 Silence Suzuka bond +5"
    "What Should I Do?": (2,2), # "Speed +5 Stamina +5 Wit +5 Silence Suzuka bond +5", "Left-Handed ○ hint +1 Silence Suzuka bond +5"

# Tokai Teio
    "My Way, Or...": (2,2), # "Mood +1 Skill points +15 Tokai Teio bond +5", "Guts +15 Tokai Teio bond +5"
    "My Weapon": (2,1), # "Mood +1 Guts +10 Tokai Teio bond +5", "Pace Chaser Straightaways ○ hint +1 Tokai Teio bond +5"

# Vodka
    "The Coolest Line": (2,1), # "Power +10 Vodka bond +5", "Power +5 Skill points +15 Vodka bond +5"
    "Enemies on Main Street": (2,2), # "Nimble Navigator hint +1 Vodka bond +5", "Power +5 Skill points +15 Vodka bond +5"

# Grass Wonder
    "(❯❯) A Moment's Respite": (2,1), # "Energy +15 Grass Wonder bond +5", "Randomly either ---------- Energy -10 Power +5 Guts +5 Wit +5 Grass Wonder bond +5 ---------- Power +5 Guts +5 Wit +10 Grass Wonder bond +5"
    "Library Vexation": (2,2), # "Wit +10 Grass Wonder bond +5", "Guts +5 Wit +5 Grass Wonder bond +5"
    "A Friendly Daytime Discussion": (2,1), # "Frenzied Pace Chasers hint +1 Grass Wonder bond +5", "Target in Sight ○ hint +1 Grass Wonder bond +5"

# El Condor Pasa
    "(❯❯) Uma-me": (2,1), # "Energy +30 El Condor Pasa bond +5", "Stamina to Spare hint +1 El Condor Pasa bond +5 Event chain ended"
    "Blazing Fire!": (2,2), # "Stamina +10 El Condor Pasa bond +5", "Energy -10 Power +20 El Condor Pasa bond +5"
    "Secret Notebook!": (2,1), # "Power +10 El Condor Pasa bond +5", "Sunny Days ○ hint +1 El Condor Pasa bond +5"

# Tamamo Cross
    "Tamamo's School Tour": (2,2), # "Wit +10 Tamamo Cross bond +5", "Stamina +5 Guts +5 Tamamo Cross bond +5"
    "A Battle I Can't Lose!": (2,2), # "Calm in a Crowd hint +1 Tamamo Cross bond +5", "Stamina +5 Wit +5 Tamamo Cross bond +5"

# Fine Motion
    "(❯) Lovely Training Weather ♪": (3,2), # "Wit +5 Skill points +20 Fine Motion bond +5", "Speed +10 Stamina +5", "Get Practice Perfect ○ status Fine Motion bond +5"
    "Wonderful New Shoes": (2,1), # "Speed +5 Skill points +10 Fine Motion bond +5", "Energy -10 Stamina +5 Skill points +20 Fine Motion bond +5"
    "Reminiscent Clover": (2,2), # "Corner Adept ○ hint +1 Fine Motion bond +5", "Guts +15 Fine Motion bond +5"

# Ines Fujin
    "It's a Game of Tag!": (2,1), # "Energy +10 Speed +5 Ines Fujin bond +5", "Fast-Paced hint +1 Ines Fujin bond +5"
    "Ten Minutes Left!": (2,1), # "Guts +15 Ines Fujin bond +5", "Wit +15 Ines Fujin bond +5"

# Air Shakur
    "//Verification Required": (2,1), # "Energy +10 Guts +5 Air Shakur bond +5", "Energy -10 Stamina +5 Guts +10 Air Shakur bond +5"
    "//Absolute Desire": (2,2), # "Pace Strategy hint +1 Air Shakur bond +5", "Maximum Energy +4 Guts +5 Air Shakur bond +5"

# Gold City
    "08:36 / Crap, I Overslept": (2,2), # "Mood -1 Skill points +45 Gold City bond +5", "Energy +10 Wit +5 Gold City bond +5"
    "13:12 / Lunch Break, Gotta Get Myself Together": (2,1), # "Skill points +30 Gold City bond +5", "A Small Breather hint +1 Gold City bond +5"

# Sakura Bakushin O
    "Genius Efficiency!": (2,1), # "Speed +15 Sakura Bakushin O bond +5", "Speed +5 Power +10 Sakura Bakushin O bond +5"
    "Enough to Break into a Dash!": (2,2), # "Gap Closer hint +1 Sakura Bakushin O bond +5", "Energy -10 Speed +10 Power +5 Sakura Bakushin O bond +5"

# Super Creek
    "Leave it to Me to Help Out! ♪": (2,1), # "Energy +15 Super Creek bond +5", "Stamina +10 Super Creek bond +5"
    "Leave it to Me to Be Considerate! ♪": (2,2), # "Deep Breaths hint +1 Super Creek bond +5", "Energy +10 Stamina +5 Super Creek bond +5"

# Smart Falcon
    "(❯) Always on Stage ☆": (2,1), # "Wit +10 Smart Falcon bond +5", "Energy +25 Focus hint +1 Smart Falcon bond +5 Event chain ended"
    "Chants Are the Life of a Concert ☆": (2,1), # "Stamina +5 Guts +10 Smart Falcon bond +5", "Wit +15 Smart Falcon bond +5"
    "If I'm Cute, Come to My Show! ☆": (2,2), # "Energy -10 Power +10 Final Push hint +1 Smart Falcon bond +5", "Energy +10 Wit +5 Smart Falcon bond +5"

# Nishino Flower
    "(❯❯) Aspiring to Adulthood": (2,1), # "Energy -10 Wit +20 Nishino Flower bond +5", "Wit +5 Skill points +15"
    "Warmth, Love, and Lunch": (2,1), # "Get Charming ○ status Nishino Flower bond +5", "Energy +20 Nishino Flower bond +5"
    "Let's Bloom Beautifully ♪": (2,2), # "Wit +15 Nishino Flower bond +5", "Speed +10 Power +5 Nishino Flower bond +5"
    "(❯❯) I Want to Say Thank You!": (2,1), # "Power +5 Straightaway Adept hint +1 Nishino Flower bond +5", "Wit +5 Straightaway Acceleration hint +1 Nishino Flower bond +5"

# Haru Urara
    "Urara's ☆ Study Review": (2,1), # "Energy +10 Wit +5 Haru Urara bond +5", "Mood +1 Wit +5 Haru Urara bond +5"
    "Urara's ☆ Long Shot Dash!": (2,2), # "Long Shot ○ hint +1 Haru Urara bond +5", "Mood +1 Energy +10 Haru Urara bond +5"

# Biko Pegasus
    "A Hero's Woes": (2,2), # "Energy +15 Biko Pegasus bond +5", "Energy +5 Power +5 Biko Pegasus bond +5"
    "Preparing My Special Move!": (2,2), # "Sprint Straightaways ○ hint +1 Biko Pegasus bond +5", "Energy +30 Biko Pegasus bond +5"

# Tazuna Hayakawa
    "(❯❯❯) Memories of Cinema": (2,1), # "Energy +35 Stamina +6 Mood +1 Tazuna Hayakawa bond +5", "Stamina +12 Guts +12 Mood +1 Tazuna Hayakawa bond +5"
    "My Chosen Way of Life": (2,1), # "Energy +14 Mood +1 Tazuna Hayakawa bond +5", "Mood +1 Wit +6 Tazuna Hayakawa bond +5"
    "Enthusiastic Pair": (2,1), # "Energy +14 Wit +6 Mood +1 Tazuna Hayakawa bond +5 Can start dating", "Mood -1 Tazuna Hayakawa bond -5 Watchful Eye hint +1 Event chain ended"

# Mejiro McQueen
    "To Maintain My Weight": (2,2), # "Energy -10 Stamina +15 Mejiro McQueen bond +5", "Maximum Energy +4 Stamina +5 Mejiro McQueen bond +5"
    "To Reach the Greatest Heights": (2,1), # "Stamina +5 Guts +5 Mejiro McQueen bond +5", "Early Lead hint +1 Mejiro McQueen bond +5"

# Rice Shower
    "A Page About Cloudy Weather": (2,1), # "Speed +5 Guts +5 Rice Shower bond +5", "Firm Conditions ○ hint +1 Rice Shower bond +5"
    "A Page of Flower Shop Assistance": (2,2), # "Mood +2 Rice Shower bond +5", "Stamina +10 Rice Shower bond +5"

# Shinko Windy
    "(❯) Dig Here, Windy!": (2,1), # "Speed +10 Shinko Windy bond +5", "Energy -5 Skill points +30 Shinko Windy bond +5"
    "Chomp Extermination!": (2,2), # "Speed +3 Mood +1 Shinko Windy bond +5", "Energy +10 Skill points +5 Shinko Windy bond +5"
    "Chomp Attack!": (2,2), # "Skill points +15 Shinko Windy bond +5", "Speed +3 Unyielding Spirit hint +1 Shinko Windy bond +5"

# Seeking the Pearl
    "(❯) No More Words ♪ Use Body Language!": (3,3), # "Mood +1 Lucky Seven hint +1 Seeking the Pearl bond +5", "Power +10 Guts +10 Seeking the Pearl bond +5", "Energy +30"
    "Full-Power Passion!": (2,1), # "Energy +10 Mood +1 Seeking the Pearl bond +5", "Power +5 Guts +5 Seeking the Pearl bond +5"
    "Full-Power Thinking!": (2,1), # "Wit +20 Seeking the Pearl bond +5", "Energy -10 Uma Stan hint +3 Seeking the Pearl bond +5"

# Zenno Rob Roy
    "(❯) The Bookworm and the Magical Girl": (2,1), # "Stamina +5 Wit +5 Zenno Rob Roy bond +5", "Energy +20 Power +10 Zenno Rob Roy bond +5 Event chain ended"
    "Book-lover Quirks": (2,2), # "Speed +5 Wit +5 Zenno Rob Roy bond +5", "Energy +10 Power +5 Zenno Rob Roy bond +5"
    "A Tale Entrusted": (2,1), # "Stamina +10 Wit +10 Zenno Rob Roy bond +5", "Medium Straightaways ○ hint +1 Zenno Rob Roy bond +5"

# Nice Nature
    "(❯) Chasing Their Backs": (2,1), # "Energy +5 Wit +3 Nice Nature bond +5", "Nice Nature bond +20"
    "Not like Meow": (2,2), # "Energy +20 Nice Nature bond +5", "Energy +10 Wit +5 Nice Nature bond +5"
    "(Delicious) Burden": (2,2), # "Ramp Up hint +1 Nice Nature bond +5", "Mood +1 Maximum Energy +4 Nice Nature bond +5"

# Ikuno Dictus
    "(❯❯) Ikuno-Style Support": (2,1), # "Wit +15 Frenzied Front Runners hint +3 Ikuno Dictus bond +5", "Wit +15 Frenzied End Closers hint +3 Ikuno Dictus bond +5"
    "Ikuno-Style Flawless Method": (2,1), # "Wit +10 Ikuno Dictus bond +5", "Skill points +30 Ikuno Dictus bond +5"
    "Ikuno-Style Management": (2,1), # "Stamina +20 Ikuno Dictus bond +5", "Trick (Rear) hint +1 Ikuno Dictus bond +5"

# Daitaku Helios
    "(❯) #BFF #Party!": (2,2), # "Power +10 Daitaku Helios bond +5", "Speed +10 Daitaku Helios bond +5"
    "(❯❯) #LOL #Party! #Round2": (2,2), # "Power +10 (random) Speed +10 Straight Descent hint +1/+3 Daitaku Helios bond +5", "Energy +20 Watchful Eye hint +1 Daitaku Helios bond +5"
    "Encounter With the Sun ☆": (2,1), # "Power +10 Daitaku Helios bond +5", "Get Hot Topic status Daitaku Helios bond +5"
    "Smiles Forever": (2,1), # "Speed +5 Power +10 Daitaku Helios bond +5", "Long Shot ○ hint +1 Daitaku Helios bond +5"

# Sweep Tosho
    "(❯) Some Very Green Friends": (2,1), # "Speed +5 Skill points +10 Lucky Seven hint +1 Sweep Tosho bond +5", "Mood -1 Maverick ○ hint +5"
    "(❯❯) Premeditated Mischief": (2,2), # "Speed +10 Skill points +20 Levelheaded hint +1 Sweep Tosho bond +5", "Mood -1 Lone Wolf hint +1"
    "Miracle ☆ Escape!": (2,1), # "Energy +10 Speed +5 Sweep Tosho bond +5", "Energy -10 Speed +20 Sweep Tosho bond +5"
    "Wonderful ☆ Mistake!": (2,1), # "Randomly either ---------- Energy -15 Skill points +40 ---------- Energy -20 Skill points +40 Sweep Tosho bond +5", "Get Charming ○ status Sweep Tosho bond +5"

# Fuji Kiseki
    "Sleight of Hand": (2,2), # "Wit +5 Skill points +15 Fuji Kiseki bond +5", "Power +5 Skill points +15 Fuji Kiseki bond +5"
    "Misdirection": (2,1), # "Prepared to Pass hint +1 Fuji Kiseki bond +5", "Skill points +30 Fuji Kiseki bond +5"

# Daiwa Scarlet
    "I'm Going to Win Tomorrow!": (2,1), # "Wit +10 Daiwa Scarlet bond +5", "Mood +1 Skill points +15 Daiwa Scarlet bond +5"
    "This Is Nothing!": (2,2), # "Stamina to Spare hint +1 Daiwa Scarlet bond +5", "Energy +20 Mood +1 Daiwa Scarlet bond +5"

# Hishi Amazon
    "Hishiama's Struggles: Problem Children": (2,1), # "Energy +10 Wit +5 Hishi Amazon bond +5", "Energy -10 Speed +10 Guts +5 Hishi Amazon bond +5"
    "Hishiama's Struggles: Final Stretch": (2,2), # "Hesitant End Closers hint +1 Hishi Amazon bond +5", "Power +5 Skill points +15 Hishi Amazon bond +5"

# Air Groove
    "Strict but Gracious": (2,2), # "Go with the Flow hint +1 Air Groove bond +5", "Energy +10 Wit +10"
    "Agile but Strong": (2,2), # "Power +15 Air Groove bond +5", "Speed +10 Stamina +5 Air Groove bond +5"

# Agnes Digital
    "Umamusume Deficiency!": (2,1), # "Energy +5 Speed +5 Agnes Digital bond +5", "Speed +5 Power +5 Agnes Digital bond +5"
    "Heavy Romance": (2,1), # "Rainy Days ○ hint +1 Agnes Digital bond +5", "Wet Conditions ○ hint +1 Agnes Digital bond +5"

# Biwa Hayahide
    "Last-Minute Modal Theory": (2,2), # "Power +15 Biwa Hayahide bond +5", "Speed +10 Skill points +15 Biwa Hayahide bond +5"
    "Step-Out-of-Your-Comfort-Zone Theory": (2,2), # "Energy -10 Inside Scoop hint +1 Biwa Hayahide bond +5", "Energy +10 Stamina +10 Biwa Hayahide bond +5"

# Mayano Top Gun
    "Snack Advice for Mayano!": (2,1), # "Stamina +5 Guts +5 Mayano Top Gun bond +5", "Stamina +10 Mayano Top Gun bond +5"
    "Fashion Advice for Mayano!": (2,2), # "Straightaway Adept hint +1 Mayano Top Gun bond +5", "Stamina +10 Mayano Top Gun bond +5"

# Manhattan Cafe
    "Solo Nighttime Run": (2,2), # "Stamina +10 Manhattan Cafe bond +5", "Energy +10 Stamina +5 Manhattan Cafe bond +5"
    "A Taste of Silence": (2,1), # "Stamina +5 Skill points +15 Manhattan Cafe bond +5", "Non-Standard Distance ○ hint +1 Manhattan Cafe bond +5"

# Mihono Bourbon
    "(❯) I'm Not a Cyborg": (2,1), # "Guts +10 Skill points +15 Mihono Bourbon bond +5", "Energy -10 Corner Recovery ○ hint +1 (random) Mihono Bourbon bond -5 Event chain ended"
    "Do No Harm": (2,2), # "Energy -10 Stamina +5 Power +15 Mihono Bourbon bond +5", "Energy +10 Wit +5 Mihono Bourbon bond +5"
    "Orders Must Be Followed": (2,2), # "Focus hint +1 Mihono Bourbon bond +5", "Speed +10 Skill points +15 Mihono Bourbon bond +5"

# Mejiro Ryan
    "My Muscles and Me, Onward to Tomorrow!": (2,2), # "Energy -10 Power +15 Mejiro Ryan bond +5", "Maximum Energy +4 Power +5 Mejiro Ryan bond +5"
    "It's Not Like I Like Romance!": (2,2), # "Pace Strategy hint +1 Mejiro Ryan bond +5", "Energy +30 Mejiro Ryan bond +5"

# Agnes Tachyon
    "The Correlation between Sleep and Efficiency": (2,1), # "Power +5 Wit +5 Agnes Tachyon bond +5", "Wit +10 Agnes Tachyon bond +5"
    "Happenstance Introduced Through Intervention": (2,2), # "Late Surger Savvy ○ hint +1 Agnes Tachyon bond +5", "Wit +10 Agnes Tachyon bond +5"

# Eishin Flash
    "Unforeseen Lunch": (2,1), # "Energy +15 Eishin Flash bond +5", "Speed +5 Guts +5 Eishin Flash bond +5"
    "Responding to the Unforeseen": (2,1), # "Guts +10 Eishin Flash bond +5", "Target in Sight ○ hint +1 Eishin Flash bond +5"

# Narita Taishin
    "Just Leave Me Alone": (2,2), # "Stamina +5 Skill points +15 Narita Taishin bond +5", "Power +5 Skill points +15 Narita Taishin bond +5"
    "Just Don't Bother Me": (2,1), # "Pressure hint +1 Narita Taishin bond +5", "Skill points +30 Narita Taishin bond +5"

# Marvelous Sunday
    "Marvelous, No Question ☆": (2,1), # "Energy +10 Speed +5 Marvelous Sunday bond +5", "Mood +1 Speed +5 Marvelous Sunday bond +5"
    "How To Be More Marvelous ☆": (2,1), # "Energy +10 Mood +1 Marvelous Sunday bond +5", "Hanshin Racecourse ○ hint +1 Marvelous Sunday bond +5"

# Matikanefukukitaru
    "(❯❯) Guidance and Friends": (2,2), # "Skill points +45 Matikanefukukitaru bond +5", "Randomly either ---------- Energy +10 Mood +1 Right-Handed ○ hint +3 Matikanefukukitaru bond +5 ---------- Energy -20 Right-Handed ○ hint +1 Matikanefukukitaru bond +5"
    "Maximum Spirituality": (2,2), # "Wit +5 Skill points +15 Matikanefukukitaru bond +5", "Energy -10 Speed +5 Stamina +5 Power +5 Matikanefukukitaru bond +5"
    "When Piety and Kindness Intersect": (2,2), # "Skill points +30 Matikanefukukitaru bond +5", "Energy +20 Matikanefukukitaru bond +5"

# Meisho Doto
    "(❯) What I'm Destined For...": (2,2), # "Energy +10 Guts +5 Meisho Doto bond +5", "Randomly either ---------- Energy -10 Wit +5 ---------- Maximum Energy +4 Mood +1 Guts +5 Wit +5 Meisho Doto bond +5"
    "I... Will Change": (2,1), # "Energy +10 Mood +1 Meisho Doto bond +5", "Guts +15 Meisho Doto bond +5"
    "Please... Buy Some Carrots": (2,1), # "Energy +10 Wit +5 Meisho Doto bond +5", "Pace Chaser Corners ○ hint +1 Meisho Doto bond +5"

# Aoi Kiryuin
    "(❯❯) How I Play at the Park": (2,1), # "Energy +35 Wit +6 Aoi Kiryuin bond +5 (random) Mood +1", "Randomly either ---------- Skill points +18 Aoi Kiryuin bond +5 ---------- Speed +6 Skill points +56 Mood +1 Aoi Kiryuin bond +5"

# Maruzensky
    "For an Adorable Younger Student": (2,2), # "Early Lead hint +1", "Energy +5 Speed +10"
    "Drive Destination": (2,1), # "Mood +1 Speed +5", "Mood +1 Wit +5"

# Taiki Shuttle
    "Yes! Let's Hug ☆": (2,1), # "Speed +10", "Speed +5 Power +5"
    "Yeehaw! Party Tonight ☆": (2,1), # "Energy -10 Speed +5 Power +10", "Prepared to Pass hint +1"

# TM Opera O
    "Etude to Victory": (2,1), # "Mood -1 Speed +5 Skill points +30", "Power +5 Skill points +15"
    "Beyond Our Limited Time": (2,1), # "Energy +10 Skill points +15", "Non-Standard Distance ○ hint +1"

# Symboli Rudolf
    "The Emperor's Encouragement": (2,1), # "Speed +10", "Energy -10 Skill points +30"
    "The Student Council President's Thoughtfulness": (2,2), # "Rainy Days ○ hint +1", "Stamina +15"



# [CHARACTERS]
  # Agnes Tachyon
    "Expression of Conviction": (2,2), # "Stamina +20", "Speed +20"
    "Obtain Data!": (2,2), # "Wit +20", "Power +20"
    "Tachyon the Spoiled Child": (2,2), # "Stamina +10 Guts +10 (random) Get Fast Learner status", "Wit +20 (random) Get Fast Learner status"
    "At Tachyon's Pace": (2,2), # "Guts +10", "Speed +5 Power +5"
    "The Strongest Collaborator?!": (2,2), # "Energy -20 Stamina +15 Guts +10", "Energy +5 Wit +5"
    "The Pressure of Justice?": (2,1), # "Wit +10 Skill points +15", "Corner Adept ○ hint +1"
    "Hamburger Helper!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Medicine That Makes You Faster?": (2,2), # "Power +5 Guts +5", "Speed +5 Wit +5"
    "The Significance of Research": (2,2), # "Wit +10", "Speed +10"
    "No Shortcuts": (3,3), # "Guts +10", "Wit +10", "Power +10"
    "A Gift From the Dark Sky": (2,1), # "Speed +5 Power +5", "Guts +10"
    "Body Modification!": (2,1), # "Power +5 Wit +5", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# Air Groove
    "Who Will Stand Beside Her?": (2,1), # "Go with the Flow hint +2", "Guts +10 Wit +10"
    "Never-Ending Road": (2,2), # "Up-Tempo hint +2", "Power +20"
    "The Empress and Mom": (2,1), # "Speed +10 Stamina +10 (random) Get Charming ○ status", "Stamina +10 Power +10 (random) Get Charming ○ status"
    "Empress and Monarch": (2,1), # "Power +10", "Wit +10"
    "Operation: Flowerbed": (2,1), # "Energy +5 Wit +5", "Energy -10 Speed +10 Power +10"
    "Empress and Emperor": (2,1), # "Homestretch Haste hint +1", "Mood +1 Skill points +15"
    "Seize Her!": (2,1), # "Energy +10", "Energy -10 Mood +1 Speed +10"
    "Take Good Care of Your Tail": (2,1), # "Energy +10", "Energy -10 Mood +1 Power +10"
    "Suggestion Box of Freedom": (2,1), # "Energy +10", "Energy -10 Mood +1 Wit +10"
    "A Taste of Effort": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "A Little Encounter": (2,1), # "Wit +10", "Guts +10"
    "Sweet Potato Cake": (2,1), # "Power +10", "Stamina +10"
    "Imprinted Memories": (3,1), # "Speed +10", "Power +10", "Stamina +10"
    "A Blinking Light Means Stop": (2,2), # "Wit +10", "Power +10"
    "Smoldering Silently": (2,2), # "Stamina +10", "Speed +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Power +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    "Flowers for You": (2,2), # "Wit +20", "Speed +20"
    "A Beautiful Stress Relief Method?": (2,1), # "Stamina +20", "Guts +20"
    "Guidepost": (2,1), # "Speed +20 (random) Get Hot Topic status", "Power +20 (random) Get Hot Topic status"

# Biwa Hayahide
    "To Keep, or Not to Keep?": (2,2), # "Wit +20", "Stamina +10 Power +10"
    "A Realistic Fairytale": (2,1), # "Power +20", "Guts +20"
    "Theory, the Greatest Weapon": (2,1), # "Randomly either ---------- Stamina +20 (random) Get Hot Topic status ---------- Wit +20 (random) Get Hot Topic status", "Wit +20 (random) Get Practice Perfect ○ status (random) Get Hot Topic status"
    "Memories of Cooking and Sisterhood": (2,1), # "Power +10", "Stamina +5 Wit +5"
    "A New Side": (2,1), # "Speed +10", "Stamina +10"
    "Battle With a Raging Dragon": (2,1), # "Power +5 Guts +10", "Hanshin Racecourse ○ hint +1"
    "Banana Fiend ♪": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Reading in a Cafe": (2,2), # "Stamina +10", "Speed +10"
    "Sharp Contrast": (2,1), # "Wit +10", "Guts +10"
    "Emergency Presentation": (3,2), # "Wit +10", "Power +10", "Stamina +10"
    "Hide and Seek Master": (2,2), # "Guts +10", "Speed +10"
    "Game Theory": (2,2), # "Wit +10", "Power +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Speed +10", "Guts +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# Curren Chan
    "Which Curren Do You Like?": (2,1), # "Speed +10 Power +10", "Stamina +10 Guts +10"
    "How Curren Handles Social Media ♪": (2,1), # "Speed +20", "Wit +20"
    "Curren's Signature Racewear": (2,1), # "Speed +10 Stamina +10 (random) Get Practice Perfect ○ status", "Speed +10 Power +10 (random) Get Practice Perfect ○ status"
    "One, Two, Three, Curren Chan!": (2,1), # "Speed +10", "Wit +10"
    "Ms. Worldwide": (2,2), # "Power +10", "Speed +10"
    "Thanks for the Lesson ♪": (2,1), # "Energy -10 Speed +20", "Frenzied Late Surgers hint +1"
    "Wanna Eat Together?": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Making Friends": (2,1), # "Power +10", "Wit +10"
    "Making Connections": (2,2), # "Guts +10", "Power +10"
    "Universal Cutie": (3,1), # "Speed +5 Power +5", "Speed +10", "Speed +5 Wit +5"
    "A Nostalgic Flavor": (2,2), # "Stamina +10", "Power +10"
    "Rattle, Rattle, Clunk": (2,1), # "Wit +10", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Speed +10", "Guts +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Daiwa Scarlet
    "The Best Pose": (2,1), # "Stamina +10 Power +10", "Wit +20"
    "The Weight of Racewear": (2,1), # "Speed +20", "Guts +20"
    "Looking Good": (2,2), # "Stamina +10 Wit +10 (random) Get Hot Topic status", "Speed +10 Guts +10 (random) Get Hot Topic status"
    "Her": (2,2), # "Power +5 Objective race changed to Japanese Oaks", "Power +5 Objective race changed to Tokyo Yushun (Japanese Derby)"
    "Recommended Restaurant": (2,1), # "Speed +5 Power +5", "Guts +5 Mood +1"
    "Advice from an Older Student": (2,1), # "Speed +10", "Power +10"
    "Enjoying Number One": (2,1), # "Stamina +10 Skill points +15", "Unyielding Spirit hint +1"
    "Can't Lose Sight of Number One!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "As a Model Student...": (2,1), # "Wit +10", "Skill points +30"
    "Just a Little More": (2,2), # "Skill points +30", "Power +10"
    "Under the Evening Star": (3,2), # "Skill points +30", "Speed +5 Stamina +5", "Power +10"
    "Rained On": (2,2), # "Guts +10", "Wit +10"
    "How to Spend a Day Off": (2,1), # "Energy +10", "Mood +1 Wit +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# El Condor Pasa
    "Passion-filled Outfit": (2,2), # "Calm in a Crowd hint +2", "Speed +7 Power +7 Guts +7"
    "Passion! Connection! Guidance!": (2,1), # "Power +20", "Mood +1 Wit +10"
    "A Challenge from the Past": (2,1), # "Speed +10 Power +10 (random) Get Charming ○ status", "Go with the Flow hint +2 (random) Get Charming ○ status"
    "A Personalized Mask": (2,1), # "Speed +10", "Power +10"
    "Salsa Roja": (2,2), # "Stamina +10", "Power +10"
    "Go for the Extra-Large Pizza!": (2,1), # "Power +10 Skill points +15", "Soft Step hint +1"
    "Hot and Spicy!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "The Wrestler I Admire": (2,2), # "Stamina +10", "Speed +10"
    "Shocking Retirement": (2,2), # "Guts +10", "Power +10"
    "Renewed Resolve": (3,3), # "Guts +10", "Stamina +10", "Speed +5 Stamina +5"
    "The Academy at Night": (2,2), # "Mood +1 Guts +5", "Energy +10"
    "Flower Language": (2,2), # "Mood +1 Wit +5", "Energy +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    "Determination of the World's Strongest": (2,1), # "Power +20", "Stamina +20"
    "Cactus Feast": (2,1), # "Speed +10 Stamina +10", "Wit +20"
    "Song of Courage": (2,2), # "Power +20 (random) Get Fast Learner status", "Speed +10 Power +10 (random) Get Fast Learner status"

# Fuji Kiseki
    "What a Wonderful Stage!": (2,2), # "Stamina +20", "Speed +10 Power +10"
    "My Dear Sister": (2,1), # "Power +20", "Wit +20"
    "A Quiet Moment": (2,2), # "Guts +20 (random) Get Practice Perfect ○ status", "Stamina +20 (random) Get Practice Perfect ○ status"
    "Act 1: Smile": (2,2), # "Objective race changed to Tokyo Yushun (Japanese Derby) Guts +10", "Objective race changed to NHK Mile Cup Power +10"
    "A Gracious Doorkeeper": (2,1), # "Speed +10", "Power +10"
    "@DREAM_MAKER": (2,1), # "Power +10", "Wit +10"
    "Two Superstars Compete": (2,1), # "Guts +10 Skill points +15", "Disorient hint +1"
    "Go Easy on the Affection": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "No Regrets": (2,2), # "Wit +10", "Power +10"
    "For Your Sake Alone": (2,2), # "Guts +10", "Speed +10"
    "The Greatest Blessing in Life": (3,3), # "Stamina +10", "Power +10", "Speed +10"
    "One Act from the Wings": (2,2), # "Guts +10", "Stamina +10"
    "Stargazing": (2,1), # "Speed +10", "Power +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Speed +10", "Stamina +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# Gold Ship
    "The Red of the Protagonist!": (2,1), # "Wit +20", "Guts +20"
    "A Date, Golshi Style": (2,2), # "Stamina +20", "Power +20"
    "A Sudden Episode from Golshi's Past!": (2,2), # "Stamina +10 Wit +10 (random) Get Fast Learner status", "Speed +20 (random) Get Fast Learner status"
    "Pair Discount Repeat Offender": (2,2), # "Guts +10", "Stamina +10"
    "Which Did You Lose?": (2,2), # "Energy -10 Power +20", "Speed +10"
    "My Part-Time Job Is... Crazy?": (2,1), # "Stamina +10 Skill points +15", "Hanshin Racecourse ○ hint +1"
    "The Day After, Voices Hoarse": (2,1), # "Stamina +10", "Guts +10"
    "This One's For Keeps!": (2,1), # "Energy +10", "Randomly either ---------- Skill points +60 Non-Standard Distance ○ hint +1 ---------- Skill points +15 Get Slacker status"
    "Killer Appetite!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Legend of the Left Pinky": (2,2), # "Stamina +10", "Speed +10"
    "Hello From About 1.5 Billion Years Ago": (2,2), # "Guts +10", "Wit +10"
    "And Then She...": (3,1), # "Speed +10", "Guts +10", "Power +10"
    "A Lovely Place": (2,2), # "Stamina +10", "Wit +10"
    "Nighttime Park Visit": (2,2), # "Guts +10", "Speed +10"
    "After the Takarazuka Kinen: Keyword 2": (2,1), # "All stats +3 Mood +1 Skill points +45 Yayoi Akikawa bond +4", "All stats +3 Mood +1 Skill points +45 (random) Get Charming ○ status (random) Obtain Gatekept skill Yayoi Akikawa bond +4"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Power +10", "Guts +10"
    "New Year's Resolutions": (3,2), # "Stamina +10", "Energy +20", "Skill points +20"
    

# Grass Wonder
    "A Warrior's Spirit": (2,2), # "Mood +1 Power +10", "Energy +15"
    "Whimsical Encounter": (2,1), # "Guts +10 Wit +10", "Stamina +20"
    "Everlasting Game": (2,2), # "Sharp Gaze hint +2 (random) Get Hot Topic status", "Speed +10 Skill points +15 (random) Get Hot Topic status"
    "Errands Have Perks": (2,2), # "Speed +5 Stamina +5", "Energy +5 Wit +5"
    "Beauteaful": (2,2), # "Wit +5 Skill points +15", "Speed +10"
    "Tracen Karuta Queen": (2,1), # "Speed +10 Wit +5", "Competitive Spirit ○ hint +1"
    "In Search of Refreshment": (2,2), # "Mood -1 Guts +25", "Mood -1 Wit +25"
    "Together for Tea": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Yamato Nadeshiko": (2,2), # "Power +5 Wit +5", "Speed +10"
    "Childhoods Apart": (2,2), # "Guts +10", "Stamina +10"
    "Nadeshiko Gal": (3,3), # "Power +10", "Wit +10", "Speed +10"
    "Childhood Dream": (2,1), # "Speed +5 Guts +5", "Stamina +5 Wit +5"
    "Flower Vase": (2,2), # "Guts +5 Wit +5", "Speed +5 Stamina +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Power +10", "Guts +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    "Hidden Meaning": (2,2), # "Stamina +10 Guts +10", "Power +20"
    "Principles": (2,1), # "Speed +20", "Stamina +20"
    "Hate to Lose": (2,1), # "Wit +20 (random) Get Fast Learner status", "Stamina +10 Guts +10 (random) Get Fast Learner status"

# Haru Urara
    "The Racewear I Love!": (2,1), # "Speed +20", "Power +20"
    "Pair Interview!": (2,1), # "Power +20", "Stamina +20"
    "Tug of War Tournament!": (2,2), # "Guts +20 (random) Get Hot Topic status", "Speed +20 (random) Get Hot Topic status"
    "Arm-Wrestling Contest": (2,2), # "Wit +10", "Power +10"
    "Looking for Something Important": (2,2), # "Energy -10 Guts +20", "Stamina +10"
    "Sand Training!": (2,2), # "Guts +10 Skill points +15", "Energy +15"
    "The Final Boss... Spe!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "A Little Detour!": (2,2), # "Skill points +30", "Stamina +10"
    "Parks Are Fun!": (2,1), # "Speed +10", "Power +10"
    "Secret Day Off Plan!": (3,1), # "Speed +10", "Power +10", "Wit +10"
    "So Cool!": (2,2), # "Skill points +30", "Wit +10"
    "Forgot to Eat!": (2,2), # "Guts +10", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Speed +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Guts +10", "Energy +20", "Skill points +20"
    

# Hishi Amazon
    "Another Level": (2,1), # "Power +20", "Guts +20"
    "One-on-One! Gangster! Racewear!": (2,1), # "Power +20", "Stamina +20"
    "Friend or Rival?": (2,1), # "Power +20 (random) Get Practice Perfect ○ status", "Wit +20 (random) Get Practice Perfect ○ status"
    "Hishiama's Dorm-Leader Breakfast": (2,1), # "Speed +10", "Power +10"
    "Hishiama's Needlework": (2,1), # "Power +10", "Stamina +5 Guts +5"
    "Hishiama's Foraging": (2,1), # "Power +10 Skill points +15", "Homestretch Haste hint +1"
    "The Magic of Sweets?": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Blazing Memories": (2,1), # "Power +10", "Wit +10"
    "Cool and Fiery Sisters": (2,1), # "Speed +10", "Stamina +10"
    "Torrential Passion": (3,1), # "Speed +10", "Wit +10", "Power +10"
    "Hishiama's Special View": (2,1), # "Speed +5 Power +5", "Guts +10"
    "Hishiama and the Arts": (2,1), # "Speed +10", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Power +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    

# King Halo
    "The Outfit That Suits Me Most": (2,1), # "Speed +10 Guts +10", "Power +20"
    "Running Isn't Everything": (2,2), # "Stamina +20", "Speed +10 Power +10"
    "Manners Are Common Sense": (2,2), # "Guts +20 (random) Get Practice Perfect ○ status", "Stamina +10 Wit +10 (random) Get Practice Perfect ○ status"
    "Movies Are Full of Learning Opportunities": (2,1), # "Speed +5 Guts +5", "Stamina +10"
    "The King Knows No Exhaustion": (2,1), # "Energy +5 (random) Mood +1", "Power +10"
    "First-Rate in Studies Too": (2,1), # "Wit +10 Skill points +15", "Outer Swell hint +1"
    "After-School Soda": (2,2), # "Guts +10", "Speed +10"
    "Three Heads Are Better than One": (2,1), # "Wit +10", "Stamina +10"
    "Sweet Tooth Temptation": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "First-Rate Spot": (2,2), # "Guts +10", "Speed +10"
    "First-Rate Harvest": (2,2), # "Power +5 Guts +5", "Speed +5 Stamina +5"
    "First-Rate Terms": (3,1), # "Power +10", "Wit +10", "Guts +10"
    "Crowds Are No Problem": (2,1), # "Speed +10", "Power +10"
    "Breaking Curfew is Second-Rate": (2,2), # "Guts +5 Wit +5", "Speed +5 Power +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Guts +10", "Energy +20", "Skill points +20"
    

# Maruzensky
    "Trendsetter": (2,1), # "Speed +10 Wit +10", "Power +20"
    "Sewing Star": (2,2), # "Guts +20", "Stamina +10 Power +10"
    "My Favorite Things": (2,1), # "Speed +20 (random) Get Fast Learner status", "Stamina +10 Guts +10 (random) Get Fast Learner status"
    "Hot Rod": (2,1), # "Speed +10", "Wit +10"
    "Let's Play ♪": (2,1), # "Energy +10", "Energy -5 Power +10 Guts +5"
    "A Lady's Style ☆": (2,1), # "Speed +5 Skill points +10 Mood +1", "Huge Lead hint +1"
    "Let's Cook!": (2,1), # "Speed +10", "Guts +10"
    "The Road to a Rad Victory!": (2,2), # "Stamina +10", "Wit +10"
    "Down to Dance!": (2,1), # "Speed +10", "Power +10"
    "Nostalgia Fever ☆": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "The Secret to Supporting Each Other": (2,1), # "Speed +10", "Power +10"
    "Even Role Models Get Lonely": (2,2), # "Stamina +5 Guts +5", "Speed +5 Power +5"
    "Take the Wheel": (3,1), # "Power +10", "Guts +10", "Wit +10"
    "Meeting New People Is Trendy ☆": (2,2), # "Guts +10", "Wit +10"
    "The Fun Never Stops ♪": (2,1), # "Speed +5 Wit +5", "Stamina +5 Power +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Speed +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Matikanefukukitaru
    "Room of the Chosen Ones": (2,2), # "Guts +20", "Speed +20"
    "Better Fortune! Lucky Telephone": (2,2), # "Stamina +10 Wit +10", "Power +20"
    "Under the Meteor Shower": (2,1), # "Speed +10 Power +10 (random) Get Charming ○ status", "Stamina +10 Guts +10 (random) Get Charming ○ status"
    "Cursed Camera": (2,1), # "Wit +10", "Skill points +30"
    "Manhattan's Dream": (2,2), # "Hesitant Front Runners hint +1", "Stamina +10"
    "Pretty Gunslingers": (2,2), # "Skill points +15 Mood +1", "Power +10"
    "Seven Gods of Fortune Fine Food Tour": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Fukukitaru's Protection against Misfortune": (2,2), # "Guts +10", "Power +10"
    "Punch in a Pinch": (2,1), # "Speed +10", "Stamina +5 Wit +5"
    "Fukukitaru's Unique Good-Luck Spell": (3,1), # "Speed +5 Guts +5", "Stamina +5 Power +5", "Wit +10"
    "Taking the Plunge": (2,2), # "Stamina +10", "Speed +5 Wit +5"
    "Shrine Visit": (2,2), # "Power +5 Guts +5", "Speed +5 Stamina +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Power +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# Mayano Top Gun
    "You're My Sunshine ☆": (2,2), # "Stamina +20", "Power +20"
    "Meant to Be ♪": (2,1), # "Pace Strategy hint +2", "Straightaway Acceleration hint +2"
    "With My Whole Heart!": (2,2), # "Stamina +10 Skill points +15 (random) Get Practice Perfect ○ status", "Energy +15 (random) Get Practice Perfect ○ status"
    "Maya Will Teach You ☆": (2,1), # "Power +5 Guts +5", "Wit +10"
    "Tips from a Top Model!": (2,2), # "Energy -10 Stamina +20", "Speed +10"
    "Maya's Race Class ☆": (2,1), # "Stamina +10 Skill points +15", "Straightaway Adept hint +1"
    "Hearty Chanko! ☆": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Maya's Exciting ☆ Livestream!": (2,1), # "Stamina +5 Power +5", "Guts +10"
    "Maya's Euphoric ☆ Livestream!": (2,1), # "Speed +10", "Stamina +10"
    "Maya's Twinkly ☆ Determination!": (3,1), # "Speed +5 Stamina +5", "Power +10", "Wit +10"
    "Maya's Special Someone!": (2,1), # "Speed +10", "Guts +10"
    "Wish on a Star": (2,2), # "Wit +10", "Speed +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Stamina +10", "Energy +20", "Skill points +20"
    "Maya's Thrilling ☆ Test of Courage": (2,1), # "Power +20", "Guts +20"
    "Sweet Feelings for You ♪": (2,2), # "Stamina +20", "Wit +20"
    "Mayano Takes Off ☆": (2,1), # "Speed +20 (random) Get Charming ○ status", "Stamina +20 (random) Get Charming ○ status"

# Mejiro McQueen
    "My Roommate's Concern": (2,2), # "Calm in a Crowd hint +2", "Stamina +10 Skill points +15"
    "My Family Make a Difficult Decision": (2,1), # "Speed +10 Power +10", "Stamina +7 Guts +7 Wit +7"
    "My Rival, No Matter the Stage": (2,2), # "Prudent Positioning hint +2 (random) Get Hot Topic status", "Wit +10 Skill points +15 (random) Get Hot Topic status"
    "Queen of the Island": (2,1), # "Speed +10", "Stamina +10"
    "It's Called a Sea Pineapple!": (2,2), # "Skill points +30", "Stamina +10"
    "Cooking Up Memories": (2,1), # "Energy +15", "Early Lead hint +1"
    "The Allure of Racecourse Food": (2,1), # "Randomly either ---------- Energy +30 Stamina +10 Skill points +10 ---------- Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status", "Guts +15 Skill points +5"
    "Attack of the Chestnut Feast!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Two Tickets for the Silver Screen": (2,2), # "Stamina +10", "Wit +5 Skill points +15"
    "An Excited Young Lady": (2,2), # "Guts +10", "Power +10"
    "Endless Kingdom": (3,3), # "Stamina +10", "Wit +10", "Speed +5 Power +5"
    "Bargain Find": (2,1), # "Speed +10", "Guts +10"
    "Three Ramen Bowls' Worth of Temptation": (2,2), # "Skill points +30", "Speed +5 Stamina +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Stamina +10", "Energy +20", "Skill points +20"
    
    "Resolve and Duty": (2,1), # "Speed +10 Wit +10", "Power +20"
    "Late-Night Fanservice Training": (2,2), # "Guts +20", "Speed +20"
    "Elegance": (2,1), # "Stamina +10 Power +10 (random) Get Practice Perfect ○ status", "Wit +20 (random) Get Practice Perfect ○ status"

# Mejiro Ryan
    "My Signature Racewear": (2,2), # "Guts +20", "Speed +20"
    "Heart-Pounding Aquarium": (2,1), # "Power +10 Wit +10", "Stamina +10 Wit +10"
    "Refreshingly Real": (2,2), # "Stamina +20 (random) Get Hot Topic status", "Power +20 (random) Get Hot Topic status"
    "Muscle Jealousy": (2,2), # "Guts +10", "Wit +10"
    "The Pony Girl and the Wolf Prince": (2,2), # "Energy +5 Stamina +5", "Energy +5 Speed +5"
    "Real Gains": (2,1), # "Power +10 Skill points +15", "Wet Conditions ○ hint +1"
    "Rest Day": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Nerve-Racking Rest Time": (2,2), # "Stamina +10", "Power +10"
    "Flush with Feelings": (2,2), # "Wit +10", "Speed +10"
    "With Relaxation and Trust Comes...": (3,1), # "Speed +10", "Stamina +10", "Power +10"
    "Ryan to the Rescue!": (2,1), # "Power +10", "Guts +10"
    "The Little Fans of the Umadol": (2,1), # "Power +10", "Wit +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Power +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    

# Mihono Bourbon
    "Trail of Light": (2,1), # "Speed +20", "Power +20"
    "Smiles Are Contagious": (2,1), # "Stamina +20", "Guts +20"
    "Who to Count On": (2,2), # "Wit +20 (random) Get Hot Topic status", "Power +20 (random) Get Hot Topic status"
    "Operation: Execute Orders": (2,2), # "Stamina +10", "Power +10"
    "Operation: Extra Classes": (2,1), # "Energy +10 Mood +1", "Wit +10"
    "Operation: Excursion Trouble": (2,1), # "Stamina +10 Skill points +15", "Wet Conditions ○ hint +1"
    "Brutal Training": (2,2), # "Energy -10 Power +5/+20 Skill points +5/+10", "Energy +5"
    "The Perfect Dessert": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Let's Make Memories": (2,1), # "Speed +10", "Guts +10"
    "Bourbon's Challenge?": (2,1), # "Power +10", "Wit +10"
    "You're Irreplaceable to Me": (3,2), # "Stamina +10", "Speed +10", "Power +10"
    "Operation: Dance Fever": (2,2), # "Stamina +5 Guts +5", "Stamina +5 Wit +5"
    "Operation: Festival Fun": (2,1), # "Power +10", "Stamina +5 Guts +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Skill points +20", "Stamina +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    

# Narita Brian
    "Strategy": (2,1), # "Speed +20", "Power +20"
    "Tact": (2,2), # "Stamina +20", "Wit +20"
    "Flexibility": (2,1), # "Speed +20 (random) Get Hot Topic status", "Guts +20 (random) Get Hot Topic status"
    "Aspiration": (2,1), # "Power +10", "Energy -10 Power +20"
    "Transcendence": (2,1), # "Power +10", "Stamina +5 Guts +5"
    "Ability": (2,1), # "Speed +15", "Passing Pro hint +1"
    "Starving Warriors": (4,1), # "Energy +5 Wit +10", "Randomly either ---------- Energy -10 Mood +1 Speed +25 ---------- Energy -10 Speed +10", "Randomly either ---------- Energy -10 Mood +1 Stamina +25 ---------- Energy -10 Stamina +10", "Randomly either ---------- Energy -10 Mood +1 Power +25 ---------- Energy -10 Power +10"
    "Carnivore": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "A Lone Wolf's Diet": (2,1), # "Speed +5 Power +5", "Stamina +10"
    "Caught by Brian!": (2,1), # "Stamina +10", "Guts +10"
    "Digging In": (3,1), # "Speed +10", "Stamina +10", "Guts +10"
    "A Lone Wolf Hunts Alone": (2,2), # "Stamina +5 Guts +5", "Power +5 Wit +5"
    "Breakthrough": (2,2), # "Stamina +10", "Wit +10"
    "Public Appearance": (2,1), # "Increased difficulty and rewards of future training goals", "Nothing happens"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    

# Narita Taishin
    "Strong Just the Way I Am": (2,2), # "Power +20", "Speed +20"
    "Taishin's SOS": (2,1), # "Speed +10 Wit +10", "Stamina +20"
    "Anxious Survival": (2,1), # "Power +20 (random) Get Charming ○ status", "Guts +10 Wit +10 (random) Get Charming ○ status"
    "Report Submitted": (2,1), # "Speed +10", "Stamina +5 Power +5"
    "Unknown Music": (2,1), # "Power +10", "Wit +10"
    "Distance": (2,1), # "Mood +1 Guts +10", "Standing By hint +1"
    "Extra Training to Blow Off Steam": (3,1), # "Energy +10", "Energy -10 Skill points +25", "Randomly either ---------- Energy -15 1 random stat +10 ---------- Energy -15 Mood +1 2 random stats +15"
    "Extra Training to De-stress?": (3,1), # "Energy +10", "Energy -10 Skill points +25", "Randomly either ---------- Energy -15 1 random stat +10 ---------- Energy -15 Mood +1 2 random stats +15"
    "Nutritional Food is the Food of Hope?": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "git gud noob": (2,2), # "Stamina +10", "Speed +10"
    "ggez": (2,1), # "Power +10", "Guts +10"
    "ggwp": (3,2), # "Guts +10", "Wit +10", "Stamina +10"
    "The Taciturn Two": (2,2), # "Stamina +10", "Speed +10"
    "Open the Cage Door with Your Own Hands": (2,2), # "Stamina +5 Guts +5", "Speed +5 Power +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Nice Nature
    "Nature and Her Tired Trainer": (2,1), # "Power +20", "Stamina +20"
    "Bittersweet Sparkle": (2,2), # "Power +20", "Speed +20"
    "Festive Colors": (2,2), # "Guts +20 (random) Get Charming ○ status", "Stamina +20 (random) Get Charming ○ status"
    "Rainy-Day Fun": (2,1), # "Wit +10", "Energy -10 Stamina +10 Guts +10"
    "Not My Style": (2,1), # "Energy +5 Mood +1", "Speed +5 Power +5"
    "Whirlwind Advice": (2,2), # "Studious hint +1", "Speed +5 Stamina +5 Power +5"
    "A Little Can't Hurt": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "A Phone Call from Mom": (2,2), # "Stamina +10", "Speed +10"
    "Once in a While": (2,2), # "Stamina +5 Guts +5", "Stamina +5 Power +5"
    "Bittersweet Twilight": (3,1), # "Speed +10", "Guts +10", "Wit +10"
    "Snapshot of Emotions": (2,1), # "Speed +10", "Power +10"
    "Let's Watch the Fish": (2,2), # "Guts +10", "Speed +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Speed +10", "Guts +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# Oguri Cap
    "Pinned Hopes": (2,1), # "Stamina +10 Power +10", "Wit +20"
    "Oguri the Forest Guide?": (2,1), # "Speed +20", "Power +20"
    "Better Than a Plushie": (2,2), # "Guts +20 (random) Get Hot Topic status", "Stamina +20 (random) Get Hot Topic status"
    "Lost Umamusume": (2,2), # "Guts +10", "Speed +10"
    "Field Workout": (2,2), # "Guts +10", "Power +10"
    "Running on Full": (2,1), # "Energy +10 Skill points +15", "Nakayama Racecourse ○ hint +1"
    "Oguri's Gluttony Championship": (2,2), # "Randomly either ---------- Energy +30 Power +10 Skill points +10 ---------- Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status", "Energy +10 Power +5 Skill points +5"
    "Bottomless Pit": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Oguri Makes a Resolution": (2,1), # "Speed +5 Wit +5", "Stamina +5 Guts +5"
    "Oguri Perseveres": (2,2), # "Guts +10", "Power +10"
    "Oguri Matures": (3,3), # "Wit +10", "Stamina +10", "Power +10"
    "Something Smells Good!": (2,1), # "Speed +10", "Guts +10"
    "High-Level Rival": (2,1), # "Speed +5 Stamina +5", "Power +5 Wit +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Power +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    

# Rice Shower
    "Am I Enough?": (2,2), # "Guts +20", "Power +20"
    "Sweet & Lively Joy": (2,1), # "Speed +10 Stamina +10", "Wit +20"
    "I Am Enough": (2,2), # "Guts +10 Wit +10 (random) Get Charming ○ status", "Stamina +10 Power +10 (random) Get Charming ○ status"
    "Training Inspiration": (2,2), # "Energy -10 Guts +20", "Energy +5 Skill points +15"
    "Wonderful New Worlds": (2,2), # "Stamina +10", "Speed +5 Wit +5"
    "Looking on the Bright Side": (2,1), # "Stamina +5 Guts +10", "Firm Conditions ○ hint +1"
    "A Page about Apples": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Even When the Ladybugs Are Gone": (2,2), # "Stamina +10", "Wit +10"
    "Even When Clouds Cover the Sky": (2,1), # "Speed +5 Power +5", "Guts +10"
    "My Sun": (3,2), # "Guts +5 Wit +5", "Speed +5 Power +5", "Stamina +10"
    "I've Got This!": (2,2), # "Guts +10", "Speed +10"
    "A Page about Sunsets": (2,1), # "Power +5 Guts +5", "Stamina +5 Wit +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Guts +10", "Energy +20", "Skill points +20"
    

# Sakura Bakushin O
    "Bakushin for Love!": (2,1), # "Stamina +10 Wit +10", "Guts +20"
    "A Day Without a Class Rep": (2,1), # "Speed +20", "Power +20"
    "Bakushin in Signature Racewear!": (2,1), # "Power +10 Guts +10 (random) Get Hot Topic status", "Wit +20 (random) Get Hot Topic status"
    "The Bakushin Book!": (2,1), # "Wit +10", "Stamina +10"
    "The Voices of the Students": (2,2), # "Energy -10 Stamina +10 Power +10", "Speed +10"
    "Solving Riddles, Bakushin Style!": (2,1), # "Guts +10 Skill points +15", "Nakayama Racecourse ○ hint +1"
    "Bakushin?! Class?!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Bakushin-ing with a Classmate!": (2,2), # "Power +5 Guts +5", "Speed +5 Wit +5"
    "The Best Bakushin!": (2,1), # "Wit +10", "Stamina +5 Guts +5"
    "Bakushin, Now and Forever!": (3,1), # "Speed +10", "Guts +5 Wit +5", "Power +10"
    "Together with Someone Important!": (2,2), # "Guts +10", "Speed +5 Stamina +5"
    "The Speed King": (2,1), # "Power +5 Wit +5", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Seiun Sky
    "Sleepy Time Incense": (2,1), # "Wit +20", "Stamina +20"
    "Tactician vs. King": (2,2), # "Guts +20", "Speed +20"
    "Who Do You Run For?": (2,2), # "Stamina +20 (random) Get Charming ○ status", "Power +20 (random) Get Charming ○ status"
    "Is Cat Language Real?": (2,2), # "Stamina +10", "Wit +10"
    "Shady Dealings": (2,1), # "Speed +10", "Power +10"
    "Sei's Escape Plan": (2,1), # "Speed +10 Skill points +15", "Subdued Late Surgers hint +1"
    "Sunny Day Standoff": (3,3), # "Randomly either ---------- Speed +20 ---------- Speed +5 Mood -1", "Randomly either ---------- Energy +20 Deep Breaths hint +1 ---------- Energy +10 Get Slacker status", "Energy +5 Speed +5"
    "I Can Unwind Outdoors Too": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Cat Expert": (2,2), # "Wit +10", "Speed +10"
    "Cat Patrol": (2,1), # "Stamina +10", "Guts +10"
    "Goodbye, Cat": (3,3), # "Wit +10", "Stamina +10", "Power +10"
    "Nap Master": (2,2), # "Stamina +10", "Wit +10"
    "Cloudy, Followed By...": (2,2), # "Guts +10", "Speed +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Stamina +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Silence Suzuka
    "The Color of the Landscape": (2,2), # "Guts +20", "Power +20"
    "Hobbies and Talents": (2,2), # "Stamina +20", "Speed +10 Wit +10"
    "Umadol ☆ Special Class!": (2,1), # "Speed +10 Power +10 (random) Get Hot Topic status", "Guts +10 Wit +10 (random) Get Hot Topic status"
    "Teaching Suzuka's Style": (2,1), # "Speed +10", "Wit +10"
    "Party Time": (2,1), # "Energy +10", "Stamina +5 Power +5"
    "On My Heels": (2,1), # "Speed +5 Skill points +15", "Left-Handed ○ hint +1"
    "White Temptation": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "My Little Snowscape": (2,2), # "Stamina +10", "Wit +10"
    "To Make You Happy": (2,2), # "Power +10", "Speed +5 Guts +5"
    "Our Little Snowscape": (3,2), # "Stamina +10", "Speed +10", "Power +10"
    "How to Spend a Rainy Day": (2,2), # "Guts +10", "Speed +5 Wit +5"
    "Are They Compatible?": (2,1), # "Power +5 Guts +5", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,1), # "Wit +10", "Guts +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Smart Falcon
    "Polished ☆ Diamond": (2,1), # "Speed +20", "Power +10 Guts +10"
    "Umadol ☆ Friendship!": (2,2), # "Wit +20", "Power +20"
    "Energetic ☆ Children": (2,1), # "Speed +20 (random) Get Charming ○ status", "Stamina +20 (random) Get Charming ○ status"
    "Studying Umadols?": (2,1), # "Power +10", "Wit +10"
    "Heart-Pounding ☆ Situation": (2,1), # "Power +10", "Stamina +10"
    "Umadol Spirit ☆ Ignited": (2,1), # "Stamina +10 Guts +10", "Leader's Pride hint +1"
    "Cuteness ☆ Research": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Test Recovery ☆": (2,2), # "Wit +10", "Power +10"
    "A Thank-You Gift for You ♪": (2,1), # "Speed +10", "Power +10"
    "Memory ☆ Lane": (3,3), # "Power +10", "Guts +10", "Speed +10"
    "Sharing ☆ Memories": (2,1), # "Stamina +10", "Guts +10"
    "Location ☆ Scouting": (2,2), # "Wit +10", "Power +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Special Week
    "How Should I Pose?": (2,1), # "Power +20", "Skill points +40"
    "Wear Your Heart on Your Sleeve": (2,1), # "Stamina +20", "Guts +20"
    "Today and Tomorrow, Too": (2,1), # "Speed +20 (random) Get Hot Topic status", "Wit +20 (random) Get Hot Topic status"
    "A Beautiful Day for Tennis": (2,1), # "Speed +10", "Stamina +10"
    "Karaoke Connoisseur ♪": (2,1), # "Energy +10", "Power +10"
    "Early Afternoon Payback": (2,1), # "Energy +5 Wit +5", "Pace Strategy hint +1"
    "Putting It Away at the Cafeteria": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Because It's Special": (2,2), # "Stamina +10", "Speed +10"
    "A Place I Want to Take You": (2,1), # "Wit +10", "Stamina +10"
    "Someone I Respect": (3,3), # "Skill points +30", "Stamina +5 Guts +5", "Speed +5 Power +5"
    "Just a Little More": (2,1), # "Homestretch Haste hint +1", "Corner Adept ○ hint +1"
    "Research Fanatic": (2,1), # "Tokyo Racecourse ○ hint +1", "Nakayama Racecourse ○ hint +1"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Stamina +10"
    "New Year's Resolutions": (3,2), # "Stamina +10", "Energy +20", "Skill points +20"
    

# Super Creek
    "A Self-Satisfying Wish": (2,1), # "Power +20", "Stamina +20"
    "Fill Life with Love": (2,1), # "Randomly either ---------- Speed +10 Stamina +10 ---------- Wit +20", "Wit +20"
    "Patience Is Key": (2,2), # "Guts +20 (random) Get Hot Topic status", "Stamina +10 Power +10 (random) Get Hot Topic status"
    "One-Day Experience ☆ Ceramics Class": (2,1), # "Speed +5 Wit +5", "Stamina +10"
    "Find the Lost Child!": (2,1), # "Energy -10 Stamina +10 Power +10", "Wit +10"
    "A Dangerous Treat": (2,1), # "Guts +10 Skill points +15", "Corner Recovery ○ hint +1"
    "Sweet Nighttime Temptation": (2,2), # "Energy +30 Speed +10 Skill points +10 (random) Mood -1 (random) Get Slow Metabolism status", "Energy +10 Speed +5 Skill points +5"
    "For My Friends": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Is Relaxing Being Spoiled?": (2,2), # "Stamina +10", "Wit +10"
    "Dispel Your Anxieties": (2,2), # "Power +10", "Speed +5 Guts +5"
    "Let's Share": (3,2), # "Stamina +10", "Speed +10", "Power +10"
    "Rough Massage!": (2,2), # "Guts +10", "Speed +5 Wit +5"
    "Stargazing is Better Together": (2,1), # "Power +5 Guts +5", "Stamina +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Stamina +10", "Energy +20", "Skill points +20"
    

# Symboli Rudolf
    "Midway Reflection": (2,1), # "Speed +20", "Power +20"
    "The Smiling Emperor's New Clothes": (2,1), # "Wit +20", "Guts +20"
    "The Distant View from the End of the Road": (2,1), # "Stamina +20 (random) Get Hot Topic status", "Guts +20 (random) Get Hot Topic status"
    "Those Who March Forth": (2,1), # "Speed +5 Power +5", "Stamina +5 Guts +5"
    "The Emperor's Social Studies": (2,1), # "Energy -10 Stamina +10 Power +10", "Wit +5 Skill points +15"
    "The Emperor's Spare Time": (2,1), # "Wit +10 Skill points +15", "Rainy Days ○ hint +1"
    "At Any Time": (2,2), # "Energy -10 Guts +20 Yayoi Akikawa bond +10", "Energy +10"
    "Sudden Kindness": (2,2), # "Energy -10 Stamina +20 Yayoi Akikawa bond +10", "Energy +10"
    "As Good As My Word": (2,2), # "Energy -10 Power +20 Yayoi Akikawa bond +10", "Energy +10"
    "The Emperor's Satiation": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Birds of a Feather": (2,1), # "Speed +10", "Stamina +10"
    "Well-Earned Respect": (2,2), # "Wit +10", "Power +10"
    "A Clear and Beautiful Night": (3,1), # "Speed +10", "Wit +10", "Stamina +10"
    "The Emperor's Daily Routine": (2,1), # "Power +10", "Guts +10"
    "The Emperor's Path": (2,2), # "Wit +10", "Power +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Wit +10", "Power +10"
    "New Year's Resolutions": (3,2), # "Wit +10", "Energy +20", "Skill points +20"
    

# Taiki Shuttle
    "Quick Draw Showdown": (2,2), # "Energy +10 Speed +10", "Energy +10 Wit +10"
    "Must-Win Match": (2,1), # "Wit +20", "Stamina +20"
    "To the Top!": (2,2), # "Power +10 Guts +10 (random) Get Fast Learner status", "Speed +10 Wit +10 (random) Get Fast Learner status"
    "Hide-and-Seek": (2,1), # "Speed +10", "Stamina +10"
    "Embracing Guidance": (2,2), # "Power +10", "Energy +10"
    "Harvest Festival": (2,1), # "Power +10 Skill points +15", "Prepared to Pass hint +1"
    "Serial Riddler": (2,1), # "Randomly either ---------- Mood +1 Stamina +5 Power +10 ---------- Mood -1", "Wit +10"
    "Taste of Home": (2,1), # "Randomly either ---------- Mood +1 Speed +10 Power +5 ---------- Mood -1", "Wit +10"
    "Meaty Heaven": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Rainy Power": (2,1), # "Power +10", "Skill points +30"
    "Rainy Choice": (2,1), # "Speed +5 Guts +5", "Stamina +5 Wit +5"
    "Rainy Rescue": (3,3), # "Skill points +30", "Power +5 Wit +5", "Speed +5 Guts +5"
    "Let's Patrol!": (2,2), # "Power +10", "Energy +10"
    "Going Home Together": (2,1), # "Mood +1 Speed +5", "Mood +1 Stamina +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Power +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# TM Opera O
    "Fit for a King": (2,2), # "Wit +20", "Power +20"
    "For My Admirer": (2,2), # "Stamina +10 Guts +10", "Speed +20"
    "Strength of Will": (2,2), # "Wit +20 (random) Get Fast Learner status", "Speed +10 Power +10 (random) Speed +20 (random) Get Fast Learner status"
    "Fantastic Voyeur": (2,1), # "Power +10", "Wit +10"
    "Blinding Beauty": (2,2), # "Energy -10 Power +20", "Speed +10"
    "Bring Me Your Finest": (2,1), # "Speed +10 Skill points +15", "Non-Standard Distance ○ hint +1"
    "Battle of Kings: The Great Ramen War": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "The Princess in Pajamas": (2,1), # "Speed +10", "Stamina +10"
    "What the Mirror Reflects": (2,1), # "Wit +10", "Guts +10"
    "My Radiance is Yours": (3,1), # "Power +10", "Guts +10", "Wit +10"
    "Maintaining Magnificence": (2,1), # "Speed +10", "Wit +10"
    "Evening Opera O Theater": (2,2), # "Power +10", "Energy +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Speed +10"
    "New Year's Resolutions": (3,2), # "Power +10", "Energy +20", "Skill points +20"
    

# Tokai Teio
    "Rivals on Paper, Friends in Practice": (2,2), # "Stamina to Spare hint +2", "Speed +10 Skill points +15"
    "The Secret to Teio Tenacity": (2,2), # "Corner Acceleration ○ hint +2", "Wit +10 Skill points +15"
    "I'm Never Giving Up!": (2,2), # "Stamina +15 Guts +5 (random) Get Practice Perfect ○ status", "Power +5 Wit +15 (random) Get Practice Perfect ○ status"
    "Empress vs Monarch": (2,1), # "Guts +10", "Skill points +30"
    "Cupcakes for All": (2,1), # "Energy +5 Mood +1", "Speed +5 Power +5"
    "Teio's Warrior Training": (2,1), # "Guts +10 Skill points +15", "Prepared to Pass hint +1"
    "Karaoke Power?": (2,2), # "Guts +10", "Speed +10"
    "Teio, an Umadol?!": (2,2), # "Power +10", "Speed +10"
    "Secret to Strength": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "I Got Praised!": (2,2), # "Stamina +10", "Speed +10"
    "I Got Scolded!": (2,2), # "Wit +10", "Power +5 Guts +5"
    "I Figured It Out!": (3,1), # "Speed +5 Stamina +5", "Guts +5 Wit +5", "Power +10"
    "Grown-Up Time": (2,2), # "Guts +10", "Wit +10"
    "Punny Prez": (2,2), # "Stamina +5 Power +5", "Speed +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Stamina +10", "Power +10"
    "New Year's Resolutions": (3,2), # "Guts +10", "Energy +20", "Skill points +20"
    "Good Luck Charm": (2,2), # "Stamina +20", "Wit +20"
    "Selfish Teio and a Nostalgic View": (2,2), # "Guts +20", "Speed +10 Power +10"
    "Racewear Like Prez": (2,1), # "Speed +10 Wit +10 (random) Get Hot Topic status", "Stamina +10 Guts +10 (random) Get Hot Topic status"

# Vodka
    "Vintage Style": (2,1), # "Power +20", "Stamina +20"
    "Makings of a Friend": (2,1), # "Speed +20 (random) Get Practice Perfect ○ status", "Guts +20"
    "Hot and Cool": (2,1), # "Speed +20 (random) Get Practice Perfect ○ status", "Speed +10 Power +10 (random) Get Practice Perfect ○ status"
    "Like a Kid": (2,1), # "Speed +10", "Power +10"
    "Challenging Fate": (2,2), # "Stamina +10", "Speed +10"
    "Showdown by the River!": (2,1), # "Wit +10 Skill points +15", "Shifting Gears hint +1"
    "Awkward Honesty": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "The Standards of Coolness": (2,1), # "Wit +10", "Guts +10"
    "Ring Out, Passionate Sound!": (2,1), # "Speed +10", "Stamina +10"
    "The Way of Cool": (3,2), # "Power +10", "Speed +10", "Stamina +5 Guts +5"
    "Let's Take a Little Detour": (2,2), # "Speed +10", "Energy +5 Mood +1"
    "Sugar and Spice": (2,1), # "Energy +5/+10", "Power +10"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Stamina +10"
    "New Year's Resolutions": (3,2), # "Speed +10", "Energy +20", "Skill points +20"
    

# Winning Ticket
    "Full-Power Testing!": (2,2), # "Guts +20", "Speed +20"
    "Full-Power Fashion!": (2,2), # "Stamina +20", "Power +10 Guts +10"
    "Full-Power Effort!": (2,1), # "Speed +10 Wit +10 (random) Get Hot Topic status", "Power +20 (random) Get Hot Topic status"
    "Rain or Shine": (2,2), # "Energy -10 Stamina +10 Skill points +15", "Power +10"
    "Overcome the Towering Obstacle!": (2,2), # "Mood +1 Guts +5", "Mood +1 Power +5"
    "A Fresh Perspective": (2,1), # "Speed +10 Skill points +15", "Nimble Navigator hint +1"
    "Full-Power Eating!": (2,2), # "Energy +10 Skill points +5", "Randomly either ---------- Energy +30 Skill points +10 or (~10%) Energy +30 Skill points +10 Speed -5 Power +5 Get Slow Metabolism status"
    "Play of the Three Kingdoms": (2,2), # "Stamina +5 Skill points +15", "Power +5 Skill points +15"
    "Futsal, Now?!": (2,2), # "Guts +10", "Speed +10"
    "The Last Ticket": (3,2), # "Guts +10", "Speed +10", "Power +10"
    "Shake Off Your Blues!": (2,2), # "Mood +1 Power +5", "Speed +5 Skill points +15"
    "Big Girls Cry Too": (2,2), # "Guts +5 Skill points +15", "Mood +1 Power +5"
    "Failed training (Get Well Soon!)": (2,1), # "Mood -1 Last trained stat -5 (random) Get Practice Poor status", "Randomly either ---------- Mood -1 Last trained stat -10 (random) Get Practice Poor status ---------- Get Practice Perfect ○ status"
    "Failed training (Don't Overdo It!)": (2,2), # "Energy +10 Mood -2 Last trained stat -10 2 random stats -10 (random) Get Practice Poor status", "Randomly either ---------- Mood -3 Last trained stat -10 2 random stats -10 Get Practice Poor status ---------- Energy +10 Get Practice Perfect ○ status"
    "Extra Training": (2,2), # "Energy -5 Last trained stat +5 (random) Heal a negative status effect Yayoi Akikawa bond +5", "Energy +5"
    "At Summer Camp (Year 2)": (2,1), # "Power +10", "Guts +10"
    "Dance Lesson": (2,2), # "Guts +10", "Wit +10"
    "New Year's Resolutions": (3,2), # "Guts +10", "Energy +20", "Skill points +20"


# [SPECIAL EVENTS]
    "New Year's Shrine Visit": (3,1), # "Energy +30", "All stats +5", "Skill points +35"
    "Acupuncture (Just an Acupuncturist, No Worries! ☆)": (5,3), # "Randomly either ---------- All stats +20 or (~70%) Mood -2 All stats -15 Get Night Owl status", "Randomly either ---------- Obtain Corner Recovery ○ skill Obtain Straightaway Recovery skill or (~55%) Energy -20 Mood -2", "Randomly either ---------- Maximum Energy +12 Energy +40 Heal all negative status effects or (~30%) Energy -20 Mood -2 Get Practice Poor status", "Randomly either ---------- Energy +20 Mood +1 Get Charming ○ status or (~15%) Energy -10/-20 Mood -1 (random) Get Practice Poor status", "Energy +10"
    "Just an Acupuncturist, No Worries!": (2, 1), # Yes, No

  
# [SCENARIOS]
# URA Finals 
    "Exhilarating! What a Scoop!": (2, 1), # "Stamina +10 Etsuko Otonashi bond +5", "Guts +10 Etsuko Otonashi bond +5"
    "A Trainer's Knowledge": (2, 2), # "Power +10 Etsuko Otonashi bond +5", "Speed +10 Etsuko Otonashi bond +5"
    "Best Foot Forward!": (2, 2), # "Energy -10 Power +20 Guts +20 Beeline Burst hint +1", "Energy +30 Stamina +20 Breath of Fresh Air hint +1"


# [RACE RESULTS]
    "Victory!": (2, 1),       # -15 Energy guaranteed
    "Solid Showing": (2, 1),  # -20 Energy guaranteed
    "Defeat": (2, 1),         # -25 Energy guaranteed
}

def get_optimal_choice(event_name):
  if not event_name:
    return (False, 1)

  cleaned_name = clean_event_name(event_name)
  
  if cleaned_name in EVENT_DATABASE:
    print(f"[INFO] Exact match found: '{cleaned_name}'.")
    return EVENT_DATABASE[cleaned_name]

  # Fuzzy match using Levenshtein distance
  best_match = find_closest_event(cleaned_name)
  
  if best_match:
    choice = EVENT_DATABASE[best_match]
    print(f"[INFO] Fuzzy match found: '{cleaned_name}' -> '{best_match}' (choice {choice[1]}).")
    return choice
  else:
    print(f"[WARNING] No suitable match found for '{cleaned_name}', using default choice 1.")
    return (False, 1)

def find_closest_event(event_name, max_distance=8):
  if not event_name:
    return None
  best_match = None
  best_distance = 99
  for db_event_name in EVENT_DATABASE.keys():
    distance = Levenshtein.distance(
      s1=event_name.lower(),
      s2=db_event_name.lower(),
      weights=(1, 1, 1)  # insertion, deletion, substitution
    )
    if distance < best_distance:
      best_distance = distance
      best_match = db_event_name
  return best_match if best_distance <= max_distance else None
    
def clean_event_name(event_name):
  cleaned = event_name.replace("`", "'")  # apostrophe variations
  cleaned = " ".join(cleaned.split())  # multiple spaces
  return cleaned
