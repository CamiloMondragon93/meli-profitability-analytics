import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Analizador de Rentabilidad ML",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Analizador de Rentabilidad para Vendedores")
st.markdown("""
**Calcula tu rentabilidad real en Mercado Libre**
1. 📋 Ingresa los datos que ves en tu panel de ML
2. ✏️ Ajusta tus costos (proveedor, envío, embalaje)
3. 📈 Ve tu ganancia en tiempo real
""")
st.divider()

# ==========================================
# 1. INFORMACIÓN DEL PRODUCTO
# ==========================================

st.header("📋 1. Datos del Producto")

col_prod1, col_prod2 = st.columns(2)

with col_prod1:
    nombre_producto = st.text_input(
        "📝 Nombre del producto",
        value="Soporte Celular Pro",
        help="Escribe el nombre de tu producto"
    )

with col_prod2:
    categoria = st.text_input(
        "📂 Categoría",
        value="Electrónicos",
        help="Ej: Electrónicos, Ropa, Hogar, etc."
    )

st.divider()

# ==========================================
# 2. DATOS DE MERCADO LIBRE (INGRESADOS POR EL USUARIO)
# ==========================================

st.header("📊 2. Datos de Mercado Libre (ingresa lo que ves en tu panel)")

st.info("💡 **Abre tu panel de ventas en Mercado Libre y copia estos valores exactos**")

col_ml1, col_ml2 = st.columns(2)

with col_ml1:
    st.subheader("💰 Precio y Comisiones")
    
    precio_ml = st.number_input(
        "Precio de publicación ($)",
        min_value=0.0,
        value=21900.0,
        step=100.0,
        help="El precio al que publicaste el producto en ML",
        key="precio_ml"
    )
    
    comision_ml = st.number_input(
        "Comisión de ML ($)",
        min_value=0.0,
        value=4161.0,
        step=100.0,
        help="Lo que ML te cobra por la venta (lo ves en el detalle de tu venta)",
        key="comision_ml"
    )
    
    costo_fijo_ml = st.number_input(
        "Costo fijo de ML ($)",
        min_value=0.0,
        value=0.0,
        step=50.0,
        help="Cargos fijos adicionales de ML (si los hay)",
        key="costo_fijo_ml"
    )

with col_ml2:
    st.subheader("🧾 Impuestos y Retenciones")
    
    retencion_iva = st.number_input(
        "Retención IVA ($)",
        min_value=0.0,
        value=419.0,
        step=50.0,
        help="Lo que ML retiene por IVA (lo ves en el detalle)",
        key="retencion_iva"
    )
    
    retencion_ganancias = st.number_input(
        "Retención Ganancias ($)",
        min_value=0.0,
        value=0.0,
        step=50.0,
        help="Retención de impuesto a las ganancias (si aplica)",
        key="retencion_ganancias"
    )
    
    otros_costos_ml = st.number_input(
        "Otros costos de ML ($)",
        min_value=0.0,
        value=0.0,
        step=50.0,
        help="Cualquier otro cargo que veas en tu panel",
        key="otros_costos_ml"
    )

# Calcular total de costos ML
total_costos_ml = comision_ml + costo_fijo_ml + retencion_iva + retencion_ganancias + otros_costos_ml

st.caption(f"💰 **Total costos de Mercado Libre:** ${total_costos_ml:,.0f}")

st.divider()

# ==========================================
# 3. TUS COSTOS (EDITABLES POR EL USUARIO)
# ==========================================

st.header("✏️ 3. Tus Costos (los que tú controlas)")

