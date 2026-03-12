import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Kalyani Medical Hall", page_icon="💊", layout="wide")

# ─────────────────────────────────────────────
# TRANSLATIONS
# ─────────────────────────────────────────────

LANG = {
    "en": {
        "dashboard": "Dashboard", "inventory": "Inventory & Purchase",
        "sales": "Sales", "customers": "Customers", "staff": "Staff",
        "doctors": "Doctors", "expenses": "Expenses", "online_store": "Online Store",
        "today_sales": "Today's Sales", "today_profit": "Today's Profit",
        "today_expenses": "Today's Expenses", "low_stock": "Low Stock",
        "suppliers": "Suppliers", "add": "Add", "save": "Save",
        "search": "Search", "category": "Category", "price": "Price ₹",
        "stock": "Stock", "total": "Total ₹", "profit": "Profit ₹",
        "name": "Name", "phone": "Phone", "role": "Role", "salary": "Salary ₹",
        "amount": "Amount ₹", "new_sale": "➕ New Sale",
        "contact": "Contact Us", "years_trust": "30 Years Trust with Empathy and Care",
        "location": "Putsuri, Burdwan, WB", "recent_sales": "Recent Sales",
        "blood_group": "Blood Group", "points": "Points",
        "specialty": "Specialty", "hospital": "Hospital",
        "add_medicine": "Add Medicine", "add_supplier": "Add Supplier",
        "add_customer": "Add Customer", "add_staff": "Add Staff",
        "add_expense": "Add Expense", "add_doctor": "Add Doctor",
        "add_to_cart": "Add to Cart", "cart": "Cart",
        "checkout": "Checkout",
    },
    "bn": {
        "dashboard": "ড্যাশবোর্ড", "inventory": "মজুদ ও ক্রয়",
        "sales": "বিক্রয়", "customers": "গ্রাহক", "staff": "কর্মী",
        "doctors": "ডাক্তার", "expenses": "খরচ", "online_store": "অনলাইন স্টোর",
        "today_sales": "আজকের বিক্রয়", "today_profit": "আজকের লাভ",
        "today_expenses": "আজকের খরচ", "low_stock": "কম স্টক",
        "suppliers": "সরবরাহকারী", "add": "যোগ", "save": "সংরক্ষণ",
        "search": "খুঁজুন", "category": "শ্রেণী", "price": "দাম ₹",
        "stock": "স্টক", "total": "মোট ₹", "profit": "লাভ ₹",
        "name": "নাম", "phone": "ফোন", "role": "পদ", "salary": "বেতন ₹",
        "amount": "পরিমাণ ₹", "new_sale": "➕ নতুন বিক্রয়",
        "contact": "যোগাযোগ", "years_trust": "৩০ বছরের বিশ্বাস ও সেবা",
        "location": "পুটসুড়ি, বর্ধমান, পশ্চিমবঙ্গ", "recent_sales": "সাম্প্রতিক বিক্রয়",
        "blood_group": "রক্তের গ্রুপ", "points": "পয়েন্ট",
        "specialty": "বিশেষত্ব", "hospital": "হাসপাতাল",
        "add_medicine": "ওষুধ যোগ", "add_supplier": "সরবরাহকারী যোগ",
        "add_customer": "গ্রাহক যোগ", "add_staff": "কর্মী যোগ",
        "add_expense": "খরচ যোগ", "add_doctor": "ডাক্তার যোগ",
        "add_to_cart": "কার্টে যোগ", "cart": "কার্ট",
        "checkout": "চেকআউট",
    },
}

# ─────────────────────────────────────────────
# SESSION STATE / DEMO DATA
# ─────────────────────────────────────────────

