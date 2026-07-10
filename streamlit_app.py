import streamlit as st
import pandas as pd
import plotly.express as px
from google.cloud import bigquery
from google.oauth2 import service_account
import json
import os

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="metric-container"] {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 10px;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

PROJECT_ID = "vetic-bcf18"
DATASET    = "analytics_336890618"
TABLE      = "events_intraday_202605*"
FULL_TABLE = f"`{PROJECT_ID}.{DATASET}.{TABLE}`"

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📊 Analytics")
    st.markdown("---")
    st.subheader("📅 Date range")
    date_range = st.selectbox("Period", [
        "Last 7 days", "Last 14 days", "Last 30 days", "All data"
    ])
    st.markdown("---")
    st.subheader("🔍 Filters")
    event_filter    = st.text_input("Event name (optional)", placeholder="e.g. screen_view")
    platform_filter = st.selectbox("Platform", ["All", "ANDROID", "IOS", "WEB"])
    st.markdown("---")
    st.caption(f"Project: `{PROJECT_ID}`")
    st.caption(f"Dataset: `{DATASET}`")
    st.caption(f"Table: `{TABLE}`")


# ─── CONNECTION via st.secrets (Streamlit Cloud) ──────────────────────────────
@st.cache_resource
def get_client():
    # Try Streamlit secrets first (for cloud deployment)
    if "gcp_service_account" in st.secrets:
        creds = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        return bigquery.Client(project=PROJECT_ID, credentials=creds)

    # Fallback: local JSON key file
    key_candidates = [
        "jayant1-362611-d9517aa717b7.json",
        os.path.expanduser("~/Downloads/jayant1-362611-d9517aa717b7.json"),
    ]
    for path in key_candidates:
        if os.path.exists(path):
            creds = service_account.Credentials.from_service_account_file(
                path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
            return bigquery.Client(project=PROJECT_ID, credentials=creds)

    raise FileNotFoundError(
        "No GCP credentials found. Add secrets in Streamlit Cloud or place "
        "the JSON key file next to this script."
    )


@st.cache_data(ttl=300, show_spinner=False)
def run_query(_client, sql):
    return _client.query(sql).to_dataframe()


# ─── CONNECT ──────────────────────────────────────────────────────────────────
st.title("📊 Analytics Dashboard")
st.caption(f"BigQuery · {PROJECT_ID} · {DATASET}.{TABLE}")

try:
    client = get_client()
    st.success("✅ Connected to BigQuery!")
except Exception as e:
    st.error(f"❌ Connection failed: {e}")
    st.markdown("""
    **To fix this on Streamlit Cloud:**
    1. Go to your app settings → **Secrets**
    2. Paste your service account JSON like this:
    ```toml
    [gcp_service_account]
    type = "service_account"
    project_id = "vetic-bcf18"
    private_key_id = "xxxx"
    private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
    client_email = "python-test@jayant1-362611.iam.gserviceaccount.com"
    client_id = "xxxx"
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    ```
    """)
    st.stop()

# Build WHERE clauses
date_map        = {"Last 7 days": 7, "Last 14 days": 14, "Last 30 days": 30, "All data": None}
days            = date_map[date_range]
date_clause     = f"AND PARSE_DATE('%Y%m%d', event_date) >= DATE_SUB(CURRENT_DATE(), INTERVAL {days} DAY)" if days else ""
event_clause    = f"AND event_name = '{event_filter}'" if event_filter else ""
platform_clause = f"AND platform = '{platform_filter}'" if platform_filter != "All" else ""
where_extra     = f"{date_clause} {event_clause} {platform_clause}"


# ════════════════════════════════════════════════════════════════════════════
# KPI CARDS
# ════════════════════════════════════════════════════════════════════════════
with st.spinner("Loading metrics..."):
    try:
        kpi = run_query(client, f"""
        SELECT
            COUNT(*)                        AS total_events,
            COUNT(DISTINCT user_pseudo_id)  AS unique_users,
            COUNT(DISTINCT event_date)      AS active_days,
            COUNT(DISTINCT event_name)      AS unique_event_types
        FROM {FULL_TABLE}
        WHERE 1=1 {where_extra}
        """).iloc[0]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("🎯 Total events",   f"{int(kpi.total_events):,}")
        c2.metric("👥 Unique users",    f"{int(kpi.unique_users):,}")
        c3.metric("📅 Active days",     f"{int(kpi.active_days):,}")
        c4.metric("🔖 Event types",     f"{int(kpi.unique_event_types):,}")
    except Exception as e:
        st.error(f"KPI error: {e}")

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# ROW 1 — Events over time  |  Platform split
# ════════════════════════════════════════════════════════════════════════════
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Events over time")
    try:
        df = run_query(client, f"""
        SELECT event_date,
               COUNT(*) AS total_events,
               COUNT(DISTINCT user_pseudo_id) AS unique_users
        FROM {FULL_TABLE}
        WHERE 1=1 {where_extra}
        GROUP BY event_date ORDER BY event_date
        """)
        df["event_date"] = pd.to_datetime(df["event_date"], format="%Y%m%d")
        fig = px.line(df, x="event_date", y=["total_events","unique_users"],
                      color_discrete_sequence=["#2a78d6","#1baf7a"],
                      labels={"value":"Count","event_date":"Date","variable":""})
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), legend_title="")
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Trend error: {e}")

