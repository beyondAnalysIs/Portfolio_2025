import streamlit as st
from streamlit_option_menu import option_menu  
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
    page_title= "Anderson Hernández",
    page_icon= "👨‍💻",
    layout= "wide",
    initial_sidebar_state= "collapsed" 
    
)
# cache data
@st.cache_data
#===========================================
# ESTILOS CSS PERSONALIZADOS
#===========================================
def load_css():
    st.markdown("""
        <style>
            /* Importar fuentes similares a Plotly */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
            
            /* Variables CSS - Plotly Dark Theme */
            :root {
                --plotly-bg-primary: #111111;
                --plotly-bg-secondary: #1a1a1a;
                --plotly-bg-tertiary: #262626;
                --plotly-accent-blue: #636efa;
                --plotly-accent-orange: #ff6692;
                --plotly-accent-green: #19d3f3;
                --plotly-text-primary: #f8f9fa;
                --plotly-text-secondary: #d1d5db;
                --plotly-text-muted: #9ca3af;
                --plotly-border: #374151;
                --plotly-border-light: #4b5563;
                --plotly-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
                --plotly-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
                --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            /* Reset y base styles */
            * {
                box-sizing: border-box;
            }
            
            .stApp {
                background: var(--plotly-bg-primary) !important;
                color: var(--plotly-text-primary) !important;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
            }
            
            .main > div {
                padding-top: 1rem !important;
                background: var(--plotly-bg-primary);
            }
            
            /* Hero Section - Plotly Style */
            .hero-section {
                background: linear-gradient(135deg, var(--plotly-bg-secondary) 0%, var(--plotly-bg-tertiary) 100%);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 4rem 3rem;
                margin: 1rem 0 2rem 0;
                text-align: center;
                position: relative;
                overflow: hidden;
                box-shadow: var(--plotly-shadow-lg);
            }
            
            .hero-section::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, var(--plotly-accent-blue), var(--plotly-accent-green), var(--plotly-accent-orange));
            }
            
            .hero-title {
                font-family: 'Inter', sans-serif;
                font-size: 3.5rem;
                font-weight: 800;
                letter-spacing: -0.025em;
                margin-bottom: 1rem;
                background: linear-gradient(135deg, var(--plotly-text-primary) 0%, var(--plotly-text-secondary) 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                line-height: 1.1;
            }
            
            .hero-subtitle {
                font-size: 1.25rem;
                font-weight: 400;
                color: var(--plotly-text-secondary);
                margin-bottom: 2rem;
                max-width: 700px;
                margin-left: auto;
                margin-right: auto;
                line-height: 1.6;
            }
            
            /* Project Cards - Plotly Style */
            .project-card {
                background: var(--plotly-bg-secondary);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 2rem;
                margin: 1.5rem 0;
                transition: var(--transition);
                box-shadow: var(--plotly-shadow);
                position: relative;
                overflow: hidden;
            }
            
            .project-card:hover {
                transform: translateY(-2px);
                border-color: var(--plotly-accent-blue);
                box-shadow: var(--plotly-shadow-lg);
                background: linear-gradient(135deg, var(--plotly-bg-secondary) 0%, rgba(99, 110, 250, 0.05) 100%);
            }
            
            .project-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 4px;
                height: 100%;
                background: var(--plotly-accent-blue);
                opacity: 0;
                transition: var(--transition);
            }
            
            .project-card:hover::before {
                opacity: 1;
            }
            
            .project-title {
                font-family: 'Inter', sans-serif;
                font-size: 1.5rem;
                font-weight: 600;
                color: var(--plotly-text-primary);
                margin-bottom: 1rem;
                line-height: 1.4;
            }
            
            .project-title:hover {
                color: var(--plotly-accent-blue);
                transition: var(--transition);
            }
            
            /* Tech Tags - Plotly Inspired */
            .tech-tag {
                display: inline-flex;
                align-items: center;
                background: rgba(99, 110, 250, 0.1);
                color: var(--plotly-accent-blue);
                border: 1px solid rgba(99, 110, 250, 0.2);
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: 500;
                margin: 0.25rem;
                transition: var(--transition);
                font-family: 'JetBrains Mono', monospace;
            }
            
            .tech-tag:hover {
                background: rgba(99, 110, 250, 0.2);
                border-color: var(--plotly-accent-blue);
                transform: scale(1.05);
            }
            
            /* Metrics - Plotly Dashboard Style */
            .custom-metric {
                background: var(--plotly-bg-secondary);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 1.5rem;
                text-align: center;
                transition: var(--transition);
                position: relative;
                overflow: hidden;
            }
            
            .custom-metric::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: var(--plotly-accent-green);
            }
            
            .custom-metric:hover {
                border-color: var(--plotly-accent-green);
                background: linear-gradient(135deg, var(--plotly-bg-secondary) 0%, rgba(25, 211, 243, 0.05) 100%);
            }
            
            .metric-value {
                font-family: 'Inter', sans-serif;
                font-size: 2.25rem;
                font-weight: 700;
                color: var(--plotly-text-primary);
                margin-bottom: 0.5rem;
                line-height: 1;
            }
            
            .metric-label {
                font-size: 0.875rem;
                color: var(--plotly-text-muted);
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            
            /* Buttons - Plotly Action Style */
            .custom-button {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: var(--plotly-accent-blue);
                color: white;
                border: 1px solid var(--plotly-accent-blue);
                padding: 0.75rem 1.5rem;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 500;
                font-size: 0.9rem;
                margin: 0.25rem;
                transition: var(--transition);
                box-shadow: var(--plotly-shadow);
            }
            
            .custom-button:hover {
                background: transparent;
                color: var(--plotly-accent-blue);
                border-color: var(--plotly-accent-blue);
                transform: translateY(-1px);
                box-shadow: var(--plotly-shadow-lg);
                text-decoration: none;
            }
            
            /* Skills Grid */
            .skills-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1rem;
                margin: 2rem 0;
            }
            
            .skill-item {
                background: var(--plotly-bg-secondary);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 1.5rem;
                text-align: center;
                transition: var(--transition);
                position: relative;
            }
            
            .skill-item:hover {
                border-color: var(--plotly-accent-orange);
                background: linear-gradient(135deg, var(--plotly-bg-secondary) 0%, rgba(255, 102, 146, 0.05) 100%);
                transform: translateY(-2px);
            }
            
            .skill-item h4 {
                color: var(--plotly-text-primary);
                font-weight: 600;
                margin-bottom: 0.5rem;
                font-size: 1rem;
            }
            
            .skill-item p {
                color: var(--plotly-text-secondary);
                font-size: 0.875rem;
                line-height: 1.5;
            }
            
            /* Sections */
            .section {
                background: var(--plotly-bg-secondary);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 2rem;
                margin: 1.5rem 0;
                box-shadow: var(--plotly-shadow);
            }
            
            /* Typography */
            h1, h2, h3, h4, h5, h6 {
                color: var(--plotly-text-primary) !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600;
                line-height: 1.3;
            }
            
            h1 { font-size: 2.5rem; }
            h2 { font-size: 2rem; }
            h3 { font-size: 1.75rem; }
            h4 { font-size: 1.5rem; }
            
            p, li, span {
                color: var(--plotly-text-secondary) !important;
                line-height: 1.6;
            }
            
            strong {
                color: var(--plotly-text-primary) !important;
                font-weight: 600;
            }
            
            /* Links */
            a {
                color: var(--plotly-accent-blue);
                text-decoration: none;
                transition: var(--transition);
            }
            
            a:hover {
                color: var(--plotly-accent-green);
                text-decoration: underline;
            }
            
            /* Contact Form */
            .contact-form {
                background: var(--plotly-bg-secondary);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 2rem;
                box-shadow: var(--plotly-shadow);
            }
            
            /* Streamlit Component Overrides */
            .stSelectbox > div > div {
                background-color: var(--plotly-bg-secondary) !important;
                border-color: var(--plotly-border) !important;
                color: var(--plotly-text-primary) !important;
            }
            
            .stMultiSelect > div > div {
                background-color: var(--plotly-bg-secondary) !important;
                border-color: var(--plotly-border) !important;
            }
            
            .stTextInput > div > div > input,
            .stTextArea > div > div > textarea {
                background-color: var(--plotly-bg-secondary) !important;
                border-color: var(--plotly-border) !important;
                color: var(--plotly-text-primary) !important;
            }
            
            .stTextInput > div > div > input:focus,
            .stTextArea > div > div > textarea:focus {
                border-color: var(--plotly-accent-blue) !important;
                box-shadow: 0 0 0 1px var(--plotly-accent-blue) !important;
            }
            
            /* Plotly Chart Containers */
            .js-plotly-plot {
                background: var(--plotly-bg-secondary) !important;
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                box-shadow: var(--plotly-shadow);
            }
            
            /* Footer */
            .footer {
                background: var(--plotly-bg-secondary);
                border: 1px solid var(--plotly-border);
                border-radius: 8px;
                padding: 2rem;
                margin-top: 3rem;
                text-align: center;
                color: var(--plotly-text-muted);
                box-shadow: var(--plotly-shadow);
            }
            
            .footer a {
                color: var(--plotly-accent-blue);
                font-weight: 500;
            }
            
            .footer a:hover {
                color: var(--plotly-accent-green);
            }
            
            /* Code blocks */
            code {
                background: rgba(99, 110, 250, 0.1) !important;
                color: var(--plotly-accent-blue) !important;
                padding: 0.2rem 0.4rem !important;
                border-radius: 4px !important;
                font-family: 'JetBrains Mono', monospace !important;
                font-size: 0.875rem !important;
            }
            
            /* Dividers */
            hr {
                border: none !important;
                height: 1px !important;
                background: var(--plotly-border) !important;
                margin: 2rem 0 !important;
            }
            
            /* Responsive Design */
            @media (max-width: 768px) {
                .hero-title {
                    font-size: 2.5rem;
                }
                
                .hero-subtitle {
                    font-size: 1.125rem;
                }
                
                .project-card,
                .custom-metric,
                .skill-item {
                    padding: 1.5rem;
                }
                
                .skills-grid {
                    grid-template-columns: 1fr;
                }
            }
            
            /* Animation for loading */
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
from streamlit_option_menu import option_menu
from streamlit_option_menu import option_menu
                to { opacity: 1; transform: translateY(0); }
            }
            
            .project-card,
            .custom-metric,
            .skill-item {
                animation: fadeIn 0.3s ease-out;
            }
            
            /* Success/Error Messages */
            .stSuccess > div {
                background: rgba(25, 211, 243, 0.1) !important;
                border-color: var(--plotly-accent-green) !important;
                color: var(--plotly-text-primary) !important;
            }
            
            .stError > div {
                background: rgba(255, 102, 146, 0.1) !important;
                border-color: var(--plotly-accent-orange) !important;
                color: var(--plotly-text-primary) !important;
            }
            
            .stInfo > div {
                background: rgba(99, 110, 250, 0.1) !important;
                border-color: var(--plotly-accent-blue) !important;
                color: var(--plotly-text-primary) !important;
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
            "github_url": "https://github.com/beyondAnalysIs/dashboard_bank",
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
    
    fig.update_layout(
        title="Timeline de Proyectos",
        xaxis_title="Fecha",
        yaxis_title= "Proyectos",
        height=400,
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
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
            <div class = "project-card">
                <div class = "project-title">{project["title"]}</div>
                <p>{project["description"]}</p>                    
                <p><strong>📅 Fecha:</strong>{project["date"]}</p>
                <p><strong>💡 Impacto:</strong>{project["impact"]}</p>
            </div>
           """, unsafe_allow_html=True)

        # Tech stack tags
        st.markdown("** 🛠️ Tecnologías")
        tech_html = ""
        for tech in project["tech_stack"]:
            tech_html += f"<span class='tech-tag'>{tech}</span>"
        st.markdown(tech_html, unsafe_allow_html=True)
        
        # Métricas del proyecto
        col1,col2,col3 = st.columns(3)
        metrics = project["metrics"]
        metric_keys = list(metrics.keys())

        with col1:
            st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">{metrics[metric_keys[0]]}</div>
                <div class="metric-label>{metric_keys[0]}</div>
            </div>    
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">{metrics[metric_keys[1]]}</div>
                <div class="metric-label">{metric_keys[1]}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">{metrics[metric_keys[2]]}</div>
                <div class="metric-label">{metric_keys[2]}</div>
            </div>
            """, unsafe_allow_html=True)
            
        # Botones de acción
        col1,col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <a href="{project["github_url"]}" target="_blank" class="custom-buttom">
                    📂 Ver Código
                </a> 
            """, unsafe_allow_html=True)

        with col2:
            if project["demo_url"]:
                st.markdown(f"""
                    <a href="{project['demo_url']}" target="_blank" class="custom-button">
                        🚀 Demo Live
                    </a>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <span style="color: #888; font-style= italic; padding: .8rem; display: inline-block;">
                        📦 Repositorio Local
                    </span>
                """, unsafe_allow_html=True)   
      
