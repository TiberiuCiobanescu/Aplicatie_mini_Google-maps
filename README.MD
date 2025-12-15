Mini Google Maps

###DESCRIERE
Acest proiect reprezinta o versiune simplificata a functionalitatilor de baza ale aplicatiei Google Maps. Utilizatorul poate introduce o locatie de plecare si o locatie de destinatie, iar aplicatia calculeaza si afiseaza ruta optima dintre cele doua puncte pe o harta interactiva.

###FUNCTIONALITATE
Aplicatia calculeaza automat ruta folosind date OpenStreetMap si afiseaza traseul pe harta. Dupa finalizarea calculului, sunt prezentate informatii despre distanta totala dintre puncte, timpul estimat de parcurs cu masina si timpul estimat pentru mersul pe jos. Valorile sunt obtinute pe baza lungimii reale a drumurilor si a unor viteze medii prestabilite.

###INTERFATA GRAFICA
Interfata grafica este realizata cu ajutorul bibliotecii PyQt6. Harta este afisata intr-o zona dedicata a aplicatiei si poate fi explorata prin zoom. In timpul calculului rutei, aplicatia afiseaza mesajul "Calculam ruta...", pentru a informa utilizatorul ca procesul este in desfasurare.

###IMPLEMENTARE
Harta este descarcata o singura data si salvata local, ceea ce permite rulari mai rapide ale aplicatiei ulterior.

###TEHNOLOGII UTILIZATE
Aplicatia este dezvoltata in Python 3.12 si utilizeaza biblioteci precum PyQt6 pentru interfata grafica, OSMnx si NetworkX pentru procesarea hartilor si calculul rutelor, Matplotlib pentru generarea imaginilor hartii si Geopy pentru conversia adreselor in coordonate geografice.

###RULARE
Pentru rularea aplicatiei este necesara instalarea pachetelor specificate in fisierul requirements.txt. Aplicatia se porneste prin rularea fisierului principal, iar la prima utilizare este necesara o conexiune la internet pentru descarcarea hartii.
