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
    page_title= "Anderson Hernández || Data Analyst & Scientist",
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
    col1, col2 = st.columns([1,2])
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
        """)
    
    with col2:
        st.header("🛠️ Stack Técnico")
        st.markdown("""
            **Lenguajes:**
            - 🐍 Python (Avanzado)
            - 📊 SQL (Intermedio)   
            
            **Líbrerias Principales:**
            - Pandas, NumPy, SciPy
            - Plotly, Matplotlib, Seaborn
            - Streamlit, Flask
            - Scikit-learn         

            **Herramientas:**
            - Git/GitHub
            - Excel Avanzado
            - Power BI
            - APIs REST
        """)
    
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
        [linkedin.com/in/anderson-hernandez](https://linkedin.com/in/anderson-hernandez)
        
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
                "icon": {"color": "#1f77b4", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "center",
                    "margin": "0px",
                    "color": "white",
                    "--hover-color": "#1e2130",
                },
                "nav-link-selected": {
                    "background-color": "#1f77b4",
                    "font-weight": "normal",
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
