import streamlit as st
import os

# Configuration de la page
st.set_page_config(
    page_title="JO Paris 2024 - Analyse des Données Olympiques",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown(
    """
    <style>
    /* Titre principal */
    h1 {
        color: #0055A4; /* Bleu JO */
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    /* En-têtes de section */
    h2 {
        color: #EF3340; /* Rouge JO */
        border-bottom: 2px solid #0055A4;
        padding-bottom: 5px;
        font-family: 'Arial', sans-serif;
    }
    /* Sidebar */
    .css-1d391kg {
        background-color: #0055A4 !important; /* Bleu JO */
        color: black !important;
    }
    .css-1d391kg h1 {
        color: black !important;
    }
    /* Boutons radio */
    .stRadio > div {
        background-color: #0055A4; /* Bleu JO */
        padding: 10px;
        border-radius: 10px;
    }
    .stRadio label {
        color: black !important;
        font-weight: bold;
    }
    /* Images */
    .stImage img {
        border: 3px solid #0055A4; /* Bleu JO */
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre de l'application
st.title("JO Paris 2024 - Analyse des Données Olympiques")

# Sidebar pour la navigation
st.sidebar.title("Navigation")

# Ajout de l'image des JO 2024 dans la sidebar
st.sidebar.image("images.jpg", use_column_width=True)

page = st.sidebar.radio(
    "Choisissez une page", 
    [
        "Vue Globale", 
        "Âge", 
        "Nombre d'athlètes envoyés", 
        "Répartition des athlètes",
        "Validation hypothèse"
    ]
)

# Fonction pour charger les images
def load_image(image_path):
    if os.path.exists(image_path):
        return image_path
    else:
        st.error(f"Image {image_path} non trouvée.")
        return None

# Page Vue Globale
if page == "Vue Globale":
    st.header("Vue Globale")
    
    st.image(load_image("top_12_pays_medailles.png"))
    st.image(load_image("repartition_type_medal.png"))
    st.image(load_image("top_10_disciplines_athletes.png"))
    st.image(load_image("top_10_lieux.png"))
    


# Page Âge
elif page == "Âge":
    st.header("Analyse par Âge")
    
    st.image(load_image("repartition_age_medal.png"))
    st.image(load_image("repartition_age_athlete.png"))
    st.image(load_image("perf_medaille_tranche_age.png"))
    st.image(load_image("age_moyen_medal.png"))
    st.image(load_image("age_moyen_athlete.png"))

# Page Nombre d'athlètes envoyés
elif page == "Nombre d'athlètes envoyés":
    st.header("Nombre d'athlètes envoyés")

    st.image(load_image("carte_athlete.png"))    
    st.image(load_image("top_12_pays_taux_conv.png"))
    st.image(load_image("nombre_athlete_continent.png"))


# Page Répartition des athlètes
elif page == "Répartition des athlètes":
    st.header("Répartition des athlètes")
    

    st.image(load_image("repartition_male_female.png"))
    st.image(load_image("top_10_coach.png"))
    st.image(load_image("top_5_disciplines.png"))
    st.image(load_image("top_-5_disciplines.png"))
    st.image(load_image("heatmap_athlete.png"))    

# Page Validation hypothèse
elif page == "Validation hypothèse":
    st.header("Validation de l'hypothèse")
    
    st.image(load_image("nombre_athlete_medal.png"))
    st.image(load_image("coach_vs_medals.png"))
    st.image(load_image("individuel_vs_collectif.png"))
