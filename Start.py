import streamlit as st

st.title('BMI Rechner')

name = st.session_state.get('name')

st.markdown("Die App ermöglicht es Ihnen, Ihren BMI zu berechnen")
        
# Add some health advice
st.info("""Der BMI ist ein Screening-Tool, aber keine Diagnose für Körperfett oder Gesundheit. 
Bitte konsultieren Sie einen Arzt für eine vollständige Beurteilung.""")

st.write("Diese App wurde von Samuel Wehrli (wehs@zhaw.ch) im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.")