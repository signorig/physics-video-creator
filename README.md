# Physics Video Creator

Applicazione didattica integrata per creare video educativi su YouTube.

## 📚 Descrizione

**Physics Video Creator** è uno strumento completo per produrre video didattici su argomenti di fisica. Integra:

- 📊 **Slide Presenter** - Visualizzazione e navigazione delle slide PowerPoint
- ⚙️ **Simulatore Fisica Interattivo** - App didattica su equilibrio statico con slider
- 🎨 **Lavagna Digitale** - Disegno a mano libera per annotazioni
- 🎬 **Modalità Presentazione** - Integrazione di tutti gli elementi

## 🎯 Caso di Studio: Equilibrio Statico

L'applicazione include un simulatore completo per l'equilibrio statico di un corpo su un piano inclinato, con:

- Visualizzazione dinamica di tutte le forze (peso, normale, attrito)
- Slider interattivi per controllare:
  - Angolo del piano inclinato (0-80°)
  - Massa del corpo (1-50 kg)
  - Coefficiente di attrito statico (0-1.0)
- Analisi automatica dell'equilibrio
- Calcolo delle accelerazioni in caso di slittamento

## 🚀 Installazione

### Prerequisiti
- Python 3.8+
- pip

### Step 1: Clona il repository
```bash
git clone https://github.com/signorig/physics-video-creator.git
cd physics-video-creator
```

### Step 2: Installa le dipendenze
```bash
pip install -r requirements.txt
```

### Step 3: Avvia l'applicazione
```bash
python app_main.py
```

## 📖 Utilizzo

### 1. Menu Principale
All'avvio, vedrai 4 opzioni:

#### 📊 SLIDE PRESENTER
- Visualizza le slide della presentazione
- Naviga con i pulsanti "Slide Precedente" e "Slide Successiva"
- Le slide di esempio sono pre-caricate in `sample_slides/`

#### ⚙️ SIMULATORE FISICA
- Apre un'applicazione Matplotlib interattiva
- **Slider Angolo**: Modifica l'inclinazione del piano (0-80°)
- **Slider Massa**: Modifica la massa del corpo (1-50 kg)
- **Slider Attrito**: Modifica il coefficiente di attrito statico (0-1.0)
- Osserva come cambiano le forze in tempo reale
- L'app mostra automaticamente se il corpo è in equilibrio statico

#### 🎨 LAVAGNA DIGITALE
- Apre una finestra Pygame con una lavagna bianca
- **Mouse**: Disegna liberamente
- **Tasti 1-4**: Cambio colore (Nero, Rosso, Blu, Verde)
- **+/-**: Aumenta/Diminuisci spessore pennello
- **C**: Cancella tutto
- **Q**: Esci

#### 🎬 MODALITÀ PRESENTAZIONE
- Layout integrato con 2 pannelli
- **Sinistra**: Slide con controlli di navigazione
- **Destra**: Pulsanti per lanciare simulatore e lavagna
- **Uso consigliato**: Usa questa modalità per registrare il video

## 📹 Come Registrare un Video

