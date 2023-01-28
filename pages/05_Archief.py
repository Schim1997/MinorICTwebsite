import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import webbrowser

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# col1, col2 = st.columns(2)

#with col1:
#    st.image('images/kluis.png')

# with col1:
st.header("Archief")
st.write('''
Voor de minor, hebben wij een archief aangemaakt. Hierin staan onze uitwerkingen en rapportages beschreven. 
Per hoofdstuk zal er een korte toelichting staan om wat overzicht en duidelijk te geven aan het archief. 
''')

url = "[Het Archief](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
      "/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments" \
      "%2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%20ers&ga=1)"
# if st. button("Naar het archief", key='archief'):
#    webbrowser.open(url)
st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("1. Belbin Testen")
st.write("""
In dit mapje staan de uitslagen en toelichtingen over de gemaakte Belbin testen. De Belbin test is een 
test die wordt gebruikt om de rollen van individuen binnen een team te identificeren en te begrijpen. Het 
evalueert de sterkte van een individu in negen verschillende rollen die nodig zijn voor een succesvol team en een 
succesvolle samenwerking.  
""")
url = "[Belbin Test](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_layouts/15/" \
      "onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20" \
      "niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen)"
st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("2. Beroepenveld analyse")
st.write("""
In dit mapje staan de indivuedele verkenningen van de verschillende beroepenvelden. Dit is een toevoeging 
aan de 'projecten' pagina. De beroepenveldanalyse is gedaan om te kijken waar 'problemen' zijn en hoe deze problemen
opgelost kunnen worden met behulp van een ICT oplossing. 
beroepenveld 
""")
url = "[Beroepenveld Analyse](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_" \
      "layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT" \
      "%20voor%20niet%20ICT%27%20ers%2F2%2E%20Beroepenveld%20analyse)"
st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("3. Design Thinking")
st.write("""
In dit mapje staan de verschillende gemaakte opdrachten met betrekking tot de design thinking methode en de 
verschillende fases daarin. Per onderdeel van de design thinking methode is er een apart mapje aangemaakt waarin al het
eerder gemaakte werkt terug te vinden is. Hier staan ook dingen in die we als opzet gebruikt hebben, maar later niks 
mee gedaan hebben in ons eindverslag. Door het maken van deze opdrachten zijn we namelijk tot bepaalde inzichten gekomen
die we anders wellicht niet hadden gehad. Om deze reden wilde we dat de bestanden terug te vinden waren in ons archief.
""")
url = "[Design Thinking](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_layouts/15" \
      "/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%" \
      "20niet%20ICT%27%20ers%2F3%2E%20Design%20Thinking)"
st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("4. Tussentijdse producten")
st.write("""
In dit mapje staan tussentijds gemaakte producten. Omdat sommige tussentijdse producten een presentatie betreffen zijn 
deze terug te vinden bij hoofdstuk 6 'Presentaties'. 
""")
url = "[Tussentijdse producten](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_" \
      "layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT" \
      "%20voor%20niet%20ICT%27%20ers%2F4%2E%20Tussentijdse%20producten)"
st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("5. Onderdelen eindopdracht")
st.write("""
In dit mapje staan 
""")
url = "[Onderdelen eindopdracht](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/" \
      "_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%" \
      "20ICT%20voor%20niet%20ICT%27%20ers%2F5%2E%20Onderdelen%20Eindopdracht)"
st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("6. Presentaties")
st.write("""
In dit mapje staan de presentaties die wij tijdens dit project, hebben gebruikt.
""")
url = "[Presentaties](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_layouts/15" \
      "/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20" \
      "voor%20niet%20ICT%27%20ers%2F6%2E%20Presentaties)"
st.markdown(url, unsafe_allow_html=True)

st.markdown("##")
st.markdown("##")

# next and previous page buttons
colp, coln = st.columns([1, 0.15])

with colp:
    if st.button("Vorige Pagina"):
        switch_page("De APK")

with coln:
    if st.button("Volgende Pagina"):
        switch_page("Contact Us")
