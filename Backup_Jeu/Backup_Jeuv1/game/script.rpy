define s = Character ("Sacha", color = "#00A6CF")
define p = Character ("Papa", color = "#D40B0B")
define m = Character ("Maman", color = "#E769E5")
define g = Character ("Grand-mère", color = "#921190")
define a = Character ("Amélie", color = "#35F2CA")

label start:

    "Je m'appelle Sacha..."
    "J'ai été séparé de mes parents à la naissance."
    "Aujourd'hui j'ai pu sortir de l'orphelinat"

    '"dring dring"'

    s "Allo?"
    a "Coucou sacha"
    "Amélia est ma meilleure amie, elle m'a toujours rendu le sourrire malgré les moments les plus difficiles"

    $ Confirmation = False

    menu :
        a "comment tu vas ?"
        "oui, ça va." :
            $ Confirmation = True
            a "Contente de l'apprendre."
        "Bof, pas vraiment..." :
            a "Roh tu pourrais être un peu plus souriant quand même..."
            s "mouais..."

label decouverte:

    a "Bref je t'appelle pour quelque chose de très important !"
    s "Ah bon ? Qu'est ce que tu vas encore me chanter ?"
    a "eh ! Fais gaffe à ce que tu dis !"
    s "ça va je rigole HaHa !"
    a "Bon j'ai retrouvé la maison où habitais tes parents biologiques."

    "À ce moment là je ne savais pas comment je devais réagir... Mon coeur commençais à battre la chamade, je tremblais, j'avais un mélange de joie mais aussi de colère..."

    a "J'ai été à la commune ce matin, et ils avaient même les clés de la maison ainsi que l'adresse."
    s "Tu les as sur toi ?!"
    a "Oui, viens vite les chercher !"

    "j'ai raccroché tout de suite et je me suis empressé d'aller chez amélia pour les récupérer"
    'Une fois les clés récupérées, je suis parti à toute vitesse à la maison de "ma famile"'
