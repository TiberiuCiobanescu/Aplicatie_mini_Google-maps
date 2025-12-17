# 🗺️ Mini Google Maps – Aplicație Desktop de Rutare

## 📖 Prezentare generală

**Mini Google Maps** este o aplicație desktop dezvoltată în **Python**, care permite utilizatorului să calculeze și să vizualizeze o rută rutieră optimă între două locații, folosind **date geografice reale furnizate de OpenStreetMap**.

Aplicația îmbină concepte de:
- programare orientată pe obiect  
- grafuri și algoritmi de rutare  
- interfețe grafice moderne  

Rezultatul este o aplicație funcțională, interactivă, apropiată conceptual de un sistem de navigație real.

---

## ✨ Funcționalități principale

- 📍 introducere punct de plecare și punct de sosire
- 🛣️ calcul rută optimă pe drumuri reale
- 📏 afișare distanță totală
- ⏱️ estimare timp de deplasare (mașină / pieton)
- 🗺️ afișare vizuală a rutei pe hartă
- 🔍 zoom și pan interactiv pe hartă
- ⚡ cache local pentru performanță ridicată

---

## 🧰 Tehnologii utilizate

### Limbaj și mediu
- **Python 3**
- **venv** – mediu virtual pentru izolarea dependențelor

### Interfață grafică
- **PyQt6**
- **Qt Designer**
- **QGraphicsView / QGraphicsScene** (zoom & pan)

### Procesare hartă și rutare
- **OpenStreetMap** – sursă de date geografice
- **OSMnx** – descărcare și procesare graf rutier
- **NetworkX** – algoritmi pe grafuri
- **GeoPy (Nominatim)** – geocodare
- **Matplotlib** – generare hartă și rută vizuală

---

## 🧠 Concepte teoretice aplicate

- Programare orientată pe obiect (OOP)
- Moștenire și suprascriere de metode
- Separarea logicii de interfață (arhitectură MVC-like)
- Grafuri ponderate
- Algoritmi de drum minim (shortest path)
- Geocodare (text → coordonate)
- Formula Haversine (distanță geografică)
- Cache și optimizare performanță
- Programare orientată pe evenimente

---

## 📁 Structura proiectului
```text
Aplicatie_mini-google_maps/
├── surse/
│   ├── main.py               # Pornirea aplicației și fereastra principală
│   ├── controller.py         # Coordonarea logicii aplicației
│   ├── incarcare_harta.py    # Descărcare hartă și calcul rută
│   ├── vizualizare_harta.py  # Generare și afișare hartă
│   └── ui_interfata.py       # Interfață grafică (Qt Designer)
│
├── date/
│   ├── cache/                # Hărți salvate local (.graphml)
│   └── imagini/              # Imagini generate cu ruta
│
├── venv/                     # Mediu virtual Python
└── README.md                 # Documentația proiectului
```


## ⚙️ Detalii de implementare

- Harta rutieră este descărcată o singură dată și salvată local
- La rulări ulterioare, aplicația folosește cache-ul
- Harta este modelată ca graf:
  - noduri → intersecții
  - muchii → drumuri (cu greutate = lungime)
- Ruta optimă este calculată folosind algoritmi de drum minim
- Nodurile de start și final sunt determinate manual prin formula Haversine
- Rezultatul este randat ca imagine și afișat în interfața PyQt

---

## ▶️ Instrucțiuni de rulare

### 1️⃣ Accesarea proiectului
```bash
cd Aplicatie_mini-google_maps

### 2️⃣ Activarea mediului virtual

source venv/bin/activate

### 3️⃣ Instalarea dependențelor
pip install PyQt6 osmnx networkx geopy matplotlib

### 4️⃣ Pornirea aplicației
cd surse
python3 main.py


