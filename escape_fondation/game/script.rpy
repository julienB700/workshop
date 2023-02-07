# Vous pouvez placer le script de votre jeu dans ce fichier.

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
    jump suivre_gardes


label suivre_gardes:
    "Vous continuez à suivre les gardes."
    "Après quelques minutes, ils arrivent dans une grande pièce.  Celle-ci semble être leur salle de pause."
    "Après quelque minutes les gardes commencent a se désarmer laissant leur armes sans surveillance."
    menu:
        "Tuer les gardes discrètement":
            jump tuer_discret
        "Prendre des armes et se cacher":
            jump armes_cacher

label tuer_discret:
    "Vous tuez les gardes."
    "Vous entendez des pas dans le couloir."
    menu:
        "Prendre les vêtements des gardes et se faufiler parmis les arrivants.":
            jump
        "Cacher les corps puis se cacher.":
            jump
        "Fouiller les corps.":
            jump fouiller_corps
    
label fouiller_corps:
    $weapon=True
    "Vous fouillez les corps et trouvez une arme à feu ainsi qu'une carte magnétique de niveau 1."
    "Le temps que vous fouilliez les corps, deux autres gardes sont arrivés. Que voulez-vous faire?"
    menu:
        "Les prendre en joue.":
            jump braquer
        "Arrêter de fouiller et se cacher.":
            jump stop_fouille

label stop_fouille:
    "Vous restez cacher, pendant ce temps d'autres gardes arrivent. Vous êtes maintenant en très mauvaise posture, si vous ne faites rien ils vous auront"
#__________________________________________________________________________________________
label armes_cacher:
    $weapon=True