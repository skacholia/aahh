import streamlit as st
import smtplib

def send_email(body):
    sender_email = "athensai.info@gmail.com" # replace with your own email address
    receiver_email = "athensai.info@gmail.com" # recipient's email address
    password = "" # get email password from Streamlit Secrets
    message = f"Subject: New feedback submission\n\n{body}" # email message

    # create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # send email
    server.sendmail(sender_email, receiver_email, message)
    st.success("Message sent!")
    server.quit()

# Streamlit app code
st.title("Send us feedback!")
body = st.text_area("Enter your message here")
if st.button("Send"):
    if body.strip() == "":
        st.warning("Message body cannot be empty")
    else:
        send_email(body)
