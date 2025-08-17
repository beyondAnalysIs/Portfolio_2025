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
    initial_sidebar_state= "collapsed" 
    
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
        },
        {
            "title": "Análisis de Ventas - Restaurante",
            "description": "Aplicación completa de EDA para optimizar análisis de ventas, identificando patrones de consumo y tendencias estacionales.",
            "tech_stack": ["Python", "Pandas", "Matplotlib", "Streamlit"],
            "github_url": "https://github.com/beyondAnalysIs/Ventas-Restaurante",
            "demo_url": "https://ventas-restaurante-app.streamlit.app/",
            "date": "Agosto 2025",
            "impact": "Redcucción 25% tiempo de análisis manual",
            "metrics": {"Eficiencia": "+25%", "Patrones": "12 identificados", "KPIs": "6 personalizados"}
        },
        {
            "title": "💰 Dashboard Salarios Tech Global",
            "description": "Exploración y visualización de tendencias salariales en la la industria tecnológica mundial con análisis comparativo por países y roles.",
            "tech_stack": ["Python", "Streamlit", "Plotly", "Data Analysis", "Global Data"],
            "github_url": "https://github.com/beyondAnalysIs/dashboard_salaries",
            "demo_url": "https://salaries-dashboard-app.streamlit.app/",
            "date": "Julio 2025",
            "impact": "Insights para negosación salarial",
            "metrics": {"Países": "50+", "Roles": "100+", "Registros": "10K+"}
        },
        {
            "title": "🌎 API Integration Dashboard",
            "description": "Aplicación web que consume APIs externas para visualización en tiempo real con manejo de errores y optimización de rendimiento.",
            "tech_stack": ["Python", "Streamlit","API REST", "JSON", "Ral-time"],
            "github_url": "https://github.com/beyondAnalysIs/streamlit_python_api",
            "demo_url": "https://api-integration-app.streamlit.app/",
            "date": "Julio 2025",
            "impact": "Monitoreo en tiempo real",
            "metrics": {"APIs": "3 integradas", "Updates": "Tiempo real", "Uptime": "99.9%"}
        },
        {
            "title": "📊 Multi-Dashboard Company Analytics",
            "description": "Dashboard empresarial completo utilizando múltiples fuentes de datos con limpieza, manipulación y visualización avanzada.",
            "tech_stack": ["Python", "Streamlit","Plotly", "Numpy", "Data Cleaning"],
            "github_url": "https://github.com/beyondAnalysIs/Dashboard_Company",
            "demo_url": "https://company-analytics-app.streamlit.app/",
            "date": "Julio 2025",
            "impact": "Centralización de métricas empresariales",
            "metrics": {"Dashboards": "5", "Fuentes": "Multiple", "Métricas": "25+"}
        },
        {
            "title": "🤖 Automatización Excel con Python",
            "description": "Scripts de automatización para manipulación masiva de hojas de cálculo, reduciendo significativamente el tiempo de procesamiento manual.",
            "tech_stack": ["Python", "OpenPyXL","Pandas", "Automation", "Excel"],
            "tech_stack": ["Python", "OpenPyXL", "Pandas", "Automation", "Excel"],
            "github_url": "https://github.com/beyondAnalysIs/Automatizacion_python",
            "demo_url": None,
            "date": "Mayo 2025",
            "impact": "De 4 horas a 15 minutos de procesamiento",
            "metrics": {"Eficiencia": "94% reducción", "Archivos": "100+", "Automatización": "Completa"}
        }
    ]
#===========================================
# FUNCIONES DE UTILIDAD
#===========================================
def create_skill_chart():
    """Crear gráfico de habilidades técnicas"""
    skills_data = {
        "Skill": ["Python", "Pandas", "Plotly", "Streamlit", "SQL", "Machine Learning", "Data Analysis", "Excel"],
        "Level": [95, 90, 88, 85, 75, 70, 92, 85],
        "Category": ["Programming", "Data", "Visualización", "Web Dev", "ML", "Analysis", "Tools", "EDA"] 
    }

    df = pd.DataFrame(skills_data)

    fig = px.bar(df, x="Level", y="Skill", orientation = 'h',
                 color="Category",title="Habilidades Técnicas", 
                 #color_discrete_secuence=px.colors.qualitative)
    )

    fig.update_layout(
        height=400,
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def create_projects_timeline():
    """Crear timeline de proyectos"""
    projects = get_projects_data()
    
    fig = go.Figure()
    
    dates = ["2025-05", "2025-06", "2025-07-10", "2025-07-19", "2025-07-21", "2025-08"]

    projects_names = [p['title'].split(" ")[1] for p in projects]

    fig.add_traces(go.Scatter(
        x=dates,
        y=projects_names,
        mode="markers+lines+text",
        marker= dict(size=15, color="#1f77b4"),
        line=dict(color="#1f77b4", width=3),
        text=projects_names,
        textposition="middle right"
    ))
    
    fig.update_layount(
        title="Timeline de Proyectos",
        xaxis_title="Fecha",
        yaxis_title= "Proyectos",
        height=400,
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font="white"
    )

    return fig
    
def create_tech_distribution():
    """ Crear gráfico de distribucion de tecnologías"""
    projects = get_projects_data()

    tech_counts = {}

    for project in projects:
        for tech in project['tech_stack']:
            if tech in tech_counts:
                tech_counts[tech] += 1
            else:
                tech_counts[tech] = 1

    fig = px.pie(
        values=list(tech_counts.values()),
        names=list(tech_counts.keys()),
        title="Distribución de Tecnologías"
    )

    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )

    return fig

def display_projects_card(project):
    """ Mostrar card de proyecto"""
    with st.container():
        st.markdown(f"""
            <div class = "project-title>{project['title']}</div>
            <p>{project["description"]}</p>                    
            <p><strong>📅 Fecha:</strong>{project["date"]}</p>
            <p><strong>💡 Impacto:</strong>{project["impact"]}</p>
           """, unsafe_allow_html=True)

        # Tech stack tags
        st.markdown("** 🛠️ Tecnologías")
#===========================================
# PÁGINAS DE LA APLICACIÓN
#===========================================