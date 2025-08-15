import streamlit as st
#from streamlit_option_menu import option_menu  
import plotly.express as px
import plotly.graph_objects as go 
import pandas as pd
import numpy as np
from datetime import datetime
import requests
from PIL import Image
import base64 # base64 

#===========================================
# CONFIGURACIÓN DE PÁGINA
#===========================================

st.set_page_config(
    page_title= "Anderson Hernández || Data Analyst & Scientist",
    page_icon= "👨‍💻",
    layout= "wide",
    initial_sidebar_state= "collapsed" # 
    
)

#===========================================
# ESTILOS CSS PERSONALIZADOS
#===========================================

def load_css():
    st.markdown("""
        <style>
            /* Importar fuentes de Google */ 
            @import url("'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap")

            /* Variables CSS */
            :root{
                --primary-color: #1f77b4;
                --secondary-color: #ff7f0e;
                --accent-color: #2ca02c;
                --background-dark: #0e1117;
                --text-light: #fafafa;
                --card-bg: #262730;
            }
            
            /* Reset y estilos generales */
            .main > div {
                padding-top: 0rem;
            }
            
            /* Estilo del header principal */
            .hero-section {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 4rem 2rem;
                border-radius: 15px;
                margin-bottom: 2rem;
                text-align: center;
                color: white;
            }
            
            .hero-title {
                font-family: 'Poppins', sans-serif;
                font-size: 3.5rem;
                font-weight: 700;
                margin-bottom: 1rem;
                background: linear-gradient(45deg, #ffffff, #e0e0e0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .hero-subtitle{
                font-family: 'Poppins', sans-serif;
                font-size: 1.2rem;
                font-weight: 300;
                opacity: 0.9;
                margin-bottom: 2rem;
            }
            
            /* Cards de proyectos */
            .project-card {
                background: #262730;
                border-radius: 15px;
                padding: 2rem;
                margin: 1rem 0;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 45px rgba(0, 0, 0, 0.4);
            }
            
            .project-title {
                font-family: 'Poppins', sans-serif;
                font-size: 1.5rem;
                font-weight: 600;
                color: #1f77b4;
                margin-bottom: 1rem;
            }
            
            .tech-tag {
                display: inline-block;
                background: linear-gradient(45deg, #1f77b4, #ff7f0e);
                color: white;
                padding: 0.3rem 0.8rem;
                border-radius: 20px;
                font-size: 0.8rem;
                margin: 0.2rem;
                font-weight: 500;
            }
            
            /* Métricas personalizadas */
            .custom-metric {
                background: #262730;
                padding: 1.5rem;
                border-radius: 10px;
                text-align: center;
                border-left: 4px solid #1f77b4;
            }
            
            .metric-value {
                font-size: 2.5rem;
                font-weight: 700;
                color: #1f77b4;
            }
            
            .metric-label {
                font-size: 1rem;
                color: #888;
                margin-top: 0.5rem;
            }
            
            /* Botones personalizados */
            .custom-button {
                background: linear-gradient(45deg, #1f77b4, #ff7f0e);
                color: white;
                padding: 0.8rem 2rem;
                border: none;
                border-radius: 25px;
                text-decoration: none;
                font-weight: 600;
                display: inline-block;
                margin: 0.5rem;
                transition: transform 0.3s ease;
            }
            
            .custom-button:hover {
                transform: scale(1.05);
                text-decoration: none;
                color: white;
            }
            
            /* Skills grid */
            .skills-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1rem;
                margin: 2rem 0
            }
            
            .skill-item {
                background: #262730;
                padding: 1rem;
                border-radius: 10px;
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            /* Footer */
            .footer {
                text-align: center;
                padding: 2rem;
                margin-top: 3rem;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                color: #888;
            }
        </style>
    """, unsafe_allow_html=True)

#===========================================
# DATOS DE PROYECTOS
#===========================================
def get_projects_data():
    return[
        {
            "title": "🏦 Dashboard Bancario Interactivo",
            "description": "Análisis exploratorio completo de datos bancarios con métricas de riesgo, filtro dinamicos y visualizaciones multidimensionales",
            "tech_stack": ["Python", "Streamlit", "Plotly", "Pandas", "EDA"],
            "gihub_url": "https://github.com/beyondAnalysIs/dashboard_bank",
            "demo_url":"",
            "date": "Junio 2025",
            "impact": "Automatización de reportes ejecutivos",
            "metrics":{"Datasets": "10K+ registros", "Visualizaciones": "15+", "KPIs": "8"}
        }
    ]
get_projects_data()

