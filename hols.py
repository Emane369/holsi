import streamlit as st

# Título
st.title("Recomendación de Producción de Cemento")
st.write("Basado en inventario diario y KPIs de demanda.")

# Tipos de cemento y KPIs fijos
cementos = {
    'ECPC30': 1300,
    'ECPC3025': 300,
    'EO-MM': 800,
    'EO-MM25': 300,
    'BB': 240
}

st.header("📦 Ingreso de Inventario Diario")
inventario = {}
for tipo, kpi in cementos.items():
    valor = st.number_input(f"{tipo} (KPI: {kpi})", min_value=0, value=0, step=10)
    inventario[tipo] = valor

# Procesamiento de prioridad
st.header("📊 Recomendación de Producción")
if st.button("Calcular"):
    recomendaciones = {}
    for tipo in cementos:
        prioridad = max(cementos[tipo] - inventario[tipo], 0)
        recomendaciones[tipo] = prioridad

    # Ordenar por prioridad
    ordenado = sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)
    for tipo, prioridad in ordenado:
        st.write(f"🔹 **{tipo}**: Prioridad de producción = {prioridad} unidades")
