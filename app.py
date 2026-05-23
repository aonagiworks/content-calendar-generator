import random
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Content Calendar Generator", page_icon="🗓️", layout="wide")

st.title("🗓️ Content Calendar Generator")
st.caption("Generator ide konten sederhana untuk UMKM, content creator, dan bisnis kecil.")

# -------------------------
# DATA
# -------------------------
NICHE_TOPICS = {
    "Coffee Shop": {
        "edukasi": [
            "Tips memilih kopi sesuai selera",
            "Perbedaan arabica dan robusta",
            "Waktu terbaik menikmati kopi",
            "Cara menyimpan kopi agar tetap fresh"
        ],
        "promo": [
            "Promo kopi favorit minggu ini",
            "Diskon menu spesial hari ini",
            "Promo bundling kopi dan snack",
            "Promo buy 1 get 1 untuk pelanggan baru"
        ],
        "testimoni": [
            "Review pelanggan tentang menu favorit",
            "Cerita pelanggan yang suka nongkrong di tempat kamu",
            "Feedback pelanggan tentang rasa kopi",
            "Testimoni pelanggan loyal"
        ],
        "behind the scenes": [
            "Proses meracik kopi di balik bar",
            "Suasana pagi sebelum toko buka",
            "Persiapan bahan baku harian",
            "Tim barista saat bekerja"
        ],
        "faq": [
            "Apakah tersedia kopi non-sugar?",
            "Jam buka coffee shop",
            "Apakah tersedia WiFi?",
            "Menu yang paling cocok untuk pemula"
        ],
        "engagement": [
            "Tim kopi panas atau kopi dingin?",
            "Lebih suka nongkrong pagi atau malam?",
            "Pilih kopi manis atau pahit?",
            "Ajak followers vote menu favorit"
        ],
        "soft selling": [
            "Rekomendasi menu untuk teman kerja",
            "Kopi yang cocok untuk nemenin deadline",
            "Pilihan minuman untuk santai sore",
            "Tempat nyaman buat kerja dan nongkrong"
        ]
    },
    "Skincare": {
        "edukasi": [
            "Urutan skincare yang benar",
            "Perbedaan moisturizer dan serum",
            "Tips memilih skincare sesuai jenis kulit",
            "Kesalahan umum saat merawat wajah"
        ],
        "promo": [
            "Promo skincare best seller minggu ini",
            "Diskon bundling serum dan moisturizer",
            "Flash sale produk pilihan",
            "Promo spesial pelanggan baru"
        ],
        "testimoni": [
            "Hasil pemakaian customer setelah 2 minggu",
            "Review customer tentang tekstur produk",
            "Before-after dari pelanggan",
            "Cerita pelanggan yang cocok dengan produk"
        ],
        "behind the scenes": [
            "Packing order skincare harian",
            "Proses cek stok produk",
            "Suasana kerja tim admin",
            "Persiapan promo bulanan"
        ],
        "faq": [
            "Apakah aman untuk kulit sensitif?",
            "Boleh dipakai remaja atau tidak?",
            "Kapan hasil mulai terlihat?",
            "Bagaimana cara pakainya?"
        ],
        "engagement": [
            "Team skincare pagi lengkap atau simpel?",
            "Masalah kulit paling sering dialami apa?",
            "Pilih sunscreen atau moisturizer dulu?",
            "Tanya followers soal masalah kulit"
        ],
        "soft selling": [
            "Produk yang cocok untuk kulit kusam",
            "Rekomendasi skincare buat pemula",
            "Solusi simpel untuk rutinitas skincare",
            "Pilihan produk untuk daily use"
        ]
    },
    "Fashion": {
        "edukasi": [
            "Tips mix and match outfit",
            "Cara pilih outfit sesuai aktivitas",
            "Warna outfit yang mudah dipadukan",
            "Basic fashion items yang wajib punya"
        ],
        "promo": [
            "Promo outfit terbaru minggu ini",
            "Diskon koleksi best seller",
            "Promo spesial payday",
            "Bundling hemat untuk beberapa item"
        ],
        "testimoni": [
            "Review pelanggan soal kenyamanan bahan",
            "Testimoni customer pakai outfit kami",
            "Foto pelanggan dengan produk favorit",
            "Feedback ukuran dan fit produk"
        ],
        "behind the scenes": [
            "Proses packing pesanan fashion",
            "Kegiatan sorting stok produk",
            "Pemotretan katalog produk",
            "Tim menyiapkan order harian"
        ],
        "faq": [
            "Apakah ukuran sesuai standar?",
            "Bahan produk ini apa?",
            "Bagaimana cara order?",
            "Apakah bisa tukar size?"
        ],
        "engagement": [
            "Lebih suka outfit casual atau formal?",
            "Warna favorit untuk outfit harian?",
            "Pilih look simple atau standout?",
            "Vote item favorit minggu ini"
        ],
        "soft selling": [
            "Outfit simpel untuk aktivitas harian",
            "Pilihan fashion item yang versatile",
            "Rekomendasi outfit buat hangout",
            "Produk yang nyaman dipakai seharian"
        ]
    }
}