def init():
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "page" not in st.session_state:
        st.session_state.page = "dashboard"
    if "cart" not in st.session_state:
        st.session_state.cart = []

    if "inventory" not in st.session_state:
        st.session_state.inventory = [
            {"id": i+1, "name": n, "category": c, "price": p, "cost": co, "stock": s, "expiry": e, "min_stock": m, "manufacturer": mfr}
            for i, (n, c, p, co, s, e, m, mfr) in enumerate([
                ("Paracetamol 500mg",  "Pain/Fever",  30,  18, 150, "2027-06", 50, "Cipla"),
                ("Metformin 500mg",    "Diabetes",    45,  28,  80, "2027-03", 50, "Sun Pharma"),
                ("Amlodipine 5mg",     "BP/Heart",    35,  20, 120, "2027-01", 50, "Zydus"),
                ("Cetirizine 10mg",    "Allergy",     25,  15, 200, "2027-08", 50, "Dr. Reddy's"),
                ("Azithromycin 500mg", "Antibiotic", 120,  85,  25, "2026-12", 30, "Cipla"),
                ("Pantoprazole 40mg",  "Gastric",     85,  55,  15, "2027-04", 30, "Lupin"),
                ("Aspirin 75mg",       "BP/Heart",    28,  15, 180, "2027-12", 50, "USV"),
                ("Glimepiride 1mg",    "Diabetes",    55,  35,  45, "2027-06", 50, "Abbott"),
                ("Omeprazole 20mg",    "Gastric",     30,  18,  35, "2027-02", 40, "Cipla"),
                ("Vitamin B Complex",  "Vitamin",     45,  28, 100, "2027-11", 50, "Mankind"),
            ])
        ]

    if "suppliers" not in st.session_state:
        st.session_state.suppliers = [
            {"id": 1, "name": "Amit Pharma Distributors", "phone": "9831234567", "address": "Kolkata",  "balance": 50000},
            {"id": 2, "name": "Bengal Medical Co",         "phone": "9876543210", "address": "Asansol",  "balance": 35000},
            {"id": 3, "name": "City Drug House",            "phone": "9901234567", "address": "Durgapur", "balance": 25000},
        ]

    if "staff" not in st.session_state:
        st.session_state.staff = [
            {"id": 1, "name": "Rajesh Kumar", "phone": "9123456789", "role": "Manager",    "salary": 18000},
            {"id": 2, "name": "Sunita Devi",  "phone": "9876543211", "role": "Pharmacist", "salary": 15000},
            {"id": 3, "name": "Mohan Lal",    "phone": "9812345678", "role": "Helper",     "salary": 10000},
        ]

    if "customers" not in st.session_state:
        st.session_state.customers = [
            {"id": 1, "name": "Babulal Saha",    "phone": "9876111222", "blood_group": "B+", "allergies": "Penicillin", "points": 150,  "balance": 0},
            {"id": 2, "name": "Usha Rani",        "phone": "9876333444", "blood_group": "O+", "allergies": "",           "points": 320,  "balance": 500},
            {"id": 3, "name": "Subhash Chandra",  "phone": "9876555666", "blood_group": "A+", "allergies": "Aspirin",    "points": 80,   "balance": 0},
        ]

    if "doctors" not in st.session_state:
        st.session_state.doctors = [
            {"id": 1, "name": "Dr. Anjan Sen",  "phone": "9001234567", "specialty": "General Medicine", "hospital": "Sen Clinic",    "patients": 45},
            {"id": 2, "name": "Dr. Moushumi",   "phone": "9901234567", "specialty": "Gynecologist",     "hospital": "Maternity Home", "patients": 30},
            {"id": 3, "name": "Dr. Tapan Das",  "phone": "9831234567", "specialty": "Cardiologist",     "hospital": "Heart Care",     "patients": 25},
        ]

    if "sales" not in st.session_state:
        today = str(date.today())
        st.session_state.sales = [
            {"id": 1, "customer": "Babulal Saha",   "items": "Paracetamol 500mg x2, Cetirizine 10mg x1", "total": 85,  "profit": 28, "payment": "Cash", "time": "10:30 AM", "date": today},
            {"id": 2, "customer": "Usha Rani",       "items": "Metformin 500mg x3, Amlodipine 5mg x1",   "total": 170, "profit": 63, "payment": "UPI",  "time": "11:15 AM", "date": today},
            {"id": 3, "customer": "Subhash Chandra", "items": "Aspirin 75mg x2",                          "total": 56,  "profit": 26, "payment": "Cash", "time": "12:00 PM", "date": today},
        ]

    if "expenses" not in st.session_state:
        today = str(date.today())
        st.session_state.expenses = [
            {"id": 1, "category": "Rent",        "amount": 15000, "date": today, "note": "Monthly Shop Rent"},
            {"id": 2, "category": "Electricity", "amount": 2500,  "date": today, "note": "Monthly Bill"},
            {"id": 3, "category": "Salary",      "amount": 43000, "date": today, "note": "March Salaries"},
        ]

