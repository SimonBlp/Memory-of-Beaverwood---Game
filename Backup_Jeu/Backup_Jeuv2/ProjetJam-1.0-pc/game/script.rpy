define s = Character ("Sacha", color = "#00A6CF")
define p = Character ("Papa", color = "#D40B0B")
define m = Character ("Maman", color = "#E769E5")
define g = Character ("Grand-mère", color = "#921190")
define d = Character ("Directrice", color = "#35F2CA")

label start:

    "Je m'appelle Sacha..."
    "J'ai été séparé de mes parents à la naissance."
    "J'ai atteind la majorité, je peux enfin quitter l'orphelinat"
    "La directrice m'a donc donné rendez-vous dans son bureau"

    s "Bonjour Madame."
    d "Bonjour Sacha, comment-vas tu ?"

    $ Confirmation = False
    menu :
        d "Comment tu vas ?"
        "oui, ça va." :
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
    "Les clés étaient un peu rouillées et le papier était froisé mais l'écriture était encore assez lisible."

    s "Ah oui c'est un peu loin quand même..."
    "La maison se trouvais à Beaverwood, il y a pas mal de distance entre là-bas et où je me situais"
    "Du coup, je décide d'aller à la gare pour pouvoir prendre un bus."

    "J'étais à la fois excité mais aussi angoissé... Je vais découvrir l'histoire de ma famille mais à quel prix ? Je vais enfin découvrir mon histoire"
