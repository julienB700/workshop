﻿# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define o  = Character('...', color="#dddddd")
define d  = Character('D-123', color="#229933")
define g1 = Character('Garde', color="#ff5555")
define g2 = Character('Autre Garde', color="#cf5555")

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0

    $ karma = 0

# Le jeu commence ici
label start:

    o "Tu te réveille dans un pièce fermée."

    scene bg room

    o "Dans la pièce il n'y a que des cadavres portant le même uniforme que toi."
    o "Mais le plus toublant se trouve juste en face de toi :"
    o "Un cadavre te ressemblant en tout point tel un jumeau."
    o "Soudain, des gardes surgissent dans la salle, l'un d'eux a un cadavre dans ses bras."

    jump choice1

label choice1:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'attaquer_gardes'

    show screen countdown
    menu:
        "Que fais-tu ?"

        "Se coucher et faire le mort.":
            hide screen countdown
            jump faire_le_mort

        "Attaquer les gardes.":
            hide screen countdown
            jump attaquer_gardes

label faire_le_mort:
    $ faire_mort = True
    "Vous décidez de vous coucher par terre et de passer pour mort en esperant que les gardes vous ignorent."
    g1 "Encore un qui n'a pas duré longtemps !"
    g2 "Je ne comprends pas le but de ces experiences..."
    g2 "Qu'espèrent-ils accomplir au juste?"
    g1 "C'est pas notre boulot de poser de question, contente toi de faire ce qu'on te demande !"
    g1 "Tiens, pose-le ici."
    "Les deux gardes jettent le corps d'un autre homme dans la salle ou vous vous trouvez et s'en vont."

    "Ils ne vous repèrent pas, après avoir jeté un cadavre dans votre salle, ils repartent."
    "Vous en profitez pour sortir de la salle avant que la porte ne se ferme, en faisant attention de ne pas vous faire repérer."

    jump suite1

label attaquer_gardes:
    $ attaquer_gardes = True
    d "BASTONNNNNNN!!"
    "Les gardes vous fument de manière unilatérale."

    jump dead_end

label suite1:
    scene bg couloir

    "Les gardes partent vers un couloir qui semble sans fin."
    menu:
        "Que fais-tu ?"

        "Les suivre":
            $ suivre_gardes = True
            jump suivre_gardes

        "Prendre un autre couloir":
            $ autre_couloir = True
            jump autre_couloir

label suivre_gardes:
    "Vous suivez les gardes."
    jump dead_end

label autre_couloir:
    "Vosu prenez l'autre couloir sans les gardes."
    jump dead_end

label dead_end:
    "*dead*"
    "FIN"
    return
