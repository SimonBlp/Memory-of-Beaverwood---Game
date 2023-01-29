define s = Character ("Sacha", color = "#00A6CF")
define p = Character ("James Marks (Papa)", color = "#D40B0B")
define m = Character ("Amy Marks (Maman)", color = "#E769E5")
define g = Character ("Lila Marks (Grand-mère)", color = "#921190")
define d = Character ("Directrice", color = "#35F2CA")

label start:

    $ inventory = []

    "Je m'appelle Sacha..."
    "J'ai été séparé de mes parents à la naissance."
    "J'ai atteind la majorité, je peux enfin quitter l'orphelinat"
    "La directrice m'a donc donné rendez-vous dans son bureau"

    s "Bonjour Madame."
    d "Bonjour Sacha, comment-vas tu ?"

    $ confirmation = False
    $ confirm1 = False
    $ confirm2 = False
    $ confirm3 = False
    menu :
        d "Comment tu vas ?"
        "Oui, ça va." :
            $ Confirmation = True
            s "Je vais bien merci."
            d "Contente de l'apprendre."
        "Bof, pas vraiment..." :
            d "Tu pourrais être plus enthousiaste !"
            s "Mouais..."

label decouverte:

    d "Allez ! C'est le grand jour aujourd'hui !"
    s "Et oui l'indépendance..."
    "Elle me tent un stylo et des papiers à signer. Pendant que je signe, elle fouille dans ses tiroirs et récupère des clés ainsi qu'un bout de papier."
    s "Voici."
    "Je lui redonnes les papiers."
    d "Merci, tout est en règles. Mais avant que tu nous quitte, je te remets ces deux objets."
    "Elle me tends les clés en premier"
    d "Ils ont été laissés par ta famille quand tu as été déposé à l'ophelinat. Malheureusement, je n'ai pas d'autres informations... À toi de découvrir."
    show screen Instruction
    s "Merci."
    hide screen Instruction
    d "Tu peux à présent y aller. Bonne continuation Sacha, nous serons ravis d'avoir de tes nouvelles..."
    "Tsss, tu parles, plus jamais je remets un pied ici et encore moins vous donnez de nouvelles..."
    "Je me lève de ma chaise et me dirige vers la sortie, je dis un dernier aurevoir sans rien ajouter."

    "Après être sortie je pris le bout de papier et les clés"
    show clemaison
    with dissolve
    "Les clés étaient un peu rouillées et le papier était froisé mais l'écriture était encore assez lisible."
    hide clemaison
    s "Ah oui c'est un peu loin quand même..."
    "La maison se trouvais à Beaverwood, il y a pas mal de distance entre là-bas et où je me situais"
    "Du coup, je décide d'aller à la gare pour pouvoir prendre un bus."
    "J'étais à la fois excité mais aussi angoissé... Je vais découvrir l'histoire de ma famille mais à quel prix ? Je vais enfin découvrir mon histoire"

label outside:

    scene entrer
    with dissolve

    "Une fois arrivé, j'ai remarqué que la maison à bien vieilli. Les herbes sont hautes, il y avait de la mousse sur les planches,..."
    "La porte étaient fermés à clé. Même si elle semblait vieille, elle n'avait pas l'air de pouvoir s'éffondrer"
    "Je pris les clés de ma poche, dévérouille la porte et j'entre sans plus attendre dans la maison"

    scene black
    with dissolve

    "Et puis... Wow..."

    scene salon

    "La maison de l'intérieur est complètement différente qu'à l'extérieur ! On dirait que les habitants étaient parties du jour au lendemain."
    "Les meubles tout droits sortie des années 80..."
    "Par contre, je sentais toujours la moisissures et je voyais pas mal de poussières, ce qui montrent que la maison est quand même bien à l'abandon."

    "Par terre, j'aperçois une feuille qui ressemble au plan de la maison."
    show screen Instruction2
    s"J'espère que ça sera utile..."
    hide screen Instruction2

label gameplay:
    show screen Instruction3
    show screen mini_map
    s "Où je vais aller ?"
    call screen mini_map

label map_salon :
    hide screen Instruction3
    hide screen mini_map
    scene salon
    with dissolve
    s "Quel beau salon il y a tellement de beaux meubles..."
    jump gameplay_salon
label gameplay_salon :
    if confirm1 == True :
        hide screen Instruction3
        hide screen salon_map
        scene salon
        $ inventory.append("livre")
        show screen Instruction5
        hide screen Instruction5
        jump gameplay
    else:
        hide screen Instruction3
        show screen salon_map
        show screen Instruction4
        s "Qu'est ce que je peux trouver dans ce salon ?"
        call screen salon_map

label map_souvenirprim1 :
    hide screen Instruction3
    hide screen Instruction4
    hide screen salon_map

    scene black
    with dissolve
    scene livre
    show gh
    with dissolve

    g "Le tout petit barde, c'est mon livre préféré. Je l'ai lu tellement de fois que je le connais par coeur."
    g "J'aime tellements lire que je ne sais plus où ranger mes livres, ma bibliothèque déborde !"

    hide gh
    with dissolve
    scene black
    with dissolve

    scene salon
    with dissolve
    show screen Instruction5
    s "Ce livre... Il me dit quelque chose... Ha oui! Je me souviens l'avoir lu à la bibliothèque de l'école, elle a raison, ce livre était trop cool!"
    hide screen Instruction5

    $ confirm1 = True
    jump gameplay_salon

