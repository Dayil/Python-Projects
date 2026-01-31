# Este script constrói um painel de controle (dashboard) interativo utilizando a biblioteca Streamlit.
# O objetivo principal é permitir a análise exploratória de dados salariais de profissionais da área de dados,
# oferecendo filtros dinâmicos e visualizações gráficas detalhadas.

# Importação das bibliotecas essenciais para o funcionamento da aplicação
import streamlit as st  # Framework utilizado para criar aplicações web de ciência de dados de forma rápida e pythonica
import pandas as pd     # Biblioteca padrão da indústria para manipulação e análise de dados tabulares (DataFrames)
import plotly.express as px # Biblioteca de alto nível para criação de gráficos interativos e visualizações complexas

# --- Configurações Iniciais da Interface ---
# A função set_page_config define as propriedades globais da página da aplicação.
# Aqui configuramos o título que aparece na aba do navegador, o ícone (favicon) e o modo de layout 'wide' (largo)
# para melhor aproveitamento do espaço horizontal da tela.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Ingestão e Leitura dos Dados ---
# Carrega o dataset a partir de um arquivo CSV hospedado remotamente no GitHub.
# O Pandas lê este arquivo e o converte em um DataFrame, que é a estrutura de tabela em memória usada para análise.
df = pd.read_csv("https://raw.githubusercontent.com/Dayil/Python-Projects/refs/heads/main/Dashboard%20Interativo%20-%20Data%20Science%20Project/dados-datascience.csv")

# --- Estrutura da Barra Lateral (Sidebar) para Filtragem ---
# Cria um cabeçalho visual na barra lateral para organizar a seção onde o usuário aplicará os filtros.
st.sidebar.header("🔍 Filtros")

# Configuração do Filtro de Ano:
# 1. Extrai os valores únicos da coluna 'ano' e os ordena de forma crescente.
anos_disponiveis = sorted(df['ano'].unique())
# 2. Cria um widget de seleção múltipla na sidebar. O parâmetro 'default' garante que todos os anos venham pré-selecionados.
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

# Configuração do Filtro de Senioridade:
# 1. Identifica os níveis de senioridade únicos presentes nos dados.
senioridades_disponiveis = sorted(df['senioridade'].unique())
# 2. Cria o seletor múltiplo para que o usuário escolha quais níveis de experiência deseja visualizar.
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Configuração do Filtro de Tipo de Contrato:
# 1. Lista os tipos de contratos únicos (ex: Full-time, Contractor, etc).
contratos_disponiveis = sorted(df['contrato'].unique())
# 2. Cria o seletor múltiplo para tipos de contrato.
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Configuração do Filtro de Tamanho da Empresa:
# 1. Obtém os tamanhos de empresa únicos disponíveis no dataset.
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
# 2. Cria o seletor múltiplo para filtrar pelo porte da organização.
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Aplicação dos Filtros no Conjunto de Dados ---
# Cria um novo DataFrame chamado 'df_filtrado' contendo apenas as linhas que satisfazem TODAS as condições selecionadas.
# Utiliza-se o método .isin() para verificar se o valor da coluna está dentro da lista de itens selecionados pelo usuário.
# A lógica '&' (AND) garante que o registro precisa atender a todos os critérios simultaneamente.
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Área Principal de Exibição ---
# Define o título principal e uma breve descrição explicativa no corpo da página para orientar o usuário.
st.title("📊📉 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Indicadores Chave de Desempenho (KPIs) ---
st.subheader("Métricas gerais (Salário anual em USD)")

# Verifica se o DataFrame filtrado possui dados. Isso é crucial para evitar erros de cálculo (como divisão por zero) se o filtro for muito restritivo.
if not df_filtrado.empty:
    # Calcula a média aritmética dos salários na coluna 'usd'.
    salario_medio = df_filtrado['usd'].mean()
    # Encontra o valor máximo absoluto de salário na coluna 'usd'.
    salario_maximo = df_filtrado['usd'].max()
    # Conta o número total de registros (linhas) que sobraram após a filtragem.
    total_registros = df_filtrado.shape[0]
    # Identifica o cargo que aparece com maior frequência (moda) na coluna 'cargo'.
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    # Define valores padrão zerados caso o filtro não retorne nenhum dado, mantendo a interface estável.
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

# Cria um layout de 4 colunas para exibir os cartões de métricas lado a lado.
col1, col2, col3, col4 = st.columns(4)
# Exibe cada métrica formatada (ex: f"${...:,.0f}" formata como moeda sem decimais e com separador de milhar).
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

# Adiciona uma linha divisória visual para separar as seções.
st.markdown("---")

# --- Visualização de Dados Gráfica (Plotly) ---
st.subheader("Gráficos")

# Cria duas colunas para organizar a primeira linha de gráficos.
col_graf1, col_graf2 = st.columns(2)

# Coluna 1: Gráfico de Barras - Top Cargos
with col_graf1:
    if not df_filtrado.empty:
        # Prepara os dados: agrupa por cargo, calcula a média salarial, seleciona os 10 maiores e ordena para visualização.
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        # Cria o gráfico de barras horizontais usando Plotly Express.
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
        )
        # Ajusta o layout para centralizar o título e garantir a ordem correta das barras.
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        # Renderiza o gráfico no Streamlit, ajustando-o à largura da coluna.
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

# Coluna 2: Histograma - Distribuição de Salários
with col_graf2:
    if not df_filtrado.empty:
        # Cria um histograma para visualizar a frequência de diferentes faixas salariais.
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        # Centraliza o título do gráfico.
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

# Cria duas colunas para a segunda linha de gráficos.
col_graf3, col_graf4 = st.columns(2)

# Coluna 3: Gráfico de Pizza (Donut) - Trabalho Remoto vs Presencial
with col_graf3:
    if not df_filtrado.empty:
        # Conta a ocorrência de cada tipo de trabalho (remoto, presencial, híbrido).
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        # Cria o gráfico de pizza com um buraco no meio (hole=0.5), transformando-o em um gráfico de rosca.
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5  
        )
        # Configura para exibir tanto a porcentagem quanto o rótulo da categoria no gráfico.
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

# Coluna 4: Mapa Coroplético - Salário de Data Scientist por País
with col_graf4:
    if not df_filtrado.empty:
        # Filtra o DataFrame especificamente para o cargo de 'Data Scientist' para uma análise geográfica focada.
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        # Agrupa por país (código ISO3) e calcula a média salarial.
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        # Cria o mapa mundi colorido onde a cor representa a intensidade do salário médio.
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.") 

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
# Exibe o DataFrame filtrado em formato de tabela interativa, permitindo que o usuário explore os dados brutos.
st.dataframe(df_filtrado)