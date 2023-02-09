# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define o  = Character('...', color="#dddddd")
define d  = Character('D-123', color="#229933")
define g1 = Character('Garde', color="#ff5555")
define g2 = Character('Autre Garde', color="#cf5555")
define r  = Character('Robert', color="#229933")

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
    $ weapon = False
    $ karma = 0

# Le jeu commence ici
label start:
    jump suivre_gardes


label suivre_gardes:
    scene bg_soldats
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
        "Cacher les corps puis se cacher.":
            jump cache_cache
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
    
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'dead_end'
    show screen countdown
    "Vous restez caché, pendant ce temps d'autres gardes arrivent. Vous êtes maintenant en très mauvaise posture, si vous ne faites rien ils vous auront"
    menu:
        "Les prendre en joue":
            hide screen countdown
            jump braquer
    
label braquer:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'rien_dire'
    show screen countdown

    "Vous prenez les gardes en joue, eux aussi vous menacent"
    menu:
        "Abattre les deux gardes":
            "Vous tirez, vous abattez le premier garde, le deuxième vous blesse légèrement à l'épaule."
            "Il ne vous tue pas et vous regarde, il n'a pas l'air agressif."
            hide screen countdown
            jump abattre

label cache_cache:
    "Vous cachez les corps puis vous vous cachez"
    jump stop_fouille

label armes_cacher:
    $weapon=True
    jump stop_fouille

label abattre:
    "Vous êtes blessé, vous devez vous reposer cependant vous n’êtes pas dans un lieu sûr. "
    menu:
        "Demander pitié au garde":
            d "Pitié monsieur laissez moi tranquille"
            jump pitie
        "Se reposer quand même":
            jump reposer
        "Fuire la salle de pause":
            jump salle_vide
label rien_dire:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'rien_faire'
    show screen countdown
    "Un des gardes prit en joue son collègue et l’abattit sèchement." 
    "Que voulez-vous faire ?"
    menu:
        "Lui demander qui il est":
            hide screen countdown
            jump pres_robert
        
label pres_robert:
    g2 "Je m'appelle Robert, je suis agent secret."
    menu:
        "Pourquoi ne pas m'avoir tué?":
            jump team_robert
        "Merci de m'avoir sauvé":
            jump team_robert

label team_robert:
    r "J'aimerai faire équipe avec toi"# BIG CHANGEMENT ICI A FAIRE ATTENTION DIQUHUIQHUIQFHUIQFHYGH!!!!!!!!!!!!!
    menu:
        "Vous mentez":
            jump mensonge
        "Lui demander les bonnes raisons de le suivre":
            jump pourquoi
        "Accepter mais le mettre en garde":
            jump acceptation

label mensonge:
    d "Vous mentez! Je ne crois pas un mot de ce que vous dîtes."
    "Une bataille fait rage entre vous et l'agent du Chaos. Vous finissez par le mettre à terre et l'exécuter "
    jump abattre

label pourquoi:
    d "Pourquoi devrais-je vous suivre? "
    r "Je suis le seul en qui vous pouvez avoir confiance pour vous sortir de cet enfer."
    menu:
        "Accepter":
            jump double_accept
        
label reposer:
    "Le temps que vous vous reposiez de nouveaux gardes sont arrivés et vous ont pourchassé, vous commencez à fuir cependant, ils continuent de vous suivre. Au bout de quelques minutes, ils commencent à vous rattraper, vous êtes fatigué. Vous tombez dans les pommes et à votre réveil vous êtes attaché sur une chaise dans une grande salle. Vous commencez à entendre des gros bruits et à apercevoir une ombre au loin. L'ombre se rapprochant de plus en plus laissant place à une silhouette abominable. Une sorte d'énorme ver commence à se rapprocher et soudain vous saute dessus. C'est la fin, vous finissez dans son estomac."
    jump start

label dead_end:
    "GAME OVER "
    return

label rien_faire:
    g2 "Bonjour, je m'appelle Robert, je suis agent secret."
    jump team_robert

label acceptation:
    d "J'accepte de vous suivre, mais vous 'avez pas intérêt de me la faire à l'envers, ou vous le regretterez."
    jump double_accept

label double_accept:
    "Il sort de sa poche une carte de l'endroit et vous montre la sortie dont-il parle."
    "Vous continuez votre route avec Robert. Vous arrivez dans une salle. Avant d'y entrer, Robert vous prévient qu'un monstre devrait se trouver dans cette salle et qu'il faudra l'affronter pour arriver à la porte menant à la suite.Robert ouvre la porte et commence à avancer. 
    Que voulez-vous faire ?"



label pitie:
    "Les gardes vous mettent une balle entre les deux yeux."
    jump start

