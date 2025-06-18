import streamlit as st
import smtplib
from email.message import EmailMessage
import uuid

# Configure page
st.set_page_config(page_title="Dr. Adekola Retirement", layout="centered")

# Title and Image
st.markdown("<h1 style='text-align: center; color: gold;'>DR. OLATUNDE ADEKOLA A.</h1>", unsafe_allow_html=True)
st.image("adekola.jpg", use_container_width=True)

# Event info in black box
st.markdown("""
<div style="background-color: black; color: white; padding: 20px; border-radius: 10px;">
    <h3>To recognize his lifetime of service, a retirement ceremony has been scheduled:</h3>
    <ul>
        <li><b>Date:</b> Saturday, July 12, 2025</li>
        <li><b>Time:</b> 2:00 PM</li>
        <li><b>Venue:</b> Vision Events Arena, Abuja</li>
    </ul>
    <p>His friends organaizing this ceremony humbly seeks your voluntary financial contribution to help in making this event a memorable occasion
     In recognition of his incredible contributions to education sector adavancements in Nigeria.</p>
    <p><b>Contribution Details:</b><br>
       Account Name: Olushola Segun Odusanya<br>
       Bank: Providus Bank<br>
       Account Number: 6506120402</p>
    <p><b>For RSVP or more information:</b><br>
       Rufai - 07032515943<br>
       Blessing - 08034689034</p>
    <p>Thank you for your kind attention and anticipated support.</p>
    <p><b>Yours faithfully,</b><br>
       Dr. Olushola Odusanya<br>
       DG/CEO, National Centre for Technology Management<br>
       Chairman, Dr. Adekola Olatunde Retirement Party LOC<br>
       08055154949</p>
</div>
""", unsafe_allow_html=True)

# Tribute form
st.markdown("## ✍️ Submit a Tribute")
with st.form("tribute_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Your Tribute Message")
    uploaded_file = st.file_uploader("Optional: Upload photo, video, or voice note", type=["jpg", "jpeg", "png", "mp4", "mp3", "wav"])
    submit = st.form_submit_button("Send Tribute")

if submit:
    if not name and not message and not uploaded_file:
        st.warning("Please provide at least your name, a message, or a file.")
    else:
        try:
            email_msg = EmailMessage()
            email_msg["Subject"] = f"New Tribute from {name}"
            email_msg["From"] = st.secrets["email"]["email_user"]
            email_msg["To"] = st.secrets["email"]["recipient"]
            content = f"Name: {name}\n\nMessage:\n{message}"
            email_msg.set_content(content)

            if uploaded_file:
                file_data = uploaded_file.read()
                file_name = f"{uuid.uuid4()}_{uploaded_file.name}"
                email_msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

            with smtplib.SMTP(st.secrets["email"]["smtp_host"], st.secrets["email"]["smtp_port"]) as server:
                server.starttls()
                server.login(st.secrets["email"]["email_user"], st.secrets["email"]["email_pass"])
                server.send_message(email_msg)

            st.success("Tribute submitted successfully. Thank you!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
