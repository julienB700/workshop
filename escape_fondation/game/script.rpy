# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define o  = Character('...', color="#dddddd", what_font="/fonts/newspaper.ttf")
define oo = Character('', color="#dddddd", what_font="/fonts/newspaper.ttf")
define d  = Character('D-123', color="#229933", what_font="/fonts/newspaper.ttf")
define g1 = Character('Garde', color="#ff5555", what_font="/fonts/typewriter_old.ttf" )
define g2 = Character('Autre Garde', color="#cf5555", what_font="/fonts/typewriter_clean.ttf")
define d1 = Character('Detenu D-182', color="#22cc33", what_font="/fonts/newspaper_clean.otf")
define d2 = Character('Detenu D-120', color="#11ff66", what_font="/fonts/newspaper.ttf")
define caca = Character('???', color="#555555", what_font="/fonts/alien2.ttf")
define waf = Character('Chien', color="#999999", what_font="/fonts/newspaper.ttf")
define r  = Character('Robert', color="#229933", what_font="/fonts/typewriter_clean.ttf")

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

transform perso:
    xzoom 1 yzoom 1
    xpos .1 ypos.3


transform perso2:
    xzoom 1 yzoom 1
    xpos .3 ypos.3

transform perso3:
    xzoom 1 yzoom 1
    xpos .3 ypos.3

transform Chien:
    xzoom 1 yzoom 1
    xpos .3 ypos.3

transform garde:
    xzoom 1 yzoom 1
    xpos .7 ypos.3

transform garde2:
    xzoom 1 yzoom 1
    xpos .1 ypos.3

transform mort:
    xzoom 2 yzoom 2
    xpos.1 ypos.3



init:
    image cacahuette = "/images/monsters/cacahuette.png"
    image chien = "/images/monsters/chien.png"
    image perso = "/images/monsters/perso.png"

    $ timer_range = 0
    $ timer_jump = 0
    $ karma = 0

    $ regarder_porte = False
    $ reste_cache = False
    $ porte_active = False
    $ levier2 = False
    $ ignore = False
    $ weapon = False
    $ dead_once = False

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
    scene bg black
    o "Vous vous réveillez dans un pièce fermée."

    scene bg start
    with dissolve

    if not dead_once:
        o "Qu'est ce que je fais ici ?"
        o "Qu'est ce qu'il m'arrive ?"
        d "D-123 ?"

        o "L'identifiant D-123 est noté sur votre vêtement."
        o "Dans la pièce il n'y a que des cadavres portant le même uniforme que vous."
        o "Mais le plus toublant se trouve juste en face de vous :"
        o "Un cadavre vous ressemblant en tout point tel un jumeau."
    else:
        o "..."
        d "Qu'est ce que je fais ici ?"
        o "Vous vous réveillez dans la même salle que la d'où vous venez."
        o "Vous observez autour de vous, toujours la même chose :"
        o "Une pile de cadavres avec un uniforme orange."

    play sound "/audio/bruit_pas.mp3"
    o "Soudain, des gardes surgissent dans la salle, l'un d'eux a un cadavre dans
        ses bras."

    jump choice1

label choice1:
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'attaquer_gardes'

    show screen countdown
    menu:
        o "Que faites-vous ?"

        "Se coucher et faire le mort.":
            hide screen countdown
            jump faire_le_mort

        "Attaquer les gardes.":
            hide screen countdown
            jump attaquer_gardes

label faire_le_mort:

    o "Vous décidez de vous coucher par terre et de passer pour mort en esperant
        que les gardes vous ignorent."

    show garde at garde with dissolve

    show garde2 at garde2 with dissolve

    g1 "Encore un qui n'a pas duré longtemps !"
    g2 "Je ne comprends pas le but de ces experiences..."
    g2 "Qu'espèrent-ils accomplir au juste?"
    g1 "C'est pas notre boulot de poser de question, contente toi de faire ce qu'on
        te demande !"
    g1 "Tiens, pose-le ici."
    play sound "/audio/bruit_corp.mp3"
    o "Les deux gardes jettent le corps d'un autre homme dans la salle ou vous vous
        trouvez et s'en vont."

    o "Il semblerait que vous soyez un genre de prisonnier, votre uniforme orange est
        exactement le même que ceux portés par les cadavres à côté de vous."
    o "Les gardes ne vous repèrent pas, après avoir jeté un cadavre dans votre salle,
        ils repartent."
    hide garde
    hide garde2
    o "Vous en profitez pour sortir de la salle avant que la porte ne se ferme, en
        faisant attention de ne pas vous faire repérer."

    jump sortie_salle