init()
t = LANG[st.session_state.lang]

# ─────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@400;600&display=swap');
    * { font-family: 'Outfit', 'Noto Sans Bengali', sans-serif !important; }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f4c75 0%, #1b6ca8 60%, #118ab2 100%) !important;
    }
    section[data-testid="stSidebar"] * { color: #ffffff !important; }
    div[data-testid="stMetric"] {
        background: white; border-radius: 16px;
        padding: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        border-left: 4px solid #1b6ca8;
    }
    .stButton > button {
        border-radius: 12px; font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────

with st.sidebar:
    # Language
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🇬🇧 EN", use_container_width=True, key="l_en"):
            st.session_state.lang = "en"; st.rerun()
    with c2:
        if st.button("🇧🇩 বাং", use_container_width=True, key="l_bn"):
            st.session_state.lang = "bn"; st.rerun()

    st.markdown("""
    <div style="text-align:center;padding:18px 0 10px;">
        <div style="font-size:3rem;">💊</div>
        <h2 style="color:#a8d8ea !important;margin:4px 0;font-size:1.4rem;">Kalyani Medical Hall</h2>
        <p style="color:#cce7ff;font-size:0.8rem;margin:0;">Putsuri, Burdwan, WB</p>
        <p style="color:#90caf9;font-size:0.85rem;margin:8px 0 0;">📞 9619464843</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    nav_items = [
        ("🏠", t["dashboard"],    "dashboard"),
        ("💰", t["sales"],        "sales"),
        ("📦", t["inventory"],    "inventory"),
        ("🧑‍🤝‍🧑", t["customers"], "customers"),
        ("👥", t["staff"],        "staff"),
        ("👨‍⚕️", t["doctors"],    "doctors"),
        ("💸", t["expenses"],     "expenses"),
        ("🛍️", t["online_store"], "online_store"),
    ]
    for icon, label, key in nav_items:
        if st.button(f"{icon}  {label}", use_container_width=True, key=f"nav_{key}"):
            st.session_state.page = key; st.rerun()

    st.markdown("---")
    st.markdown(f"<p style='color:#90caf9;font-size:0.72rem;text-align:center;'>{t['years_trust']}</p>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────

page = st.session_state.page

# ── DASHBOARD ──────────────────────────────
if page == "dashboard":
    st.markdown("## 💊 Kalyani Medical Hall")
    st.caption(t["location"] + "  |  " + t["years_trust"])
    st.divider()

    today = str(date.today())
    today_sales   = sum(s["total"]  for s in st.session_state.sales    if s["date"] == today)
    today_profit  = sum(s["profit"] for s in st.session_state.sales    if s["date"] == today)
    today_exp     = sum(e["amount"] for e in st.session_state.expenses  if e["date"] == today)
    low_stock_cnt = sum(1 for i in st.session_state.inventory if i["stock"] < i["min_stock"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"📊 {t['today_sales']}",   f"₹{today_sales:,}")
    c2.metric(f"📈 {t['today_profit']}",  f"₹{today_profit:,}")
    c3.metric(f"💸 {t['today_expenses']}", f"₹{today_exp:,}")
    c4.metric(f"⚠️ {t['low_stock']}",     str(low_stock_cnt))

    st.divider()
    st.markdown(f"### 🏢 {t['suppliers']}")
    for s in st.session_state.suppliers:
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(f"**{s['name']}**")
            c2.write(f"📞 {s['phone']}")
            c3.write(f"💰 ₹{s['balance']:,}")

    st.divider()
    st.markdown("### 📋 Recent Sales")
    for s in st.session_state.sales[-3:]:
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            c1.write(f"**{s['customer']}** — {s['items']}")
            c2.write(f"₹{s['total']}  🕐 {s['time']}")

# ── SALES ──────────────────────────────────
elif page == "sales":
    st.markdown(f"## 💰 {t['sales']}")
    st.divider()

    # New Sale
    with st.expander(t["new_sale"], expanded=False):
        with st.form("new_sale_form"):
            c1, c2 = st.columns(2)
            customer = c1.text_input(t["customers"])
            payment  = c2.selectbox("Payment", ["Cash", "UPI", "Card", "Credit"])
            medicines = [m["name"] for m in st.session_state.inventory]
            med       = st.selectbox(t["inventory"], medicines)
            qty       = st.number_input("Qty", min_value=1, value=1)
            if st.form_submit_button(t["save"]):
                inv_item = next((m for m in st.session_state.inventory if m["name"] == med), None)
                if inv_item:
                    total  = inv_item["price"] * qty
                    profit = (inv_item["price"] - inv_item["cost"]) * qty
                    new_id = max((s["id"] for s in st.session_state.sales), default=0) + 1
                    st.session_state.sales.append({
                        "id": new_id, "customer": customer or "Walk-in",
                        "items": f"{med} x{qty}", "total": total, "profit": profit,
                        "payment": payment, "time": datetime.now().strftime("%I:%M %p"),
                        "date": str(date.today()),
                    })
                    st.success(f"Sale recorded — ₹{total}")
                    st.rerun()

    st.markdown(f"### {t['recent_sales']}")
    for s in reversed(st.session_state.sales):
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 1, 1])
            c1.write(f"**{s['customer']}**  \n{s['items']}")
            c2.write(f"₹{s['total']}")
            c3.write(f"🕐 {s['time']}")

# ── INVENTORY ──────────────────────────────
elif page == "inventory":
    st.markdown(f"## 📦 {t['inventory']}")
    st.divider()

    search = st.text_input(f"🔍 {t['search']}")
    cats   = ["All"] + sorted({m["category"] for m in st.session_state.inventory})
    cat    = st.selectbox(t["category"], cats)

    items = st.session_state.inventory
    if search:
        items = [m for m in items if search.lower() in m["name"].lower()]
    if cat != "All":
        items = [m for m in items if m["category"] == cat]

    for m in items:
        low = m["stock"] < m["min_stock"]
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            c1.write(f"**{m['name']}**  \n{m['manufacturer']} · {m['category']}")
            c2.metric(t["stock"], m["stock"], delta=None if not low else "Low ⚠️")
            c3.metric(t["price"], f"₹{m['price']}")
            c4.write(f"Exp: {m['expiry']}")

    st.divider()
    with st.expander(f"➕ {t['add_medicine']}"):
        with st.form("add_med"):
            c1, c2 = st.columns(2)
            name   = c1.text_input(t["name"])
            cat_i  = c2.text_input(t["category"])
            price  = c1.number_input(t["price"], min_value=0)
            cost   = c2.number_input("Cost ₹", min_value=0)
            stock  = c1.number_input(t["stock"], min_value=0, value=0)
            mfr    = c2.text_input("Manufacturer")
            if st.form_submit_button(t["save"]) and name:
                new_id = max(m["id"] for m in st.session_state.inventory) + 1
                st.session_state.inventory.append({
                    "id": new_id, "name": name, "category": cat_i, "price": price,
                    "cost": cost, "stock": stock, "expiry": "2027-12",
                    "min_stock": 30, "manufacturer": mfr,
                })
                st.success(f"Added {name}")
                st.rerun()

    st.divider()
    st.markdown(f"### 🏢 {t['suppliers']}")
    for s in st.session_state.suppliers:
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(f"**{s['name']}**  \n📍 {s['address']}")
            c2.write(f"📞 {s['phone']}")
            c3.metric("Balance", f"₹{s['balance']:,}")

    with st.expander(f"➕ {t['add_supplier']}"):
        with st.form("add_sup"):
            c1, c2 = st.columns(2)
            sname   = c1.text_input(t["name"])
            sphone  = c2.text_input(t["phone"])
            saddr   = st.text_input(t["address"] if "address" in t else "Address")
            if st.form_submit_button(t["save"]) and sname:
                new_id = max(s["id"] for s in st.session_state.suppliers) + 1
                st.session_state.suppliers.append({"id": new_id, "name": sname, "phone": sphone, "address": saddr, "balance": 0})
                st.success(f"Added {sname}")
                st.rerun()

# ── CUSTOMERS ──────────────────────────────
elif page == "customers":
    st.markdown(f"## 🧑‍🤝‍🧑 {t['customers']}")
    st.divider()

    search = st.text_input(f"🔍 {t['search']}")
    items  = st.session_state.customers
    if search:
        items = [c for c in items if search.lower() in c["name"].lower() or search in c["phone"]]

    for c in items:
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            c1.write(f"**{c['name']}**  \n📞 {c['phone']}")
            c2.write(f"🩸 {c['blood_group']}")
            c3.write(f"⭐ {c['points']} pts")
            if c["balance"] > 0:
                c4.error(f"₹{c['balance']} due")
            else:
                c4.success("Cleared")

    st.divider()
    with st.expander(f"➕ {t['add_customer']}"):
        with st.form("add_cust"):
            c1, c2 = st.columns(2)
            cname  = c1.text_input(t["name"])
            cphone = c2.text_input(t["phone"])
            cblood = c1.selectbox(t["blood_group"], ["A+","A-","B+","B-","O+","O-","AB+","AB-"])
            callergy = c2.text_input("Allergies")
            if st.form_submit_button(t["save"]) and cname:
                new_id = max(c["id"] for c in st.session_state.customers) + 1
                st.session_state.customers.append({"id": new_id, "name": cname, "phone": cphone, "blood_group": cblood, "allergies": callergy, "points": 0, "balance": 0})
                st.success(f"Added {cname}")
                st.rerun()

# ── STAFF ──────────────────────────────────
elif page == "staff":
    st.markdown(f"## 👥 {t['staff']}")
    st.divider()

    for s in st.session_state.staff:
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(f"**{s['name']}**  \n{s['role']}")
            c2.write(f"📞 {s['phone']}")
            c3.metric(t["salary"], f"₹{s['salary']:,}")

    st.divider()
    with st.expander(f"➕ {t['add_staff']}"):
        with st.form("add_staff"):
            c1, c2 = st.columns(2)
            sname   = c1.text_input(t["name"])
            sphone  = c2.text_input(t["phone"])
            srole   = c1.selectbox(t["role"], ["Manager","Pharmacist","Sales Staff","Compounder","Helper","Delivery Boy"])
            ssalary = c2.number_input(t["salary"], min_value=0, value=10000)
            if st.form_submit_button(t["save"]) and sname:
                new_id = max(s["id"] for s in st.session_state.staff) + 1
                st.session_state.staff.append({"id": new_id, "name": sname, "phone": sphone, "role": srole, "salary": ssalary})
                st.success(f"Added {sname}")
                st.rerun()

# ── DOCTORS ────────────────────────────────
elif page == "doctors":
    st.markdown(f"## 👨‍⚕️ {t['doctors']}")
    st.divider()

    for d in st.session_state.doctors:
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 2, 1])
            c1.write(f"**{d['name']}**  \n{d['specialty']}")
            c2.write(f"🏥 {d['hospital']}  \n📞 {d['phone']}")
            c3.metric("Patients", d["patients"])

    st.divider()
    with st.expander(f"➕ {t['add_doctor']}"):
        with st.form("add_doc"):
            c1, c2 = st.columns(2)
            dname  = c1.text_input(t["name"])
            dphone = c2.text_input(t["phone"])
            dspec  = c1.text_input(t["specialty"])
            dhosp  = c2.text_input(t["hospital"])
            if st.form_submit_button(t["save"]) and dname:
                new_id = max(d["id"] for d in st.session_state.doctors) + 1
                st.session_state.doctors.append({"id": new_id, "name": dname, "phone": dphone, "specialty": dspec, "hospital": dhosp, "patients": 0})
                st.success(f"Added {dname}")
                st.rerun()

# ── EXPENSES ───────────────────────────────
elif page == "expenses":
    st.markdown(f"## 💸 {t['expenses']}")
    st.divider()

    total_exp = sum(e["amount"] for e in st.session_state.expenses)
    st.metric("Total Expenses", f"₹{total_exp:,}")
    st.divider()

    for e in reversed(st.session_state.expenses):
        with st.container(border=True):
            c1, c2, c3 = st.columns([2, 3, 1])
            c1.write(f"**{e['category']}**")
            c2.write(f"{e['note']}  \n📅 {e['date']}")
            c3.metric("", f"₹{e['amount']:,}")

    st.divider()
    with st.expander(f"➕ {t['add_expense']}"):
        with st.form("add_exp"):
            c1, c2 = st.columns(2)
            ecat  = c1.selectbox(t["category"], ["Rent","Electricity","Salary","Transport","Internet","Maintenance","Other"])
            eamt  = c2.number_input(t["amount"], min_value=0)
            enote = st.text_input("Note")
            if st.form_submit_button(t["save"]) and eamt > 0:
                new_id = max(e["id"] for e in st.session_state.expenses) + 1
                st.session_state.expenses.append({"id": new_id, "category": ecat, "amount": eamt, "date": str(date.today()), "note": enote})
                st.success(f"Added ₹{eamt} ({ecat})")
                st.rerun()

# ── ONLINE STORE ───────────────────────────
elif page == "online_store":
    st.markdown(f"## 🛍️ {t['online_store']}")
    st.divider()

    cart_count = len(st.session_state.cart)
    if cart_count:
        st.info(f"🛒 {t['cart']}: {cart_count} item(s) — ₹{sum(i['total'] for i in st.session_state.cart):,}")

    search = st.text_input(f"🔍 {t['search']}")
    products = st.session_state.inventory
    if search:
        products = [m for m in products if search.lower() in m["name"].lower()]

    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx % 3]:
            with st.container(border=True):
                st.write(f"**{p['name']}**")
                st.caption(p["category"])
                st.write(f"₹{p['price']}")
                qty = st.number_input("Qty", min_value=1, value=1, key=f"qty_{p['id']}")
                if st.button(t["add_to_cart"], key=f"cart_{p['id']}"):
                    existing = next((x for x in st.session_state.cart if x["id"] == p["id"]), None)
                    if existing:
                        existing["qty"]   += qty
                        existing["total"] += p["price"] * qty
                    else:
                        st.session_state.cart.append({"id": p["id"], "name": p["name"], "price": p["price"], "qty": qty, "total": p["price"] * qty})
                    st.rerun()

    if st.session_state.cart:
        st.divider()
        st.markdown(f"### 🛒 {t['cart']}")
        cart_total = 0
        for item in st.session_state.cart:
            c1, c2, c3 = st.columns([4, 1, 1])
            c1.write(f"{item['name']} × {item['qty']}")
            c2.write(f"₹{item['total']}")
            if c3.button("✕", key=f"rm_{item['id']}"):
                st.session_state.cart.remove(item)
                st.rerun()
            cart_total += item["total"]

        st.metric("Total", f"₹{cart_total:,}")
        if st.button(f"✅ {t['checkout']}", type="primary"):
            st.session_state.cart = []
            st.success("Order placed!")
            st.rerun()
