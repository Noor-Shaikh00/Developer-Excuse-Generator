import streamlit as st
import random
import pyperclip

# Funny excuses list
excuses = {
    "Halka Phulka Bahana": [
        "Sir, code likh diya tha, par GitHub ne upload nahi kiya! 😅",
        "Boss, system update ho raha tha, isliye kaam slow ho gaya! 🖥️🐢",
        "Teacher, WiFi bohot slow tha, file attach nahi hui! 📡",
        "Mujhe laga aaj Sunday hai, isliye nahi bheja! 😆"
    ],
    "Masalaydaar Drama": [
        "Sir, code likhne ja raha tha magar bijli chali gayi, pura progress ud gaya! ⚡😭",
        "Boss, main ne submit kar diya tha, magar system crash ho gaya! 💻🔥",
        "Teacher, project complete tha, magar USB dhoond nahi raha! 🤯",
        "Sir, coding kar raha tha, magar laptop garam ho ke fry ho gaya! 🍳💀"
    ],
    "Full Tareefo Wala Bahana": [
        "Sir, aap ke standards bohot high hain, isliye project ko aur behtar bana raha hoon! 🎯🔥",
        "Boss, mujhe laga ye project bohot important hai, isliye extra perfection add kar raha hoon! 🤓✨",
        "Sir, main ne project almost complete kar diya, bas final magic touch bacha hai! 🎩😎",
        "Boss, aap dekh ke waqai khush ho jaoge, bas thoda aur patience! 😁🙏"
    ]
}

st.title("🚀 Developer Excuse Generator 😆")
st.markdown("### 👨‍💻 Boss ya Teacher ko ullu banane ka ultimate tool! 😎")

# Select urgency level
mode = st.radio("⚡ Urgency Level Chuno:", ["Halka Phulka Bahana", "Masalaydaar Drama", "Full Tareefo Wala Bahana"])

# Generate excuse
if st.button("🎲 Generate Excuse!"):
    excuse = random.choice(excuses[mode])
    st.success(f"💡 **Excuse:** {excuse}")
    
    # Copy to clipboard button
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(excuse)
        st.info("✅ Excuse copied! Ab boss ko bhejo! 📩")

st.markdown("---")
st.markdown("💡Developed by Noor Shaikh.👀😁🖤")