label attaquer_gardes:
    d "BASTONNNNNNN!!"
    play sound "/audio/bruit_fusillade.mp3"
    o "Les gardes vous fument de manière unilatérale."

    jump dead_reset

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
    o "Que fais-tu?"

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'suivre_gardes2'
    show screen countdown
    menu:
        "Attaquer discrètement":
            hide screen countdown
            jump attaque_discret

        "Attaquer frontalement":
            hide screen countdown
            jump attaque_frontale

label attaque_discret:
    $ weapon = True
    $ carte_magnetique = True
    o "Vous attaquez les gardes par derrière : l'effet de surprise
        les rends confus et vous arrivez a les immobiliser et les
        rendre hors d'état de nuire."
    o "En les fouillant vous trouvez une arme et une carte d'accès."

    o "Vous continuez de marcher et arrivez a une intersection."

    jump choice_couloir

label attaque_frontale:
     o "Les gardes vous explosent assez facilement."
     jump dead_reset

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

    if reste_cache or porte_active or regarder_porte or levier2 or ignore:
        o "Vous revenez sur vos pas et arrivez à l'intersection d'avant."
    o "Où irez-vous ?"

    menu:
        "Couloir d'où vient le cri" if not (reste_cache or porte_active or regarder_porte or levier2 or ignore):
            jump couloir_cri

        "Couloir à l'opposé d'où vient le cri":
            jump couloir_oppose

label couloir_oppose:
    o "Vous décidez de vous éloigner de la d'où venait le cri, ça fait peur."
    o "Au bout de quelques temps vous tombez sur une porte, mais au même moment,
        des gardes arrivent, en face de la porte se trouve un distributeur derrière
        lequel vous pouvez vous cacher."

    o "Que faites-vous ?"

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'dead_reset' #TODO quoi ici
    show screen countdown
    menu:
        "Porte":
            hide screen countdown
            jump porte_droite
        "Se cacher":
            hide screen countdown
            jump se_cacher

label se_cacher:
    o "Vous tentez de vous cacher derrière le distributeur."
    o "En vous postant derrière celui-ci, vous vous cognez le coude ce qui provoque
        un bruit assez conséquent."
    d "Aïe."
    g1 "Qui est là ?"

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'rien_dire'
    show screen countdown

    o "Que faites-vous ?"
    menu:
        "Ne rien dire/faire":
            hide screen countdown
            jump rien_dire
        "Les prendre en joue" if weapon:
            hide screen countdown
            jump braquer


label couloir_cri:
    o "Vous vous dirigez vers le couloir d'où venait le cri."
    o "Le cri était si inquiétant que vous vous précipitez pour de qui venait le cri."
    o "Vous arrivez à la source du bruit et constatez la scène : "
    scene bg cellule
    o "Un garde envoie des prisonniers dans une cellule ou se trouve un sorte de
        d'entité en forme de statue."
    o "Sur le mur à votre gauche se trouve un levier, ainsi qu'un gros bouton.
        Il n'y a pas d'indication sur ce que font ni le lever, ni le bouton."
    o "Vous trouvez une carte magnétique de niveau 1 posée à côté du bouton."

    $ carte_magnetique = True

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

        "Attaquer les gardes avec l'arme" if weapon:
            hide screen countdown
            jump attaquer_arme_cellule

