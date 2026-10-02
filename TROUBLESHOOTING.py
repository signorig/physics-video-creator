"""
TROUBLESHOOTING E FAQ
Physics Video Creator
"""

TROUBLESHOOTING = """
╔═══════════════════════════════════════════════════════════════╗
║              TROUBLESHOOTING E FAQ                            ║
╚═══════════════════════════════════════════════════════════════╝

🔴 ERRORE: "ModuleNotFoundError: No module named 'matplotlib'"
────────────────────────────────────────────────────────────────
SOLUZIONE:
1. Installa matplotlib:
   pip install matplotlib

2. Se persiste, reinstalla tutto:
   pip install --upgrade -r requirements.txt

3. Verifica l'installazione:
   python -c "import matplotlib; print(matplotlib.__version__)"


🔴 ERRORE: "ModuleNotFoundError: No module named 'pygame'"
────────────────────────────────────────────────────────────────
SOLUZIONE:
1. Installa pygame:
   pip install pygame

2. Se su Linux, potrebbe servire:
   pip install pygame --upgrade


🔴 ERRORE: "No display name and no $DISPLAY environment variable"
────────────────────────────────────────────────────────────────
CAUSA: Stai usando Linux senza ambiente grafico (server)
SOLUZIONE:
1. Se possibile, usa una GUI
2. Per server remoti, usa X11 forwarding:
   ssh -X utente@server
   python app_main.py


🔴 ERRORE: "No module named 'cv2'"
────────────────────────────────────────────────────────────────
SOLUZIONE:
1. Installa OpenCV:
   pip install opencv-python

2. Verifica:
   python -c "import cv2; print(cv2.__version__)"


🟡 AVVERTIMENTO: "Finestra non risponde"
────────────────────────────────────────────────────────────────
CAUSA: Il simulatore è in esecuzione (normale)
SOLUZIONE:
1. Attendi il caricamento (2-3 secondi)
2. Se continua, prova:
   - Chiudi la finestra Matplotlib
   - Riprova l'app_main


🟡 PROBLEMA: Le slide non si caricano
────────────────────────────────────────────────────────────────
VERIFICA:
1. Esiste la cartella "sample_slides/"?
   - Se no, esegui app_main.py almeno una volta

2. Ci sono file PNG nella cartella?
   - Controlla: ls sample_slides/

3. I permessi sono corretti?
   - Su Linux: chmod 644 sample_slides/*.png

SOLUZIONE:
Se sample_slides non esiste, aggiungilo manualmente:
1. mkdir sample_slides
2. Metti i tuoi file PNG dentro
3. Riavvia l'app


🟡 PROBLEMA: OBS Studio non cattura la finestra di Python
────────────────────────────────────────────────────────────────
SOLUZIONE:
1. Assicurati che l'app Python sia lanciata PRIMA di OBS
2. In OBS: Sorgente > Cattura Finestra > Seleziona finestra
3. Se non appare, prova "Cattura Schermo" (meno elegante ma funziona)
4. Regola la risoluzione in OBS (1920x1080 per YouTube)


🟡 PROBLEMA: Audio non sincronizzato con video in OBS
────────────────────────────────────────────────────────────────
SOLUZIONE in OBS:
1. Vai su Impostazioni > Audio
2. Configura i ritardi (solitamente 0)
3. Se necessario, usa "Sincronizzazione Audio" nel menu
4. Fai un test: registra 5 secondi, parla, controlla


🟡 PROBLEMA: Il video è sfocato/pixelato
────────────────────────────────────────────────────────────────
SOLUZIONE in OBS:
1. Impostazioni > Uscita > Risoluzione Base Tela
   Imposta a 1920x1080 (per YouTube HD)

2. Codec: Seleziona NVENC (se hai NVIDIA) o Software (lento)

3. Bitrate: 
   - Download 10 Mbps → Usa 5000 kbps
   - Download 25 Mbps → Usa 10000 kbps

4. FPS: Mantieni 30 o 60


🟡 PROBLEMA: Python usa troppa memoria
────────────────────────────────────────────────────────────────
CAUSA: Il simulatore mantiene la finestra aperta
SOLUZIONE:
1. Chiudi il simulatore quando non serve (premi Q o chiudi)
2. Non lasciare aperte troppe finestre
3. Se persiste, verifica altre app in background


🟡 PROBLEMA: La lavagna è lenta
────────────────────────────────────────────────────────────────
CAUSA: Bassa frequenza di refresh o CPU sovraccarica
SOLUZIONE:
1. Chiudi altre app in background
2. Controlla CPU: top (Linux) o Task Manager (Windows)
3. Riduci lo spessore del pennello (tasto -)
4. Se molto lenta, la tua CPU è insufficiente


❓ FAQ - DOMANDE FREQUENTI
═════════════════════════════════════════════════════════════════

D: Posso usare le mie slide PowerPoint?
R: Sì, ma devi convertirle in PNG/JPG prima:
   - LibreOffice: Esporta > Esporta come PDF
   - Poi converti PDF in PNG con un convertitore online
   - Metti i PNG in una cartella
   - Modifica app_main.py per usare quella cartella

D: Come registro solo il simulatore senza l'app principale?
R: Avvia direttamente il simulatore:
   python interactive_physics.py
   Poi cattura con OBS Studio

D: Come registro solo la lavagna?
R: Avvia direttamente la lavagna:
   python whiteboard.py
   Cattura con OBS Studio

D: Posso salvare il disegno della lavagna?
R: Attualmente non è supportato, ma puoi:
   1. OBS salva lo schermo comunque
   2. Oppure modifica whiteboard.py per aggiungere:
      pygame.image.save(self.canvas, 'whiteboard.png')

D: Il simulatore ha unità di misura reali?
R: Sì:
   - Massa: chilogrammi (kg)
   - Forze: Newton (N)
   - Accelerazione: m/s²
   - Gravità: 9.8 m/s²

D: Posso aggiungere più modalità/argomenti?
R: Certo! Copia interactive_physics.py e:
   1. Modifica la classe per il tuo argomento
   2. Aggiungi un bottone in app_main.py
   3. Lancia la tua classe come gli altri

D: Il video è troppo lungo/corto - come tagliarlo?
R: Usa un editor video:
   - DaVinci Resolve (gratuito)
   - Shotcut (gratuito)
   - Adobe Premiere (a pagamento)
   Oppure su YouTube Studio quando carichi

D: Posso aggiungere musica di sottofondo?
R: Sì, con un editor video:
   - Aggiungi traccia audio
   - Regola il volume della voce vs musica
   - Esporta e carica

D: Come faccio sottotitoli?
R: Opzioni:
   1. YouTube auto-genera sottotitoli (imperfetti)
   2. Carica file SRT a mano
   3. Usa un servizio (Rev, 3PlayMedia)

D: Posso usare questo commercialmente?
R: Sì, è MIT License (libero per qualsiasi uso)

D: Dove metto i miei file personali?
R: Crea una cartella nella radice del progetto:
   mkdir mie_lezioni
   metti i file qui
   modifica app_main.py per usarla

═════════════════════════════════════════════════════════════════

Altre domande?
Controlla il file README.md per informazioni complete!

"""

if __name__ == "__main__":
    print(TROUBLESHOOTING)
