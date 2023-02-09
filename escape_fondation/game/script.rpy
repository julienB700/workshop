# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define o  = Character('...', color="#dddddd", what_font="/fonts/newspaper.ttf")
define oo = Character('', color="#dddddd", what_font="/fonts/newspaper.ttf")
define d  = Character('D-123', color="#229933", what_font="/fonts/newspaper.ttf")
define g1 = Character('Garde', color="#ff5555", what_font="/fonts/typewriter_old.ttf" )
define g2 = Character('Autre Garde', color="#cf5555", what_font="/fonts/typewriter_clean.ttf")

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform shaking:
    xzoom 1.1 yzoom 1.1

    linear 0.1 xoffset -2 yoffset 2
    linear 0.1 xoffset 3 yoffset -3
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    repeat

transform cacahuette_pos1:
    xzoom .2 yzoom .2
    xpos .5 ypos .25

transform cacahuette_pos2:
    xzoom .4 yzoom .4
    xpos .3 ypos .30

init:
    image cacahuette = "/images/monsters/cacahuette.png"

    $ timer_range = 0
    $ timer_jump = 0

    $ karma = 0

    $ reste_cache = False
    $ porte_active = False

screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 3:
        add "chrono red.png" xpos .1 ypos .1 at alpha_dissolve
        text str(time) xpos .15 ypos .1 color "#FF0000" at alpha_dissolve
    else:
        add "chrono white.png" xpos .1 ypos .1 at alpha_dissolve
        text str(time) xpos .15 ypos .1 at alpha_dissolve

# Le jeu commence ici
label start:
    o "Tu te réveille dans un pièce fermée."

    scene bg start
    with dissolve

    o "Dans la pièce il n'y a que des cadavres portant le même uniforme que toi."
    o "Mais le plus toublant se trouve juste en face de toi :"
    o "Un cadavre te ressemblant en tout point tel un jumeau."
    o "Soudain, des gardes surgissent dans la salle, l'un d'eux a un cadavre dans
    ses bras."

    jump choice1

label choice1:
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'attaquer_gardes'

    show screen countdown
    menu:
        o "Que fais-tu ?"

        "Se coucher et faire le mort.":
            hide screen countdown
            jump faire_le_mort

        "Attaquer les gardes.":
            hide screen countdown
            jump attaquer_gardes

label faire_le_mort:
    o "Vous décidez de vous coucher par terre et de passer pour mort en esperant
    que les gardes vous ignorent."
    g1 "Encore un qui n'a pas duré longtemps !"
    g2 "Je ne comprends pas le but de ces experiences..."
    g2 "Qu'espèrent-ils accomplir au juste?"
    g1 "C'est pas notre boulot de poser de question, contente toi de faire ce qu'on
    te demande !"
    g1 "Tiens, pose-le ici."
    o "Les deux gardes jettent le corps d'un autre homme dans la salle ou vous vous
    trouvez et s'en vont."

    o "Il semblerait que vous soyez un genre de prisonnier, votre uniforme blanc est
    moche."
    o "Ils ne vous repèrent pas, après avoir jeté un cadavre dans votre salle, ils
    repartent."
    o "Vous en profitez pour sortir de la salle avant que la porte ne se ferme, en
    faisant attention de ne pas vous faire repérer."

    jump sortie_salle

label attaquer_gardes:
    d "BASTONNNNNNN!!"
    o "Les gardes vous fument de manière unilatérale."

    jump dead_end

label sortie_salle:
    scene bg couloir
    with dissolve

    o "Les gardes partent vers un couloir qui semble sans fin."

    menu:
        o "Que fais-tu ?"

        "Les suivre":
            $ suivre_gardes = True
            jump suivre_gardes

        "Prendre un autre couloir":
            $ autre_couloir = True
            jump autre_couloir

label suivre_gardes:
    o "Vous suivez les gardes."
    jump dead_end

label autre_couloir:
    scene bg couloir
    with dissolve

    o "Vous prenez l'autre couloir sans les gardes."

    scene bg intersection
    with dissolve

    o "Après avoir marché une vingtaine de secondes, vous faites face a une
    intersection."

    scene bg intersection at shaking, truecenter
    with dissolve

    play sound "/audio/scream.mp3"

    oo "..."
    scene bg intersection

    o "Vous entendez un cri de détresse inquiétant venant d'un d'un des couloirs en
    face de vous."

    jump choice_couloir