label attaquer_arme_cellule:
    o "Vous attaquez les deux gardes qui se trouvent devant vous."
    o "Par miracle, les gardes, tels des stormtroopers, ne parviennent pas vous mettre
        en danger, et vous parvenez a leur tirer tout les deux dessus."
    o "Les deux gardes tombent à terre, ggwp ez"
    o "Vous aperçevez à côté des deux corps, deux personnes se tenant debout, vous vous demandez
        un moment si vous voyez double et si vous n'êtes pas fou."
    o "Ils s'avèrent après vérification occulaire qu'il ne s'agit pas de gardes mais de deux
        prisonniers que vous avez sauvé."

    o "Que faites-vous ?"
    menu:
        "Leur taper la discute":
            jump prisonniers_discuter
        "Saluer et continuer votre chemin":
            jump prisonniers_ignorer

label prisonniers_ignorer:
    $ ignore = True
    if aggro:
        o "Vous décidez de ne pas être gentil et, de manière totalement irrespectueuse
            ignorer l'approche du prisonnier en face de vous pour vous éloigner."
    else:
        o "Vous saluez de loin les prisonniers, ils vous font signe en retour."

    o "Il n'y a pas d'autre chemin ou progresser, vous décidez donc de retourner sur vos pas."

    jump choice_couloir

label prisonniers_discuter:
    o "Vous vous approchez des deux détenus."
    o "L'un deux fait un pas en avant :"
    g1 "Qui es-tu ?"

    menu:
        "\"Qu'est ce que ça peut te faire ?\"":
            $ aggro = True
            jump prisonniers_ignorer
        "Expliquer la situation":
            jump explications
        "Esquiver la question et proposer de s'entraider":
            jump vesqui_question

label explications:
    d "Je ne sais pas ce que je fais ici, je me suis réveillé ici mais je ne
        me souviens de rien..."
    d2 "Personne ne semble se souvenir, nous non plus ne savons pas comment nous sommes
        arrivés ici, mais de ce qu'on a appris, nous sommes dans un centre de la fondation
        SCP."
    d2 "Ils font des expériences sur nous et sur des monstres bizarres. Nous on leur sert
        simplement de cobayes."
    d1 "Certains se font torturer juste sous prétexte de la scie..."

    jump bebette

label vesqui_question:
    d "Eh vous !"
    d "Joingez-vous à moi, on arrivera pas a survivre si on ne s'entraide pas !"
    d1 "Euhh, d'accord, mais qu'est ce qu'on fait maintenant ?"
    d "Essayons de trouver un moyen de sortir."
    d2 "On devrait avancer, j'entends des pas au fond du cou..."

    jump bebette

label bebette:
    waf "grrrr..."
    o "L'alarme SCP évadé retentit."
    scene bg couloirchien
    with dissolve
    show chien at chien
    show perso at perso
    show perso2 at perso2
    show perso3 at perso3
    d2 "Oh un gros chien !"
    d "COURREZZZ !"
    o "Les portes du couloirs se ferment, surement pour tenter de contenir la bestiole
        devant vous."
    o "Vous et vos nouveaux camarades courrez pour fuire la le monstre."
    d1 "AAAAAAAARGRHGERGGHDLGFDBJBJETOPREGUERPOGIR"
    o "L'un de vos collègues vient de se faire schlasser par le gros chien"
    waf "WOOF WOOF GRGR GRRGGRR NOM NOM"
    o "Le chien arrête sa course et se concentre sur son repas fraîchement acquis."
    o "Le monstre ayant arrêté sa course, les portes se referment sur lui et le corps
        sans vie d'un des prisonniers que vous avez sauvé."

    scene bg bonbon
    with dissolve
    show perso at perso1
    show perso3 at perso2
    o "Vous prenez le temps de réaliser ce qu'il vient de vous arriver, mais ce temps est
        vite interrompu, vous vous rendez compte que vous êtes arrivé dans une salle lugubre:"
    o "La salle ressemble a une salle d'opération, quelques taches de sang anciennes sont
        encore visibles."
    o "Sur ce qui semble être la salle d'opération se trouve un bol avec une inscription :"
    o "\"Pas plus de deux.\""
    o "Vous vous penchez et vous trouvez des sortes de bonbons dans le bol."

    o "Que faites-vous ?"

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'allie_pas_patient'
    show screen countdown
    menu:
        "Prendre deux bonbons":
            hide screen countdown
            jump deux_bonbons
        "Prendre plus de deux bonbons":
            hide screen countdown
            jump gourmand

