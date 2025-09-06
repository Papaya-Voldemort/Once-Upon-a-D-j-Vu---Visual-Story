init python:
    import random

define b = Character('Bob (You)', color="#c8ffc8")
define o = Character('Old Man Yells-a-Lot', color="#ffc8c8")
define p = Character('Princess Snore', color="#ffc8ff")
define d = Character('Dark Overlord', color="#ffb6c1")

define n = Character("Narrator", color="#c8c8ff")

default specialty = ""
default gold = 0
default health = 100
default stamina = 50

label start:
    show screen stats
    scene pra_a3_day1
    with fade
    n "You wake up in your bedroom, the morning sun streaming through the window."
    n "But something feels off. You hear a loud banging noise coming from outside."
    b "What the...?"

    menu:
        "Get out of bed and investigate the noise.":
            jump investigate_noise
        "Ignore it and go back to sleep.":
            jump go_back_to_sleep

    label go_back_to_sleep:
        b "It's probably nothing. I'll just go back to sleep."
        n "You close your eyes and try to ignore the noise, but it only gets louder."
        n "Suddenly, the door bursts open and an scruffy old man storms in."
        o "What are you doing sleeping through my banging?!"
        o "The chosen one must rise!"
        jump regular_person

    label investigate_noise:
        b "I should check out that noise."
        n "You get out of bed and head towards the door. As you open it, you see an old man banging on your front door."
        o "Finally! Someone who can help me!"
        o "You must be the chosen one!"
        o "The fate of the world rests on your shoulders!"
        jump regular_person

    label regular_person:
    b "What are you talking about? I'm just a regular person!"
    o "Nonsense! You have a great destiny ahead of you!"
    o "Come with me, we have much to discuss!"

    menu:
        "Go with the the Old Man.":
            jump go_with_old_man
        "Refuse and ask him to leave.":
            jump refuse_old_man

    label refuse_old_man:
        b "Look, I don't know who you are, but I don't want any part of this. Please leave."
        n "The old man looks disappointed but eventually nods."
        o "Very well I will have to do this the hard way."
        n "He runs over to you and grabs you by the arm. You try to pull away, but he's surprisingly strong."
        b "Let go of me!"
        n "Suddenly, you feel a strange sensation wash over you. The world around you starts to blur and fade away."
        scene black
        with fade

        scene restaurant_booth_day4
        with fade
        n "When you open your eyes again, you find yourself in a completely different place."
        n "You are no longer in your bedroom, but Coffee Shop."
        jump not_a_coffee_shop
        #TODO add other scene changes

    label go_with_old_man:
        n "You decide to follow the old man. Because, why not?"
        n "He leads you out of your house and into the bustling streets of the city."
        n "As you walk, he explains that you have been chosen to save the world from an impending doom."
        n "You are skeptical, but the old man insists that you have a special destiny."
        n "Suddenly, you feel a strange sensation wash over you. The world around you starts to blur and fade away."
        scene black
        with fade

        scene restaurant_booth_day4
        with fade
        n "When you open your eyes again, you find yourself in a completely different place."
        n "You are no longer in your bedroom, but Coffee Shop."
        jump not_a_coffee_shop

    label not_a_coffee_shop:
        n "You look around and realize that this is not a coffee shop at all, but a Hot Cocoa Shop."
        o "Welcome to the Hot Cocoa Shop, chosen one!"
        n "The old man sits at a table making notes on a paper, he looks up at you."
        o "Just so you know you owe me 20,000 gold for the cocoa."
        b "What?! I don't have that kind of money!"
        o "And 400,000 gold for the Chosen-One Destiny Package™"
        b "This is ridiculous! I don't want any part of this!"
        o "Nonsense! You have a great destiny ahead of you!"
        o "And you will pay for it!"

    menu:
         "Pay the ridiculously high fees and go along with the Old Man.":
             jump pay_fees
         "Refuse and try to run away.":
             jump run_away
         "Complain loudly about the absurdity of it all.":
             jump complain
         "Attempt to negotiate for a discount (or free cocoa).":
             jump negotiate

    label pay_fees:
        b "Fine! I'll pay the fees. Just give me the cocoa."
        $ gold -= 420000
        n "The old smiles and hands you a cup of hot cocoa."
        n "You take a sip and feel a warm sensation spread through your body."
        n "Suddenly, the world around you starts to blur and fade away."
        with fade
        jump training

    label run_away:
        b "I can't believe this! I'm out of here!"
        n "You turn and run out of the shop, the old man yelling after you."
        o "You can't escape your destiny, or your fees!"
        n "You run through the streets, trying to put as much distance between you and the old man."
        n "After a few blocks, you finally stop to catch your breath."
        n "You realize that you are lost and have no idea where you are."
        o "Well, well, well. Look who decided to run away."
        n "You turn around to see the old man had somehow caught up to you."
        o "You can't escape your destiny, or your fees!"
        $ gold -= 420000
        n "He grabs you by the arm and puts a cup of hot cocoa in your hand."
        n "You sigh and take a sip a warm sensation spreads through your body."
        n "Suddenly, the world around you starts to blur and fade away."
        with fade
        jump training

    label complain:
        b "This is absurd! 20,000 gold for a cup of cocoa? And 400,000 gold for some destiny package? Who do you think I am, a millionaire?"
        n "The old man sighs and shakes his head."
        o "You don't understand, chosen one. This is a once in a lifetime opportunity."
        o "You must pay the fees if you want to fulfill your destiny."
        b "I still think it's ridiculous. I never ordered any of this."
        b "Do you do this to your other customers?"
        o "Of course not! You are special, I only charge 17,000 gold for regular customers."
        b "WHAT!? Why don't I get charged the same?"
        o "Because you are the chosen one! You have a great destiny ahead of you!"
        b "This is unbelievable. I can't believe I'm even considering this."
        b "Just give me the cocoa and I'll pay your fees."
        $ gold -= 420000
        n "You sigh and take a sip a warm sensation spreads through your body."
        n "Suddenly, the world around you starts to blur and fade away."
        with fade
        jump training

    label negotiate:
        b "Look, I don't have that kind of money. Is there any way we can work something out? Maybe a discount or a payment plan?"
        n "The old man looks over at you, a glint of greed in his eyes."
        o "Hmm, I suppose I could give you a payment plan. How about 10,000 gold a month for the next 500 years?"
        b "500 years!? That's ridiculous! I can't afford that!"
        o "Well, if you want to fulfill your destiny, you'll have to find a way to pay."
        b "This is unbelievable. I can't believe I'm even considering this."
        b "Just give me the cocoa and I'll start my payments."
        $ gold -= 10000
        n "You sigh and take a sip a warm sensation spreads through your body."
        n "Suddenly, the world around you starts to blur and fade away."
        with fade
        jump training

    label training:
        n "When you open your eyes again, you find yourself in a training room."
        n "The old man stands in front of the room, a young girl asleep on the ground."
        o "Welcome to your training, chosen one!"
        o "This is Princess Snore the only other surviving participant in the Chosen-One Package!"
        o "She is a powerful sorceress, but she sleeps a LOT, like a lot a lot."
        o "You will need to train hard to keep up with her."
        b "Great, just what I always wanted. To train with a sleeping princess."
        o "Now, let's get started!"
        n "Insert training montage here!"
        n "I mean: After weeks of intense training, you and Princess Snore have become quite the team."
        n "Princess Snore may sleep a lot, but when she's awake, she's a force to be reckoned with."
        n "And you... well, your getting better at dodging her spells."

        o "Now, chosen one, it's time for your final test."
        o "You must pick your specialty, the one skill that will define your destiny."

    label final_test:
        menu:
            "Become a Therapist (listener of woes).":
                $ specialty = "Therapist"
                jump confirm_specialty

            "Become a Dog Walker (bringer of brisk strolls).":
                $ specialty = "Dog Walker"
                jump confirm_specialty


            "Become an Accountant (keeper of mysterious ledgers).":
                $ specialty = "Accountant"
                jump confirm_specialty


            "Become an Event Planner (organizer of excessive banquets).":
                $ specialty = "Event Planner"
                jump confirm_specialty



    label confirm_specialty:
        n "You have chosen to become a [specialty] right?"
        menu:
            "Yes, that's right.":
                jump battle_preparation
            "Wait, can I change my mind?":
                jump final_test

    label battle_preparation:
        o "Odd choice, but I suppose it will do. I am not sure what a [specialty] does, but it sounds important."
        o "Now, we must prepare for the final battle against the Dark Overlord."
        o "First you must beat Princess Snore, she is the final test."
        n "Princess Snore wakes up, stretching and yawning."
        p "Oh, hey there! Ready for our final battle?"
        b "Sure, let's get this over with."

        label battle_choice:
        n "What is your move?"
        menu:
            "Use your specialty to outsmart Princess Snore.":
                jump use_specialty
            "Try to reason with Princess Snore.":
                jump reason_with_princess
            "Dodge her attacks and wait for an opening.":
                jump dodge_attacks
            "Attempt to flee the battle.":
                jump flee_battle
            "Try to land a hit.":
                jump land_hit

    label use_specialty:
        if specialty == "Therapist":
            b "Princess Snore, I understand that you may be feeling overwhelmed with all this training and the pressure of being the chosen one. But you don't have to do this alone. I'm here to listen and support you."
            p "Wow, I never thought of it that way. Thank you for understanding."
            n "Princess Snore lowers her weapon and sits down, looking thoughtful."
            n "You have successfully used your specialty to outsmart Princess Snore."
            jump end_of_final_test
        elif specialty == "Dog Walker":
            b "Princess Snore, I know this battle is intense, but sometimes a good walk can help clear your mind and reduce stress. How about we take a break and go for a walk?"
            p "A walk does sound nice. Maybe we can talk things over while we stroll."
            n "She looks up at you, considering your suggestion."
            p "But walks are for dogs!"
            n "She launches a spell at you, while you're distracted."
            if random.randint(1, 100) <= 50:
                n "You manage to dodge the spell and continue the battle."
                jump battle_choice
            else:
                n "The spell hits you, and you feel a sharp pain."
                $ health -= 20
                if health <= 0:
                    n "You have been defeated by Princess Snore."
                    jump game_over
                else:
                    n "You are injured but still in the fight."
                    jump battle_choice
        elif specialty == "Accountant":
            b "Princess Snore, have you considered the financial implications of this battle? The cost of magical damage to the city could be astronomical. Perhaps we can find a more cost-effective solution."
            p "Hmm, I hadn't thought about that. Maybe we can negotiate a truce."
            n "Princess Snore lowers her weapon, intrigued by your argument."
            p "Let's discuss this further. After I destroy you!"
            n "She launches a spell at you."
            if random.randint(1, 100) <= 50:
                n "You manage to dodge the spell and continue the battle."
                jump battle_choice
            else:
                n "The spell hits you, and you feel a sharp pain."
                $ health -= 20
                if health <= 0:
                    n "You have been defeated by Princess Snore."
                    jump game_over
                else:
                    n "You are injured but still in the fight."
                    jump battle_choice
        elif specialty == "Event Planner":
            b "Princess Snore, I understand that battles can be chaotic and stressful. Perhaps we can organize a grand event to celebrate our training and the journey we've been on. It could be a way to channel our energies positively."
            p "An event? That sounds... interesting. Maybe we can plan something together."
            n "Princess Snore lowers her weapon, intrigued by your suggestion."
            p "But first, I must defeat you!"
            n "She launches a spell at you."
            if random.randint(1, 100) <= 50:
                n "You manage to dodge the spell and continue the battle."
                jump battle_choice
            else:
                n "The spell hits you, and you feel a sharp pain."
                $ health -= 20
                if health <= 0:
                    n "You have been defeated by Princess Snore."
                    jump game_over
                else:
                    n "You are injured but still in the fight."
                    jump battle_choice

    label reason_with_princess:
        b "Princess Snore, we don't have to fight. We can work together to defeat the Dark Overlord."
        p "Hmm, you make a good point. Maybe we can team up."
        n "Princess Snore lowers her weapon, considering your words."
        p "Or I could take all the fame for myself!"
        n "She launches a spell at you."
        if random.randint(1, 100) <= 50:
            n "You manage to dodge the spell and continue the battle."
            jump battle_choice
        else:
            n "The spell hits you, and you feel a sharp pain."
            $ health -= 20
            if health <= 0:
                n "You have been defeated by Princess Snore."
                jump game_over
            else:
                n "You are injured but still in the fight."
                jump battle_choice

    label dodge_attacks:
        n "You focus on dodging Princess Snore's attacks, waiting for an opening."
        $ stamina -= 10
        if stamina <= 0:
            n "You are too exhausted to continue dodging effectively."
            n "Princess Snore lands a major hit on you."
            $ health -= 100
            if health <= 0:
                n "You have been defeated by Princess Snore."
                jump game_over
            else:
                n "You are injured but still in the fight."
                jump battle_choice
        if random.randint(1, 100) <= 90:
            n "You successfully dodge her spell and find an opening."
            jump battle_choice
        else:
            n "The spell hits you, and you feel a sharp pain."
            $ health -= 20
            if health <= 0:
                n "You have been defeated by Princess Snore."
                jump game_over
            else:
                n "You are injured but still in the fight."
                jump battle_choice

    label flee_battle:
        b "I can't do this! I'm out of here!"
        n "You turn and run, but Princess Snore quickly catches up to you."
        p "You can't escape your destiny!"
        n "She lands a major hit on you as you try to flee."
        $ health -= 100
        if health <= 0:
            n "You have been defeated by Princess Snore."
            jump game_over
        else:
            n "You are injured but still in the fight."
            jump battle_choice

    label land_hit:
        if random.randint(1, 100) <= 30:
            n "You land a hit on Princess Snore, catching her off guard."
            n "She stumbles back, surprised by your attack."
            n "You have successfully defeated Princess Snore."
            jump end_of_final_test
        else:
            n "Your attack misses, and Princess Snore quickly retaliates."
            n "You feel a sharp pain as she lands a hit on you."
            $ health -= 20
            if health <= 0:
                n "You have been defeated by Princess Snore."
                jump game_over
            else:
                n "You are injured but still in the fight."
                jump battle_choice







    label end_of_final_test:
        n "With Princess Snore defeated, you have passed your final test."
        o "Nice work, chosen one! You are ready to face the Dark Overlord."
        o "But first can I interest you in our Deluxe Destiny Package™ for only 1,000,000 gold?"
        b "Ugh, not again. Do I have to?"
        o "Of course! It's a once in a lifetime opportunity!"
        b "I am OK, thanks."
        o "It includes a shiny new sword and a map to the Dark Overlord's lair!"

        menu:
            "Reluctantly agree to buy the Deluxe Destiny Package™.":
                $ gold -= 1000000
                n "You hand over the gold and receive the Deluxe Destiny Package™."
                n "You feel a surge of power as you equip the shiny new sword."
                $ sword = True
                $ map = True
                jump final_battle
            "Refuse and prepare to face the Dark Overlord without it.":
                n "You decide to face the Dark Overlord without the Deluxe Destiny Package™."
                n "You steel yourself for the final battle ahead."
                jump travel_final_battle

    label travel_final_battle:
        n "You and Princess Snore travel for days, following the map to the Dark Overlord's lair."
        n "Along the way, you encounter various challenges and obstacles, but you manage to overcome them together."
        n "You did lose some health and stamina along the way, but you are determined to see this through."
        $ health -= 20
        $ stamina -= 10
        if health <= 0 or stamina <= 0:
            n "You have become too weak to continue your journey."
            jump game_over
        n "Finally, you reach the entrance to the Dark Overlord's lair."
        jump final_battle

    label final_battle:
        n "You and Princess Snore enter the Dark Overlord's lair, ready for the final battle."
        n "The Dark Overlord stands before you, a menacing figure shrouded in darkness."
        d "So, you have made it this far, chosen one. But this is where your journey ends."
        n "The final battle begins!"
        if sword and map:
            n "The Dark Overlord sees your shiny new sword and the map, and he looks worried."
            d "Avada Kedav-"
            d "Oops that might be copyrighted..."
            d "Die you insignificant mortal!"
            n "Princess Snore falls over."
            n "Asleep of course."
            d "What do you want from me?"

            menu:
                "To destroy you and stop your evil plans.":
                    n "You raise your shiny new sword and strike down the Dark Overlord."
                    n "With a final roar, he collapses to the ground, defeated."
                    n "You have saved the world!"
                    n "Congratulations, chosen one! You have fulfilled your destiny."
                    $ price = gold + gold*2
                    o "All for the low, low price of [price] gold!"
                    return
                "Why am I even doing this? This is all so absurd.":
                    n "You lower your sword, feeling disillusioned with the whole situation."
                    d "Good! I was hoping you'd say that. Because I'm actually just a regular guy trying to make a living."
                    d "This whole 'Dark Overlord' thing is just the only way I can make money right now"
                    d "You see this awful old man scammed me out of my Hot Cocoa Shop and now I'm stuck doing this."
                    b "Wait, I know that guy!"
                    b "I owe him a lot of money too!"
                    b "Lets go take back your Hot Cocoa Shop and get rid of that old guy!"
                    n "You and the Dark Overlord team up to take down Old Man Yells-a-Lot freeing countless people from his fees and getting the Hot Cocoa Shop back!"
                    n "You have saved the world!"
                    n "Congratulations, chosen one! You have fulfilled your true destiny."
                    return
        else:
            #TODO make other ending

            return









    label game_over:
        n "Game Over. You have been defeated."
        return