label map_souvenirsec1 :

    hide screen Instruction3
    hide screen Instruction4
    hide screen salon_map
    scene tableau
    with dissolve

    '"Photo de pêche. 23ème champion national de pêche : James Marks."'
    s "Un tournoi de pêche... avec le nombre de lacs que compte le Canada ça ne m'étonne même pas."
    s "Je vais sûrement en apprendre plus sur James plus tard..."

    scene salon
    with dissolve
    jump gameplay_salon

label map_souvenirtri1:

    hide screen Instruction3
    hide screen Instruction4
    hide screen salon_map
    scene lotterie
    with dissolve

    '"Lila, habitante de Beaverwood gagne le gros lot"'
    s "En plus ils avaient de la thune ?! Mais pourquoi cette cabane est restée à l'abandon? Hmm... Bizarre tout ça..."

    scene salon
    jump gameplay_salon

label map_cuisine :
    hide screen Interaction3
    hide screen mini_map
    scene cuisine
    with dissolve
    s "La cuisine à l'air vraiment bien rangé..."
    jump gameplay_cuisine
label gameplay_cuisine :

    if confirm2 == True :
        show screen cuisine_map
        hide screen Instruction3
        hide screen cuisine_map
        $ inventory.append("rouleau")
        jump gameplay
    else:
        hide screen Instruction3
        show screen cuisine_map
        show screen Instruction4
        s "Qu'est ce que je peux trouver dans cette cuisine ?"
        call screen cuisine_map

label map_souvenirprim2 :
    hide screen Instruction3
    hide screen Instruction4
    hide screen cuisine_map

    scene black
    with dissolve
    scene facture
    with dissolve

    show pa
    with dissolve
    p "Comment ça tu es encore allé au Casino maman ??"
    hide pa
    with dissolve
    show ga
    with dissolve
    g "Écoute James, c'est mon argent j'en fais ce que je veux. Je vous ai donné une part à vous deux, j'aurais pu m'abstenir."
    hide ga
    with dissolve
    show pe
    with dissolve
    p "Maman ! Tu te rend compte qu'on risque de perdre la maison à Ottawa avec toutes ces conneries ?!"
    hide pe
    with dissolve
    show ms
    with dissolve
    m "Calme toi James... ça ne sert à rien de s'énerver comme ça."
    hide ms
    with dissolve
    show pe
    with dissolve
    p "Tu ne te rends pas compte Amy, ce n'est pas la première fois qu'elle fait ça."
    hide pe
    with dissolve
    '"CLACK"'
    show ma
    with dissolve
    m "Vous devriez faire attention Belle-maman, je n'ai aucune envie de que nous nous retrouvions à la rue vous, James et Moi..."
    hide ma
    with dissolve
    show gn
    with dissolve
    g"..."
    hide gn
    with dissolve

    scene black
    with dissolve

    scene cuisine
    with dissolve

    show screen Instruction5
    s"..."
    s"Des factures, des factures et encore des factures. Elles sont quasiment toutes impayés"
    s "Riches mais endettés... décidément."
    hide screen Instruction5

    $ confirm2 = True
    jump gameplay_cuisine
label map_souvenirsec2 :
    hide screen Instruction3
    hide screen Instruction4
    hide screen cuisine_map

    scene black
    with dissolve
    scene rouleau

    show pn
    with dissolve

    p "Cette cuisine c'est toute mon enfance, je me souviens quand ma grand-mère faisait sa tarte aux bleuets."
    p "Malgré qu'elle m'ait donné sa recette je n'arrive pas à la reproduire..."
    p "Heureusement que j'ai d'autres spécialités comme la tarte aux pacanes, Amy l'adore et moi aussi."
    p "J'aime la pâtisseries mais aussi la cuisine ! Je pêche souvent dans la région des beaux poissons que l'on aime déguster grillés quand l'on invite les voisins."

    hide pn
    with dissolve
    scene black
    with dissolve
    scene cuisine
    with dissolve

    s "C'est donc lui sur la photo du salon. Un vrai papa gâteau !"
    s "J'aurais aimé déguster cette fameuse tartes aux pacanes..."
    s "Je crois bien qu'il n'avait pas envie que j'y goûte"

    jump gameplay_cuisine
label map_souvenirstri2 :
    hide screen Instruction3
    hide screen Instruction4
    hide screen cuisine_map

    scene black
    with dissolve
    scene the
    with dissolve

    show me
    with dissolve
    m "Je ne me sens pas dans mon assiette ces temps-ci, je ne sais pas ce que j'ai..."
    m "Depuis que ma belle mère a touché le gros lot, je donne cours de violon une fois par seamine, je peux donc plus souffler, ni me reposer..."
    hide me
    show mn
    m "Boire du thé me permet de me sentir plus apaisée"
    hide mn
    with dissolve

    scene black
    with dissolve
    scene cuisine
    with dissolve

    s "Un bon petit thé camomille saveur poussière, pas sûr que tu l’apprécie encore."

    jump gameplay_cuisine

