import streamlit as st
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="EM Lyon | Cybersecurity Treasure Chest", 
    page_icon="🔒", 
    layout="wide" # Utilise toute la largeur de l'écran
)

# --- STYLE CSS PERSONNALISÉ (HAUTEMENT STYLISÉ) ---
st.markdown("""
    <style>
    /* Fond général */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding-top: 2rem;
    }

    /* Titres */
    .main-title {
        font-family: 'Montserrat', sans-serif;
        color: #D31145;
        text-align: center;
        font-weight: 900;
        font-size: 4rem;
        margin-bottom: 0.2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-title {
        font-family: 'Open Sans', sans-serif;
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }

    /* LA BOITE DE SAISIE (FIX : TEXTE QUI DÉPASSE) */
    div[data-baseweb="input"] {
        border-radius: 25px !important;
        border: 4px solid #D31145 !important;
        background-color: #ffffff !important;
        padding: 25px !important; /* Plus d'espace pour que le texte respire */
        min-height: 140px !important; /* Force la boîte à être haute */
        box-shadow: 0 15px 35px rgba(211, 17, 69, 0.1) !important;
    }

    input {
        font-size: 4rem !important; /* Texte encore plus massif */
        height: 100% !important;
        line-height: 1.5 !important; /* FIX : Aligne les points du MDP au centre */
        text-align: center !important;
        color: #D31145 !important;
        font-weight: bold !important;
        background-color: transparent !important;
    }
    
    /* On force le conteneur du bouton à devenir un flexbox centré */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 30px !important;
    }
    
    /* Bouton de Déverrouillage MASSIF */
    .stButton>button {
        width: 100%;
        border-radius: 60px;
        height: 5rem; /* Hauteur augmentée */
        background: linear-gradient(45deg, #D31145, #b00d3a);
        color: white;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        border: none;
        margin-top: 30px;
        box-shadow: 0 8px 15px rgba(176, 13, 58, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(45deg, #b00d3a, #D31145);
        transform: translateY(-3px);
        box-shadow: 0 12px 20px rgba(176, 13, 58, 0.4);
    }
    
    /* Conteneur central */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    /* Image du coffre-fort */
    .vault-image {
        max-width: 300px;
        margin-bottom: 1rem;
        filter: drop-shadow(0 10px 10px rgba(0,0,0,0.2));
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE L'APPLICATION ---
def load_secret_code():
    if os.path.exists("code_secret.txt"):
        with open("code_secret.txt", "r") as f:
            return f.read().strip()
    return None

correct_code = load_secret_code()

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.image("https://keystoneacademic-res.cloudinary.com/image/upload/c_pad,w_3840,h_1280/dpr_auto/f_auto/q_auto/v1/element/17/174471_emlyon_logo.png", use_container_width=True)
    st.markdown("---")
    st.markdown("### 🎯 System Goal")
    st.info("""
    Welcome to the Cybersecurity Treasure Chest challenge! Your mission is to find the secret access key hidden within the course materials to unlock the treasure chest. This exercise is designed to test your attention to detail and your ability to uncover hidden information.
    """)
    st.markdown("---")
    st.caption("© 2026 EM Lyon Business School - Makers Academy")

# --- CORPS DE L'APPLICATION (CENTRE) ---
# Utilisation de colonnes pour centrer le contenu sur une page large
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<p class="main-title">EM Lyon | Cybersecurity Treasure Chest</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Please enter your high-security access key to unlock the treasure chest of the Cybersecurity Course.</p>', unsafe_allow_html=True)
    
    # Image du coffre-fort réduite à 40% de la largeur de sa colonne
    st.markdown(
        '<div class="center-container"><img src="https://png.pngtree.com/png-clipart/20250117/original/pngtree-closed-treasure-chest-isolated-on-clear-background-png-image_19933561.png" class="vault-image" style="width: 40%;"></div>',
        unsafe_allow_html=True
    )
    
    # Champ de texte géant et stylisé
    user_input = st.text_input("code", placeholder="••••••", label_visibility="collapsed")

    # Bouton de déverrouillage massif
    if st.button("🔓 UNLOCK VAULT"):
        if correct_code is None:
            st.error("System Error: 'code_secret.txt' not found.")
        elif user_input == correct_code:
            st.balloons()
            st.success("✨ **ACCESS GRANTED!** The vault has been unlocked successfully.")
            st.markdown("""
                <div style="padding:30px; border-radius:20px; background-color:#e8f5e9; border: 2px solid #2e7d32; text-align:center; margin-top:20px;">
                    <h2 style="color:#2e7d32; margin:0;">You succeed to open the Treasure Chest</h2>
                    <p style="color:#2e7d32; font-size:1.2rem;">The name of my two children are Liên and Léo</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ **ACCESS DENIED.** The key is incorrect. Please try again.")