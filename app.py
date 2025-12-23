import streamlit as st
import joblib
import pandas as pd

# Page config
st.set_page_config(page_title="CO2 Predictor", page_icon="🌍", layout="wide")

# Ultra minimal dark theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: #0a0e14;
    }
    .main {
        padding: 1.5rem 2rem !important;
        max-width: 1300px;
        margin: 0 auto;
    }
    
    /* Minimal Header */
    .header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .title {
        color: #ffffff;
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Clean input cards */
    .input-card {
        background: #151b23;
        border: 1px solid #1f2937;
        border-radius: 16px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    .input-card:hover {
        border-color: #374151;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }
    
    .card-title {
        color: #10b981;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }
    
    label {
        color: #9ca3af !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
    }
    
    /* Clean inputs */
    div[data-baseweb="select"] > div {
        background-color: #0a0e14 !important;
        border: 1px solid #1f2937 !important;
        color: #e5e7eb !important;
        border-radius: 10px !important;
        transition: all 0.2s ease !important;
    }
    div[data-baseweb="select"] > div:hover {
        border-color: #10b981 !important;
    }
    
    input {
        background-color: #0a0e14 !important;
        border: 1px solid #1f2937 !important;
        color: #e5e7eb !important;
        border-radius: 10px !important;
        transition: all 0.2s ease !important;
    }
    input:hover {
        border-color: #10b981 !important;
    }
    
    /* Minimal button */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: #ffffff;
        font-size: 0.95rem;
        font-weight: 600;
        padding: 0.9rem 2rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 16px rgba(16, 185, 129, 0.25);
        width: 100%;
        margin-top: 1.5rem;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.4);
    }
    
    /* Beautiful result */
    .result-container {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 16px 48px rgba(16, 185, 129, 0.2);
        margin: 2rem 0 1.5rem 0;
        position: relative;
        overflow: hidden;
    }
    .result-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(52, 211, 153, 0.1) 0%, transparent 70%);
        animation: pulse 3s ease-in-out infinite;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    .result-label {
        font-size: 0.85rem;
        color: #6ee7b7;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
        position: relative;
        z-index: 1;
    }
    .result-value {
        font-size: 3.5rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -2px;
        position: relative;
        z-index: 1;
    }
    .result-unit {
        font-size: 1.2rem;
        color: #a7f3d0;
        font-weight: 600;
        margin-left: 0.5rem;
    }
    
    /* Elegant metrics */
    .metrics-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin-top: 1.5rem;
    }
    .metric {
        background: #151b23;
        border: 1px solid #1f2937;
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric:hover {
        border-color: #10b981;
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.3rem;
    }
    .metric-label {
        font-size: 0.7rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 500;
    }
    
    /* Responsive spacing */
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Load model
try:
    model = joblib.load("co2_pipeline.pkl")
except:
    st.error("Model not found")
    st.stop()

# Header
st.markdown("""
<div class="header">
    <h1 class="title">CO2 EMISSION PREDICTOR</h1>
    <p class="subtitle">Analyze your vehicle's carbon footprint</p>
</div>
""", unsafe_allow_html=True)

# Input grid
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown('<div class="input-card"><div class="card-title">Vehicle</div>', unsafe_allow_html=True)
    Make = st.selectbox("Make", ['ACURA', 'ALFA ROMEO', 'ASTON MARTIN', 'AUDI', 'BENTLEY', 'BMW',
       'BUICK', 'CADILLAC', 'CHEVROLET', 'CHRYSLER', 'DODGE', 'FIAT',
       'FORD', 'GMC', 'HONDA', 'HYUNDAI', 'INFINITI', 'JAGUAR', 'JEEP',
       'KIA', 'LAMBORGHINI', 'LAND ROVER', 'LEXUS', 'LINCOLN', 'MASERATI',
       'MAZDA', 'MERCEDES-BENZ', 'MINI', 'MITSUBISHI', 'NISSAN',
       'PORSCHE', 'RAM', 'ROLLS-ROYCE', 'SCION', 'SMART', 'SRT', 'SUBARU',
       'TOYOTA', 'VOLKSWAGEN', 'VOLVO', 'GENESIS', 'BUGATTI'], label_visibility="visible")
    Vehicle_Class = st.selectbox("Class", ['COMPACT', 'SUV - SMALL', 'MID-SIZE', 'TWO-SEATER', 'MINICOMPACT',
       'SUBCOMPACT', 'FULL-SIZE', 'STATION WAGON - SMALL',
       'SUV - STANDARD', 'VAN - CARGO', 'VAN - PASSENGER',
       'PICKUP TRUCK - STANDARD', 'MINIVAN', 'SPECIAL PURPOSE VEHICLE',
       'STATION WAGON - MID-SIZE', 'PICKUP TRUCK - SMALL'])
    Transmission = st.selectbox("Transmission",['AS5', 'M6', 'AV7', 'AS6', 'AM6', 'A6', 'AM7', 'AV8', 'AS8', 'A7',
       'A8', 'M7', 'A4', 'M5', 'AV', 'A5', 'AS7', 'A9', 'AS9', 'AV6',
       'AS4', 'AM5', 'AM8', 'AM9', 'AS10', 'A10', 'AV10'])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-card"><div class="card-title">Engine</div>', unsafe_allow_html=True)
    Engine_Size = st.number_input("Size (L)", 0.0, 10.0, step=0.1)
    Cylinders = st.number_input("Cylinders", 0, 16, step=1)
    Fuel_Type = st.selectbox("Fuel Type", ['Z - Premium', 'X - Regular', 'D - Diesel', 'E - Ethanol', 'N - Natural Gas'])
    Fuel_Type = Fuel_Type[0]
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="input-card"><div class="card-title">Consumption</div>', unsafe_allow_html=True)
    Fuel_Consumption_City = st.number_input("City (L/100km)", 0.0, 50.0, step=0.5)
    Fuel_Consumption_Hwy = st.number_input("Highway (L/100km)", 0.0, 50.0, step=0.5)
    Fuel_Consumption_Comb = st.number_input("Combined (L/100km)", 0.0, 50.0, step=0.5)
    st.markdown('</div>', unsafe_allow_html=True)

Fuel_Consumption_Comb_MPG = 235.214 / Fuel_Consumption_Comb if Fuel_Consumption_Comb > 0 else 0.0

# Predict
if st.button("Analyze Emission"):
    input_df = pd.DataFrame([{
        "Make": Make,
        "Vehicle Class": Vehicle_Class,
        "Engine Size(L)": Engine_Size,
        "Cylinders": Cylinders,
        "Transmission": Transmission,
        "Fuel Type": Fuel_Type,
        "Fuel Consumption City (L/100 km)": Fuel_Consumption_City,
        "Fuel Consumption Hwy (L/100 km)": Fuel_Consumption_Hwy,
        "Fuel Consumption Comb (L/100 km)": Fuel_Consumption_Comb,
        "Fuel Consumption Comb (mpg)": Fuel_Consumption_Comb_MPG
    }])
    
    try:
        result = model.predict(input_df)[0]
        
        # Result
        st.markdown(f"""
        <div class="result-container">
            <div class="result-label">Predicted Emission</div>
            <div class="result-value">{result:.1f}<span class="result-unit">g/km</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Metrics
        annual = (result * 15000) / 1000
        
        if result < 200:
            category, color = "Low", "#10b981"
        elif result < 250:
            category, color = "Medium", "#f59e0b"
        else:
            category, color = "High", "#ef4444"
        
        col_a, col_b, col_c = st.columns(3)
        
        metrics = [
            (f"{result:.0f}g", "Per KM", col_a),
            (f"{annual:.1f}kg", "Yearly", col_b),
            (category, "Level", col_c)
        ]
        
        for value, label, col in metrics:
            with col:
                color_style = f'style="color: {color}"' if label == "Level" else ""
                st.markdown(f"""
                <div class="metric">
                    <div class="metric-value" {color_style}>{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")