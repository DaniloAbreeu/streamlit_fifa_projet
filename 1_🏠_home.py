import streamlit as st
import webbrowser
import pandas as pd


if "data" not in st.session_state:
    df_data = pd.read_csv("C:\\Users\\danil\\OneDrive\\pasta danilo\\GitHub\\streamlit_fifa_projet\\CLEAN_FIFA23_official_data.cvs", index_col=0)
    st.session_state["data"]=df_data


st.title("#FIFA 2023 OFFICIAL DATESET! ⚽️")
st.sidebar.markdown("Desenvolvido por **Danilo Abreu Sousa** Redes Socias: @dan.abreeu")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown("""Um conjunto de dados do FIFA 2023 pode oferecer uma ampla gama de informações úteis para análise e compreensão do jogo, tanto para jogadores casuais quanto para entusiastas de análise de desempenho. Esses dados geralmente contêm detalhes sobre os atributos de jogadores, clubes, ligas, rankings, habilidades técnicas, performances em campo e muito mais. Aqui estão algumas das principais informações que um conjunto de dados do FIFA 2023 pode incluir:

**Atributos dos Jogadores**: Este é um dos elementos mais ricos do conjunto de dados, contendo informações detalhadas sobre as habilidades de cada jogador, como velocidade, finalização, controle de bola, passes, dribles, força, entre outros. Esses atributos podem ser usados para realizar análises de desempenho e comparações entre jogadores de diferentes clubes ou ligas.

**Clubes e Ligas**: Os dados incluem informações sobre os times, competições e ligas representadas no jogo. Detalhes como elenco de jogadores, táticas preferidas, formações mais utilizadas, além do desempenho dos clubes em competições são frequentemente representados.

**Avaliações de Performance**: Esses dados refletem como os jogadores são avaliados em diferentes aspectos, como potencial de crescimento, valor de mercado, e classificação geral. Eles são úteis para identificar talentos promissores ou avaliar a evolução de jogadores ao longo das temporadas.

**Posições e Funções**: Os conjuntos de dados também trazem informações sobre as posições preferidas dos jogadores em campo, permitindo análises de como as formações e estratégias de jogo podem ser otimizadas com base nos pontos fortes e fracos de cada atleta.

**Estatísticas de Jogo**: Em alguns casos, os dados incluem estatísticas geradas durante os jogos simulados no FIFA, como gols marcados, passes completados, desarmes, e desempenho defensivo. Essas informações podem ser usadas para fazer previsões, analisar padrões de jogo e tomar decisões estratégicas.

**Dados Financeiros**: Muitos conjuntos de dados do FIFA 2023 também incluem informações financeiras sobre o valor dos jogadores, custos de transferências, e orçamentos dos clubes, o que é valioso para análises de mercado e tomada de decisões em modos como o Carreira.

Esses dados, quando bem organizados e analisados, podem fornecer insights importantes para jogadores que buscam melhorar suas táticas e estratégias no jogo, além de oferecer uma visão mais profunda sobre a mecânica do FIFA e o comportamento dos jogadores no ambiente virtual.
            




""")