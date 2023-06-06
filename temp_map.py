import random
import os
import folium

# def random_red(feature):
#     return random.choice(['#d0312d','#990f02','#b90e0a','#5e1916','#4e0707'])
# def random_orange(feature):
#     return random.choice(['#ed7014','#fcae1e','#b56727','#fc6a03','#8d4004'])
# def random_yellow(feature):
#     return random.choice(['#e6dbac','#f9e076','#f3eaaf','#e7c37d','#fde992'])
# def random_green(feature):
#     return random.choice(['#3cb043','#b0fc38','#5dbb63','#028a0f','#234f1e'])
# def random_blue(feature):
#     return random.choice(['#3944bc','#3c5da','#0a1172','#0492c2','#241571'])

# def random_color():
#     return random.choice([random_red, random_orange, random_yellow, random_green, random_blue])

jlst = os.listdir("./data/json")
jlst = [os.path.join("./data/json",j) for j in jlst if j.lower().endswith('.json')]

m = folium.Map(location = (37.0902, -95.7129), zoom_start = 6, tiles = "OpenStreetMap")
for j in jlst:
    # color = random_color()
    folium.GeoJson(j,
                tooltip=folium.GeoJsonTooltip(fields=["ZCTA5CE10"],aliases=["ZIP code"]),
                style_function= lambda feature: {#'fillColor':color(feature), 
                                                'fillOpacity':0.9, 'weight':0}).add_to(m)
m.save("map1.html")
