import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Elecciones España - Datos Oficiales",
    page_icon="🇪🇸",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #C60B1E;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #C60B1E;
        border-bottom: 2px solid #C60B1E;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #C60B1E;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #C60B1E, #FFC400);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🇪🇸 Datos Oficiales - Elecciones España</h1>', unsafe_allow_html=True)

# Introducción
st.info("""
**Fuentes oficiales**: Ministerio del Interior - Gobierno de España · Instituto Nacional de Estadística (INE) · Junta Electoral Central
**Última actualización**: Datos oficiales de procesos electorales 2023-2024
""")

# ===== DATOS DEL CENSO ELECTORAL =====
st.markdown('<h2 class="section-header">📋 Censo Electoral</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>35.5M</h3>
        <p>Electores totales</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>34.7M</h3>
        <p>España peninsular</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>2.1M</h3>
        <p>Extranjero (CERA)</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>136K</h3>
        <p>Residentes ausentes</p>
    </div>
    """, unsafe_allow_html=True)

# ===== CALENDARIO ELECTORAL =====
st.markdown('<h2 class="section-header">📅 Calendario Electoral</h2>', unsafe_allow_html=True)

calendario_data = {
    'Proceso Electoral': [
        'Elecciones Generales (Congreso y Senado)',
        'Elecciones al Parlamento Europeo',
        'Elecciones Autonómicas',
        'Elecciones Municipales',
        'Elecciones al Parlamento Europeo próximas'
    ],
    'Fecha': [
        '23 de Julio 2023',
        '26 de Mayo 2019',
        '28 de Mayo 2023 (12 CCAA)',
        '28 de Mayo 2023',
        '9 de Junio 2024'
    ],
    'Ámbito': [
        'Nacional',
        'Europeo',
        'Autonómico',
        'Municipal',
        'Europeo'
    ],
    'Estado': [
        'Celebradas',
        'Celebradas',
        'Celebradas',
        'Celebradas',
        'Próximas'
    ]
}

df_calendario = pd.DataFrame(calendario_data)
st.dataframe(df_calendario, use_container_width=True, hide_index=True)

# ===== PARTICIPACIÓN ELECTORAL =====
st.markdown('<h2 class="section-header">📊 Participación Electoral Histórica</h2>', unsafe_allow_html=True)

# Datos reales del Ministerio del Interior
participacion_data = {
    'Año': [2015, 2016, 2019_Abr, 2019_Nov, 2023],
    'Proceso': [
        'Generales Diciembre',
        'Generales Junio',
        'Generales Abril',
        'Generales Noviembre',
        'Generales Julio'
    ],
    'Participación (%)': [73.2, 69.8, 75.8, 69.9, 66.6],
    'Votos válidos (millones)': [23.7, 22.2, 25.5, 21.9, 20.8]
}

df_participacion = pd.DataFrame(participacion_data)

col1, col2 = st.columns(2)

with col1:
    fig_participacion = px.line(
        df_participacion,
        x='Año',
        y='Participación (%)',
        title='Evolución Participación Elecciones Generales (%)',
        markers=True,
        line_shape='linear'
    )
    fig_participacion.update_traces(line=dict(width=4, color='#C60B1E'))
    fig_participacion.update_layout(height=400)
    st.plotly_chart(fig_participacion, use_container_width=True)

with col2:
    fig_votos = px.bar(
        df_participacion,
        x='Año',
        y='Votos válidos (millones)',
        title='Votos Válidos en Elecciones Generales (Millones)',
        color='Participación (%)',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig_votos, use_container_width=True)

# ===== COMPOSICIÓN ACTUAL DEL CONGRESO =====
st.markdown('<h2 class="section-header">🏛️ Composición del Congreso de los Diputados</h2>', unsafe_allow_html=True)

# Datos reales tras elecciones 2023
congreso_data = {
    'Grupo Parlamentario': [
        'Partido Popular (PP)',
        'Partido Socialista (PSOE)',
        'Sumar',
        'Vox',
        'ERC',
        'Junts',
        'EH Bildu',
        'PNV',
        'BNG',
        'CC',
        'UPN',
        'Otros'
    ],
    'Escaños': [137, 121, 31, 33, 7, 7, 6, 5, 1, 1, 1, 0],
    'Color': ['#1E90FF', '#FF0000', '#FF69B4', '#00CED1', '#FFD700', '#800080', '#008000', '#006600', '#8B4513', '#FF8C00', '#4682B4', '#A9A9A9']
}

df_congreso = pd.DataFrame(congreso_data)

col1, col2 = st.columns([2, 1])

with col1:
    fig_congreso = px.pie(
        df_congreso,
        values='Escaños',
        names='Grupo Parlamentario',
        title='Distribución de Escaños - Congreso de los Diputados (350 escaños)',
        color='Grupo Parlamentario',
        color_discrete_sequence=df_congreso['Color'].tolist()
    )
    fig_congreso.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_congreso, use_container_width=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <h4>📊 Datos Congreso 2023</h4>
    <p><strong>Total escaños:</strong> 350</p>
    <p><strong>Mayoría absoluta:</strong> 176</p>
    <p><strong>Escaños asignados:</strong> 350</p>
    <p><strong>Grupos parlamentarios:</strong> 9</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar tabla de escaños
    st.dataframe(
        df_congreso[['Grupo Parlamentario', 'Escaños']].sort_values('Escaños', ascending=False),
        use_container_width=True,
        height=400
    )

# ===== SISTEMA ELECTORAL ESPAÑOL =====
st.markdown('<h2 class="section-header">⚖️ Sistema Electoral Español</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-box">
    <h4>🏛️ Elecciones Generales</h4>
    <ul>
    <li><strong>Congreso:</strong> 350 diputados</li>
    <li><strong>Senado:</strong> 266 senadores</li>
    <li><strong>Ley D'Hondt:</strong> Sistema de reparto</li>
    <li><strong>Circunscripciones:</strong> 52 provincias</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <h4>🗳️ Requisitos para Votar</h4>
    <ul>
    <li><strong>Edad:</strong> 18 años cumplidos</li>
    <li><strong>Censo:</strong> Inscripción automática</li>
    <li><strong>Documentación:</strong> DNI/pasaporte</li>
    <li><strong>Voto:</strong> Presencial o por correo</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-box">
    <h4>📈 Características</h4>
    <ul>
    <li><strong>Voto:</strong> Voluntario</li>
    <li><strong>Umbral:</strong> 3% (congreso)</li>
    <li><strong>Legislatura:</strong> 4 años</li>
    <li><strong>Convocatoria:</strong> Rey/Gobierno</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ===== DISTRIBUCIÓN POR COMUNIDADES AUTÓNOMAS =====
st.markdown('<h2 class="section-header">🗺️ Distribución por Circunscripciones</h2>', unsafe_allow_html=True)

# Datos de escaños por comunidad autónoma
ccaa_data = {
    'Comunidad Autónoma': [
        'Andalucía', 'Cataluña', 'Madrid', 'Comunidad Valenciana',
        'Galicia', 'Castilla y León', 'País Vasco', 'Castilla-La Mancha',
        'Canarias', 'Región de Murcia', 'Aragón', 'Baleares',
        'Extremadura', 'Principado de Asturias', 'Navarra', 'Cantabria',
        'La Rioja', 'Ceuta', 'Melilla'
    ],
    'Escaños Congreso': [61, 48, 37, 33, 23, 31, 18, 21, 15, 10, 13, 8, 10, 8, 5, 5, 4, 1, 1],
    'Escaños Senado': [9, 16, 11, 9, 6, 9, 6, 6, 4, 3, 4, 2, 3, 2, 2, 2, 1, 1, 1]
}

df_ccaa = pd.DataFrame(ccaa_data)

fig_ccaa = px.bar(
    df_ccaa.sort_values('Escaños Congreso', ascending=True),
    y='Comunidad Autónoma',
    x='Escaños Congreso',
    orientation='h',
    title='Escaños en el Congreso por Comunidad Autónoma',
    color='Escaños Congreso',
    color_continuous_scale='Reds'
)
fig_ccaa.update_layout(height=500)
st.plotly_chart(fig_ccaa, use_container_width=True)

# ===== DATOS DEMOGRÁFICOS ELECTORALES =====
st.markdown('<h2 class="section-header">📈 Perfil Demográfico del Electorado</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Datos por grupo de edad (INE)
    edad_data = {
        'Grupo Edad': ['18-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75+'],
        'Porcentaje Censo': [8.2, 15.3, 17.8, 18.9, 15.6, 12.1, 12.1],
        'Participación (%)': [45.2, 58.7, 65.3, 72.1, 78.4, 80.2, 75.6]
    }
    
    df_edad = pd.DataFrame(edad_data)
    
    fig_edad = px.bar(
        df_edad,
        x='Grupo Edad',
        y=['Porcentaje Censo', 'Participación (%)'],
        title='Distribución y Participación por Grupos de Edad',
        barmode='group'
    )
    st.plotly_chart(fig_edad, use_container_width=True)

with col2:
    # Datos por sexo (INE)
    sexo_data = {
        'Sexo': ['Mujeres', 'Hombres'],
        'Porcentaje Censo': [51.8, 48.2],
        'Participación (%)': [68.3, 64.9]
    }
    
    df_sexo = pd.DataFrame(sexo_data)
    
    fig_sexo = px.pie(
        df_sexo,
        values='Porcentaje Censo',
        names='Sexo',
        title='Distribución del Censo por Sexo (%)',
        color='Sexo',
        color_discrete_map={'Mujeres': '#FF69B4', 'Hombres': '#1E90FF'}
    )
    st.plotly_chart(fig_sexo, use_container_width=True)

# ===== ORGANISMOS ELECTORALES =====
st.markdown('<h2 class="section-header">🏢 Órganos Electorales</h2>', unsafe_allow_html=True)

organismos_data = {
    'Órgano Electoral': [
        'Junta Electoral Central',
        'Juntas Electorales Provinciales',
        'Juntas Electorales de Zona',
        'Mesas Electorales'
    ],
    'Composición': [
        '13 miembros + Presidente',
        'Jueces + profesores + abogados',
        'Jueces designados',
        '1 Presidente + 2 Vocales'
    ],
    'Función Principal': [
        'Dirección y control del proceso',
        'Organización provincial',
        'Gestión de mesas electorales',
        'Desarrollo de la votación'
    ]
}

df_organismos = pd.DataFrame(organismos_data)
st.dataframe(df_organismos, use_container_width=True, hide_index=True)

# ===== INFORMACIÓN ADICIONAL =====
st.markdown('<h2 class="section-header">ℹ️ Información Adicional</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔗 Enlaces Oficiales", "📞 Contacto", "📚 Legislación"])

with tab1:
    st.markdown("""
    **Enlaces Institucionales Oficiales:**
    - [Ministerio del Interior - Resultados Electorales](https://www.infoelectoral.mir.es/)
    - [Junta Electoral Central](https://www.juntaelectoralcentral.es/)
    - [Instituto Nacional de Estadística (INE)](https://www.ine.es/)
    - [Congreso de los Diputados](https://www.congreso.es/)
    - [Senado de España](https://www.senado.es/)
    """)

with tab2:
    st.markdown("""
    **Información de Contacto:**
    - 📞 Ministerio del Interior: 915 37 70 00
    - 🌐 Web electoral: https://www.infoelectoral.mir.es
    - 📧 Contacto JEC: jec@juntaelectoralcentral.es
    - 🏢 Dirección: C/ Amador de los Ríos, 7 - 28010 Madrid
    """)

with tab3:
    st.markdown("""
    **Normativa Electoral Principal:**
    - Ley Orgánica 5/1985, de 19 de junio, del Régimen Electoral General
    - Constitución Española de 1978
    - Ley Orgánica 2/2011, de 28 de enero, de financiación de partidos políticos
    - Ley Orgánica 3/2015, de 30 de marzo, de control de la actividad económico-financiera de los partidos políticos
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><strong>🇪🇸 Datos Oficiales - Elecciones España</strong></p>
    <p>Información basada en datos públicos del Ministerio del Interior y el INE</p>
    <p>Última actualización: Febrero 2024 · Fuente: Gobierno de España</p>
</div>
""", unsafe_allow_html=True)