#===========================================
# PÁGINAS DE LA APLICACIÓN
#===========================================
def home_page():
    """ Página principal / Landing"""
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">Anderson Hernández</div>   
        <div class="hero-subtitle">Data Analyst & Data Scientist | Transformando datos en decisiones estratégicas</div>   
       <p>🏠 Madrid, España | 💼 + Proyectos | 📊 Especialista en Python & Machine Learning</p> 
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas Principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">15+</div>
                <div class="metric-label">Proyectos Completados</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">8</div>
                <div class="metric-label">Apps Streamlit</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">50K</div>
                <div class="metric-label">Registros Analizados</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown(f"""
            <div class="custom-metric">
                <div class="metric-value">2+</div>
                <div class="metric-label">Años Experiencia</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Resumen Profesional
    col1, col2 = st.columns([2,1])
    with col1: 
        st.header("🎯 Perfil Profesional")
        st.write("""
            Soy un **Data Analyst especializado en Python** con experiencia demostrable en el desarrollo de 
            dashboards interactivos, análisis exploratorio de datos y automatización de procesos.

            Mi expertise incluye:
            - 📊 **Análisis Exploratorio de Datos (EDA)** con datasets complejos
            - 🔍 **Business Intelligence** y creación de KPIs personalizados  
            - 🚀 **Desarrollo de aplicaciones web** con Streamlit y Plotly
            - 🤖 **Automatización de procesos** reduciendo tiempo manual hasta 94%
            - 📈 **Visualización avanzada** para toma de decisiones empresariales
            
            **Actualmente buscando oportunidades en Madrid** como Data Analyst, Business Intelligence Analyst 
            o Data Scientist Junior en empresas que valoren la innovación y el crecimiento basado en datos.
        """, unsafe_allow_html=True)
    data_stack_tecnico = {
        "Categoría": [
            "Lenguajes",
            "Librerías Principales",
            "Herramientas"
        ],
        "Detalles": [
            "Python (Avanzado)| SQL (Intermedio)",
            "Pandas| NumPy| SciPy | Plotly| Matplotlib|  Seaborn| Streamlit| Flask| Scikit-learn",
            "Git/GitHub| Excel Avanzado| Power BI| APIs REST"
        ]
    }
    df_stack_tecnico = pd.DataFrame(data_stack_tecnico)
    df_stack_tecnico["Detalles"]=df_stack_tecnico["Detalles"].apply(lambda x: x.replace("|","<br>"))
    
    with col2:
        st.header("🛠️ Stack Técnico")
        df_html = df_stack_tecnico.to_html(index=False, escape=False)
        st.markdown(df_html, unsafe_allow_html=True) 
    
    # Timeline reciente y distribución de tecnologías
    col1,col2 = st.columns(2)
    
    with col1:
        st.header("📈 Timeline de Proyectos")
        fig_timeline = create_projects_timeline()
        st.plotly_chart(fig_timeline, use_container_width=True)
        
    with col2:
        st.header("🔧 Tecnologías más Usadas")
        fig_tech = create_tech_distribution()
        st.plotly_chart(fig_tech, use_container_width=True)

def show_projects():
    """ Pagina de Proyectos"""
    st.header("📂 Portafolio de Proyectos")
    st.write("Selecciona de mis mejores proyectos de análisis de datos y ciencia de datos:")

    # Filtros
    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        tech_filter = st.multiselect(
            "Filtrar por tecnología:",
            ["Python", "Streamlit", "Plotly", "Pandas", "API", "Automation", "EDA"],
            default=[]    
        )
    with col2:
        date_filter = st.selectbox(
            "FIltrar por período:",
            ["Todos", "2025", "Julio 2025", "Agosto 2025"]
        )
    with col3:
        sort_by = st.selectbox(
            "Ordenar por:",
            ["Fecha (más reciente)", "Fecha (más antiguo)", "Título A-Z"]
        )
    projects = get_projects_data()
    
    # Aplicar filtros
    if tech_filter:
        projects = [p for p in projects if any(tech in p['tech_stack'] for tech in tech_filter)]

    if date_filter != "Todos":
        projects = [p for p in projects if date_filter in p['date']]
    
    # Aplicar ordenamiento
    if sort_by == "Fecha (más reciente)":
        projects = sorted(projects, key=lambda x: x['date'], reverse=True)
    elif sort_by == "Fecha (más antiguo)":
        projects = sorted(projects, key=lambda x: x['date'])
    elif sort_by == "Título A-Z":
        projects = sorted(projects, key=lambda x: x['title'])
    
    # Mostrar proyectos
    if projects:
        for i,project in enumerate(projects):
            display_projects_card(project)
            if i < len(projects) - 1:
                st.markdown("---")
    else:
        st.write("NO se encontraron proyectos con los filtro seleccionados")

    # Estadísticas de proyectos
    if projects:
        st.markdown("---")
        st.header("📊 Estadísticas del Portfolio")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_projects= len(projects)
            st.metric("Total Proyectos Mostrados", total_projects)

        with col2:
            unique_tech = set()
            for p in projects:
                unique_tech.update(p['tech_stack'])
            st.metric("Tecnologías Únicas", len(unique_tech))
        
        with col3:
            with_demo =len([p for p in projects if p['demo_url']])
            st.metric("Proyectos con Demo", with_demo)
            
        with col4:
            github_projects = len([p for p in projects if p['github_url']])
            st.metric("Repositorio GitHub", github_projects)
        
def show_skills():
    """ Pagina de Habilidades"""
    st.header("🛠️ Habilidades y Competencias")
    
    # Gráfco de habilidades
    col1, col2 = st.columns([2,1])
    with col1:
        fig_skills = create_skill_chart()
        st.plotly_chart(fig_skills, use_container_width=True)
    
    with col2:
        st.subheader("💡 Competencias Clave")
        st.markdown("""
        **🔍 Análisis de Datos:**
        - Análisis Exploratorio (EDA)
        - Limpieza y Preparación
        - Estadística Descriptiva
        - Identificación de Patrones
        
        **📊 Visualización:**
        - Dashboards Interactivos
        - Storytelling con Datos
        - KPIs y Métricas
        - Reportes Ejecutivos
        
        **💻 Desarrollo:**
        - Aplicaciones Web
        - APIs y Integraciones
        - Automatización
        - Control de Versiones    
        """)
    
    # Certificaciones y formación
    st.markdown("---")
    st.subheader("🎓  Formación y Certificaciones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
         **📚 Formación Técnica:**
        - Data Science Specialization
        - Python para Análisis de Datos
        - Business Intelligence & Analytics  
        - Machine Learning Fundamentals
        - SQL para Data Analysis
        """)
        
    with col2: 
        st.markdown("""
        **🏆 Logros Destacados:**
        - 15+ proyectos públicos en GitHub
        - 8+ aplicaciones Streamlit desplegadas
        - Automatización con 94% reducción de tiempo
        - Análisis de 50K+ registros de datos
        - Portfolio técnico completo y documentado
        """)
        
    # Herramientas por categoría
    st.markdown("---")
    st.subheader("🛠️ Herramientas y Categoría")
    
    tools_data = {
        "Data Analysis": ["Python", "Pandas", "NumPy", "SciPy", "Jupyter"],
        "Visualization": ["Plotly", "Matplotlib", "Seaborn", "Altair", "Power BI"],
        "Web Development": ["Streamlit", "Flask", "HTML/CSS", "Bootstrap"],
        "Database": ["SQL", "SQLite", "MySQL", "PostgreSQL"],
        "ML & AI": ["Scikit-learn", "TensorFlow", "Keras", "XGBoost"],
        "Tools & Others": ["Git", "Docker", "APIs", "Excel", "n8n"]
    }
    
    cols = st.columns(3)
    for i, (category, tools) in enumerate(tools_data.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="skill-item">
                <h4>{category}</h4>
                <p>{' · '.join(tools)}</p>
            </div>
            """, unsafe_allow_html=True)
            
def show_about():
    """ Pagina de Sobre Mí"""
    st.header("👨‍💼 Sobre Mí")
    
    col1, col2  = st.columns([1,2])
    
    with col1:
        # Placeholder para foto profesional
        st.markdown("""
        <div style= 'text-aling:center; padding: 2rem; background: #262730; border-radius: 15px;'>
            <div style='font-size: 8rem;'>👨‍💻</div>
            <h3>Anderson Hernández</h3>
            <p style='color: #1f77b4; font-weight: 600;'>Data Analyst & Scientist</p>
            <p>📍 Madrid, España</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Intereses personales
        st.subheader("🎯 Intereses")
        st.markdown("""
        - 📚 Aprendizaje continuo
        - 🧩 Resolución de problemas
        - 📊 Visualización de datos
        - 🤖 Automatización
        - 🌐 Tecnologías emergentes                        
        """, unsafe_allow_html=True)
    
    with col2: 
        st.markdown("""
         ## 🚀 Mi Historia
        
        Soy un apasionado del análisis de datos con **experiencia práctica** desarrollando soluciones 
        que transforman información compleja en insights accionables para la toma de decisiones empresariales.
        
        ### 💼 Experiencia
        - **Portfolio activo** con 15+ proyectos de análisis de datos
        - **Especialización** en Python, Streamlit y visualización interactiva
        - **Enfoque práctico** resolviendo problemas reales de negocio
        - **Automatización** de procesos reduciendo tiempos manuales hasta 94%
        
        ### 🎯 Lo que me motiva
        - Descubrir patrones ocultos en los datos
        - Crear visualizaciones que cuenten historias
        - Automatizar procesos repetitivos
        - Convertir datos en ventajas competitivas
        
        ### 🔮 Objetivos
        Busco unirme a un equipo dinámico en Madrid donde pueda aplicar mis habilidades técnicas 
        para impulsar decisiones basadas en datos y contribuir al crecimiento empresarial.
        """)
        
        st.markdown("---")
        
        # Valores y Metodología
        col1,col2,col3 = st.columns(3)
        
        with col1:
            st.markdown(""""
            ### 🔍 Metodología
            - **Exploración profunda** de datos
            - **Validación** de hipótesis
            - **Iteración rápida** de prototipos
            - **Documentación** clara y completa
            - **Testing** y validación continua     
            """)
            
        with col2:
            st.markdown(""""
            ### 💡 Valores
            - **Excelencia técnica**
            - **Transparencia** analítica
            - **Ética** en el uso de datos
            - **Colaboración** multidisciplinar
            - **Innovación** constante
            """)
            
        with col3:
            st.markdown("""
            ### 🌐 Enfoque
            - **Soluciones centradas** en negocio
            - **Comunicación efectiva** de resultados
            - **Impacto medible** en KPIs
            - **Adaptabilidad** a nuevos retos
            - **Mejora continua** de procesos
            """)
        
        # Frase Inspiradora
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: #262730; border-radius: 15px;">
            <h3 style="color: #1f77b4;">"Transformo datos en decisiones, complejidad en claridad"</h3>
        </div>
        """, unsafe_allow_html=True)
        
def show_contact():
    """ Página de contacto"""
    st.header("📬 Contacto")
    
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.subheader("🌍 Información de Contacto")
        st.markdown("""
        **📧 Email:**  
        [anderson.ing.24@gmail.com](mailto:anderson.ing.24@gmail.com)
        
        **💼 LinkedIn:**  
        [linkedin.com/in/anderson-hern%C3%A1ndez-1681a82a3](https://www.linkedin.com/in/anderson-hern%C3%A1ndez-1681a82a3/)
        
        **💻 GitHub:**  
        [github.com/beyondAnalysIs](https://github.com/beyondAnalysIs)
        
        **📍 Ubicación:**  
        Madrid, España
        """)
        st.markdown("---")
        st.subheader("🕒 Disponibilidad")
        st.markdown("""
        - **Actualmente:** Buscando oportunidades
        - **Tipo de contrato:** Indefinido, freelance
        - **Modalidad:** Presencial, híbrido o remoto
        - **Inicio:** Inmediato
        """)
        
        with col2:
            st.subheader("""✉️ Envíame un Mensaje""")

            with st.form("contac_form"):
                name = st.text_input("Nombre completo")
                email = st.text_input("Email")
                subject = st.text_input("Asunto")
                message = st.text_area("Mensaje*", height=200)
                
                # Botón de envío
                submitted = st.form_submit_button("Enviar Mensaje")
                if submitted:
                    if not name or not email or not subject or not message:
                        st.error("Por favor completa todos los campos obligatorios (*)")
                    else:
                        # envío de mensaje
                        st.success("¡Mensaje enviado con éxito!")
                        st.balloons() 
                        st.info("Te responderé tan pronto como sea posible. Gracias por contactarme.")   

            st.markdown("---")
            st.subheader("📱  Redes Sociales")
            
            # botones de redes sociales
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <a href="https:/www.linkedin.com/in/anderson-hernández-1681a82a3" target="_blank" class="custom-button">
                    LinkedIn
                </a>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <a href="https://github.com/beyondAnalysIs" target="_blank" class="custom-button">
                    GitHub
                </a>
                """, unsafe_allow_html=True)
#==========================================
# FOOTER
#===========================================            
def footer():
    """ Mostrar footer en todas las páginas"""
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p>© 2025 Anderson Hernández | Data Analyst & Data Scientist</p>
        <p>
            Desarrollado con ❤️ usando Python, Streamlit y Plotly |
            <a href="https://github.com/beyondAnalysIs/portfolio" target="_blank">Código Fuente</a>
        </p>
    </div>               
    """, unsafe_allow_html=True)
    
#==========================================
# APLICACIÓN PRINCIPAL
#===========================================
def main():
    # Cargar CSS personalizado
    load_css()    
    # Barra de navegación horizontal
    with st.container():
        selected = option_menu(
            menu_title = None,
            options = ["Inicio", "Proyectos", "Habilidades", "Sobre Mí", "Contacto"],
            icons=["house", "folder", "tools", "person", "envelope"],
            menu_icon = "cast",
            default_index= 0,
            orientation= "horizontal",
            styles= {
                "container": {"padding": "0!important", "background-color": "#0e1117"},
                "icon": {"font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "center",
                    "margin": "0px",
                    "color": "#1f77b4",
                    "--hover-color": "#1e2130",
                },
                
                "nav-link-selected": {
                    "background-color": "#1f77b4",
                    "font-weight": "normal",
                    "color": "white",
                },
                
            }
        )
    
     # Mostrar página seleccionada
    if selected == 'Inicio':
        home_page()
    elif selected == 'Proyectos':
        show_projects()
    elif selected == 'Habilidades':
        show_skills()
    elif selected == 'Sobre Mí':
        show_about()
    elif selected == 'Contacto':
        show_contact()
        
     # Mostrar footer en todas las páginas
    footer()
    
if __name__ == "__main__":
    main()
