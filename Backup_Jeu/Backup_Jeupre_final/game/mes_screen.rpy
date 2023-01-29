screen Instruction :
    text "Vous récupérez les clés et le papier."

screen Instruction2 :
    text "Vous récuperez le plan de la maison."

screen Instruction3 :
    text "Choisissez une pièce."

screen Instruction4 :
    text "Trouvez des objets."

screen Instruction5 :
    text "Vous vous êtes souvenu de quelque chose..."

transform custom_zoom :
    zoom 0.5

screen mini_map :
    frame :
        xalign 1.0
        at custom_zoom
        imagemap :
            ground "minimap.png"
            hotspot (30, 366, 321, 321) action Jump("map_salon")
            hotspot (360, 424, 311, 266) action Jump("map_cuisine")
            hotspot (30, 30, 324, 326) action Jump("map_chambre")
            hotspot (362, 303, 150, 110) action Jump("map_secret")

screen salon_map :
    frame :
        imagemap :
            ground "salon.png"
            hotspot (831, 474, 120, 53) action Jump("map_souvenirprim1")
            hotspot (1243, 375, 99, 123) action Jump("map_souvenirsec1")
            hotspot (1401, 273, 166, 169) action Jump("map_souvenirtri1")
screen cuisine_map :
    frame :
        imagemap :
            ground "cuisine.png"
            hotspot (441, 418, 136, 321) action Jump("map_souvenirprim2")
            hotspot (1591, 632, 326, 225) action Jump("map_souvenirsec2")
            hotspot (657, 393, 260, 65) action Jump("map_souvenirstri2")
screen chambre_map :
    frame :
        imagemap :
            ground "chambre.png"
            hotspot (1719, 533, 134, 439) action Jump("map_souvenirprim3")
            hotspot (962, 608, 169, 126) action Jump("map_souvenirsec3")