label map_chambre :
    hide screen mini_map
    scene chambre
    with dissolve
    s"Le lit à l'air si confortable"
    jump gameplay_chambre
label gameplay_chambre :

    if confirm3 == True :
        hide screen Instruction3
        hide screen chambre_map
        $ inventory.append("violon")
        show screen Instruction5
        hide screen Instruction5
        jump gameplay
    else:
        hide screen Instruction3
        show screen chambre_map
        show screen Instruction4
        s "Qu'est ce que je peux trouver dans cette chambre ?"
        call screen chambre_map

label map_souvenirprim3 :
    hide screen Instruction3
    hide screen Instruction4
    hide screen chambre_map

    scene black
    with dissolve
    scene violon
    with dissolve

    show me
    with dissolve
    m "Je viens de rentrer de mon cours de violon, je suis épuisée. Mon nouvel élève a beaucoup de difficultés mais c'est normal, ce n'est que sa 3ème leçon en même temps"
    hide me
    show mn
    m "J'ai bien fait de changer de travail, vivre de sa passion c'est tellement mieux."
    m "Dans deux semaines, je participes au concert du championnat local de pêche"
    hide mn
    show ms
    m "faut que je m'entraîne sinon le stress va m'envahir et je vais tout faire foirer..."
    hide ms
    with dissolve

    scene black
    with dissolve
    scene chambre
    with dissolve

    show screen Instruction5
    s "Serait-ce donc ma mère ? Elle a le même nom que la grand-mère qui a gagner à la loterie. Une passionnée de musique..."
    s "À l'orphelinat, il y avait un piano dans la salle commune, j'aimais bien en jouer."
    s "J'étais pas un pro mais je me débrouillais plutôt bien. Si seulement j'avais pu prendre des cours à l'académie de musique..."
    hide screen Instruction5

    $ confirm3 = True
    jump gameplay_chambre
label map_souvenirsec3 :
    hide screen Instruction3
    hide screen Instruction4
    hide screen chambre_map

    scene maquillage
    with dissolve
    '"Une vielle boîte avec des vieux produits mais qui coûtent chers"'
    s "Elle devait être très belle vu le nombres de produits qu'elle avait"

    scene chambre
    with dissolve
    jump gameplay_chambre

label map_secret :
    hide screen mini_map
    hide screen Interaction3
    scene portesecret
    with dissolve
    jump confirmend

label confirmend :
        $ i = 3
        if i > len(inventory):
            s "La porte est bien fermé, il me faudrait une clé pour l'ouvrir..."
            jump gameplay
        else :
            jump end
label end :
    hide screen Instruction3
    scene saloncle
    s "?"
    "Un objet scintilliait devant mes yeux dans le coin du salon"
    "C'était une clé en or, et elle correspondait parfaitement à la serrure de la grande porte"
    scene black
    with  dissolve
    scene portesecret
    with dissolve
    "Je m'y précipitai alors vers la porte mais je me repris de suite"
    "Je commençais à trembler et mon coeur se resert..."
    scene black
    with dissolve
    s "Allez un peu de courage tu y es presque !"
    "J'ouvre délicatement la porte..."
    "Et là...."
    scene secret
    with dissolve
    "Je finis sur une toute petite buandrie assez poussiéreuse"
    "Je commençais à être très déçu jusqu'à ce que je vis deux lettre à l'intérieur d'une sorte de mini coffre fort."
    "je commençais à la lire la première..."

    scene black
    with dissolve

    show letter1
    ''

    hide letter1
    with dissolve
    scene black

    "Á ce moment là, je ne voulais plus la lire... Mais d'un côté, si je ne continue pas, je n'aurais plus d'autres réponses à mes questions..."
    $ confirmation = False
    menu :
        s "Que dois-je faire ?"
        "Arrêter de lire et s'enfuir":
            $ confirmation = True
            scene secret
            with dissolve
            "Pour finir, je ne voulais pas savoir la suite, je n'étais plus intéresser..."
            "J'ai déchiré la lettre et je suis partie sans même me retourner."
            scene black
            with dissolve
            scene end
            ""
            scene black
            with dissolve
            scene credit
            with dissolve
            ""

            scene black
            with dissolve
            return
        "Continuer à lire et apprendre la vérité":
            s "autant connaître la suite..."
            scene black
            with dissolve

            show letter2
            ''

            hide letter2
            with dissolve
            scene black
            "Une fois la lettre lu, je l'ai redéposer la où je l'ai trouvé et..."
            '"grincement de porte"'
            s "y... y a quelqu'un ?"
            scene black
            with dissolve
            scene end
            ""
            scene black
            with dissolve
            scene credit
            with dissolve
            ""

            scene black
            with dissolve
            return