label allie_pas_patient:
    o "Votre co-détenu perd patience, il a faim."
    o "Après tout, il a raison, on ne vous nourrit pas bien, voire pas du tout ici."
    o "Il se précipite vers le bol et sors une dizaine de bonbons d'une traite."
    o "A peine sort-il sa main du bol que ses mains tombent de sont corps."
    o "Votre co-détenu saigne, il se vide de son sang. Ses cris d'agonie font
        résonner la pièce."
    o "L'homme s'écroule net au sol, puni de sa gourmandise."
    o "Vous avez bien fait de ne pas vous précipiter."

    o "La scène vous choque."
    jump folie

label deux_bonbons:
    scene bg bonbon
    with dissolve
    show perso at perso
    show perso3 at perso3

    o "Vous décidez de suivre l'indication et de ne vous servir que deux bonbons."
    o "Vous les mangez, c'est la première fois que vous mangez depuis votre réveil ici."
    o "Le goût sucré des bonbons vous apaise."

    o "Après vous avoir vu manger ces bonbons, votre co-détenu à la preuve que ceux-cis ne
        sont pas piégés, il décide donc de s'en servir a son tour."
    d2 "De toutes façon, qu'est ce qui m'empêche de m'en servir plus ?"
    d2 "miam"
    o "Votre allié prends une poignée de bonbons, et les ingurgite d'une traite."
    o "Seulement, sa gourmandise eut raison de lui. L'indication sur le bol n'était
        pas a ommetre."
    o "Les mains votre collègue se détachent de son corps, il saigne, énromement."
    o "Il n'y a rien que vous puissiez faire, il finit par se vider de son sang."

    o "La scène vous choque."
    jump folie

label gourmand:
    o "Stop bouffer là gros porc"
    jump dead_reset


label suivre_gardes2:
    scene bg_soldats
    o "Vous continuez à suivre les gardes."
    o "Après quelques minutes, ils arrivent dans une grande pièce.  Celle-ci semble être leur salle de pause."
    o "Après quelque minutes les gardes commencent a se désarmer laissant leur armes sans surveillance."
    menu:
        "Tuer les gardes discrètement":
            jump tuer_discret
        "Prendre des armes et se cacher":
            jump armes_cacher

label tuer_discret:
    o "Vous tuez les gardes."
    o "Vous entendez des pas dans le couloir."
    menu:
        "Cacher les corps puis se cacher.":
            jump cache_cache
        "Fouiller les corps.":
            jump fouiller_corps

label fouiller_corps:
    $weapon=True
    o "Vous fouillez les corps et trouvez une arme à feu ainsi qu'une carte magnétique de niveau 1."
    o "Le temps que vous fouilliez les corps, deux autres gardes sont arrivés. Que voulez-vous faire?"
    menu:
        "Les prendre en joue.":
            jump braquer
        "Arrêter de fouiller et se cacher.":
            jump stop_fouille

label stop_fouille:

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'dead_reset'
    show screen countdown

    o "Vous restez caché, pendant ce temps d'autres gardes arrivent. Vous êtes maintenant en très mauvaise posture, si vous ne faites rien ils vous auront"
    menu:
        "Les prendre en joue":
            hide screen countdown
            jump braquer

label braquer:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'rien_dire'
    show screen countdown

    o "Vous prenez les gardes en joue, eux aussi vous menacent"
    menu:
        "Abattre les deux gardes":
            "Vous tirez, vous abattez le premier garde, le deuxième vous blesse légèrement à l'épaule."
            "Il ne vous tue pas et vous regarde, il n'a pas l'air agressif."
            hide screen countdown
            jump abattre

label cache_cache:
    o "Vous cachez les corps puis vous vous cachez"
    jump stop_fouille