with col2:
    st.subheader("📱 Platform")
    try:
        df = run_query(client, f"""
        SELECT platform, COUNT(DISTINCT user_pseudo_id) AS users
        FROM {FULL_TABLE}
        WHERE platform IS NOT NULL {where_extra}
        GROUP BY platform ORDER BY users DESC
        """)
        fig = px.pie(df, names="platform", values="users", hole=0.55,
                     color_discrete_sequence=["#2a78d6","#1baf7a","#eda100","#e34948"])
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), legend_title="")
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Platform error: {e}")

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# ROW 2 — Top events  |  Top countries
# ════════════════════════════════════════════════════════════════════════════
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏆 Top event names")
    try:
        df = run_query(client, f"""
        SELECT event_name, COUNT(*) AS event_count,
               COUNT(DISTINCT user_pseudo_id) AS unique_users
        FROM {FULL_TABLE}
        WHERE 1=1 {where_extra}
        GROUP BY event_name ORDER BY event_count DESC LIMIT 15
        """)
        fig = px.bar(df, x="event_count", y="event_name", orientation="h",
                     color="event_count", color_continuous_scale="Blues",
                     labels={"event_count":"Count","event_name":"Event"})
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0),
                          coloraxis_showscale=False,
                          yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Events error: {e}")

with col4:
    st.subheader("🌍 Top countries")
    try:
        df = run_query(client, f"""
        SELECT geo.country AS country,
               COUNT(DISTINCT user_pseudo_id) AS users
        FROM {FULL_TABLE}
        WHERE geo.country IS NOT NULL {where_extra}
        GROUP BY country ORDER BY users DESC LIMIT 10
        """)
        fig = px.bar(df, x="users", y="country", orientation="h",
                     color="users", color_continuous_scale="Greens",
                     labels={"users":"Users","country":"Country"})
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0),
                          coloraxis_showscale=False,
                          yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Geo error: {e}")

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# ROW 3 — Device  |  Hourly distribution
# ════════════════════════════════════════════════════════════════════════════
col5, col6 = st.columns(2)

with col5:
    st.subheader("💻 Device category")
    try:
        df = run_query(client, f"""
        SELECT device.category AS device_category,
               COUNT(DISTINCT user_pseudo_id) AS users
        FROM {FULL_TABLE}
        WHERE device.category IS NOT NULL {where_extra}
        GROUP BY device_category ORDER BY users DESC
        """)
        fig = px.pie(df, names="device_category", values="users",
                     color_discrete_sequence=["#2a78d6","#1baf7a","#eda100"])
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0))
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Device error: {e}")

with col6:
    st.subheader("⏰ Hourly distribution")
    try:
        df = run_query(client, f"""
        SELECT EXTRACT(HOUR FROM TIMESTAMP_MICROS(event_timestamp)) AS hour,
               COUNT(*) AS events
        FROM {FULL_TABLE}
        WHERE event_timestamp IS NOT NULL {where_extra}
        GROUP BY hour ORDER BY hour
        """)
        fig = px.bar(df, x="hour", y="events",
                     color="events", color_continuous_scale="Purples",
                     labels={"hour":"Hour of day","events":"Events"})
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Hourly error: {e}")

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# ROW 4 — OS breakdown  |  New vs returning
# ════════════════════════════════════════════════════════════════════════════
col7, col8 = st.columns(2)

with col7:
    st.subheader("📱 Operating system")
    try:
        df = run_query(client, f"""
        SELECT device.operating_system AS os,
               COUNT(DISTINCT user_pseudo_id) AS users
        FROM {FULL_TABLE}
        WHERE device.operating_system IS NOT NULL {where_extra}
        GROUP BY os ORDER BY users DESC LIMIT 8
        """)
        fig = px.bar(df, x="os", y="users",
                     color="users", color_continuous_scale="Teal",
                     labels={"os":"OS","users":"Users"})
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"OS error: {e}")

with col8:
    st.subheader("🔄 New vs returning users")
    try:
        df = run_query(client, f"""
        SELECT
          CASE WHEN first_date = event_date THEN 'New' ELSE 'Returning' END AS user_type,
          COUNT(DISTINCT user_pseudo_id) AS users
        FROM (
          SELECT user_pseudo_id, event_date,
                 MIN(event_date) OVER (PARTITION BY user_pseudo_id) AS first_date
          FROM {FULL_TABLE}
          WHERE 1=1 {where_extra}
        )
        GROUP BY user_type
        """)
        fig = px.pie(df, names="user_type", values="users", hole=0.55,
                     color_discrete_sequence=["#2a78d6","#eda100"])
        fig.update_layout(margin=dict(l=0,r=0,t=10,b=0))
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Retention error: {e}")

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# RAW DATA TABLE
# ════════════════════════════════════════════════════════════════════════════
st.subheader("📋 Raw events sample")
try:
    raw_df = run_query(client, f"""
    SELECT
        event_date,
        event_name,
        platform,
        geo.country             AS country,
        geo.city                AS city,
        device.category         AS device,
        device.operating_system AS os,
        user_pseudo_id
    FROM {FULL_TABLE}
    WHERE 1=1 {where_extra}
    LIMIT 1000
    """)
    st.dataframe(raw_df, use_container_width=True, height=320)
    st.download_button(
        "⬇️ Download CSV",
        raw_df.to_csv(index=False).encode("utf-8"),
        "analytics_export.csv", "text/csv"
    )
except Exception as e:
    st.error(f"Raw data error: {e}")
