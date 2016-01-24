#!/usr/bin/env python
# -*- coding: utf-8 -*-

gemeinden_tirol = ["Erl",
"Walchsee",
"Kössen",
"Rettenschöss",
"Niederndorferberg",
"Niederndorf",
"Schwendt",
"Ebbs",
"Waidring",
"Thiersee",
"Kirchdorf in Tirol",
"Jungholz",
"Kufstein",
"Brandenberg",
"Achenkirch",
"Vils",
"Schattwald",
"Langkampfen",
"Pinswang",
"Scheffau am Wilden Kaiser",
"Eben am Achensee",
"Musau",
"Zöblen",
"Tannheim",
"Grän",
"Steinberg am Rofan",
"Ellmau",
"St. Ulrich am Pillersee",
"Schwoich",
"Pflach",
"Going am Wilden Kaiser",
"Reutte",
"St. Johann in Tirol",
"Söll",
"Angerberg",
"Mariastein",
"Kirchbichl",
"Breitenbach am Inn",
"Lechaschau",
"Nesselwängle",
"Wängle",
"Vomp",
"Bad Häring",
"Wängle",
"Angath",
"Breitenwang",
"Oberndorf in Tirol",
"St. Jakob in Haus",
"Fieberbrunn",
"Weißenbach am Lech",
"Höfen",
"Lermoos",
"Hochfilzen",
"Ehenbichl",
"Reith bei Kitzbühel",
"Wörgl",
"Heiterwang",
"Itter",
"Kramsach",
"Kundl",
"Ehrwald",
"Brixen im Thale",
"Kitzbühel",
"Wildschönau",
"Münster",
"Kirchberg in Tirol",
"Hopfgarten im Brixental",
"Radfeld",
"Bichlbach",
"Westendorf",
"Scharnitz",
"Forchach",
"Berwang",
"Leutasch",
"Rattenberg",
"Aurach bei Kitzbühel",
"Brixlegg",
"Wiesing",
"Reith im Alpbachtal",
"Vorderhornbach",
"Stanzach",
"Jenbach",
"Biberwier",
"Alpbach",
"Namlos",
"Hinterhornbach",
"Wildermieming",
"Mieming",
"Strass im Zillertal",
"Nassereith",
"Stans",
"Bruck am Ziller",
"Jochberg",
"Elmen",
"Schlitters",
"Buch bei Jenbach",
"Tarrenz",
"Hart im Zillertal",
"Seefeld in Tirol",
"Gallzein",
"Absam",
"Schwaz",
"Fügen",
"Häselgehr",
"Obsteig",
"Telfs",
"Zirl",
"Innsbruck",
"Fügenberg",
"Imst",
"Gnadenwald",
"Pfafflar",
"Elbigenalp",
"Thaur",
"Terfens",
"Holzgau",
"Reith bei Seefeld",
"Stummerberg",
"Pill",
"Uderns",
"Rum",
"Fritzens",
"Weer",
"Oberhofen im Inntal",
"Pettnau",
"Gramais",
"Weerberg",
"Bach",
"Steeg",
"Stumm",
"Baumkirchen",
"Mils",
"Pfaffenhofen",
"Kolsass",
"Ried im Zillertal",
"Mötz",
"Flaurling",
"Rietz",
"Wattens",
"Stams",
"Volders",
"Kolsassberg",
"Polling in Tirol",
"Kaltenbach",
"Silz",
"Hall in Tirol",
"Inzing",
"Haiming",
"Wattenberg",
"Tulfes",
"Ampass",
"Aschau im Zillertal",
"Gerlos",
"Unterperfuss",
"Kematen in Tirol",
"Karrösten",
"Ranggen",
"Schönwies",
"Völs",
"Rinn",
"Zams",
"Kaisers",
"Aldrans",
"Oberperfuss",
"Karres",
"Roppen",
"Zellberg",
"Rohrberg",
"Axams",
"Götzens",
"Lans",
"Mils bei Imst",
"Birgitz",
"Natters",
"Grinzens",
"Hippach",
"Gerlosberg",
"Sistrans",
"Oetz",
"Sautens",
"Mutters",
"Zell am Ziller",
"Sellrain",
"Arzl im Pitztal",
"St. Sigmund im Sellrain",
"Imsterberg",
"Gries im Sellrain",
"Patsch",
"Hainzenberg",
"Schönberg im Stubaital",
"Flirsch",
"Ellbögen",
"Pettneu am Arlberg",
"Ramsau im Zillertal",
"Telfes im Stubai",
"Tux",
"Wenns",
"Umhausen",
"Schwendau",
"Grins",
"Stanz bei Landeck",
"St. Anton am Arlberg",
"Strengen",
"Jerzens",
"Mayrhofen",
"Mieders",
"Mühlbachl",
"Brandberg",
"Pfons",
"Landeck",
"Navis",
"Finkenberg",
"Fließ",
"Fulpmes",
"Pians",
"Tobadill",
"Neustift im Stubaital",
"Matrei in Osttirol",
"St. Leonhard im Pitztal",
"Kappl",
"Schmirn",
"Matrei am Brenner",
"Längenfeld",
"Kaunerberg",
"Faggen",
"Ladis",
"Prutz",
"Fiss",
"Steinach am Brenner",
"Kals am Großglockner",
"See",
"Trins",
"Kauns",
"Prägraten",
"Kaunertal",
"Ried im Oberinntal",
"Serfaus",
"Fendels",
"Ischgl",
"Gries am Brenner",
"Gschnitz",
"Vals",
"Tösens",
"Obernberg am Brenner",
"Virgen",
"Pfunds",
"Spiss",
"Sölden",
"Galtür",
"St. Jakob in Defereggen",
"Nauders",
"Nußdorf-Debant",
"St. Veit in Defereggen",
"Hopfgarten in Defereggen",
"St. Johann im Walde",
"Ainet",
"Dölsach",
"Iselsberg-Stronach",
"Schlaiten",
"Thurn",
"Außervillgraten",
"Innervillgraten",
"Oberlienz",
"Gaimberg",
"Anras",
"Assling",
"Lienz",
"Tristach",
"Nikolsdorf",
"Amlach",
"Leisach",
"Lavant",
"Abfaltersbach",
"Strassen",
"Sillian",
"Heinfels",
"Obertilliach",
"Kartitsch",
"Untertilliach"]