label armes_cacher:
    $weapon=True
    jump stop_fouille

label abattre:
    o "Vous êtes blessé, vous devez vous reposer cependant vous n’êtes pas dans un lieu sûr. "
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
    o "Un des gardes prit en joue son collègue et l’abattit sèchement."
    o "Que voulez-vous faire ?"
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
    o "Une bataille fait rage entre vous et l'agent du Chaos. Vous finissez par le mettre à terre et l'exécuter "
    jump abattre

label pourquoi:
    d "Pourquoi devrais-je vous suivre? "
    r "Je suis le seul en qui vous pouvez avoir confiance pour vous sortir de cet enfer."
    menu:
        "Accepter":
            jump double_accept

label reposer:
    o "Le temps que vous vous reposiez de nouveaux gardes sont arrivés et vous ont pourchassé,
        vous commencez à fuir cependant, ils continuent de vous suivre."
    o "Au bout de quelques minutes, ils commencent à vous rattraper, vous êtes fatigué."
    o "Vous tombez dans les pommes et à votre réveil vous êtes attaché sur une chaise dans une grande salle.
        Vous commencez à entendre des gros bruits et à apercevoir une ombre au loin. "
    o "L'ombre se rapprochant de plus en plus laissant place à une silhouette abominable. Une sorte d'énorme
        ver commence à se rapprocher et soudain vous saute dessus."
    o " C'est la fin, vous finissez dans son estomac."
    jump dead_reset

label folie:
    scene couloir2
    with dissolve

    o "Vous errez"
    o "Vous devienne fou, la scène a laquelle vous venez d'assiter était des plus atroces."
    o "Vous entendez du bruit venir de derrière vous, le big toutou est de retour."
    o "Il y a derrière vous un gros chien, et devant vous se trouve un cul de sac."
    o "A votre gauche, il y a une porte derrière laquelle vous entendez du bruit, le
        stress vous empêche de déterminer ce qu'il y a derrière la porte."
    o "A votre droite, se trouve une porte, totalement silencieuse."

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'get_bouffed'
    show screen countdown
    menu:
        "Porte de gauche":
            hide screen countdown
            jump porte_gauche
        "Porte de droite":
            hide screen countdown
            jump porte_droite

label get_bouffed:
    o "Vous aimez tant ce chien que vous finissez par lui faire un câlin d'amour."
    o "Lui aussi exprime son amour envers vous, en vous déchiquetant le bras."
    o "puis l'autre"
    o "puis une jambe"
    o "puis l'autre"

    jump dead_reset

label porte_droite:
    o "Vous entrez dans la pièce, et fermez rapidement derrière vous."
    o "La salle est totalement sombre, on n'y voit strictement rien."
    o "Un grognement se fait entendre en face de vous."
    o "La salle silencieuse n'était clairement pas vide."

    jump dead_reset

label porte_gauche:
    o "Vous entrez dans la pièce, et fermez rapidement derrière vous."
    o "La salle est quasiment vide, au milieu de la salle se trouve un écran cathodique
        avec un ordinateur. A côté de celui-ci se trouve des dossiers, vous ne savez pas
        ce qu'ils contiennent."
    o "Un programme semble être lancé sur l'écran."

    o "Que faire ?"
    menu:
        "Arrêter le programme de l'ordinateur":
            jump stop_ordi
        "Fouiller dossiers":
            jump fouiller

label fouiller:
    o "Vous prenez un dossier et commencez a feuilleter."
    o "Il s'avère que l'infrastructure dans laquelle vous vous trouvez est un centre SCP :
        un endroit on l'on enferme des créatures pour experimenter dessus."
    o "Les humains qui se trouvent dans ce bâtiment sont soit des gardes, soit des condamnés à
        mort dont la vie n'a plus de 'valeur'. La fondation se sert de ces condamnés pour
        experimenter sur les créatures."
    o "En continuant de fouiller vous vous rendez compte que "

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
    $ regarder_porte = True
    o "Vous aperçevez la scène à travers vitre de la porte :"
    o "Les gardes envoient des détenus dans une étrange cellule blindée, les portes se
        referement derrière les prisonniers."
    o "Des cris étouffés par le blindage de la cellule retentissent."
    o "Quand les portes se rouvrent, vous aperçevez une marre de sang couler de la porte,
        ainsi qu'une sorte d'entité postée devant l'entrée."

    menu:
        "Attaquer les gardes avec votre arme ?" if weapon:
            jump attaquer_arme_porte
        "Attaquer les gardes ?":
            jump attaquer_sans_arme
        "Rebrousser chemin ?":
            jump choice_couloir