label choice_couloir:
    scene bg intersection

    if reste_cache or porte_active:
        o "Vous revenez sur vos pas et arrivez à l'intersection d'avant."
    o "Où irez-vous ?"

    menu:
        "Couloir d'où vient le cri" if not (reste_cache or porte_active):
            jump couloir_cri

        "Couloir à l'opposé d'où vient le cri":
            jump dead_end # TODO changer ici

label couloir_cri:
    o "Vous vous dirigez vers le couloir d'où venait le cri."
    o "Le cri était si inquiétant que vous vous précipitez pour de qui venait le cri."
    o "Vous arrivez à la source du bruit et constatez la scène : "
    scene bg cellule
    o "Un garde envoie des prisonniers dans une cellule ou se trouve un sorte de
    d'entité en forme de statue."
    o "Sur le mur à votre gauche se trouve un levier, ainsi qu'un gros bouton.
    Il n'y a pas d'indication sur ce que font ni le lever, ni le bouton."

    jump choice_cellule

label choice_cellule:
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'rester_cache'
    show screen countdown

    menu:
        o "Que faites-vous ?"

        "Appuyer sur le bouton":
            hide screen countdown
            jump appuie_bouton

        "Activer le levier":
            hide screen countdown
            jump activer_levier1

label rester_cache:
    $ reste_cache = True

    o "Vous êtes désemparé par la situation en face de vous et préférez rester caché."
    o "Vous entendez des cris de détenus, vous ne savez pas exactement ce qu'il
    leur arrive mais vous n'imaginez rien de bon."
    o "Vous ne pouvez rien faire de la où vous êtes et, pour éviter de vous faire
    repérer par les gardes, vous décidez de rebrousser chemin."
    scene bg intersection
    jump choice_couloir

label activer_levier1:
    $ porte_active = True

    o "Vous activez le levier à votre gauche."
    o "Le levier active une porte de secours et enferme les gardes et les prisonniers."
    o "Vous êtes séparés du groupe."
    o "Vous ne savez toujours pas ce que fait le bouton."

    menu:
        "Appuyer sur le bouton.":
            jump appuie_bouton
        "Regarder au travers de la porte.":
            jump regarder_porte

label regarder_porte:
    o "Vous aperçevez à travers "

label appuie_bouton:
    o "Vous appuyez le bouton à votre gauche."
    o "Les lumières de la zone s'éteignent, au même moment, les portes donnant sur
    la cellule s'ouvrent."

    scene bg black
    play sound "/audio/scream.mp3"

    o "Des cris retentissent dans toute la zone."
    scene bg cellule

    o "Vous rappuyez sur le bouton en esperant que la lumère se rallume."
    o "Une marre de sang coule de la porte de la cellule."
    o "Les gardes et les détenus se sont fait massacrer devant vous par l'entité que
    vous aviez entre-aperçu."

    scene bg black
    pause .5
    scene bg cellule

    o "La lumière ne semble pas correctement rétablie."

    scene bg black
    pause .5
    scene bg cellule
    show cacahuette at cacahuette_pos1

    o "Au milieu des corps apparait l'entité."
    o "La lumière clignote et vous entendez des grincement à chaque clignotements."

    scene bg black
    pause .5
    scene bg cellule
    show cacahuette at cacahuette_pos2

    o "L'entité se rapproche de vous. Vous savez ce dont elle est capable."

    if porte_active:
        o "Mais la porte que vous avez activé semble vous protéger, l'entité ne s'approche
        pas d'avantage,
        malgré le fait que la lumière continue de clignoter."
        o "Vous ne pouvez pas progresser d'avantage ici."

        jump choice_couloir

    jump choice_entite

label choice_entite:
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'fixer_entite'
    show screen countdown

    o "Que faites-vous ?"
    menu:
        "Activer le levier":
            jump activer_levier2

        "Fuir":
            jump fuite_entite

label fixer_entite:
    o "Vous fixez le monstre dans les yeux."
    o "Vous perdez la battle de regard."
    jump dead_end

label fuite_entite:
    o "Vous tentez de prendre la fuite."
    o "A peine vous tournez le regard que votre se fait briser, le monstre vous a eu."
    jump dead_end

label activer_levier2:
    jump dead_end

label dead_end:
    oo "*dead*"
    oo "FIN"
    return
