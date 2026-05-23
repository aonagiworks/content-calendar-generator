import random
import pandas as pd
import streamlit as st
from data import NICHE_TOPICS, FORMAT_OPTIONS, CTA_OPTIONS, PILLARS

st.set_page_config(
    page_title="Content Calendar Generator",
    page_icon="🗓️",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        background-color: #f6f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .hero-box {
        background: linear-gradient(135deg, #f7f8ff, #ffffff);
        padding: 3rem 2rem;
        border-radius: 24px;
        border: 1px solid #e6e8f0;
        box-shadow: 0 8px 30px rgba(0,0,0,0.04);
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: 2.7rem;
        font-weight: 700;
        color: #111827;
        line-height: 1.15;
        margin-bottom: 1rem;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #6b7280;
        max-width: 760px;
        margin-bottom: 1.5rem;
        line-height: 1.7;
    }

    .metric-card {
        background: white;
        padding: 1.2rem;
        border-radius: 20px;
        border: 1px solid #e8ebf3;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        text-align: center;
    }

    .metric-number {
        font-size: 1.8rem;
        font-weight: 700;
        color: #111827;
    }

    .metric-label {
        font-size: 0.95rem;
        color: #6b7280;
        margin-top: 0.3rem;
    }

    .section-card {
        background: white;
        padding: 1.5rem;
        border-radius: 22px;
        border: 1px solid #e8ebf3;
        box-shadow: 0 6px 24px rgba(0,0,0,0.03);
        margin-bottom: 1.2rem;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.5rem;
    }

    .section-desc {
        color: #6b7280;
        font-size: 0.96rem;
        margin-bottom: 1rem;
        line-height: 1.6;
    }

    .feature-card {
        background: #ffffff;
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid #e8ebf3;
        min-height: 130px;
    }

    .feature-title {
        font-weight: 600;
        font-size: 1rem;
        color: #111827;
        margin-bottom: 0.5rem;
    }

    .feature-text {
        color: #6b7280;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    .small-badge {
        display: inline-block;
        background: #eef2ff;
        color: #4f46e5;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        font-size: 0.8rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .insight-box {
        background: linear-gradient(135deg, #ffffff, #f8faff);
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid #e8ebf3;
    }
</style>
""", unsafe_allow_html=True)

def generate_calendar(niche, days):
    rows = []
    niche_data = NICHE_TOPICS[niche]

    for day in range(1, days + 1):
        pillar = PILLARS[(day - 1) % len(PILLARS)]
        idea = random.choice(niche_data[pillar])
        content_format = random.choice(FORMAT_OPTIONS[pillar])
        cta = random.choice(CTA_OPTIONS[pillar])

        rows.append({
            "Day": day,
            "Content Pillar": pillar.title(),
            "Content Idea": idea,
            "Recommended Format": content_format,
            "Suggested CTA": cta
        })

    return pd.DataFrame(rows)

st.markdown("""
<div class="hero-box">
    <div class="small-badge">Strategic Content Planning for Modern Brands</div>
    <div class="hero-title">Plan Smarter Content Ideas<br>For Consistent Business Growth</div>
    <div class="hero-subtitle">
        Build a structured content calendar in seconds with ready-to-use ideas tailored to your business niche.
        Designed for UMKM, product brands, service businesses, and creators who want more consistency with less planning friction.
    </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{len(NICHE_TOPICS)}</div>
        <div class="metric-label">Available Business Niches</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{len(PILLARS)}</div>
        <div class="metric-label">Core Content Pillars</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">30</div>
        <div class="metric-label">Maximum Planning Duration</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([1, 1])

with left:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Generate Your Content Calendar</div>
        <div class="section-desc">
            Select your business niche and planning duration, then instantly generate a structured content calendar
            with varied themes, content formats, and calls-to-action.
        </div>
    </div>
    """, unsafe_allow_html=True)

    niche = st.selectbox("Select your business niche", list(NICHE_TOPICS.keys()))
    days = st.slider("Select planning duration (days)", min_value=7, max_value=30, value=14)
    generate_button = st.button("Generate Content Calendar", use_container_width=True)

with right:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Why growing businesses use this tool</div>
        <div class="section-desc">
            Many brands struggle to stay consistent because content planning takes too much time.
            This tool helps transform scattered ideas into a more focused, strategic, and usable publishing plan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Faster Planning</div>
            <div class="feature-text">Generate weekly or monthly content ideas in seconds without starting from scratch.</div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Better Consistency</div>
            <div class="feature-text">Maintain a healthier balance of educational, promotional, and engagement content.</div>
        </div>
        """, unsafe_allow_html=True)

    f3, f4 = st.columns(2)
    with f3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Built for Practical Use</div>
            <div class="feature-text">Suitable for UMKM, service businesses, digital creators, and modern small brands.</div>
        </div>
        """, unsafe_allow_html=True)

    with f4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Ready to Export</div>
            <div class="feature-text">Download your generated plan instantly and apply it directly to your workflow.</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if generate_button:
    df = generate_calendar(niche, days)

    st.markdown("""
    <div class="section-card">
        <div class="section-title">Your Generated Content Calendar</div>
        <div class="section-desc">
            Below is your structured content plan, ready to review, refine, and export for your publishing workflow.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True)

    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV File",
        data=csv_data,
        file_name=f"content_calendar_{niche.lower().replace(' ', '_').replace('/', '_')}.csv",
        mime="text/csv",
        use_container_width=True
    )

    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown(f"""
        <div class="insight-box">
            <strong>Selected Niche</strong><br>{niche}
        </div>
        """, unsafe_allow_html=True)

    with i2:
        st.markdown(f"""
        <div class="insight-box">
            <strong>Planning Duration</strong><br>{days} days
        </div>
        """, unsafe_allow_html=True)

    with i3:
        st.markdown(f"""
        <div class="insight-box">
            <strong>Total Content Ideas</strong><br>{len(df)} ideas generated
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Start with a niche and planning duration</div>
        <div class="section-desc">
            Select your business category and number of content days, then generate a ready-to-use content calendar
            tailored to your niche.
        </div>
    </div>
    """, unsafe_allow_html=True)