label attaquer_sans_arme:
    o "Vous vous faites tirer dessus par les gardes."
    jump dead_reset

label attaquer_arme_porte:
    o "Vous rouvrez la porte et sortez votre arme."
    play sound "audio/bruit_sort_et_tire_arme.mp3"
    o "Vous butez les gardes, bien ouèj"
    jump dead_reset # TODO lier avec theo

label appuie_bouton:
    o "Vous appuyez le bouton à votre gauche."
    o "Les lumières de la zone s'éteignent, au même moment, les portes donnant sur
        la cellule s'ouvrent."

    scene bg black
    play sound "/audio/scream.mp3"
    play sound "/audio/bruit_craquote.mp3"

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
            pas d'avantage, malgré le fait que la lumière continue de clignoter."
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
            hide screen countdown
            jump activer_levier2

        "Fuir":
            hide screen countdown
            jump fuite_entite

label fixer_entite:
    o "Vous fixez le monstre dans les yeux."
    o "Vous perdez la battle de regard."
    jump dead_reset

label fuite_entite:
    o "Vous tentez de prendre la fuite."
    o "A peine vous tournez le regard que votre se fait briser, le monstre vous a eu."
    jump dead_reset

label activer_levier2:
    $ levier2 = True
    o "Tout en regardant le monstre dans les yeux, vous tirez le levier à côté de vous."
    o "C'est un levier d'urgence qui referme une porte blindée entre vous et l'entité,
        l'entité se retrouve confinée tandis que vous êtes sain et sauf."

    play sound "/audio/alert_scp_173_breach_out.mp3"
    o "L'alarme SCP évadé retentit, vous n'avez d'autre choix que de rebrousser chemin
        et rester discret pour éviter de vous faire repérer."

    o "Vous n'avez pas d'autre choix que de revenir sur vos pas."
    jump choice_couloir


scene bg panneauelectrique
with dissolve

scene bg separerapreslevier
with dissolve

scene bg aurevoircacahuette
with dissolve

scene bg cacahuettetue
with dissolve

scene bg couloirchien
with dissolve
show chien at cacahuette_pos1
show perso at cacahuette_pos1
show perso2 at cacahuette_pos1
show perso3 at cacahuette_pos1



scene bg salleordi
with dissolve
show perso at cacahuette_pos2

scene bg ordi1
with dissolve

scene bg ordi2
with dissolve


label dead_reset:
    scene bg black
    show mort at mort
    with dissolve
    ** "Vous êtes mort..."

    $ dead_once = True
    jump start

label Win_end:
    scene bg Win
    with dissolve
    oo "*Victoire*"
    return

label rien_faire:
    g2 "Bonjour, je m'appelle Robert, je suis agent secret."
    jump team_robert

label acceptation:
    d "J'accepte de vous suivre, mais vous 'avez pas intérêt de me la faire à l'envers, ou vous le regretterez."
    jump double_accept

label double_accept:
    o "Il sort de sa poche une carte de l'endroit et vous montre la sortie dont-il parle."
    o "Vous continuez votre route avec Robert. Vous arrivez dans une salle. Avant d'y entrer, Robert vous prévient
        qu'un monstre devrait se trouver dans cette salle et qu'il faudra l'affronter pour arriver à la porte menant
        à la suite.Robert ouvre la porte et commence à avancer."
    o "Que voulez-vous faire ?"
    jump start #TODO faire ca

label pitie:
    o "Les gardes vous mettent une balle entre les deux yeux."
    jump dead_reset
