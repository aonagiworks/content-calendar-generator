import random
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Content Calendar Generator",
    page_icon="🗓️",
    layout="wide"
)

# -------------------------
# HEADER
# -------------------------
st.title("🗓️ Content Calendar Generator")
st.markdown(
    "Buat ide konten otomatis untuk **UMKM, content creator, dan bisnis kecil** "
    "tanpa ribet."
)

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
    },

    "Makanan Rumahan": {
        "edukasi": [
            "Tips menyimpan makanan agar tetap fresh",
            "Kenapa makanan rumahan lebih nyaman dikonsumsi",
            "Menu rumahan yang cocok untuk bekal",
            "Tips memilih lauk yang praktis"
        ],
        "promo": [
            "Promo paket hemat menu harian",
            "Diskon spesial order hari ini",
            "Promo bundling lauk dan nasi",
            "Gratis ongkir untuk area tertentu"
        ],
        "testimoni": [
            "Review pelanggan tentang rasa makanan",
            "Cerita pelanggan yang repeat order",
            "Testimoni menu favorit minggu ini",
            "Feedback pelanggan soal porsi dan rasa"
        ],
        "behind the scenes": [
            "Proses masak di dapur",
            "Persiapan bahan baku segar",
            "Suasana packing order pagi hari",
            "Tim menyiapkan menu harian"
        ],
        "faq": [
            "Apakah menu bisa request pedas?",
            "Apakah menerima pre-order?",
            "Jam pengiriman mulai kapan?",
            "Berapa lama makanan tahan?"
        ],
        "engagement": [
            "Tim sambal atau non-sambal?",
            "Menu favorit kamu lauk apa?",
            "Lebih suka ayam atau ikan?",
            "Vote menu yang harus hadir minggu depan"
        ],
        "soft selling": [
            "Pilihan menu rumahan untuk makan siang",
            "Solusi makan praktis tanpa ribet",
            "Menu hangat yang cocok buat keluarga",
            "Rekomendasi lauk harian yang hemat"
        ]
    },

    "Jasa Desain": {
        "edukasi": [
            "Pentingnya desain visual untuk brand",
            "Kesalahan umum dalam desain promosi",
            "Tips memilih warna brand",
            "Kenapa desain konsisten itu penting"
        ],
        "promo": [
            "Promo jasa desain bulan ini",
            "Diskon khusus logo dan feed desain",
            "Paket hemat desain UMKM",
            "Promo untuk klien pertama"
        ],
        "testimoni": [
            "Review klien setelah redesign brand",
            "Cerita klien yang puas dengan hasil desain",
            "Feedback soal proses revisi yang nyaman",
            "Testimoni hasil desain untuk promosi"
        ],
        "behind the scenes": [
            "Proses brainstorming desain",
            "Tampilan workspace desain",
            "Proses revisi dari draft ke final",
            "Behind the scenes pengerjaan project"
        ],
        "faq": [
            "Berapa lama pengerjaan desain?",
            "Apakah ada revisi?",
            "Format file yang didapat apa saja?",
            "Bisa desain untuk UMKM kecil?"
        ],
        "engagement": [
            "Lebih suka desain minimalis atau ramai?",
            "Warna brand favorit kamu apa?",
            "Logo simpel atau detail?",
            "Vote desain A atau B"
        ],
        "soft selling": [
            "Desain yang bikin brand terlihat lebih profesional",
            "Solusi visual untuk promosi bisnis kecil",
            "Tampilan feed yang lebih rapi dan menarik",
            "Desain yang bantu bisnis lebih stand out"
        ]
    },

    "Bengkel": {
        "edukasi": [
            "Tanda motor perlu servis",
            "Pentingnya ganti oli tepat waktu",
            "Cara merawat motor agar awet",
            "Kesalahan kecil yang bikin kendaraan cepat rusak"
        ],
        "promo": [
            "Promo servis minggu ini",
            "Diskon ganti oli hari ini",
            "Paket hemat servis ringan",
            "Promo khusus pelanggan baru"
        ],
        "testimoni": [
            "Review pelanggan setelah servis",
            "Cerita pelanggan yang puas dengan hasil kerja",
            "Testimoni tentang pelayanan bengkel",
            "Feedback pelanggan soal kecepatan servis"
        ],
        "behind the scenes": [
            "Mekanik sedang melakukan pengecekan",
            "Suasana bengkel di pagi hari",
            "Proses servis kendaraan pelanggan",
            "Kegiatan tim bengkel sehari-hari"
        ],
        "faq": [
            "Berapa lama proses servis?",
            "Apakah bisa booking dulu?",
            "Apakah tersedia sparepart tertentu?",
            "Jam operasional bengkel kapan?"
        ],
        "engagement": [
            "Kamu rutin servis tiap berapa bulan?",
            "Lebih pilih servis pagi atau sore?",
            "Masalah motor yang paling sering kamu alami apa?",
            "Pilih motor matic atau manual?"
        ],
        "soft selling": [
            "Saatnya cek kondisi kendaraan kamu",
            "Servis rutin untuk perjalanan lebih nyaman",
            "Biar motor tetap enak dipakai harian",
            "Perawatan kendaraan tanpa ribet"
        ]
    },

    "Toko Aksesoris": {
        "edukasi": [
            "Tips memilih aksesoris sesuai outfit",
            "Cara merawat aksesoris agar tahan lama",
            "Aksesoris simpel yang bikin look lebih menarik",
            "Perbedaan aksesoris harian dan formal"
        ],
        "promo": [
            "Promo aksesoris minggu ini",
            "Diskon pembelian item pilihan",
            "Bundling hemat aksesoris favorit",
            "Promo spesial pelanggan setia"
        ],
        "testimoni": [
            "Review pelanggan tentang kualitas produk",
            "Foto pelanggan memakai aksesoris favorit",
            "Feedback soal packaging dan kualitas",
            "Testimoni pelanggan repeat order"
        ],
        "behind the scenes": [
            "Proses packing order aksesoris",
            "Suasana menyiapkan stok produk",
            "Kegiatan cek kualitas barang",
            "Persiapan launching koleksi baru"
        ],
        "faq": [
            "Apakah bahan aman dipakai harian?",
            "Apakah ada garansi produk?",
            "Bagaimana cara order?",
            "Apakah bisa gift wrapping?"
        ],
        "engagement": [
            "Lebih suka aksesoris gold atau silver?",
            "Pilih style minimalis atau statement?",
            "Item favorit kamu cincin, gelang, atau kalung?",
            "Vote produk favorit minggu ini"
        ],
        "soft selling": [
            "Aksesoris simpel untuk tampilan lebih manis",
            "Pilihan item yang cocok untuk daily wear",
            "Produk yang bikin outfit makin lengkap",
            "Aksesoris yang cocok untuk hadiah"
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
# FUNCTION
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
            "Format Konten": content_format,
            "CTA": cta
        })

    return pd.DataFrame(rows)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.header("⚙️ Pengaturan")
