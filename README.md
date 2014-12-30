Shirra's Ren'Py Battle Framework
=================
<br>
<br>Designed to handle a 1 on 1 battle setup, much like classic Dragon Warrior, or Monster Girl Quest.
<br>
<br>http://creativecommons.org/licenses/by-nc/3.0/
<br>Taking a page from the admittedly far more amazing Battle Engine for Ren'Py by Jake, this is Licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License.  If you really want to license it, realize you won't get much support.  If you really want to work with an engine for a commercial project, hire a programmer!  .. Unless you really want to give me money.  I like money!
<br>
<br>Uses Ren'Py v6.18.3.761
<br>http://www.renpy.org/latest.html
<br>
<br>Current Builds - https://github.com/ShirraWhitefur/PyBattleFramework/tree/master/Builds
<br>Current Code - https://github.com/ShirraWhitefur/PyBattleFramework/tree/master/
<br>
<br>Feature List:
<br>  One on One battles (And -only- one on one, not intended for more.)
<br>  Initiative system (You and the enemy choose your actions, but who acts first is random.)
<br>  14 Different attributes for bonuses.
<br>  No statistic system built in, but room to add it.
<br>  Health Points, Ability Points, Will Points
<br>  Damage types for Melee, Ranged, Magic, Will
<br>  Armor types for Physical, Magic, Will.
<br>  Accuracy vs Dodge for physical attacks.
<br>  Equipment system with Weapon, Upper and Lower Armor, Necklace, and Rings already set up.
<br>  Healing and AP potions already set up.
<br>  Auto-detection of weapon to-hit and damage type for main weapon attack.
<br>  Weapon damages separate from the damage bonuses
<br>  Status Effects
<br>	Poison / Regen, Slow / Haste, Weaken / Strengthen
<br>	Paralyse, Charm, Sleep (The last two are functionally the same at the moment)
<br>	Disarm, Remove Equipment (To be used with Armor Break or other similar actions)
<br>  Ugly Status frames in combat to show most of the above for debugging and ideas on how to link in your better looking graphical ui later.
<br>  Likewise ugly out of combat status screen.
<br>  Two premade, fairly simple enemies.. who use every variable the player does.
<br>  Enemies laid out to be loaded from files, making it easier to add new ones.
<br>  Enemies using a random weighted choice based AI, with examples.
<br>  Enemies also use the equipment system.
<br>  Simple test area, with very basic menu driven vendor.
<br>  Most things sectioned off into their own files for easier organization.
<br>  Intelligent / Self-Apparent variable and label names, to make it far easier to pick apart and figure out what the heck various things do.
<br>  Fairly heavily commented code.  Apologies for where I ramble.
<br>  Aside from a blank blue background, _NO_ graphics included (or needed.) 
<br>   ... That enough examples for people to learn with?
<br>
<br>There's one -BIG- downside though.  This is coded in the most basic fashion, making tons of use of variables, if-else, jumps, and calls.  It's probably done in the most inefficient possible methods, though it does make it quite a bit easier for the non-programmer (or someone who's last big programming project was Basic) to follow and understand.  Alas, that inefficiency has caused some rather appalled reactions from professional programmer friends.  It's also why there's an extremely brief pause when battle starts, as it gets all of it's variables in order.
<br>Total days spent programming for the 0.6b3 release, the official 'Open' release - 6 days of around 10-15 hours each.  There are likely to be bugs that were missed.
<br>Disarm and Remove Equipment status effects have not been thoroughly tested yet.  It's on the to do.
<br>
<br>Further notes.
<br>  Yes, I'm willing to build and up the Linux and Mac builds.. though why not just install the SDK and build it instead.. since you're going to need the SDK to build your VN anyways?
<br>  No.  I will not customize this for your VN for free.  And honestly, I recommend more experienced programmers over me (who don't code like a run away train wreck, cackling all the while.) if you want to pay for customization.
<br>  No.  I will not sit down and carefully explain large chains of functions.  I might answer some questions, maybe, but I'm trying to rely on commenting and self-apparent naming to solve most of the questions.
<br>  Generally assume anything that boils down to 'Do it for me' is a 'no'.
<br>  Yes, I'll take donations.  I'm shameless that way.  Absolutely shameless.  Though consider if you should donate to PyTom first for the awesome engine.  .. .. Can we donate to PyTom even?  I honestly don't know!
<br>  I have -no- idea if I'll post any updates to the github, as I will be shortly starting on adapting my framework further for my own game design.  We'll see if I bring any useful things back to it!  That said, I do want to update it with more of the abilities ready to use and a monster that pretty much rains status effects on the player, for easier testing of them.
<br>
<br>Huge thanks go out to:
<br>  PyTom for making Ren'Py utterly awesome and continuing to support it.  Good gods, the awesome things I've been able to do within a mere six days!
<br>  Jake for frustrating me by making absurdly awesome battle engine stuff that would need licensing for the commercial bit I want to do.. and thusly leading me to make my own far less grand battle engine.  If his had been totally free, I wouldn't have gotten to have all this fun!  Seriously folks, check that thing out.
<br>  Asceai - For a snippet of code I stumbled on in the forums to do weighted random choices leading to jumps and calls.  It's pretty much the enemy AI.
<br>  Xavimat - For answering my only forum posted question by pointing me at screens.  I did a lil' hair pulling trying to switch from ui.* to screens because they don't call things the same or function quite the same.. but once I got into it, it works soooo much nicer.
<br>  Whoever made the tutorial - Since I don't see any credits in it.  Thanks for that lovely thing.  It got me over a few questions.. though I admit to only realizing I had it 24 hours into coding.  Hehe.
<br>  The Forums In General - There's a ton of people on http://lemmasoft.renai.us who are really really helpful, and my websearches there answered probably a dozen quick questions before I had to ask them.
<br>    Rock on folks.
