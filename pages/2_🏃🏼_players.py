import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data=st.session_state["data"]


clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube",clubes)

df_playes = df_data[(df_data["Club"] == club)]
players = df_playes["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador",players)

player_stets = df_data[df_data["Name"] == player].iloc[0]
st.image(player_stets["Photo"])
st.title(player_stets["Name"])

st.markdown(f"**Clube:** {player_stets['Club']}")
st.markdown(f"**Posição:** {player_stets['Position']}")

col1,col2,col3,col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stets['Age']}")
col2.markdown(f"**Altura:** {player_stets['Height(cm.)'] /100}")
col3.markdown(f"**Peso:** {player_stets['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stets['Overall']}")
st.progress(int(player_stets["Overall"]))

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Valor de marcado", value=f"£{player_stets['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£{player_stets['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£{player_stets['Release Clause(£)']:,}")