with st.container():
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border: 2px solid #4CAF50;">
    <p style="color: #2E7D32; font-weight: bold;">🖊️ Estos valores dependen de ti, ¡ajústalos libremente!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_edit1, col_edit2 = st.columns(2)
    
    with col_edit1:
        st.markdown("**🏭 Costo de Compra**")
        costo_proveedor = st.number_input(
            "Lo que pagas al proveedor ($)",
            min_value=0.0,
            value=4000.0,
            step=100.0,
            help="💡 Buscar un mejor proveedor aumenta tu ganancia",
            key="costo_proveedor",
            label_visibility="collapsed"
        )
        st.caption("💡 ¿Puedes conseguir un mejor precio?")
        
        st.markdown("**🚚 Costo de Envío**")
        costo_envio = st.number_input(
            "Costo de envío a tu cargo ($)",
            min_value=0.0,
            value=8000.0,
            step=500.0,
            help="💡 Negocia con tu mensajería para reducirlo",
            key="costo_envio",
            label_visibility="collapsed"
        )
        st.caption("💡 ¿Puedes optimizar tus envíos?")
    
    with col_edit2:
        st.markdown("**📦 Embalaje y otros**")
        gastos_adicionales = st.number_input(
            "Embalaje, etiquetas, etc. ($)",
            min_value=0.0,
            value=500.0,
            step=50.0,
            help="💡 Compra materiales al por mayor",
            key="gastos_adicionales",
            label_visibility="collapsed"
        )
        st.caption("💡 Revisa si puedes reducir estos gastos")
        
        st.markdown("**📦 Otros costos tuyos**")
        otros_costos_usuario = st.number_input(
            "Otros costos que tengas ($)",
            min_value=0.0,
            value=0.0,
            step=50.0,
            help="💡 Publicidad, almacenamiento, etc.",
            key="otros_costos_usuario",
            label_visibility="collapsed"
        )
        st.caption("💡 Incluye cualquier otro gasto")

# Calcular total de costos usuario
total_costos_usuario = costo_proveedor + costo_envio + gastos_adicionales + otros_costos_usuario

st.divider()

# ==========================================
# 4. CÁLCULO DE RENTABILIDAD
# ==========================================

st.header("📊 4. Resultados en Tiempo Real")

# --- Calcular todo ---
payout_ml = precio_ml - total_costos_ml  # Lo que realmente te paga ML
costo_total = total_costos_ml + total_costos_usuario
ganancia_neta = precio_ml - costo_total
margen = (ganancia_neta / precio_ml * 100) if precio_ml > 0 else 0

# --- Métricas principales ---
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.metric("💰 Precio Venta", f"${precio_ml:,.0f}")

with col_m2:
    st.metric("💵 Pago Neto (Payout)", f"${payout_ml:,.0f}", 
              help=f"Total costos ML: ${total_costos_ml:,.0f}")

with col_m3:
    st.metric("✅ Ganancia Neta", f"${ganancia_neta:,.0f}", 
              delta=f"{margen:.1f}% margen")

with col_m4:
    st.metric("📈 Margen Neto", f"{margen:.1f}%")

# --- Alerta ---
if ganancia_neta > 0:
    if margen >= 15:
        st.success(f"🟢 **¡Excelente!** Ganancia de ${ganancia_neta:,.0f} por unidad. ¡Sigue así!")
    elif margen >= 5:
        st.warning(f"🟡 **Rentabilidad ajustada.** Ganancia de ${ganancia_neta:,.0f} por unidad. Busca optimizar.")
    else:
        st.warning(f"🟠 **Margen bajo.** Ganancia de ${ganancia_neta:,.0f} por unidad. Considera ajustar precios.")
else:
    st.error(f"🔴 **¡ALERTA!** Estás perdiendo ${abs(ganancia_neta):,.0f} por unidad. ¡Revisa tus costos!")

st.divider()

# ==========================================
# 5. DESGLOSE DETALLADO
# ==========================================

st.subheader("📋 Desglose Detallado")