FORMAT_OPTIONS = {
    "edukasi": ["Carousel", "Feed", "Short Video"],
    "promo": ["Feed", "Story", "Short Video"],
    "testimoni": ["Story", "Feed", "Carousel"],
    "behind the scenes": ["Story", "Short Video", "Feed"],
    "faq": ["Carousel", "Story", "Feed"],
    "engagement": ["Story", "Feed", "Short Video"],
    "soft selling": ["Feed", "Carousel", "Short Video"]
}

CTA_OPTIONS = {
    "edukasi": [
        "Simpan postingan ini untuk nanti.",
        "Share ke teman kamu yang butuh info ini.",
        "Komentar kalau kamu mau tips lainnya."
    ],
    "promo": [
        "Order sekarang sebelum promo habis.",
        "DM untuk pemesanan hari ini.",
        "Cek produk kami sekarang juga."
    ],
    "testimoni": [
        "Yuk cobain juga produk ini.",
        "Lihat sendiri kenapa banyak yang suka.",
        "Saatnya kamu coba juga."
    ],
    "behind the scenes": [
        "Mau lihat proses lainnya? Tulis di komentar.",
        "Ikuti terus untuk lihat aktivitas kami berikutnya.",
        "Support terus perjalanan brand kami ya."
    ],
    "faq": [
        "Kalau masih ada pertanyaan, DM kami ya.",
        "Tulis pertanyaanmu di komentar.",
        "Hubungi kami untuk info lebih lanjut."
    ],
    "engagement": [
        "Jawab di komentar ya.",
        "Vote pilihan kamu sekarang.",
        "Tag teman kamu yang relate."
    ],
    "soft selling": [
        "Kalau cocok, langsung cek produk kami ya.",
        "DM kami untuk info lengkap.",
        "Coba sekarang dan rasakan manfaatnya."
    ]
}

PILLARS = [
    "edukasi",
    "promo",
    "testimoni",
    "behind the scenes",
    "faq",
    "engagement",
    "soft selling"
]

# -------------------------
# GENERATOR FUNCTION
# -------------------------
def generate_calendar(niche, days):
    rows = []
    niche_data = NICHE_TOPICS[niche]

    for day in range(1, days + 1):
        pillar = PILLARS[(day - 1) % len(PILLARS)]
        idea = random.choice(niche_data[pillar])
        content_format = random.choice(FORMAT_OPTIONS[pillar])
        cta = random.choice(CTA_OPTIONS[pillar])

        rows.append({
            "Hari": day,
            "Jenis Konten": pillar.title(),
            "Ide Konten": idea,
            "Format": content_format,
            "CTA": cta
        })

    return pd.DataFrame(rows)

# -------------------------
# UI
# -------------------------
col1, col2 = st.columns(2)

with col1:
    niche = st.selectbox("Pilih niche bisnis", list(NICHE_TOPICS.keys()))
    days = st.slider("Jumlah hari konten", min_value=7, max_value=30, value=14)

with col2:
    st.info(
        "Tool ini membuat ide konten berdasarkan niche bisnis dan rotasi jenis konten.\n\n"
        "Cocok untuk UMKM, admin sosmed, dan content creator."
    )

if st.button("Generate Content Calendar"):
    df = generate_calendar(niche, days)

    st.subheader("Hasil Content Calendar")
    st.dataframe(df, use_container_width=True)

    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name=f"content_calendar_{niche.lower().replace(' ', '_')}.csv",
        mime="text/csv"
    )