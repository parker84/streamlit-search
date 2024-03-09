import os

# Names for Streamlit app pages
page_names = [
    "🌌 Holodeck_Adventures",
    "🚀 Warp_Map_Expedition",
    "📊 Data_Log_Analysis",
    "🎶 Sonic_Visualizations",
    "🌠 Galactic_Exploration",
    "🪄 Quantum_Data_Magic",
    "🔍 Insights_Nebula_Explorer",
    "📈 Star_Charts_Fiesta",
    "⚔️ Graph_Commander",
    "📉 Astro_Data_Analysis",
    "📈 Trend_Captaincy",
    "🌌 Market_Quasar_Research",
    "🪐 Cosmic_Data_Exploration",
    "📝 Reports_Log",
    "📡 Signal_Interceptor",
    "📋 Data_Cosmos_Management",
    "📄 Data_Validator",
    "🚿 Data_Cleanser",
    "🏰 Data_Architect",
    "🛰️ Data_Starship_Storage",
]

# Create the pages directory if it doesn't exist
pages_directory = "pages"
if not os.path.exists(pages_directory):
    os.makedirs(pages_directory)

# Generate Python files for each page
for i, page_name in enumerate(page_names, start=1):
    file_content = f"""
import streamlit as st

st.title("{page_name.replace('_', ' ').title()}")

st.write("This is a Streamlit app page, bonjour 👋🏻.")
"""
    file_path = os.path.join(pages_directory, f"{i}_{page_name.replace(' ', '_')}.py")

    with open(file_path, "w") as file:
        file.write(file_content)

print("Pages created successfully! ✅")
