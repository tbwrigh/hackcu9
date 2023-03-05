import json

countries = ['togo', 'slovakia', 'switzerland', 'kenya', 'liberia', 'tanzania', 'georgia', 'south korea', 'mexico', 'bolivia', 'serbia', 'morocco', 'uruguay', 'kazakhstan', 'belarus', 'new zealand', 'mali', 'egypt', 'malaysia', 'senegal', 'belgium', 'spain', 'japan', 'norway', 'thailand', 'italy', 'pakistan', 'qatar', 'mauritania', 'netherlands', 'saudi arabia', 'zimbabwe', 'croatia', 'haiti', 'burkina faso', 'jordan', 'sierra leone', 'china', 'peru', 'sweden', 'afghanistan', 'guatemala', 'latvia', 'colombia', 'dominican republic', 'hungary', 'jamaica', 'congo', 'ukraine', 'bahrain', 'india', 'mozambique', 'singapore', 'mongolia', 'nicaragua', 'brazil', 'iran', 'greece', 'philippines', 'finland', 'albania', 'cameroon', 'bangladesh', 'ghana', 'czech republic', 'central african republic', 'united arab emirates', 'australia', 'ethiopia', 'bulgaria', 'bosnia and herzegovina', 'romania', 'lithuania', 'oman', 'costa rica', 'portugal', 'poland', 'ireland', 'tunisia', 'yemen', 'panama', 'cambodia', 'niger', 'slovenia', 'chad', 'canada', 'united kingdom', 'chile', 'honduras', 'france', 'austria', 'sri lanka', 'argentina', 'el salvador', 'united states', 'denmark', 'armenia', 'germany', 'indonesia', 'namibia', 'burundi', 'turkey', 'azerbaijan', 'israel']

polygons = {}

with open("shape_data/countries_min.json", "w") as o:
    with open("shape_data/countries.json") as f:
        cnt = 0
        while True:
            line = f.readline()

            if not line:
                break
            
            line = json.loads(line)

            for c in countries:
                if c.title() in line["properties"]["ADMIN"]:
                    cnt+=1
                    print(cnt)
                    polygons.update({c: line["geometry"]["coordinates"]})
    o.write(json.dumps(polygons))


