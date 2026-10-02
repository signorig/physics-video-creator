"""
GUIDA RAPIDA PER INIZIARE
Physics Video Creator - Setup e primo utilizzo
"""

GUIA_RAPIDA = """
╔═══════════════════════════════════════════════════════════════╗
║          PHYSICS VIDEO CREATOR - GUIDA RAPIDA                ║
║                 Equilibrio Statico                            ║
╚═══════════════════════════════════════════════════════════════╝

📋 PREREQUISITI
───────────────────────────────────────────────────────────────
✓ Python 3.8+
✓ pip package manager
✓ ~200MB di spazio libero

🚀 INSTALLAZIONE (2 minuti)
───────────────────────────────────────────────────────────────

1. Scarica il progetto:
   git clone https://github.com/signorig/physics-video-creator.git
   cd physics-video-creator

2. Installa le dipendenze:
   pip install -r requirements.txt

3. Avvia l'applicazione:
   python app_main.py

⚡ USO RAPIDO
───────────────────────────────────────────────────────────────

Opzione 1: SLIDE PRESENTER
├─ Visualizza le 5 slide di esempio
├─ Naviga con i pulsanti
└─ Tempo: 2 minuti

Opzione 2: SIMULATORE FISICA
├─ Apre Matplotlib con slider interattivi
├─ Modifica angolo, massa, attrito
├─ Osserva le forze cambiare
└─ Tempo: 5 minuti

Opzione 3: LAVAGNA DIGITALE
├─ Disegna con il mouse
├─ Cambia colore (tasti 1-4)
├─ Cancella tutto (tasto C)
└─ Tempo: illimitato

Opzione 4: MODALITÀ PRESENTAZIONE (CONSIGLIATA)
├─ Integra slide + simulatore + lavagna
├─ Usa per registrare video
└─ Tempo: variabile

🎬 COME REGISTRARE UN VIDEO
───────────────────────────────────────────────────────────────

Step 1: Installa OBS Studio (gratuito)
        https://obsproject.com/

Step 2: Avvia Python
        python app_main.py

Step 3: Seleziona "MODALITÀ PRESENTAZIONE"

Step 4: In OBS Studio:
        - Aggiungi sorgente → Cattura Finestra
        - Seleziona la finestra di Python
        - Configura microfono per voce narrante

Step 5: Premi "Avvia Registrazione"

Step 6: Usa l'app:
        - Naviga slide (pulsanti ◀ ▶)
        - Lancia simulatore (pulsante 🚀)
        - Apri lavagna (pulsante 🎨)
        - Parla e spiega

Step 7: Al termine premi "Ferma Registrazione"

Step 8: Elabora il video (montaggio, titoli, effetti)

Step 9: Carica su YouTube

⏱️ TEMPO TOTALE PER UN VIDEO
───────────────────────────────────────────────────────────────
- Registrazione: 15-30 minuti (a seconda della lunghezza)
- Montaggio: 30-60 minuti (titoli, transizioni, effetti)
- Upload: 10-20 minuti (dipende dalla connessione)

TOTALE: 1-2 ore per un video completo

📚 CONTENUTO INCLUSO
───────────────────────────────────────────────────────────────

5 SLIDE PRE-CARICATE:
1. Equilibrio Statico - Definizione e concetti
2. Forze su Piano Inclinato - Decomposizione vettoriale
3. Coefficiente di Attrito - Statico vs Dinamico
4. Condizione di Equilibrio - Matematica
5. Applicazioni Pratiche - Esempi reali

SIMULATORE FISICA:
✓ Visualizzazione di tutte le forze
✓ Slider per angolo (0-80°)
✓ Slider per massa (1-50 kg)
✓ Slider per attrito (0-1.0)
✓ Analisi automatica dell'equilibrio
✓ Calcolo accelerazioni

🎨 PERSONALIZZAZIONE
───────────────────────────────────────────────────────────────

Aggiungere slide personali:
- Prepara immagini PNG/JPG
- Metti in cartella (es: mie_slide/)
- Modifica in app_main.py:
  self.slides_manager.load_slides_from_folder("mie_slide/")

Modificare parametri di fisica:
- Modifica interactive_physics.py
- Cambia valori iniziali di mass, angle, mu_s
- Regola range dei slider

Personalizzare lavagna:
- Modifica whiteboard.py
- Cambia colori nella sezione self.color_*
- Regola dimensioni finestra

🔧 COMANDI CHIAVE
───────────────────────────────────────────────────────────────

SIMULATORE FISICA:
- Slider: Modifica i parametri
- Grafico: Mostra tutte le forze

LAVAGNA DIGITALE:
- Mouse: Disegna
- Tasti 1-4: Colore (Nero, Rosso, Blu, Verde)
- +/-: Spessore pennello
- C: Cancella tutto
- Q: Esci

❓ DOMANDE COMUNI
───────────────────────────────────────────────────────────────

D: Dove metto le mie slide?
R: Crea una cartella (es: mie_slide/) con PNG/JPG
   Poi modifica app_main.py nella sezione slides_manager

D: Posso cambiare i colori della lavagna?
R: Sì! Modifica whiteboard.py nelle linee dei colori

D: Il video non è sincronizzato con l'audio
R: In OBS Studio configura i ritardi audio/video corretti

D: Come faccio sottotitoli al video?
R: Usa YouTube Studio o editor video (DaVinci Resolve, etc)

D: Posso salvare la lavagna?
R: Il codice attuale non salva, ma puoi catturare con OBS
   Per salvare, modifica whiteboard.py per screenshot

📞 SUPPORTO
───────────────────────────────────────────────────────────────

Problemi?
1. Leggi il file TROUBLESHOOTING.py
2. Controlla che Python sia 3.8+
3. Reinstalla dipendenze: pip install --upgrade -r requirements.txt
4. Verifica i permessi di file/cartelle

🎓 CASI D'USO
───────────────────────────────────────────────────────────────

✓ Lezioni per studenti di liceo scientifico
✓ Video educativi per YouTube
✓ Lezioni online sincrone
✓ Registrazioni per archivi didattici
✓ Supporto a insegnanti di fisica
✓ Studi di equilibrio statico

🎬 ESEMPI DI VIDEO DA FARE
───────────────────────────────────────────────────────────────

Scenario 1 - Lezione Teorica (15 min)
- Slide 1: Concetti e definizioni
- Simulatore: Mostra equilibrio statico
- Slide 2-3: Analisi matematica
- Lavagna: Disegna diagrammi di forze
- Slide 4-5: Applicazioni pratiche

Scenario 2 - Demo Interattiva (10 min)
- Simulatore aperto dall'inizio
- Modifica i parametri in tempo reale
- Parla dei risultati
- Usa la lavagna per annotazioni

Scenario 3 - Esercizio Risolto (20 min)
- Slide con problema
- Lavagna: Risolvi passo dopo passo
- Simulatore: Verifica la soluzione
- Slide finale: Risposta e conclusioni

═══════════════════════════════════════════════════════════════

Buona didattica! 🎓
Crea video meravigliosi! 🎬

"""

if __name__ == "__main__":
    print(GUIDA_RAPIDA)