niche = st.sidebar.selectbox("Pilih niche bisnis", list(NICHE_TOPICS.keys()))
days = st.sidebar.slider("Jumlah hari konten", min_value=7, max_value=30, value=14)
generate_button = st.sidebar.button("Generate Calendar")

# -------------------------
# MAIN CONTENT
# -------------------------
col_a, col_b, col_c = st.columns(3)
col_a.metric("Total Niche", len(NICHE_TOPICS))
col_b.metric("Jenis Konten", len(PILLARS))
col_c.metric("Maksimal Hari", "30")

st.divider()

if generate_button:
    df = generate_calendar(niche, days)

    st.success(f"Content calendar untuk niche **{niche}** berhasil dibuat.")

    st.subheader("📋 Hasil Content Calendar")
    st.dataframe(df, use_container_width=True)

    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name=f"content_calendar_{niche.lower().replace(' ', '_')}.csv",
        mime="text/csv"
    )

    st.subheader("💡 Insight Singkat")
    st.write(f"- Niche bisnis: **{niche}**")
    st.write(f"- Jumlah hari konten: **{days} hari**")
    st.write(f"- Total ide konten yang dihasilkan: **{len(df)}**")

else:
    st.info("Pilih niche bisnis dan jumlah hari di sidebar, lalu klik **Generate Calendar**.")