# Crear tabla de desglose
desglose = pd.DataFrame({
    "Concepto": [
        "💰 Precio de Venta",
        "📊 Comisión ML",
        "📋 Costo Fijo ML",
        "🧾 Retención IVA",
        "🧾 Retención Ganancias",
        "📋 Otros Costos ML",
        "🏭 Costo Proveedor",
        "🚚 Costo Envío",
        "📦 Embalaje y otros",
        "📦 Otros Costos Tuyos",
        "✅ GANANCIA NETA"
    ],
    "Valor": [
        precio_ml,
        -comision_ml,
        -costo_fijo_ml,
        -retencion_iva,
        -retencion_ganancias,
        -otros_costos_ml,
        -costo_proveedor,
        -costo_envio,
        -gastos_adicionales,
        -otros_costos_usuario,
        ganancia_neta
    ],
    "Tipo": [
        "Ingreso",
        "Costo ML",
        "Costo ML",
        "Costo ML",
        "Costo ML",
        "Costo ML",
        "Costo Usuario",
        "Costo Usuario",
        "Costo Usuario",
        "Costo Usuario",
        "Resultado"
    ]
})

def colorear(valor):
    if isinstance(valor, (int, float)):
        if valor > 0 and valor == desglose['Valor'].max():
            return 'background-color: #d4edda; color: #155724; font-weight: bold'
        elif valor < 0:
            return 'background-color: #f8d7da; color: #721c24'
    return ''

st.dataframe(
    desglose.style.map(colorear, subset=['Valor']).format({'Valor': '${:,.0f}'}),
    hide_index=True,
    use_container_width=True
)

# --- Resumen visual de costos ---
st.subheader("📊 Distribución de Costos")

col_resumen1, col_resumen2, col_resumen3 = st.columns(3)

with col_resumen1:
    st.metric("Costos ML", f"${total_costos_ml:,.0f}", 
              help="Comisiones, impuestos y otros cargos de ML")

with col_resumen2:
    st.metric("Tus Costos", f"${total_costos_usuario:,.0f}", 
              help="Proveedor, envío, embalaje y otros")

with col_resumen3:
    porcentaje_ml = (total_costos_ml / costo_total * 100) if costo_total > 0 else 0
    porcentaje_user = (total_costos_usuario / costo_total * 100) if costo_total > 0 else 0
    st.metric("Distribución", f"ML: {porcentaje_ml:.0f}% | Tú: {porcentaje_user:.0f}%")

st.divider()

# ==========================================
# 6. RECOMENDACIONES PERSONALIZADAS
# ==========================================

st.header("💡 Recomendaciones")

# Análisis de costos
if ganancia_neta > 0:
    if margen >= 15:
        st.markdown("""
        ### ✅ Excelente rentabilidad
        
        **Para mantenerla:**
        - ✅ Monitorea que tus proveedores no suban precios
        - ✅ Revisa periódicamente los costos de envío
        - ✅ Considera expandir tu línea de productos similares
        - ✅ Aprovecha tu buen margen para promocionar el producto
        """)
    elif margen >= 5:
        st.markdown("""
        ### 📈 Rentabilidad aceptable, pero mejorable
        
        **Para mejorar tu margen:**
        1. 📉 **Busca un proveedor más económico** (reduce costo de compra)
        2. 📦 **Negocia mejores tarifas de envío** con tu mensajería
        3. 💰 **Compra insumos al por mayor** para reducir embalaje
        4. 💡 **Prueba subir ligeramente el precio** (si el mercado lo permite)
        
        **Objetivo:** Llegar al 15% de margen
        """)
    else:
        st.markdown("""
        ### ⚠️ Margen bajo, necesitas actuar
        
        **Acciones recomendadas:**
        1. 🔍 **Revisa tus costos de proveedor** - ¿Puedes encontrar uno mejor?
        2. 📦 **Optimiza tus envíos** - ¿Vale la pena cambiar de mensajería?
        3. 💰 **Reduce gastos de embalaje** - ¿Puedes comprar al por mayor?
        4. 📈 **Ajusta el precio** - Prueba aumentarlo ligeramente
        5. 🔄 **¿Vale la pena este producto?** - Considera descontinuarlo si no mejora
        """)
