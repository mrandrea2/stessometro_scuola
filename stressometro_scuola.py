import streamlit as st

# Imposta lo sfondo verde chiaro
st.markdown(
    """
    <style>
    body {
        background-color: #d4edda; /* Verde chiaro */
    }
    h2 {
        font-size: 22px;
    }
    h3 {
        font-size: 20px;
    }
    .large-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #2d6a4f; /* Verde scuro */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titolo e autore
st.title("📚 Stressometro per la Scuola")
st.write("### Creato da Andrea Bertelli ©")

# Istruzioni per la compilazione
st.subheader("📝 Istruzioni")
st.write("""
Questo test ti aiuterà a valutare il tuo livello di stress scolastico.  
- **Si tratta di uno strumento di auto-monitoraggio**. I risultati **non vengono registrati** né inviati ad alcuna piattaforma.  
- Per ogni area, assegna un punteggio da **1 (basso) a 10 (alto)**.  
- Alla fine, otterrai un'analisi dettagliata e consigli utili per gestire lo stress.  
""")

# Selezione del profilo
profilo = st.radio("Sei un:", ("Studente", "Docente"))

# Aree di valutazione con descrizioni
if profilo == "Studente":
    aree = {
        "Carico di studio": "Mi sento sopraffatto dal numero di compiti, verifiche e interrogazioni.",
        "Qualità del sonno": "Dormo bene e mi sento riposato al mattino.",
        "Concentrazione": "Riesco a mantenere l'attenzione durante le lezioni e lo studio.",
        "Pressione per i voti": "Mi sento sotto pressione per ottenere buoni voti.",
        "Ansia da interrogazione/verifica": "Mi sento molto ansioso prima di verifiche e interrogazioni.",
        "Motivazione scolastica": "Ho voglia di studiare e apprendere nuove cose.",
        "Rapporto con i docenti": "Sento di avere un buon rapporto con gli insegnanti e posso comunicare con loro.",
        "Tempo libero": "Riesco a bilanciare studio e tempo libero.",
        "Relazioni sociali": "Mi sento supportato dai miei amici e compagni di classe.",
        "Gestione del tempo": "Riesco a organizzare bene il mio tempo tra studio e attività personali."
    }
else:
    aree = {
        "Carico di lavoro": "Il numero di ore di insegnamento e correzione mi sembra eccessivo.",
        "Qualità del sonno": "Dormo bene e mi sento riposato al mattino.",
        "Concentrazione": "Riesco a mantenere la concentrazione durante le lezioni e la preparazione didattica.",
        "Pressione da parte della scuola": "Sento di dover soddisfare troppe richieste burocratiche o didattiche.",
        "Ansia da valutazione": "Mi sento sotto pressione nel valutare e gestire il comportamento degli studenti.",
        "Motivazione professionale": "Mi sento motivato nel mio lavoro di docente.",
        "Rapporto con gli studenti": "Sento di avere un buon rapporto con gli studenti e posso comunicare con loro.",
        "Tempo libero": "Riesco a bilanciare il lavoro con il mio tempo libero.",
        "Rapporto con i colleghi": "Mi sento supportato dai miei colleghi e dalla scuola.",
        "Gestione del tempo": "Riesco a organizzare bene le mie attività professionali e personali."
    }

# Creazione degli slider con descrizione
punteggi = []
for area, descrizione in aree.items():
    st.markdown(f"### **{area}**")  # Testo più grande e in grassetto
    st.write(f"*{descrizione}*")  
    punteggio = st.slider(f"{area}", 1, 10, 5, key=area)

    # Se l'area è positiva, inverto il punteggio senza indicarlo
    if area in ["Qualità del sonno", "Concentrazione", "Motivazione scolastica", "Rapporto con i docenti",
                "Tempo libero", "Relazioni sociali", "Gestione del tempo", "Motivazione professionale",
                "Rapporto con gli studenti", "Rapporto con i colleghi"]:
        punteggio = 11 - punteggio  # Esempio: se scelgo 9, diventa 2

    punteggi.append(punteggio)

# Calcolo dell'indice di stress (0-100)
stress_index = int((sum(punteggi) / (10 * len(punteggi))) * 100)
st.subheader(f"**Indice di Stress: {stress_index}/100**")

# Analisi dettagliata con consigli specifici
st.subheader("📊 Interpretazione del tuo stress")

if stress_index <= 20:
    st.success("**Nessuno Stress ✅** - Ottimo, continua così!")
    st.write("""
    **Consigli per mantenere il benessere:**  
    - Continua a mantenere una routine sana e bilanciata.  
    - Mantieni il giusto equilibrio tra impegni e tempo libero.  
    - Aiuta gli altri condividendo strategie che funzionano per te!  
    """)

elif stress_index <= 40:
    st.success("**Stress Moderato 🟢** - Nulla di preoccupante, ma migliorabile.")
    st.write("""
    **Consigli per ridurre lo stress:**  
    - Assicurati di dormire almeno 7-8 ore per recuperare bene.  
    - Trova modi per rendere lo studio/lavoro più interessante e meno pesante.  
    - Concediti momenti di pausa strategici per evitare il sovraccarico.  
    """)

elif stress_index <= 60:
    st.warning("**Stress Medio ⚠️** - Stai iniziando a sentire il peso dello stress.")
    st.write("""
    **Suggerimenti per migliorare:**  
    - Organizza meglio il tuo tempo con una lista di priorità.  
    - Evita il multitasking e concentrati su un compito alla volta.  
    - Parla con qualcuno di fidato per sfogarti e ricevere supporto.  
    """)

elif stress_index <= 80:
    st.error("**Stress Alto 🟠** - Lo stress sta influenzando il tuo benessere.")
    st.write("""
    **Azioni da intraprendere subito:**  
    - Rallenta il ritmo e concediti più tempo per rilassarti.  
    - Pratica tecniche di rilassamento come respirazione profonda o mindfulness.  
    - Cerca supporto, non devi affrontare tutto da solo!  
    """)

else:
    st.error("**Stress Molto Alto 🔴** - Attenzione, lo stress è troppo elevato!")
    st.write("""
    **Strategie urgenti per ridurre lo stress:**  
    - Rivaluta le tue priorità: cosa puoi delegare o ridurre?  
    - Parla con un esperto (psicologo, tutor, coach) per trovare soluzioni concrete.  
    - Prenditi una pausa: il recupero è essenziale per la tua salute mentale.  
    """)

# Messaggio finale in grande
st.markdown('<p class="large-text">🔄 Compila il test una volta a settimana per monitorare il tuo stress!</p>', unsafe_allow_html=True)
