# 🛍️ Klasifikacija proizvoda po kategorijama (Tehnomedija)

## 📌 Opis projekta
Ovaj projekat implementira API koji prima **naziv** i **opis** proizvoda i klasifikuje ga u jednu od unapred definisanih kategorija. Model je treniran na podacima sa sajta [Tehnomedija.rs](https://tehnomedija.rs), uz dodatnu obradu i balansiranje klasa.

---

## 🎯 Ciljevi i realizacija

### 1. Prikupljanje i priprema podataka

- **Skrejpovanje**: Korišćen je Scrapy za automatsko prikupljanje proizvoda i njihovih opisa.
- **Čišćenje podataka**:
  - Uklanjanje šifara, HTML tagova i specijalnih karaktera.
  - Normalizacija teksta (lowercasing, uklanjanje stop-reči).
- **Balansiranje klasa**:
  - Proširenje podataka za retke kategorije korišćenjem generisanih primera uz pomoć LLM-a.
- **Konačni skup podataka**:
  - ✅ 18,223 trening primera
  - ✅ 4,494 test primera

---

### 2. Izbor i treniranje modela

- **Modeli testirani**:
  - TF-IDF + Logistička regresija
  - BERT (eksperimentalno za složenije opise)
- **Rezultati**:
  - TF-IDF + LR postigao **F1-score: 98%**
  - Visoka preciznost i odziv po svim klasama
- **Preprocesing**:
  - Tokenizacija, čišćenje šuma, lowercasing

---

### 3. API implementacija (FastAPI)

- **Ulaz**:
  ```json
  {
    "naziv": "Samsung televizor 55\"",
    "opis": "Smart 4K LED TV sa HDR podrškom"
  }
Izlaz:

json
Always show details

Copy
[
  ["Televizori", 0.97],
  ["Audio-video", 0.02],
  ["Bela tehnika", 0.01]
]
Testiranje:

Pokriven širok spektar kombinacija naziva i opisa

Brz i stabilan odgovor (< 100ms na prosečan zahtev)

### 4. Monitoring
Praćenje performansi modela u produkciji

Logovanje zahteva i odgovora radi analize i debagovanja

### 5. Dokumentacija
✅ Komentari u kodu

✅ .readme.md sa detaljnim uputstvom

✅ Test primeri uključeni

✅ Zaključak
Projekat je uspešno realizovan sa sledećim rezultatima:

=================================================================================================================================

##### 🎯 Visoka tačnost klasifikacije (F1-score 98%)

##### ⚡ Brz i funkcionalan API preko FastAPI-ja

##### 🧼 Dobro strukturirani i očišćeni podaci

#### 🔧 Moguća poboljšanja

Prikupljanje podataka sa dodatnih e-commerce sajtova

Fine-tuning BERT modela za složenije klasifikacije

Dodavanje autentifikacije i skalabilnosti API endpointa

#### 📝 Zapažanja
Neki sajtovi imaju zaštitu protiv skrejpovanja (npr. Tehnomanija)

Model koristi naziv proizvoda, što često sadrži naziv kategorije → visoka tačnost

FastAPI je jednostavan za osnovne primene, ali zahteva dodatnu praksu za skaliranje