else:
    st.markdown("""
    ### 🚨 ¡ALERTA ROJA! Estás operando a pérdida
    
    **Acciones urgentes necesarias:**
    
    1. 📈 **AUMENTA EL PRECIO** (si la competencia lo permite)
    2. 🏭 **BUSCA OTRO PROVEEDOR** - Necesitas reducir el costo de compra
    3. 🚚 **OPTIMIZA TUS ENVÍOS** - Consolida pedidos, cambia de mensajería
    4. 📦 **REDUCE COSTOS DE EMBALAJE** - Compra al por mayor, busca alternativas
    5. 📊 **ANALIZA LA COMPETENCIA** - ¿Cómo logran ellos ser rentables?
    6. ❓ **CONSIDERA DESCONTINUAR** - Si no puedes mejorar, mejor retirar el producto
    
    **⚠️ No ignores este problema. Cada venta te está costando dinero.**
    """)

st.divider()

# ==========================================
# 7. GUARDAR Y EXPORTAR
# ==========================================

st.header("💾 Guardar y Exportar")

col_g1, col_g2 = st.columns(2)

with col_g1:
    if st.button("💾 Guardar Análisis", use_container_width=True):
        if 'historial' not in st.session_state:
            st.session_state.historial = []
        
        registro = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "producto": nombre_producto,
            "precio_venta": precio_ml,
            "comision_ml": comision_ml,
            "costo_proveedor": costo_proveedor,
            "costo_envio": costo_envio,
            "gastos_adicionales": gastos_adicionales,
            "costos_ml": total_costos_ml,
            "costos_usuario": total_costos_usuario,
            "costo_total": costo_total,
            "ganancia_neta": ganancia_neta,
            "margen": margen
        }
        st.session_state.historial.append(registro)
        st.success("✅ Análisis guardado correctamente")

with col_g2:
    if st.button("📊 Ver Historial", use_container_width=True):
        if 'historial' in st.session_state and st.session_state.historial:
            df_historial = pd.DataFrame(st.session_state.historial)
            st.dataframe(df_historial)
        else:
            st.info("Aún no hay análisis guardados")

# --- Exportar ---
st.subheader("📥 Exportar Datos")

col_export1, col_export2 = st.columns(2)

with col_export1:
    if st.button("📥 Descargar Análisis en CSV", use_container_width=True):
        datos_exportar = {
            "Producto": nombre_producto,
            "Categoría": categoria,
            "Precio Venta": precio_ml,
            "Comisión ML": comision_ml,
            "Costo Fijo ML": costo_fijo_ml,
            "Retención IVA": retencion_iva,
            "Retención Ganancias": retencion_ganancias,
            "Otros Costos ML": otros_costos_ml,
            "Costo Proveedor": costo_proveedor,
            "Costo Envío": costo_envio,
            "Gastos Adicionales": gastos_adicionales,
            "Otros Costos": otros_costos_usuario,
            "Total Costos ML": total_costos_ml,
            "Total Costos Usuario": total_costos_usuario,
            "Costo Total": costo_total,
            "Pago Neto (Payout)": payout_ml,
            "Ganancia Neta": ganancia_neta,
            "Margen %": margen
        }
        df_export = pd.DataFrame([datos_exportar])
        csv = df_export.to_csv(index=False)
        st.download_button(
            label="📥 Descargar CSV",
            data=csv,
            file_name=f"analisis_{nombre_producto.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True,
            key="descargar_csv"
        )

with col_export2:
    # Ver historial completo en tabla
    if st.button("📊 Ver Análisis Completos", use_container_width=True):
        if 'historial' in st.session_state and st.session_state.historial:
            df_historial = pd.DataFrame(st.session_state.historial)
            st.dataframe(df_historial, use_container_width=True)
            
            # Botón para descargar historial
            csv_historial = df_historial.to_csv(index=False)
            st.download_button(
                label="📥 Descargar Historial CSV",
                data=csv_historial,
                file_name=f"historial_analisis_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True,
                key="descargar_historial"
            )
        else:
            st.info("Aún no hay análisis guardados")

st.caption("💡 *Todos los cálculos se actualizan en tiempo real al cambiar cualquier valor.*")
st.caption("📋 *Ingresa los datos exactos que ves en tu panel de Mercado Libre para obtener resultados precisos.*")