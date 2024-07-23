import streamlit as st
import webbrowser

import streamlit.components.v1 as components

page_bg_img = """
<style>
div.stButton > button:first-child {
    all: unset;
    width: 300px;
    height: 60px;
    font-size: 32px;
    background: transparent;
    border: none;
    position: relative;
    color: #f0f0f0;
    cursor: pointer;
    z-index: 1;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;

}
div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
    transition: all .4s;
}

div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: #001a00;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 35px;
  height: 35px;
  background: #ffffff15;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 50px;
}

div.stButton > button:hover::before {
    transform: translate(5%, 20%);
    width: 110%;
    height: 110%;
}


div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
}

div.stButton > button:active::after {
    transition: 0s;
    transform: translate(0, 5%);
}

[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1581084324492-c8076f130f86?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background-image: url("https://img.freepik.com/free-vector/emerald-background-design_23-2150317701.jpg?t=st=1720042071~exp=1720045671~hmac=9ba5de4d9099fb8ddd7ab39b1540692bc9c69e1b25cf8fda43322d96f7d6c704&w=1060");
background-size: cover;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Moodwave-Spotify 💚")
st.markdown(''':green[**Note : It is recommended that you scan your face , for Moodwave to groove with you!**]''')
st.sidebar.success("Spotify has been selected as your music player.")


if "run" not in st.session_state:
    st.write("**Looks like you have skipped the face scan on the homepage and came here, just for music, just choose your vibe manually for Moodwave to groove with you!**")
    option = st.selectbox(
    'What''s your vibe today?',
    ('Happy', 'Sad', 'Angry','Fear','Surprise','Neutral'))
    if option == "Happy":
        st.session_state["emotion"] = "Happy"
    elif option == "Sad":
        st.session_state["emotion"] = "Sad"
    elif option == "Angry":
        st.session_state["emotion"] = "Angry"
    elif option == "Fear":
        st.session_state["emotion"] = "Fear"
    elif option == "Surprise":
        st.session_state["emotion"] = "Surprise"
    else:
        st.session_state["emotion"] = "Neutral"
else:
    st.write("You current emotion is: " , st.session_state["emotion"])

col1, col2 = st.columns(2)

with col1:
    Gospel = st.button("Gospel")
    if Gospel:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWTwbZHrJRIgD?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdFesNN9TzXT?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2r9tRVoHG3AMBTvKJ8abOl?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7EZ4lWeM1OLxZYfGmhDbJI?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7vatYrf39uVaZ8G2cVtEik?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX0XUfTFmNBRM?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1E4mS880sTV9QE?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
    AfroBeats= st.button("Afro Beats")
    if AfroBeats:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIfPJlPqfLhbI?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIhesKwAgSumh?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7x67PlR1qbTSRBAuEIRvVR?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/0oU30cCr8klmMsuOKHDLkh?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1MV2upgyEGw846M3S9kxz8?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWVA9JQScfrfL?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7cOYpcvIHxyNdu1DhXkCpu?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            

   
with col2:
   RnB = st.button("RnB")
   if RnB:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1sLNVfSmgmJftGqppElxi6?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6Fn4CdwJMtnAcz6iK2JMDn?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIeepeV6siJHB?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/766Z0zF2632cl5Y83IbZCq?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5tSbO6M5AT7r91ytDd4nNP?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3SsPWyQnAh1ccWEXZPYaCY?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/60eEo5VdhekyGJKTjK2xSV?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
   Kpop = st.button("Kpop")
   if Kpop:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7QeQjujWh9l?utm_source=generator&theme=0 width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWWfmbQgZIznF?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5ecJF7ZFkufISEw6SZdKrB?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            st.write("No playlist available for this emotion. Hence default playlist is being played.")
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWZY9CnWbvq8Q?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWZY9CnWbvq8Q?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWXVJK4aT7pmk?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3sKYXN4FEWLpg4FiJlxSrN?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
   