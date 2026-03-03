import streamlit as st
import plotly.graph_objects as go

def create_gauge_chart(score: float, title: str, color: str):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 16, 'color': '#e2e8f0'}},
        number={'font': {'size': 40, 'color': color}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
            'bar': {'color': color},
            'bgcolor': "rgba(15, 23, 42, 0.4)",
            'borderwidth': 2,
            'bordercolor': "#475569",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.2)'},
                {'range': [50, 75], 'color': 'rgba(234, 179, 8, 0.2)'},
                {'range': [75, 100], 'color': 'rgba(34, 197, 94, 0.2)'}
            ],
        }
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "#e2e8f0"},
        height=250,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def render_gauges(result):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.plotly_chart(create_gauge_chart(result["tech_score"], "Technical", "#60a5fa"), use_container_width=True)
    with col2:
        st.plotly_chart(create_gauge_chart(result["comm_score"], "Communication", "#34d399"), use_container_width=True)
    with col3:
        st.plotly_chart(create_gauge_chart(result["soft_score"], "Soft Skills", "#fbbf24"), use_container_width=True)
    with col4:
        st.plotly_chart(create_gauge_chart(result["exp_score"], "Experience", "#a78bfa"), use_container_width=True)