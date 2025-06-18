import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Dr. Adekola Retirement", layout="centered", page_icon="🎓")

# Title
st.markdown("<h1 style='text-align: center; color: gold;'>DR. OLATUNDE ADEKOLA A.</h1>", unsafe_allow_html=True)

# Image
image = Image.open("adekola.jpg")
st.image(image, use_container_width=True, caption="In honor of a life of service")

# Background and event details
st.markdown(
    """
    <div style='background-color: black; padding: 20px; border-radius: 10px; color: white;'>
        <p style='font-size: 18px;'>To recognize his lifetime of service, a retirement ceremony has been scheduled:</p>
        <ul style='font-size: 16px;'>
            <li><strong>Date:</strong> Saturday, July 12, 2025</li>
            <li><strong>Time:</strong> 4:00 PM</li>
            <li><strong>Venue:</strong> Vision Events Arena, Abuja</li>
        </ul>
        <p style='margin-top:20px;'>We respectfully invite <strong>Your Excellency</strong> to attend or delegate a representative to the occasion.</p>
        <p>Furthermore, we humbly seek financial support from the Kaduna State Government to assist in hosting this memorable event in recognition of Dr. Adekola's indelible contributions to the educational advancement of Kaduna State.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Contribution Details
st.markdown("### 💳 Contribution Details")
st.markdown(
    """
    - **Account Name:** Olushola Segun Odusanya  
    - **Bank:** Providus Bank  
    - **Account Number:** 6506120402
    """
)

# Contact
st.markdown("### 📞 For RSVP or More Information")
st.markdown(
    """
    - **Rufai:** 07032515943  
    - **Blessing:** 08034689034
    """
)

# Closing
st.markdown(
    """
    <hr>
    <p><strong>Thank you, Your Excellency, for your kind attention and anticipated support.</strong></p>
    <p><strong>Yours faithfully,</strong></p>
    <p>
    <strong>Dr. Olushola Odusanya</strong><br>
    DG/CEO, National Centre for Technology Management<br>
    Chairman, Dr. Adekola Olatunde Retirement Party LOC<br>
    08055154949
    </p>
    """,
    unsafe_allow_html=True
)