### Preparazione
1. Avvia l'app: `python app_main.py`
2. Seleziona "MODALITÀ PRESENTAZIONE"
3. Apri OBS Studio (https://obsproject.com/)

### Configurazione OBS Studio
1. **Aggiungi Sorgente** → **Cattura Finestra** → Seleziona la finestra di Python
2. **Audio**: Configura il microfono per la voce narrante
3. **Layout**: Regola la risoluzione per YouTube (1920x1080 consigliato)

### Registrazione
1. Avvia la registrazione in OBS
2. Naviga tra le slide nell'app
3. Quando necessario, lancia il simulatore di fisica (appare sopra le slide)
4. Quando necessario, apri la lavagna digitale per annotazioni
5. Spiega mentre navighi
6. Interrompi la registrazione al termine

### Post-Produzione
- Elabora il video in un editor (DaVinci Resolve, Adobe Premiere, OpenShot)
- Aggiungi titoli, musica di sottofondo, effetti
- Esporta e carica su YouTube

## 📁 Struttura dei File

```
physics-video-creator/
├── app_main.py              # Applicazione principale
├── interactive_physics.py    # Simulatore di fisica
├── whiteboard.py            # Lavagna digitale
├── slides_manager.py        # Gestore slide
├── requirements.txt         # Dipendenze Python
├── sample_slides/           # Cartella slide di esempio
│   ├── slide_00.png
│   ├── slide_01.png
│   ├── slide_02.png
│   ├── slide_03.png
│   └── slide_04.png
└── README.md               # Questo file
```

## 🎓 Argomenti Trattati

### Equilibrio Statico
Le slide di esempio trattano:
1. Definizione di equilibrio statico
2. Forze su un piano inclinato (decomposizione)
3. Coefficiente di attrito (statico vs dinamico)
4. Condizione di equilibrio: μ_s ≥ tan(θ)
5. Applicazioni pratiche

### Fisica Applicata
Il simulatore mostra:
- ✓ Equilibrio mantenuto quando: `f ≥ W·sin(θ)`
- ✗ Corpo in slittamento quando: `f < W·sin(θ)`
- Accelerazione di slittamento: `a = (W·sin(θ) - f) / m`

## 🛠️ Personalizzazione

### Aggiungere Slide Personali
1. Prepara le tue slide come immagini PNG/JPG
2. Metti i file in una cartella (es: `mie_slide/`)
3. Nel codice `app_main.py`, modifica:
   ```python
   self.slides_manager.load_slides_from_folder("mie_slide/")
   ```

### Modificare i Parametri di Fisica
Modifica `interactive_physics.py`:
- `self.mass` = massa iniziale (kg)
- `self.angle` = angolo iniziale (°)
- `self.mu_s` = coefficiente attrito iniziale
- Range degli slider nelle funzioni `setup_sliders()`

### Personalizzare la Lavagna
Modifica `whiteboard.py`:
- Colori personalizzati nella sezione `self.color_*`
- Spessore pennello di default: `self.brush_size`
- Dimensioni finestra: parametri di `__init__`

## 📊 Caratteristiche Avanzate

### Analisi Automatica
Il simulatore calcola automaticamente:
- Componenti del peso (parallela e perpendicolare)
- Forza normale e attrito massimo
- Stato di equilibrio
- Accelerazione in caso di slittamento

### Visualizzazione Fisica
- Vettori di forza in scala
- Componenti decomposte (linea tratteggiata)
- Codice colore per le forze:
  - 🔴 Rosso = Peso
  - 🟢 Verde = Forza Normale
  - 🔵 Blu = Attrito
  - 🟠 Arancio = Componenti

## 🐛 Troubleshooting

### Il simulatore non si apre
- Verifica di aver installato matplotlib: `pip install matplotlib`
- Prova a lanciarlo da terminale per vedere gli errori: `python interactive_physics.py`

### La lavagna non funziona
- Controlla Pygame: `pip install pygame`
- Assicurati di avere uno schermo disponibile

### Le slide non si caricano
- Verifica che la cartella `sample_slides/` esista
- Controlla i permessi di lettura sui file PNG

## 📝 Licenza

MIT License - Libero per uso educativo e commerciale

## 👨‍🏫 Per gli Insegnanti

Questo strumento è stato creato per facilitare la didattica interattiva:

- **Coinvolgimento**: Gli studenti vedono subito la fisica in azione
- **Interattività**: Puoi cambiare i parametri durante la lezione
- **Registrazione**: Perfetto per lezioni a distanza e archivi
- **Estendibilità**: Facilmente adattabile ad altri argomenti di fisica

## 🤝 Contributi

Sei benvenuto a proporre miglioramenti! Esempi:
- Nuovi simulatori di fisica
- Temi aggiuntivi per le slide
- Miglioramenti all'interfaccia
- Traduzioni in altre lingue

---

**Creato per l'insegnamento della fisica moderna e interattiva** 🎓
