import streamlit as st
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Kalyani Medical Hall", page_icon="💊", layout="wide")

# ============================================================
# LANGUAGE
# ============================================================

if 'lang' not in st.session_state:
    st.session_state.lang = "en"

# Translations
translations = {
    "en": {
        "dashboard": "Dashboard", "sales": "Sales", "inventory": "Inventory",
        "purchases": "Purchases", "suppliers": "Suppliers", "staff": "Staff",
        "customers": "Customers", "doctors": "Doctors", "expenses": "Expenses",
        "reports": "Reports", "online_store": "Online Store", "online_orders": "Online Orders",
        "today_sales": "Today's Sales", "today_profit": "Today's Profit", "today_expenses": "Today's Expenses",
        "mtd_sales": "MTD Sales", "mtd_profit": "MTD Profit",
        "doctor_appointments": "Doctor Appointments", "todays_appointments": "Today's Appointments",
        "low_stock": "Low Stock", "medicines": "Medicines", "add": "Add", "save": "Save",
        "search": "Search", "category": "Category", "price": "Price", "stock": "Stock",
        "total": "Total", "customer": "Customer", "payment": "Payment", "profit": "Profit",
        "name": "Name", "phone": "Phone", "address": "Address", "role": "Role",
        "salary": "Salary", "amount": "Amount", "note": "Note", "status": "Status",
        "pending": "Pending", "ordered": "Ordered", "received": "Received",
        "active": "Active", "cash": "Cash", "upi": "UPI", "card": "Card", "credit": "Credit",
        "new_sale": "New Sale", "add_medicine": "Add Medicine", "add_supplier": "Add Supplier",
        "add_staff": "Add Staff", "add_customer": "Add Customer", "record_visit": "Record Visit",
        "add_expense": "Add Expense", "create_order": "Create Order", "add_to_cart": "Add to Cart",
        "attach_doc": "Attach Document",
        "this_month": "This Month", "overview": "Overview", "all_well": "All medicines well stocked!",
        "contact": "Contact Us",         "years_trust": "30 Years Trust with Empathy and Care", "by": "By Apurba Koner (Nupur)",
        "location": "Putsuri, Burdwan, WB", "tagline": "Empathy n Care"
    },
    "bn": {
        "dashboard": "ড্যাশবোর্ড", "sales": "বিক্রয়", "inventory": "মজুদ",
        "purchases": "ক্রয়", "suppliers": "সরবরাহকারী", "staff": "কর্মী",
        "customers": "গ্রাহক", "doctors": "ডাক্তার", "expenses": "খরচ",
        "reports": "রিপোর্ট", "online_store": "অনলাইন স্টোর", "online_orders": "অনলাইন অর্ডার",
        "today_sales": "আজকের বিক্রয়", "today_profit": "আজকের লাভ", "today_expenses": "আজকের খরচ",
        "mtd_sales": "এই মাসের বিক্রয়", "mtd_profit": "এই মাসের লাভ",
        "doctor_appointments": "ডাক্তার অ্যাপয়েন্টমেন্ট", "todays_appointments": "আজকের অ্যাপয়েন্টমেন্ট",
        "low_stock": "কম স্টক", "medicines": "ওষুধ", "add": "যোগ", "save": "সংরক্ষণ",
        "search": "খুঁজুন", "category": "শ্রেণী", "price": "দাম", "stock": "স্টক",
        "total": "মোট", "customer": "গ্রাহক", "payment": "পেমেন্ট", "profit": "লাভ",
        "name": "নাম", "phone": "ফোন", "address": "ঠিকানা", "role": "পদ",
        "salary": "বেতন", "amount": "পরিমাণ", "note": "নোট", "status": "অবস্থা",
        "pending": "মেয়াদী", "ordered": "অর্ডার হয়েছে", "received": "প্রাপ্ত",
        "active": "সক্রিয়", "cash": "নগদ", "upi": "UPI", "card": "কার্ড", "credit": "বাকি",
        "new_sale": "নতুন বিক্রয়", "add_medicine": "ওষুধ যোগ", "add_supplier": "সরবরাহকারী যোগ",
        "add_staff": "কর্মী যোগ", "add_customer": "গ্রাহক যোগ", "record_visit": "ভিজিট রেকর্ড",
        "add_expense": "খরচ যোগ", "create_order": "অর্ডার তৈরি", "add_to_cart": "কার্টে যোগ",
        "attach_doc": "ডকুমেন্ট সংযুক্ত করুন",
        "this_month": "এই মাস", "overview": "ওভারভিউ", "all_well": "সব ওষুধ মজুদ আছে!",
        "contact": "যোগাযোগ", "years_trust": "৩০ বছরের বিশ্বাস ও সেবা", "by": "অপূর্ব কোনার (নুপুর)",
        "location": "পুটসুড়ি, বর্ধমান, পশ্চিমবঙ্গ", "tagline": "সহানুভূতির সাথে সেবা"
    }
}

t = translations[st.session_state.lang]

# ============================================================
# DATABASE
# ============================================================

def init_db():
    from datetime import datetime, timedelta
    
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    last_week = today - timedelta(days=7)
    
    if 'inventory' not in st.session_state:
        st.session_state.inventory = [
            {"id": 1, "name": "Paracetamol 500mg", "category": "Pain/Fever", "price": 30, "cost": 18, "stock": 150, "expiry": "2027-06", "min_stock": 50, "manufacturer": "Cipla", "gst": 12, "batch_no": "P001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 2, "name": "Metformin 500mg", "category": "Diabetes", "price": 45, "cost": 28, "stock": 80, "expiry": "2027-03", "min_stock": 50, "manufacturer": "Sun Pharma", "gst": 12, "batch_no": "M001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 3, "name": "Amlodipine 5mg", "category": "BP/Heart", "price": 35, "cost": 20, "stock": 120, "expiry": "2027-01", "min_stock": 50, "manufacturer": "Zydus", "gst": 12, "batch_no": "A001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 4, "name": "Cetirizine 10mg", "category": "Allergy", "price": 25, "cost": 15, "stock": 200, "expiry": "2027-08", "min_stock": 50, "manufacturer": "Dr. Reddy's", "gst": 12, "batch_no": "C001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 5, "name": "Azithromycin 500mg", "category": "Antibiotic", "price": 120, "cost": 85, "stock": 25, "expiry": "2026-12", "min_stock": 30, "manufacturer": "Cipla", "gst": 12, "batch_no": "AZ001", "hsn_code": "3004", "pack_size": "1x3"},
            {"id": 6, "name": "Pantoprazole 40mg", "category": "Gastric", "price": 85, "cost": 55, "stock": 15, "expiry": "2027-04", "min_stock": 30, "manufacturer": "Lupin", "gst": 12, "batch_no": "PP001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 7, "name": "Aspirin 75mg", "category": "BP/Heart", "price": 28, "cost": 15, "stock": 180, "expiry": "2027-12", "min_stock": 50, "manufacturer": "USV", "gst": 12, "batch_no": "AS001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 8, "name": "Glimepiride 1mg", "category": "Diabetes", "price": 55, "cost": 35, "stock": 45, "expiry": "2027-06", "min_stock": 50, "manufacturer": "Abbott", "gst": 12, "batch_no": "GL001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 9, "name": "Omeprazole 20mg", "category": "Gastric", "price": 30, "cost": 18, "stock": 35, "expiry": "2027-02", "min_stock": 40, "manufacturer": "Cipla", "gst": 12, "batch_no": "OM001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 10, "name": "Metronidazole 400mg", "category": "Antibiotic", "price": 35, "cost": 22, "stock": 90, "expiry": "2027-09", "min_stock": 40, "manufacturer": "Sun Pharma", "gst": 12, "batch_no": "MT001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 11, "name": "Amoxicillin 500mg", "category": "Antibiotic", "price": 85, "cost": 55, "stock": 60, "expiry": "2027-05", "min_stock": 40, "manufacturer": "Zydus", "gst": 12, "batch_no": "AMX001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 12, "name": "Vitamin B Complex", "category": "Vitamin", "price": 45, "cost": 28, "stock": 100, "expiry": "2027-11", "min_stock": 50, "manufacturer": "Mankind", "gst": 18, "batch_no": "VB001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 13, "name": "Calcium D3", "category": "Vitamin", "price": 120, "cost": 75, "stock": 70, "expiry": "2027-08", "min_stock": 40, "manufacturer": "Abbott", "gst": 18, "batch_no": "CD001", "hsn_code": "3004", "pack_size": "30 tablets"},
            {"id": 14, "name": "Iron Tablet", "category": "Vitamin", "price": 25, "cost": 15, "stock": 150, "expiry": "2027-10", "min_stock": 50, "manufacturer": "FDC", "gst": 12, "batch_no": "FE001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 15, "name": "Combiflam", "category": "Pain/Fever", "price": 20, "cost": 12, "stock": 200, "expiry": "2027-07", "min_stock": 60, "manufacturer": "Sanofi", "gst": 12, "batch_no": "CF001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 16, "name": "Dolo 650", "category": "Pain/Fever", "price": 35, "cost": 20, "stock": 180, "expiry": "2027-12", "min_stock": 50, "manufacturer": "Micro Labs", "gst": 12, "batch_no": "D6501", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 17, "name": "Cetcip 10mg", "category": "Allergy", "price": 45, "cost": 28, "stock": 120, "expiry": "2027-06", "min_stock": 50, "manufacturer": "Alkem", "gst": 12, "batch_no": "CT001", "hsn_code": "3004", "pack_size": "10x10"},
            {"id": 18, "name": "Augmentin 625mg", "category": "Antibiotic", "price": 320, "cost": 220, "stock": 20, "expiry": "2026-11", "min_stock": 25, "manufacturer": "GSK", "gst": 12, "batch_no": "AG001", "hsn_code": "3004", "pack_size": "1x6"},
            {"id": 19, "name": "Augmentin 625mg", "category": "Antibiotic", "price": 320, "cost": 220, "stock": 35, "expiry": "2027-08", "min_stock": 25, "manufacturer": "GSK", "gst": 12, "batch_no": "AG002", "hsn_code": "3004", "pack_size": "1x6"},
            {"id": 20, "name": "Montek LC", "category": "Allergy", "price": 95, "cost": 60, "stock": 55, "expiry": "2027-04", "min_stock": 30, "manufacturer": "Sun Pharma", "gst": 12, "batch_no": "MLC01", "hsn_code": "3004", "pack_size": "10x10"},
        ]
    
    if 'customers' not in st.session_state:
        st.session_state.customers = [
            {"id": 1, "name": "Ramesh Kumar", "phone": "9876543210", "address": "Putsuri, Burdwan", "total_spent": 15500, "visits": 45, "dob": "1975-03-15", "blood_group": "B+", "emergency": "9876543211", "allergies": "None", "points": 1550},
            {"id": 2, "name": "Sunita Devi", "phone": "9876543211", "address": "Memari, Burdwan", "total_spent": 12300, "visits": 32, "dob": "1980-07-22", "blood_group": "O+", "emergency": "9876543212", "allergies": "Penicillin", "points": 1230},
            {"id": 3, "name": "Mohan Lal", "phone": "9876543213", "address": "Burdwan Sadar", "total_spent": 8500, "visits": 20, "dob": "1968-11-05", "blood_group": "A+", "emergency": "9876543214", "allergies": "None", "points": 850},
            {"id": 4, "name": "Laxmi Shaw", "phone": "9876543215", "address": "Putsuri", "total_spent": 6200, "visits": 15, "dob": "1985-02-18", "blood_group": "AB+", "emergency": "9876543216", "allergies": "Aspirin", "points": 620},
            {"id": 5, "name": "Babulal Sharma", "phone": "9876543217", "address": "Memari", "total_spent": 15800, "visits": 52, "dob": "1970-09-30", "blood_group": "B-", "emergency": "9876543218", "allergies": "None", "points": 1580},
            {"id": 6, "name": "Anita Das", "phone": "9876543219", "address": "Burdwan", "total_spent": 9200, "visits": 28, "dob": "1990-05-12", "blood_group": "O-", "emergency": "9876543220", "allergies": "Sulpha", "points": 920},
            {"id": 7, "name": "Pranab Ghosh", "phone": "9876543221", "address": "Putsuri, Burdwan", "total_spent": 4500, "visits": 12, "dob": "1978-08-25", "blood_group": "A-", "emergency": "9876543222", "allergies": "None", "points": 450},
            {"id": 8, "name": "Usha Devi", "phone": "9876543223", "address": "Memari", "total_spent": 11200, "visits": 35, "dob": "1982-12-08", "blood_group": "B+", "emergency": "9876543224", "allergies": "None", "points": 1120},
        ]
    
    if 'staff' not in st.session_state:
        st.session_state.staff = [
            {"id": 1, "name": "Ramesh Kumar", "phone": "9876543211", "role": "Manager", "salary": 15000, "joining": "2020-01-15", "aadhar": "123456789012", "address": "Putsuri, Burdwan"},
            {"id": 2, "name": "Sunita Devi", "phone": "9876543212", "role": "Sales Staff", "salary": 10000, "joining": "2021-06-01", "aadhar": "123456789013", "address": "Memari, Burdwan"},
            {"id": 3, "name": "Mintu Shaw", "phone": "9876543213", "role": "Delivery Boy", "salary": 8000, "joining": "2022-03-10", "aadhar": "123456789014", "address": "Burdwan"},
            {"id": 4, "name": "Kabita Paul", "phone": "9876543214", "role": "Compounder", "salary": 12000, "joining": "2021-09-05", "aadhar": "123456789015", "address": "Putsuri"},
        ]
    
    if 'distributors' not in st.session_state:
        st.session_state.distributors = [
            {"id": 1, "name": "Ganga Medical Hall", "contact": "9432123456", "address": "Burdwan, Station Road", "balance": 15000},
            {"id": 2, "name": "Basu Dev & Sons", "contact": "9876543210", "address": "Kolkata, B.B.D. Bag", "balance": 8500},
            {"id": 3, "name": "Agrawal Pharma", "contact": "9432012345", "address": "Asansol", "balance": 12000},
            {"id": 4, "name": "Chatterjee Agencies", "contact": "9876123456", "address": "Durgapur", "balance": 5500},
            {"id": 5, "name": "MediCare Distributors", "contact": "9330012345", "address": "Kolkata", "balance": 20000},
        ]
    
    if 'daily_sales' not in st.session_state:
        # Generate demo data for last 6 months
        demo_sales = []
        
        # Current month (March 2026)
        demo_sales.extend([
            {"id": 1, "date": str(today), "customer": "Ramesh Kumar", "items": "Metformin 500mg x2, Amlodipine 5mg x1", "total": 135, "profit": 52, "payment": "Cash", "discount": 0, "doctor": "Dr. Amit Kumar"},
            {"id": 2, "date": str(today), "customer": "Sunita Devi", "items": "Amlodipine 5mg x3, Cetirizine 10mg x1", "total": 130, "profit": 55, "payment": "UPI", "discount": 0, "doctor": "Dr. Santanu Das"},
            {"id": 3, "date": str(today), "customer": "Mohan Lal", "items": "Paracetamol 500mg x3", "total": 90, "profit": 36, "payment": "Cash", "discount": 0, "doctor": "Dr. Amit Kumar"},
            {"id": 4, "date": str(yesterday), "customer": "Laxmi Shaw", "items": "Combiflam x2, Vitamin B Complex x1", "total": 85, "profit": 38, "payment": "UPI", "discount": 5, "doctor": "Dr. Priya Singh"},
            {"id": 5, "date": str(yesterday), "customer": "Babulal Sharma", "items": "Metformin 500mg x3, Amlodipine 5mg x2", "total": 195, "profit": 77, "payment": "Credit", "discount": 0, "doctor": "Dr. Amit Kumar"},
            {"id": 6, "date": str(last_week), "customer": "Anita Das", "items": "Azithromycin 500mg x1", "total": 120, "profit": 35, "payment": "Card", "discount": 0, "doctor": "Dr. Santanu Das"},
            {"id": 7, "date": str(last_week), "customer": "Walk-in", "items": "Paracetamol 500mg x5, Cetirizine 10mg x2", "total": 200, "profit": 90, "payment": "Cash", "discount": 10, "doctor": "None"},
        ])
        
        # February 2026
        feb_dates = [f"2026-02-{i:02d}" for i in range(1, 29)]
        import random
        doctors = ["Dr. Amit Kumar", "Dr. Santanu Das", "Dr. Priya Singh", "Dr. Subrata Mukherjee", "None"]
        customers = ["Ramesh Kumar", "Sunita Devi", "Mohan Lal", "Laxmi Shaw", "Babulal Sharma", "Anita Das", "Pranab Ghosh", "Usha Devi", "Walk-in"]
        items_list = [
            ("Metformin 500mg x2", 90, 36), ("Amlodipine 5mg x1", 35, 15), ("Paracetamol 500mg x3", 90, 36),
            ("Cetirizine 10mg x2", 50, 20), ("Vitamin B Complex x1", 45, 17), ("Calcium D3 x1", 120, 45),
            ("Combiflam x2", 40, 16), ("Azithromycin 500mg x1", 120, 35), ("Dolo 650 x2", 70, 30),
        ]
        
        sid = 8
        for d in feb_dates[:20]:  # 20 days with sales
            num_sales = random.randint(3, 8)
            for _ in range(num_sales):
                item_data = random.choice(items_list)
                demo_sales.append({
                    "id": sid, "date": d, "customer": random.choice(customers),
                    "items": item_data[0], "total": item_data[1], "profit": item_data[2],
                    "payment": random.choice(["Cash", "UPI", "Card", "Credit"]), "discount": random.choice([0, 0, 0, 5]),
                    "doctor": random.choice(doctors)
                })
                sid += 1
        
        # January 2026
        jan_dates = [f"2026-01-{i:02d}" for i in range(1, 32)]
        for d in jan_dates[:22]:
            num_sales = random.randint(4, 9)
            for _ in range(num_sales):
                item_data = random.choice(items_list)
                demo_sales.append({
                    "id": sid, "date": d, "customer": random.choice(customers),
                    "items": item_data[0], "total": item_data[1], "profit": item_data[2],
                    "payment": random.choice(["Cash", "UPI", "Card", "Credit"]), "discount": random.choice([0, 0, 0, 5, 10]),
                    "doctor": random.choice(doctors)
                })
                sid += 1
        
        # December 2025
        dec_dates = [f"2025-12-{i:02d}" for i in range(1, 32)]
        for d in dec_dates[:20]:
            num_sales = random.randint(3, 7)
            for _ in range(num_sales):
                item_data = random.choice(items_list)
                demo_sales.append({
                    "id": sid, "date": d, "customer": random.choice(customers),
                    "items": item_data[0], "total": item_data[1], "profit": item_data[2],
                    "payment": random.choice(["Cash", "UPI", "Card"]), "discount": random.choice([0, 0, 5]),
                    "doctor": random.choice(doctors)
                })
                sid += 1
        
        # November 2025
        nov_dates = [f"2025-11-{i:02d}" for i in range(1, 31)]
        for d in nov_dates[:18]:
            num_sales = random.randint(2, 6)
            for _ in range(num_sales):
                item_data = random.choice(items_list)
                demo_sales.append({
                    "id": sid, "date": d, "customer": random.choice(customers),
                    "items": item_data[0], "total": item_data[1], "profit": item_data[2],
                    "payment": random.choice(["Cash", "UPI", "Credit"]), "discount": random.choice([0, 0, 5]),
                    "doctor": random.choice(doctors)
                })
                sid += 1
        
        # October 2025
        oct_dates = [f"2025-10-{i:02d}" for i in range(1, 32)]
        for d in oct_dates[:20]:
            num_sales = random.randint(3, 7)
            for _ in range(num_sales):
                item_data = random.choice(items_list)
                demo_sales.append({
                    "id": sid, "date": d, "customer": random.choice(customers),
                    "items": item_data[0], "total": item_data[1], "profit": item_data[2],
                    "payment": random.choice(["Cash", "UPI", "Card", "Credit"]), "discount": random.choice([0, 0, 0, 5]),
                    "doctor": random.choice(doctors)
                })
                sid += 1
        
        # September 2025
        sep_dates = [f"2025-09-{i:02d}" for i in range(1, 31)]
        for d in sep_dates[:18]:
            num_sales = random.randint(2, 6)
            for _ in range(num_sales):
                item_data = random.choice(items_list)
                demo_sales.append({
                    "id": sid, "date": d, "customer": random.choice(customers),
                    "items": item_data[0], "total": item_data[1], "profit": item_data[2],
                    "payment": random.choice(["Cash", "UPI"]), "discount": random.choice([0, 0]),
                    "doctor": random.choice(doctors)
                })
                sid += 1
        
        st.session_state.daily_sales = demo_sales
    
    if 'expenses' not in st.session_state:
        demo_expenses = []
        
        # Current month expenses
        demo_expenses.extend([
            {"id": 1, "category": "Rent", "amount": 8000, "date": str(today - timedelta(days=1)), "payment": "Bank Transfer", "description": "Monthly Shop Rent", "vendor": "Property Owner"},
            {"id": 2, "category": "Electricity", "amount": 2500, "date": str(today - timedelta(days=2)), "payment": "UPI", "description": "Monthly Bill", "vendor": "WBSEB"},
            {"id": 3, "category": "Salary", "amount": 15000, "date": str(today - timedelta(days=3)), "payment": "Bank Transfer", "description": "Manager Salary", "vendor": "Ramesh Kumar"},
            {"id": 4, "category": "Salary", "amount": 10000, "date": str(today - timedelta(days=3)), "payment": "Bank Transfer", "description": "Staff Salary", "vendor": "Sunita Devi"},
            {"id": 5, "category": "Transport", "amount": 1500, "date": str(today - timedelta(days=4)), "payment": "Cash", "description": "Medicine Delivery", "vendor": "Local Transport"},
            {"id": 6, "category": "Internet", "amount": 999, "date": str(today - timedelta(days=5)), "payment": "UPI", "description": "Monthly WiFi", "vendor": "Jio Fiber"},
            {"id": 7, "category": "Maintenance", "amount": 2000, "date": str(today - timedelta(days=7)), "payment": "Cash", "description": "AC Servicing", "vendor": "Service Center"},
        ])
        
        # Monthly recurring expenses for last 6 months
        months_expenses = [
            ("2026-02", [("Rent", 8000), ("Electricity", 2200), ("Salary", 25000), ("Internet", 999)]),
            ("2026-01", [("Rent", 8000), ("Electricity", 2800), ("Salary", 25000), ("Internet", 999), ("Maintenance", 1500)]),
            ("2025-12", [("Rent", 8000), ("Electricity", 3500), ("Salary", 25000), ("Internet", 999)]),
            ("2025-11", [("Rent", 7500), ("Electricity", 2100), ("Salary", 25000), ("Internet", 999)]),
            ("2025-10", [("Rent", 7500), ("Electricity", 2400), ("Salary", 25000), ("Internet", 999), ("Transport", 2000)]),
            ("2025-09", [("Rent", 7500), ("Electricity", 2000), ("Salary", 25000), ("Internet", 899)]),
        ]
        
        eid = 8
        for month, exp_list in months_expenses:
            for exp_name, exp_amt in exp_list:
                day = random.randint(1, 28)
                demo_expenses.append({
                    "id": eid, "category": exp_name, "amount": exp_amt,
                    "date": f"{month}-{day:02d}", "payment": "Bank Transfer",
                    "description": f"Monthly {exp_name}", "vendor": "Various"
                })
                eid += 1
        
        st.session_state.expenses = demo_expenses
    
    if 'purchase_orders' not in st.session_state:
        st.session_state.purchase_orders = [
            {"id": 1, "supplier": "Ganga Medical Hall", "date": str(yesterday), "expected": str(today + timedelta(days=3)), "status": "Ordered", "items": "Metformin 500mg x100, Amlodipine 5mg x100", "notes": "Urgent"},
            {"id": 2, "supplier": "Basu Dev & Sons", "date": str(last_week), "expected": str(today), "status": "Received", "items": "Azithromycin 500mg x50, Paracetamol 500mg x200", "notes": ""},
        ]
    
    if 'visiting_doctors' not in st.session_state:
        st.session_state.visiting_doctors = [
            {"id": 1, "name": "Dr. Amit Kumar", "degree": "MBBS, MD (Medicine)", "hospital": "Burdwan Medical College", "date": str(today), "patients": 12, "specialization": "General Medicine", "phone": "9432011111", "fee": 300, "days": ["Mon", "Wed", "Fri"], "timing": "10AM - 2PM"},
            {"id": 2, "name": "Dr. Santanu Das", "degree": "MBBS", "hospital": "Rural Hospital", "date": str(today), "patients": 8, "specialization": "General Medicine", "phone": "9432022222", "fee": 200, "days": ["Tue", "Thu", "Sat"], "timing": "9AM - 1PM"},
            {"id": 3, "name": "Dr. Priya Singh", "degree": "MBBS, DGO", "hospital": "Life Care Hospital", "date": str(today), "patients": 6, "specialization": "Gynecologist", "phone": "9432033333", "fee": 400, "days": ["Mon", "Thu"], "timing": "11AM - 3PM"},
            {"id": 4, "name": "Dr. Subrata Mukherjee", "degree": "MBBS, MS (Ortho)", "hospital": "Burdwan Ortho Center", "date": str(today), "patients": 5, "specialization": "Orthopedic", "phone": "9432044444", "fee": 350, "days": ["Wed", "Sat"], "timing": "10AM - 2PM"},
            {"id": 5, "name": "Dr. Anjan Das", "degree": "MBBS, MD (Pediatric)", "hospital": "Children Care", "date": str(yesterday), "patients": 10, "specialization": "Pediatrician", "phone": "9432055555", "fee": 250, "days": ["Mon", "Tue", "Wed", "Thu", "Fri"], "timing": "9AM - 12PM"},
        ]
    
    if 'online_orders' not in st.session_state:
        st.session_state.online_orders = [
            {"id": 1, "date": str(today), "time": "10:30", "customer": "Riya Sharma", "phone": "9876543210", "email": "riya@gmail.com", "address": "12, ABC Road, Putsuri, Burdhan", "notes": "Ring bell", "delivery_type": "Home Delivery", "items": [{"medicine": "Paracetamol 500mg", "price": 35, "qty": 2, "total": 70}, {"medicine": "Vitamin B Complex", "price": 45, "qty": 1, "total": 45}], "subtotal": 115, "gst": 14, "delivery": 50, "total": 179, "payment": "COD", "status": "Pending", "payment_status": "Pending"},
            {"id": 2, "date": str(yesterday), "time": "14:20", "customer": "Ajay Kumar", "phone": "9876543211", "email": "ajay@gmail.com", "address": "45, XYZ Lane, Memari", "notes": "Leave at gate", "delivery_type": "Home Delivery", "items": [{"medicine": "Metformin 500mg", "price": 45, "qty": 3, "total": 135}, {"medicine": "Amlodipine 5mg", "price": 35, "qty": 2, "total": 70}], "subtotal": 205, "gst": 25, "delivery": 0, "total": 230, "payment": "UPI", "status": "Delivered", "payment_status": "Paid"},
            {"id": 3, "date": str(last_week), "time": "09:15", "customer": "Smt. Gita Devi", "phone": "9876543212", "email": "gita@gmail.com", "address": "Putsuri Bazar", "notes": "", "delivery_type": "Pickup", "items": [{"medicine": "Calcium D3", "price": 120, "qty": 1, "total": 120}], "subtotal": 120, "gst": 22, "delivery": 0, "total": 142, "payment": "COD", "status": "Delivered", "payment_status": "Paid"},
        ]
    
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "dashboard"

init_db()

# ============================================================
# UI DESIGN SELECTOR (Sidebar)
# ============================================================

with st.sidebar:
    st.markdown("---")
    design = st.selectbox("🎨 Choose Theme", 
        ["Medical Blue", "Nature Green", "Royal Purple", "Elegant Gold"],
        index=0,
        key="design_selector"
    )
    st.session_state.ui_design = design.lower().replace(" ", "_")

design = st.session_state.ui_design

# ============================================================
# STYLES
# ============================================================

# Theme configurations
theme_configs = {
    "medical_blue": {
        "primary": "#0284c7", "light": "#38bdf8", "dark": "#0369a1",
        "bg": "#f0f9ff", "gradient": "linear-gradient(135deg, #0284c7 0%, #38bdf8 100%)",
        "sidebar": "linear-gradient(180deg, #0369a1 0%, #0284c7 50%, #0ea5e9 100%)"
    },
    "nature_green": {
        "primary": "#16a34a", "light": "#22c55e", "dark": "#15803d",
        "bg": "#f0fdf4", "gradient": "linear-gradient(135deg, #16a34a 0%, #22c55e 100%)",
        "sidebar": "linear-gradient(180deg, #15803d 0%, #16a34a 50%, #22c55e 100%)"
    },
    "royal_purple": {
        "primary": "#7c3aed", "light": "#a78bfa", "dark": "#6d28d9",
        "bg": "#faf5ff", "gradient": "linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%)",
        "sidebar": "linear-gradient(180deg, #6d28d9 0%, #7c3aed 50%, #8b5cf6 100%)"
    },
    "elegant_gold": {
        "primary": "#b45309", "light": "#d97706", "dark": "#92400e",
        "bg": "#fffbeb", "gradient": "linear-gradient(135deg, #b45309 0%, #d97706 100%)",
        "sidebar": "linear-gradient(180deg, #92400e 0%, #b45309 50%, #d97706 100%)"
    }
}

theme = theme_configs.get(design, theme_configs["medical_blue"])

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Noto+Sans+Bengali:wght@300;400;500;600;700&display=swap');
    
    * {{ font-family: 'Outfit', 'Noto Sans Bengali', sans-serif; }}
    
    :root {{
        --medical-primary: {theme['primary']};
        --medical-light: {theme['light']};
        --medical-dark: {theme['dark']};
        --medical-bg: {theme['bg']};
    }}
    
    .stApp {{ 
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 60%, #f1f5f9 100%); 
    }}
    
    section[data-testid="stSidebar"] {{
        background: {theme['sidebar']} !important;
    }}
    
    section[data-testid="stSidebar"] * {{ 
        color: #ffffff !important; 
    }}
    
    h1, h2, h3, h4 {{ 
        color: {theme['dark']} !important; 
        font-weight: 700 !important;
    }}
    
    div[data-testid="stMetric"] {{
        background: linear-gradient(135deg, #ffffff 0%, {theme['bg']} 100%);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
    }}
    
    .stButton > button {{
        background: {theme['gradient']};
        color: white !important;
        border-radius: 14px;
        border: none;
        padding: 14px 28px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    
    .gradient-text {{
        background: {theme['gradient']};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

def render_sidebar():
    with st.sidebar:
        # Language Toggle
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🇬🇧 EN", use_container_width=True, key="lang_en"):
                st.session_state.lang = "en"
                st.rerun()
        with col2:
            if st.button("🇧🇩 বাং", use_container_width=True, key="lang_bn"):
                st.session_state.lang = "bn"
                st.rerun()
        
        t = translations[st.session_state.lang]
        
        # Logo
        st.markdown(f"""
        <div style="text-align:center;padding:20px 10px;">
            <div style="font-size:3.5rem;">💊</div>
            <h1 style="color:#5eead4 !important;font-size:1.6rem;margin:0;text-shadow:0 2px 10px rgba(94,234,212,0.3);">Kalyani</h1>
            <p style="color:#99f6e4;font-size:0.85rem;">Medical Hall</p>
        </div>
        
        <div style="background:linear-gradient(135deg,#0d9488,#14b8a6);border-radius:16px;padding:18px;margin:10px 0;text-align:center;box-shadow:0 4px 20px rgba(13,148,136,0.3);">
            <p style="color:rgba(255,255,255,0.85);font-size:0.8rem;margin:0;">📞 {t['contact']}</p>
            <p style="color:white;font-size:1rem;font-weight:700;margin:10px 0 0;">9619464843</p>
            <p style="color:white;font-size:1rem;font-weight:700;margin:5px 0 0;">7977932585</p>
        </div>
        
        <p style="color:#5eead4;font-size:0.7rem;font-weight:600;margin:15px 0 10px;text-align:center;text-shadow:0 2px 8px rgba(94,234,212,0.2);">
            ✨ {t['years_trust']}
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Dashboard
        if st.button(f"  🏠  Dashboard", use_container_width=True, key="nav_dashboard"):
            st.session_state.current_page = "dashboard"
            st.rerun()
        
        # Store Management - Merged
        if st.button(f"  📦  Inventory & Purchase", use_container_width=True, key="nav_inventory"):
            st.session_state.current_page = "inventory"
            st.rerun()
        
        st.markdown("---")
        
        # People
        for icon, label, key in [("👥", t['staff'], "staff"), ("🧑‍🤝‍🧑", t['customers'], "customers"), ("👨‍⚕️", t['doctors'], "doctors")]:
            if st.button(f"  {icon}  {label}", use_container_width=True, key=f"nav_{key}"):
                st.session_state.current_page = key
                st.rerun()
        
        st.markdown("---")
        
        # Finance
        for icon, label, key in [("💸", t['expenses'], "expenses"), ("📈", t['reports'], "reports")]:
            if st.button(f"  {icon}  {label}", use_container_width=True, key=f"nav_{key}"):
                st.session_state.current_page = key
                st.rerun()
        
        st.markdown("---")
        
        # Online
        for icon, label, key in [("🛍️", t['online_store'], "online_store"), ("📦", t['online_orders'], "online_orders")]:
            if st.button(f"  {icon}  {label}", use_container_width=True, key=f"nav_{key}"):
                st.session_state.current_page = key
                st.rerun()
        
        st.markdown(f"""
        <div style="text-align:center;padding:20px 0 10px;">
            <p style="color:#99f6e4;font-size:0.75rem;">📍 {t['location']}</p>
            <p style="color:#5eead4;font-size:0.7rem;">📍 {t['location']}</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# PAGES
# ============================================================

def page_dashboard():
    t = translations[st.session_state.lang]
    
    st.markdown(f"""
    <div style="text-align:center;padding:25px 0 15px;">
        <h1 class="gradient-text" style="font-size:2.4rem;margin:0;font-weight:700;">Kalyani Medical Hall</h1>
        <p style="color:#64748b;margin:12px 0;font-size:1rem;">{t['by']} | {t['location']}</p>
        <p style="background:linear-gradient(90deg,#0d9488,#14b8a6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600;font-size:1.1rem;">
            ✨ {t['years_trust']} | {t['tagline']} ✨
        </p>
    </div>
    <hr style="margin:20px 0;border:none;border-top:1px solid #e2e8f0;">
    """, unsafe_allow_html=True)
    
    today = str(datetime.now().date())
    today_sales = [s for s in st.session_state.daily_sales if s['date'] == today]
    today_income = sum(s['total'] for s in today_sales)
    today_profit = sum(s['profit'] for s in today_sales)
    today_expenses = sum(e['amount'] for e in st.session_state.expenses if e['date'] == today)
    low_stock = len([i for i in st.session_state.inventory if i['stock'] < i.get('min_stock', 50)])
    
    current_month = datetime.now().strftime("%Y-%m")
    mtd_sales_list = [s for s in st.session_state.daily_sales if s['date'].startswith(current_month)]
    mtd_income = sum(s['total'] for s in mtd_sales_list)
    mtd_profit = sum(s['profit'] for s in mtd_sales_list)
    
    today_str = str(datetime.now().date())
    todays_appointments = len([d for d in st.session_state.visiting_doctors if d.get('date', '') == today_str])
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"📊 {t['today_sales']}", f"₹{today_income:,}")
    c2.metric(f"📈 {t['today_profit']}", f"₹{today_profit:,}")
    c3.metric(f"💳 {t['today_expenses']}", f"₹{today_expenses:,}")
    c4.metric(f"⚠️ {t['low_stock']}", f"{low_stock}")
    
    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"📅 {t['mtd_sales']}", f"₹{mtd_income:,}")
    c2.metric(f"💹 {t['mtd_profit']}", f"₹{mtd_profit:,}")
    c3.metric(f"👨‍⚕️ {t['todays_appointments']}", f"{todays_appointments}")
    c4.metric(f"🛒 Online Orders", f"{len(st.session_state.online_orders)}")
    
    st.markdown("---")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.info(f"📦 **{len(st.session_state.inventory)}** {t['medicines']}")
    c2.success(f"🧑‍🤝‍🧑 **{len(st.session_state.customers)}** {t['customers']}")
    c3.warning(f"👥 **{len(st.session_state.staff)}** {t['staff']}")
    c4.info(f"🚚 **{len(st.session_state.distributors)}** {t['suppliers']}")
    total_supplier_due = sum(d.get('balance', 0) for d in st.session_state.distributors)
    c5.error(f"💰 Due: ₹{total_supplier_due:,}")
    
    st.markdown("---")
    
    # Quick Suppliers Summary
    st.markdown("### 🚚 Suppliers / Distributors - Quick View")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for sup in st.session_state.distributors[:3]:
            with st.expander(f"🏢 {sup['name']} - 💰 ₹{sup.get('balance', 0):,}"):
                st.write(f"📞 {sup.get('contact', 'N/A')}")
                st.write(f"📍 {sup.get('address', 'N/A')}")
                if sup.get('balance', 0) > 0:
                    st.warning(f"⚠️ Pending: ₹{sup['balance']:,}")
                else:
                    st.success("✅ All cleared")
    
    with col2:
        st.markdown("#### 📊 Supplier Summary")
        total_due = sum(d.get('balance', 0) for d in st.session_state.distributors)
        st.metric("Total Due", f"₹{total_due:,}", delta_color="inverse")
        st.metric("Active Suppliers", len(st.session_state.distributors))

def page_sales():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">💰 {t["sales"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🆕 New Sale", "📊 Sales History", "📈 Reports", "💳 Credit Management"])
    
    with tab1:
        with st.expander(f"➕ {t['new_sale']}", expanded=True):
            with st.form("sale_form"):
                c1, c2 = st.columns(2)
                with c1:
                    customer = st.selectbox(t['customer'], [c['name'] for c in st.session_state.customers] + ["Walk-in"])
                    payment = st.selectbox(t['payment'], ["Cash", "UPI", "Card", "Credit"])
                    prescription = st.file_uploader("📎 Attach Prescription", type=['jpg', 'png', 'jpeg', 'pdf'])
                with c2:
                    items = st.text_area("Items (Medicine Name, Qty, Rate)")
                    total = st.number_input(f"{t['total']} (₹)", min_value=0)
                    cost = st.number_input("Cost (₹)", min_value=0)
                    discount = st.number_input("Discount (₹)", min_value=0, value=0)
                
                if st.form_submit_button(f"💾 {t['save']}"):
                    final_total = total - discount
                    profit = final_total - cost
                    st.session_state.daily_sales.append({
                        "id": len(st.session_state.daily_sales) + 1,
                        "date": str(datetime.now().date()),
                        "customer": customer, "items": items, "total": final_total,
                        "profit": profit, "payment": payment, "discount": discount
                    })
                    st.success(f"✅ Sale recorded! Profit: ₹{profit}")
    
    with tab2:
        st.markdown("### 📋 Sales History")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            start_date = st.date_input("From Date", datetime.now().date())
        with c2:
            end_date = st.date_input("To Date", datetime.now().date())
        with c3:
            filter_payment = st.selectbox("Payment Mode", ["All", "Cash", "UPI", "Card", "Credit"])
        
        filter_customer = st.selectbox("Filter by Customer", ["All"] + [c['name'] for c in st.session_state.customers] + ["Walk-in"])
        
        filtered_sales = st.session_state.daily_sales
        filtered_sales = [s for s in filtered_sales if start_date <= datetime.strptime(s['date'], "%Y-%m-%d").date() <= end_date]
        
        if filter_payment != "All":
            filtered_sales = [s for s in filtered_sales if s['payment'] == filter_payment]
        if filter_customer != "All":
            filtered_sales = [s for s in filtered_sales if s['customer'] == filter_customer]
        
        total_amount = sum(s['total'] for s in filtered_sales)
        total_profit = sum(s['profit'] for s in filtered_sales)
        total_discount = sum(s.get('discount', 0) for s in filtered_sales)
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Sales", f"₹{total_amount:,}")
        c2.metric("Total Profit", f"₹{total_profit:,}")
        c3.metric("Discount Given", f"₹{total_discount:,}")
        c4.metric("Transactions", len(filtered_sales))
        
        st.markdown("### 🧾 Transaction Details")
        for s in reversed(filtered_sales):
            color = "success" if s['payment'] != "Credit" else "warning"
            st.markdown(f"""
            <div style="padding:12px;margin:8px 0;border-radius:12px;background:{'#ecfdf5' if s['payment'] != 'Credit' else '#fffbeb'};border:1px solid {'#10b981' if s['payment'] != 'Credit' else '#f59e0b'};">
                <strong>📅 {s['date']}</strong> | <strong>{s['customer']}</strong> | 
                💰 ₹{s['total']} | 💵 Profit: ₹{s['profit']} | 
                💳 {s['payment']} {"| 🔴 PENDING" if s['payment'] == "Credit" else ""}
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 📈 Sales Reports")
        
        today = str(datetime.now().date())
        today_list = [s for s in st.session_state.daily_sales if s['date'] == today]
        
        current_month = datetime.now().strftime("%Y-%m")
        month_sales = [s for s in st.session_state.daily_sales if s['date'].startswith(current_month)]
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📅 Today's Summary")
            c_a, c_b, c_c = st.columns(3)
            c_a.metric("Sales", f"₹{sum(s['total'] for s in today_list)}")
            c_b.metric("Profit", f"₹{sum(s['profit'] for s in today_list)}")
            c_c.metric("Transactions", len(today_list))
            
            st.markdown("**By Payment Mode:**")
            for mode in ["Cash", "UPI", "Card", "Credit"]:
                mode_sales = [s for s in today_list if s['payment'] == mode]
                if mode_sales:
                    st.write(f"• {mode}: ₹{sum(s['total'] for s in mode_sales)}")
        
        with c2:
            st.markdown("#### 📅 This Month's Summary")
            c_a, c_b, c_c = st.columns(3)
            c_a.metric("Sales", f"₹{sum(s['total'] for s in month_sales)}")
            c_b.metric("Profit", f"₹{sum(s['profit'] for s in month_sales)}")
            c_c.metric("Transactions", len(month_sales))
            
            st.markdown("**By Payment Mode:**")
            for mode in ["Cash", "UPI", "Card", "Credit"]:
                mode_sales = [s for s in month_sales if s['payment'] == mode]
                if mode_sales:
                    st.write(f"• {mode}: ₹{sum(s['total'] for s in mode_sales)}")
        
        st.markdown("---")
        st.markdown("### 🏆 Top Customers This Month")
        customer_totals = {}
        for s in month_sales:
            customer_totals[s['customer']] = customer_totals.get(s['customer'], 0) + s['total']
        for customer, total in sorted(customer_totals.items(), key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"• **{customer}**: ₹{total:,}")
    
    with tab4:
        st.markdown("### 💳 Credit / Pending Payments")
        
        credit_sales = [s for s in st.session_state.daily_sales if s['payment'] == "Credit"]
        
        total_credit = sum(s['total'] for s in credit_sales)
        st.metric("Total Credit Due", f"₹{total_credit:,}")
        
        st.markdown("#### Pending Payments")
        for s in credit_sales:
            with st.expander(f"📋 {s['date']} - {s['customer']} - ₹{s['total']}"):
                st.write(f"**Items:** {s['items']}")
                st.write(f"**Profit:** ₹{s['profit']}")
                col1, col2 = st.columns(2)
                if col1.button(f"✅ Mark Paid", key=f"paid_{s['id']}"):
                    s['payment'] = "Cash"
                    st.success("Marked as paid!")
                    st.rerun()
                if col2.button(f"🗑️ Delete", key=f"del_{s['id']}"):
                    st.session_state.daily_sales.remove(s)
                    st.success("Deleted!")
                    st.rerun()

def page_inventory():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">📦 Inventory, Purchase & Suppliers</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["💊 Medicines", "⚠️ Low Stock", "📅 Expiry", "🛒 Purchase Orders", "🚚 Suppliers", "📊 Summary"])
    
    with tab1:
        with st.expander(f"➕ {t['add_medicine']}", expanded=True):
            with st.form("med_form"):
                c1, c2 = st.columns(2)
                with c1:
                    name = st.text_input(t['name'])
                    category = st.selectbox(t['category'], ["Pain/Fever", "Diabetes", "BP/Heart", "Antibiotic", "Gastric", "Allergy", "Vitamin", "Syrup", "Ointment", "Eye/Ear Drops", "Injection"])
                    manufacturer = st.text_input("Manufacturer")
                with c2:
                    price = st.number_input(f"MRP {t['price']} (₹)", min_value=0)
                    cost = st.number_input("Purchase Cost (₹)", min_value=0)
                    gst = st.number_input("GST %", min_value=0, max_value=28, value=12)
                
                c3, c4 = st.columns(2)
                with c3:
                    stock = st.number_input(t['stock'], min_value=0)
                    min_stock = st.number_input("Min Stock Alert", min_value=0, value=50)
                    batch_no = st.text_input("Batch Number")
                with c4:
                    expiry = st.date_input("Expiry Date")
                    hsn_code = st.text_input("HSN Code", value="3004")
                    pack_size = st.text_input("Pack Size")
                
                barcode = st.text_input("Barcode Number (Optional)")
                
                if st.form_submit_button(f"➕ {t['add']}"):
                    med = {
                        "id": len(st.session_state.inventory) + 1,
                        "name": name, "category": category, "price": price, "cost": cost,
                        "stock": stock, "expiry": str(expiry), "min_stock": min_stock,
                        "manufacturer": manufacturer, "gst": gst, "batch_no": batch_no,
                        "hsn_code": hsn_code, "pack_size": pack_size, "barcode": barcode
                    }
                    st.session_state.inventory.append(med)
                    st.success(f"✅ {name} added! Profit: ₹{price - cost}/unit")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Medicines", len(st.session_state.inventory))
        total_stock = sum(m['stock'] for m in st.session_state.inventory)
        c2.metric("Total Stock Units", total_stock)
        total_value = sum(m['price'] * m['stock'] for m in st.session_state.inventory)
        c3.metric("Stock Value (MRP)", f"₹{total_value:,}")
        total_cost = sum(m['cost'] * m['stock'] for m in st.session_state.inventory)
        c4.metric("Stock Value (Cost)", f"₹{total_cost:,}")
        
        search = st.text_input(f"🔍 {t['search']} Medicine", placeholder="Search by name, category, or barcode")
        
        filter_cat = st.selectbox("Filter by Category", ["All"] + ["Pain/Fever", "Diabetes", "BP/Heart", "Antibiotic", "Gastric", "Allergy", "Vitamin", "Syrup", "Ointment", "Eye/Ear Drops", "Injection"])
        
        meds = st.session_state.inventory
        if search:
            meds = [m for m in meds if search.lower() in m['name'].lower() or search in m.get('barcode', '') or search in m.get('manufacturer', '')]
        if filter_cat != "All":
            meds = [m for m in meds if m['category'] == filter_cat]
        
        for med in meds:
            is_low = med['stock'] < med.get('min_stock', 50)
            is_expiring = med.get('expiry', '') and med['expiry'][:7] <= datetime.now().strftime("%Y-%m")
            
            if is_low:
                st.warning(f"🔴 **[LOW STOCK]** **{med['name']}** | ₹{med['price']} | Stock: **{med['stock']}** | {med.get('category', '')}")
            elif is_expiring:
                st.error(f"⚠️ **[EXPIRING]** **{med['name']}** | Exp: {med.get('expiry', 'N/A')} | Stock: {med['stock']}")
            else:
                with st.expander(f"✅ {med['name']} | ₹{med['price']} | Stock: {med['stock']}"):
                    c1, c2 = st.columns(2)
                    c1.write(f"**Category:** {med.get('category', 'N/A')}")
                    c2.write(f"**Manufacturer:** {med.get('manufacturer', 'N/A')}")
                    c1.write(f"**Cost:** ₹{med.get('cost', 0)} | **GST:** {med.get('gst', 0)}%")
                    c2.write(f"**Batch:** {med.get('batch_no', 'N/A')} | **HSN:** {med.get('hsn_code', 'N/A')}")
                    c1.write(f"**Expiry:** {med.get('expiry', 'N/A')}")
                    c2.write(f"**Pack:** {med.get('pack_size', 'N/A')}")
                    
                    col1, col2, col3 = st.columns(3)
                    if col1.button(f"✏️ Edit", key=f"edit_{med['id']}"):
                        st.info("Edit dialog would open")
                    if col2.button(f"➕ Add Stock", key=f"add_{med['id']}"):
                        st.info("Add stock dialog")
                    if col3.button(f"🗑️ Delete", key=f"del_{med['id']}"):
                        st.session_state.inventory.remove(med)
                        st.success("Deleted!")
                        st.rerun()
    
    with tab2:
        st.markdown("### ⚠️ Low Stock Alert")
        
        low_stock_meds = [m for m in st.session_state.inventory if m['stock'] < m.get('min_stock', 50)]
        
        if low_stock_meds:
            st.warning(f"⚠️ **{len(low_stock_meds)} medicines** are running low!")
            
            for med in low_stock_meds:
                with st.expander(f"🔴 {med['name']} - Current: {med['stock']} | Minimum: {med.get('min_stock', 50)}"):
                    c1, c2 = st.columns(2)
                    c1.write(f"**Category:** {med.get('category', 'N/A')}")
                    c2.write(f"**Price:** ₹{med['price']}")
                    needed = med.get('min_stock', 50) - med['stock'] + 50
                    c1.write(f"**Recommended Order:** {needed} units")
                    c2.write(f"**Estimated Cost:** ₹{needed * med.get('cost', 0):,}")
        else:
            st.success("✅ All medicines are well stocked!")
        
        st.markdown("### 🛒 Create Purchase Order for Low Stock")
        if low_stock_meds and st.button("📝 Create PO for All Low Stock Items"):
            st.success(f"PO created for {len(low_stock_meds)} items!")
    
    with tab3:
        st.markdown("### 📅 Expiry Alerts")
        
        current_month = datetime.now().strftime("%Y-%m")
        next_month = datetime.now().date().replace(month=datetime.now().month % 12 + 1)
        next_month_str = next_month.strftime("%Y-%m")
        
        expiring_soon = [m for m in st.session_state.inventory if m.get('expiry', '') and m['expiry'][:7] <= next_month_str]
        expired = [m for m in st.session_state.inventory if m.get('expiry', '') and m['expiry'][:7] < current_month]
        
        c1, c2 = st.columns(2)
        c1.error(f"⚠️ Expired: {len(expired)}")
        c2.warning(f"📅 Expiring This/Next Month: {len(expiring_soon)}")
        
        if expired:
            st.markdown("#### ❌ Expired Medicines")
            for med in expired:
                st.error(f"❌ **{med['name']}** - Expired on {med.get('expiry', 'N/A')} | Stock: {med['stock']}")
                if st.button(f"🗑️ Dispose", key=f"dispose_{med['id']}"):
                    st.warning("Marked for disposal!")
        
        if expiring_soon:
            st.markdown("#### ⚠️ Expiring Soon")
            for med in expiring_soon:
                st.warning(f"⏰ **{med['name']}** - Expires: {med.get('expiry', 'N/A')} | Stock: {med['stock']}")
    
    with tab4:
        st.markdown("### 🏷️ Barcode & HSN Management")
        
        with st.expander("➕ Generate/Add Barcode"):
            with st.form("barcode_form"):
                barcode_med = st.selectbox("Select Medicine", [m['name'] for m in st.session_state.inventory])
                barcode_num = st.text_input("Barcode Number")
                if st.form_submit_button("🏷️ Generate"):
                    st.success(f"Barcode {barcode_num} linked to {barcode_med}")
        
        st.markdown("### 📋 HSN Code Reference")
        
        hsn_codes = [
            {"hsn": "3004", "category": "Medicines", "gst": "12%"},
            {"hsn": "3005", "category": "Medicines (Unani/Ayurvedic)", "gst": "12%"},
            {"hsn": "2101", "category": "Food Supplements", "gst": "18%"},
            {"hsn": "3304", "category": "Cosmetics", "gst": "28%"},
            {"hsn": "9018", "category": "Surgical Items", "gst": "12%"},
        ]
        
        for h in hsn_codes:
            st.info(f"**HSN {h['hsn']}:** {h['category']} - GST: {h['gst']}")
    
    with tab5:
        st.markdown("### 📊 Category Analysis")
        
        categories = {}
        for m in st.session_state.inventory:
            cat = m.get('category', 'Other')
            categories[cat] = categories.get(cat, 0) + 1
        
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            st.write(f"**{cat}:** {count} medicines")
    
    with tab4:
        st.markdown("### 🛒 Purchase Orders")
        
        with st.expander("➕ Create New Order", expanded=True):
            with st.form("po_form_merge"):
                c1, c2 = st.columns(2)
                with c1:
                    po_supplier = st.selectbox("Supplier", [d['name'] for d in st.session_state.distributors])
                    po_date = st.date_input("Order Date", datetime.now().date())
                with c2:
                    po_expected = st.date_input("Expected Delivery")
                    po_status = st.selectbox("Status", ["Pending", "Ordered", "Received"])
                
                po_items = st.text_area("Items (Medicine - Qty - Cost)")
                po_notes = st.text_area("Notes")
                
                if st.form_submit_button("💾 Create Order"):
                    st.session_state.purchase_orders.append({
                        "id": len(st.session_state.purchase_orders) + 1,
                        "supplier": po_supplier, "date": str(po_date),
                        "expected": str(po_expected), "status": po_status,
                        "items": po_items, "notes": po_notes
                    })
                    st.success("✅ Purchase order created!")
        
        st.markdown("#### 📋 Active Orders")
        for po in st.session_state.purchase_orders:
            status_icon = "🟡" if po['status'] == "Pending" else "🔵" if po['status'] == "Ordered" else "🟢"
            with st.expander(f"{status_icon} PO #{po['id']} - {po['supplier']} - {po['date']}"):
                st.write(f"**Status:** {po['status']}")
                st.write(f"**Expected:** {po['expected']}")
                st.write(f"**Items:** {po['items']}")
                if po['status'] != "Received":
                    if st.button(f"Mark Received", key=f"rec_{po['id']}"):
                        po['status'] = "Received"
                        st.rerun()
    
    with tab6:
        st.markdown("### 🚚 Suppliers / Distributors")
        
        with st.expander("➕ Add Supplier", expanded=True):
            with st.form("supplier_form_merge"):
                c1, c2 = st.columns(2)
                with c1:
                    sup_name = st.text_input("Supplier Name")
                    sup_contact = st.text_input("Phone")
                with c2:
                    sup_address = st.text_input("Address")
                    sup_balance = st.number_input("Pending Balance (₹)", min_value=0)
                
                sup_doc = st.file_uploader("📎 Attach Document")
                
                if st.form_submit_button("➕ Add Supplier"):
                    st.session_state.distributors.append({
                        "id": len(st.session_state.distributors) + 1,
                        "name": sup_name, "contact": sup_contact,
                        "address": sup_address, "balance": sup_balance
                    })
                    st.success("✅ Supplier added!")
        
        total_balance = sum(d['balance'] for d in st.session_state.distributors)
        st.metric("Total Pending Payments", f"₹{total_balance:,}")
        
        st.markdown("#### 📋 Supplier List")
        for sup in st.session_state.distributors:
            with st.expander(f"🏢 **{sup['name']}** | 📞 {sup['contact']}"):
                c1, c2 = st.columns(2)
                c1.write(f"📍 {sup['address']}")
                c2.write(f"💰 Balance: ₹{sup['balance']:,}")
                
                col1, col2 = st.columns(2)
                if col1.button(f"💸 Pay", key=f"pay_sup_{sup['id']}"):
                    sup['balance'] = 0
                    st.rerun()
                if col2.button(f"🗑️ Delete", key=f"del_sup_{sup['id']}"):
                    st.session_state.distributors.remove(sup)
                    st.rerun()


def page_staff():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">👥 {t["staff"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Staff List", "📅 Attendance", "📊 Leave Management", "💰 Payroll"])
    
    with tab1:
        with st.expander(f"➕ {t['add_staff']}", expanded=True):
            with st.form("staff_form"):
                c1, c2 = st.columns(2)
                with c1:
                    name = st.text_input(t['name'])
                    phone = st.text_input(t['phone'])
                    role = st.selectbox(t['role'], ["Manager", "Sales Staff", "Delivery Boy", "Compounder", "Accountant"])
                with c2:
                    salary = st.number_input(f"{t['salary']} (₹)", min_value=0)
                    joining_date = st.date_input("Joining Date", datetime.now().date())
                
                aadhar = st.text_input("Aadhar Card Number")
                address = st.text_input(t['address'])
                
                if st.form_submit_button(f"➕ {t['add']}"):
                    st.session_state.staff.append({
                        "id": len(st.session_state.staff) + 1,
                        "name": name, "phone": phone, "role": role,
                        "salary": salary, "joining": str(joining_date),
                        "aadhar": aadhar, "address": address
                    })
                    st.success("✅ Staff added!")
        
        total = sum(s['salary'] for s in st.session_state.staff)
        st.metric(f"Total Monthly {t['salary']}", f"₹{total:,}")
        
        for staff in st.session_state.staff:
            with st.expander(f"👤 **{staff['name']}** | {staff['role']}"):
                c1, c2 = st.columns(2)
                c1.write(f"📞 {staff['phone']}")
                c2.write(f"💰 ₹{staff['salary']:,}/month")
                c1.write(f"📅 Joined: {staff.get('joining', 'N/A')}")
    
    with tab2:
        st.markdown("### 📅 Daily Attendance")
        
        c1, c2 = st.columns(2)
        with c1:
            att_date = st.date_input("Select Date", datetime.now().date())
        with c2:
            shift = st.selectbox("Shift", ["Morning", "Evening", "Full Day"])
        
        st.markdown("### Mark Attendance")
        for staff in st.session_state.staff:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col1:
                st.write(f"**{staff['name']}**")
            with col2:
                if st.button("✅ Present", key=f"p_{staff['id']}_{att_date}"):
                    st.success("Marked Present")
            with col3:
                if st.button("❌ Absent", key=f"a_{staff['id']}_{att_date}"):
                    st.warning("Marked Absent")
            with col4:
                if st.button("⏰ Late", key=f"l_{staff['id']}_{att_date}"):
                    st.info("Marked Late")
        
        st.markdown("---")
        st.markdown("### 📊 Attendance Summary (This Month)")
        st.info("Attendance report would show here")
    
    with tab3:
        st.markdown("### 📊 Leave Management")
        
        with st.expander("➕ Apply Leave", expanded=True):
            with st.form("leave_form"):
                c1, c2 = st.columns(2)
                with c1:
                    leave_staff = st.selectbox("Select Staff", [s['name'] for s in st.session_state.staff])
                    leave_type = st.selectbox("Leave Type", ["Sick Leave", "Casual Leave", "Emergency", "Paid Leave"])
                with c2:
                    leave_from = st.date_input("From Date")
                    leave_to = st.date_input("To Date")
                
                reason = st.text_area("Reason")
                
                if st.form_submit_button(f"📝 Submit Leave"):
                    st.success("✅ Leave application submitted!")
        
        st.markdown("### 📋 Leave Balance")
        for staff in st.session_state.staff:
            with st.expander(f"👤 {staff['name']}"):
                c1, c2, c3 = st.columns(3)
                c1.metric("Sick Leave", "2/6")
                c2.metric("Casual Leave", "3/6")
                c3.metric("Paid Leave", "1/3")
    
    with tab4:
        st.markdown("### 💰 Payroll Management")
        
        c1, c2 = st.columns(2)
        with c1:
            payroll_month = st.date_input("Select Month", datetime.now().date(), format="YYYY-MM")
        with c2:
            st.write("") 
            st.write("")
        
        total_salary = sum(s['salary'] for s in st.session_state.staff)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Salary Bill", f"₹{total_salary:,}")
        c2.metric("Staff Count", len(st.session_state.staff))
        c3.metric("Average Salary", f"₹{total_salary // len(st.session_state.staff) if st.session_state.staff else 0:,}")
        
        st.markdown("### 💵 Salary Slip Generation")
        for staff in st.session_state.staff:
            with st.expander(f"📄 {staff['name']} - ₹{staff['salary']:,}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Basic Salary:** ₹{staff['salary']:,}")
                    st.write(f"**Conveyance:** ₹1,000")
                with col2:
                    st.write(f"**Gross:** ₹{staff['salary'] + 1000:,}")
                    st.write(f"**Deductions:** ₹0")
                if st.button(f"🖨️ Generate Slip", key=f"slip_{staff['id']}"):
                    st.success("Salary slip generated!")

def page_customers():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">🧑‍🤝‍🧑 {t["customers"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["👥 Customer List", "📋 Prescriptions", "⭐ Loyalty Points", "📅 Visit History"])
    
    with tab1:
        with st.expander(f"➕ {t['add_customer']}", expanded=True):
            with st.form("cust_form"):
                c1, c2 = st.columns(2)
                with c1:
                    name = st.text_input(t['name'])
                    phone = st.text_input(t['phone'])
                    dob = st.date_input("Date of Birth", datetime.now().date())
                with c2:
                    address = st.text_input(t['address'])
                    blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-", "Unknown"])
                
                emergency_contact = st.text_input("Emergency Contact")
                allergies = st.text_area("Known Allergies")
                
                if st.form_submit_button(f"➕ {t['add']}"):
                    st.session_state.customers.append({
                        "id": len(st.session_state.customers) + 1,
                        "name": name, "phone": phone, "address": address,
                        "dob": str(dob), "blood_group": blood_group,
                        "emergency": emergency_contact, "allergies": allergies,
                        "total_spent": 0, "visits": 0, "points": 0
                    })
                    st.success("✅ Customer added!")
        
        search = st.text_input("🔍 Search Customer", placeholder="Name or Phone")
        
        for cust in st.session_state.customers:
            if search and search.lower() not in cust['name'].lower() and search not in cust['phone']:
                continue
            with st.expander(f"👤 **{cust['name']}** | 📞 {cust['phone']}"):
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Total Spent", f"₹{cust.get('total_spent', 0):,}")
                c2.metric("Visits", cust.get('visits', 0))
                c3.metric("Points", cust.get('points', 0))
                c4.metric("Blood Group", cust.get('blood_group', 'N/A'))
                st.write(f"📍 {cust.get('address', 'N/A')}")
                st.write(f"🩸 Allergies: {cust.get('allergies', 'None')}")
    
    with tab2:
        st.markdown("### 📋 Customer Prescriptions")
        
        with st.expander("➕ Upload Prescription", expanded=True):
            with st.form("pres_form"):
                c1, c2 = st.columns(2)
                with c1:
                    pres_customer = st.selectbox("Customer", [c['name'] for c in st.session_state.customers])
                    pres_date = st.date_input("Prescription Date", datetime.now().date())
                with c2:
                    pres_doctor = st.text_input("Doctor Name")
                    pres_hospital = st.text_input("Hospital/Clinic")
                
                pres_file = st.file_uploader("📎 Upload Prescription Image/PDF", type=['jpg', 'png', 'jpeg', 'pdf'])
                pres_notes = st.text_area("Notes")
                
                if st.form_submit_button(f"💾 Save Prescription"):
                    st.success("✅ Prescription saved!")
        
        st.markdown("### 📂 Prescription History")
        st.info("No prescriptions uploaded yet")
    
    with tab3:
        st.markdown("### ⭐ Loyalty Points Program")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Points Issued", "2,500")
        c2.metric("Total Points Redeemed", "1,200")
        c3.metric("Active Members", len(st.session_state.customers))
        
        st.markdown("### 🏆 Top Members")
        
        sorted_customers = sorted(st.session_state.customers, key=lambda x: x.get('points', 0), reverse=True)
        for i, cust in enumerate(sorted_customers[:5], 1):
            with st.expander(f"{'🥇' if i==1 else '🥈' if i==2 else '🥉' if i==3 else '🏅'} #{i} {cust['name']} - {cust.get('points', 0)} points"):
                c1, c2 = st.columns(2)
                c1.write(f"📞 {cust.get('phone', 'N/A')}")
                c2.write(f"💰 Total Spent: ₹{cust.get('total_spent', 0):,}")
                if st.button(f"🎁 Redeem Points", key=f"redeem_{cust['id']}"):
                    st.info("Points redemption dialog")
        
        st.markdown("### ⚙️ Points Configuration")
        with st.form("points_config"):
            c1, c2 = st.columns(2)
            with c1:
                points_per_rupee = st.number_input("Points per ₹1 spent", value=1)
            with c2:
                redemption_rate = st.number_input("₹ per 10 points", value=1)
            
            if st.form_submit_button("💾 Save Configuration"):
                st.success("Configuration saved!")
    
    with tab4:
        st.markdown("### 📅 Visit History")
        
        c1, c2 = st.columns(2)
        with c1:
            visit_customer = st.selectbox("Select Customer", ["All"] + [c['name'] for c in st.session_state.customers])
        with c2:
            visit_date = st.date_input("Visit Date", datetime.now().date())
        
        st.markdown("### 📊 Today's Visits")
        for cust in st.session_state.customers:
            with st.expander(f"👤 {cust['name']} - {cust.get('visits', 0)} visits"):
                st.write(f"📞 {cust.get('phone', 'N/A')}")
                st.write(f"📍 {cust.get('address', 'N/A')}")

def page_doctors():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">👨‍⚕️ {t["doctors"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗓️ Appointments", "👨‍⚕️ Doctor Directory", "🏥 Patient Queue", "💰 Doctor-wise Sales", "📊 Doctor Reports"])
    
    with tab1:
        st.markdown("### 🗓️ Book Appointment")
        
        with st.expander("➕ New Appointment", expanded=True):
            with st.form("appt_form"):
                c1, c2 = st.columns(2)
                with c1:
                    appt_doctor = st.selectbox("Select Doctor", ["Dr. Amit Kumar (MBBS, MD)", "Dr. Santanu Das (MBBS)", "Dr. Priya Singh (Gynecologist)"])
                    appt_date = st.date_input("Appointment Date", datetime.now().date())
                with c2:
                    appt_time = st.selectbox("Time Slot", ["09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM", "02:00 PM", "02:30 PM", "03:00 PM", "03:30 PM", "04:00 PM", "04:30 PM"])
                    appt_type = st.selectbox("Consultation Type", ["New Patient", "Follow-up", "Emergency"])
                
                c1, c2 = st.columns(2)
                with c1:
                    appt_patient = st.text_input("Patient Name")
                    appt_phone = st.text_input("Patient Phone")
                with c2:
                    appt_age = st.number_input("Age", min_value=0, max_value=120)
                    appt_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                
                symptoms = st.text_area("Symptoms")
                consultation_fee = st.number_input("Consultation Fee (₹)", value=200)
                
                if st.form_submit_button(f"💾 Book Appointment"):
                    st.success("✅ Appointment booked!")
        
        st.markdown("### 📋 Today's Appointments")
        
        today_str = str(datetime.now().date())
        today_docs = [d for d in st.session_state.visiting_doctors if d.get('date', '') == today_str]
        
        for doc in today_docs:
            with st.expander(f"👨‍⚕️ {doc['name']} - {doc.get('patients', 0)} patients"):
                st.write(f"🏥 {doc.get('hospital', 'N/A')}")
                st.write(f"📅 Date: {doc.get('date', 'N/A')}")
                if st.button(f"▶️ Start Consultation", key=f"start_{doc['id']}"):
                    st.info("Starting consultation...")
    
    with tab2:
        st.markdown("### 👨‍⚕️ Visiting Doctors Directory")
        
        with st.expander("➕ Add Doctor", expanded=True):
            with st.form("doc_form"):
                c1, c2 = st.columns(2)
                with c1:
                    doc_name = st.text_input(t['name'])
                    doc_degree = st.text_input("Degree(s)")
                    doc_specialization = st.selectbox("Specialization", ["General Medicine", "Gynecologist", "Pediatrician", "Cardiologist", "Orthopedic", "Dentist", "Eye Specialist", "ENT"])
                with c2:
                    doc_hospital = st.text_input("Hospital/Clinic")
                    doc_phone = st.text_input("Contact Number")
                    doc_fee = st.number_input("Consultation Fee (₹)", min_value=0)
                
                doc_days = st.multiselect("Visiting Days", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
                doc_timing = st.text_input("Visiting Hours (e.g., 10AM - 2PM)")
                
                if st.form_submit_button(f"➕ {t['record_visit']}"):
                    st.session_state.visiting_doctors.append({
                        "id": len(st.session_state.visiting_doctors) + 1,
                        "name": doc_name, "degree": doc_degree, "hospital": doc_hospital,
                        "specialization": doc_specialization, "phone": doc_phone,
                        "fee": doc_fee, "days": doc_days, "timing": doc_timing,
                        "date": str(datetime.now().date()), "patients": 0
                    })
                    st.success("✅ Doctor added!")
        
        for doc in st.session_state.visiting_doctors:
            with st.expander(f"👨‍⚕️ **{doc['name']}** | {doc.get('specialization', 'General')}"):
                c1, c2 = st.columns(2)
                c1.write(f"📚 {doc.get('degree', 'N/A')}")
                c2.write(f"🏥 {doc.get('hospital', 'N/A')}")
                c1.write(f"📞 {doc.get('phone', 'N/A')}")
                c2.write(f"💰 Fee: ₹{doc.get('fee', 'N/A')}")
                st.write(f"📅 Days: {', '.join(doc.get('days', []))}")
                st.write(f"⏰ Timing: {doc.get('timing', 'N/A')}")
    
    with tab3:
        st.markdown("### 🏥 Patient Queue")
        
        c1, c2 = st.columns(2)
        with c1:
            queue_doctor = st.selectbox("Select Doctor", ["All"] + [d['name'] for d in st.session_state.visiting_doctors])
        with c2:
            queue_date = st.date_input("Date", datetime.now().date())
        
        st.markdown("### 📋 Current Queue")
        st.info("No patients in queue")
        
        with st.expander("➕ Add to Queue"):
            with st.form("queue_form"):
                q_patient = st.text_input("Patient Name")
                q_doctor = st.selectbox("Doctor", [d['name'] for d in st.session_state.visiting_doctors])
                q_type = st.selectbox("Type", ["New", "Follow-up"])
                if st.form_submit_button("➕ Add to Queue"):
                    st.success("Added to queue!")
    
    with tab4:
        st.markdown("### 💰 Doctor-wise Sales Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            doc_sales_month = st.selectbox("Select Month", 
                ["This Month", "Last 1 Month", "Last 3 Months", "Last 6 Months", "All Time"],
                key="doc_sales_month")
        
        doctor_sales = {}
        for sale in st.session_state.daily_sales:
            doctor = sale.get('doctor', 'None')
            if doctor not in doctor_sales:
                doctor_sales[doctor] = {'sales': 0, 'patients': 0, 'revenue': 0, 'profit': 0}
            doctor_sales[doctor]['sales'] += 1
            doctor_sales[doctor]['patients'] += 1
            doctor_sales[doctor]['revenue'] += sale.get('total', 0)
            doctor_sales[doctor]['profit'] += sale.get('profit', 0)
        
        st.markdown("---")
        
        total_doc_sales = sum(d['sales'] for d in doctor_sales.values())
        total_doc_revenue = sum(d['revenue'] for d in doctor_sales.values())
        total_doc_profit = sum(d['profit'] for d in doctor_sales.values())
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Referrals", total_doc_sales)
        c2.metric("Total Revenue", f"₹{total_doc_revenue:,}")
        c3.metric("Total Profit", f"₹{total_doc_profit:,}")
        c4.metric("Active Doctors", len([d for d in doctor_sales.keys() if d != 'None']))
        
        st.markdown("---")
        st.markdown("#### 📊 Doctor-wise Sales Details")
        
        doc_data = []
        for doctor, data in sorted(doctor_sales.items(), key=lambda x: x[1]['revenue'], reverse=True):
            avg_bill = data['revenue'] // max(data['sales'], 1)
            doc_data.append({
                "Doctor": doctor if doctor != 'None' else "Walk-in (No Reference)",
                "Sales": data['sales'],
                "Patients": data['patients'],
                "Revenue": f"₹{data['revenue']:,}",
                "Profit": f"₹{data['profit']:,}",
                "Avg Bill": f"₹{avg_bill:,}"
            })
        
        if doc_data:
            import pandas as pd
            df = pd.DataFrame(doc_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("#### 👨‍⚕️ Individual Doctor Performance")
        
        for doctor, data in sorted(doctor_sales.items(), key=lambda x: x[1]['revenue'], reverse=True):
            if doctor != 'None':
                with st.expander(f"👨‍⚕️ {doctor}"):
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Total Sales", data['sales'])
                    c2.metric("Patients", data['patients'])
                    c3.metric("Revenue", f"₹{data['revenue']:,}")
                    c4.metric("Profit", f"₹{data['profit']:,}")
        
        if doctor_sales:
            top_doc = max(doctor_sales.items(), key=lambda x: x[1]['revenue'])
            if top_doc[0] != 'None':
                st.success(f"🏆 Top Performing Doctor: **{top_doc[0]}** with ₹{top_doc[1]['revenue']:,} revenue!")
    
    with tab5:
        st.markdown("### 📊 Doctor Performance Reports")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Doctors", len(st.session_state.visiting_doctors))
        c2.metric("Total Patients Today", sum(d.get('patients', 0) for d in st.session_state.visiting_doctors))
        c3.metric("Active Doctors Today", len([d for d in st.session_state.visiting_doctors if d.get('date', '') == today_str]))
        
        st.markdown("### 📈 Monthly Performance")
        for doc in st.session_state.visiting_doctors:
            with st.expander(f"📊 {doc['name']}"):
                st.write(f"**Patients this month:** {doc.get('patients', 0)}")
                st.write(f"**Estimated Revenue:** ₹{doc.get('patients', 0) * doc.get('fee', 0):,}")

def page_expenses():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">💸 {t["expenses"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Daily Expenses", "🔄 Recurring Expenses", "📊 Expense Reports", "📂 Expense Categories"])
    
    with tab1:
        with st.expander(f"➕ {t['add_expense']}", expanded=True):
            with st.form("exp_form"):
                c1, c2 = st.columns(2)
                with c1:
                    category = st.selectbox(t['category'], ["Rent", "Electricity", "Salary", "Transport", "Internet", "Telephone", "Water", "Maintenance", "Insurance", "License Fee", "Marketing", "Miscellaneous"])
                    expense_date = st.date_input("Date", datetime.now().date())
                with c2:
                    amount = st.number_input(f"{t['amount']} (₹)", min_value=0)
                    payment_mode = st.selectbox("Payment Mode", ["Cash", "UPI", "Bank Transfer", "Cheque"])
                
                description = st.text_area("Description")
                vendor = st.text_input("Vendor/Party Name")
                bill_upload = st.file_uploader("📎 Attach Bill", type=['jpg', 'png', 'jpeg', 'pdf'])
                
                if st.form_submit_button(f"💾 {t['save']}"):
                    st.session_state.expenses.append({
                        "id": len(st.session_state.expenses) + 1,
                        "category": category, "date": str(expense_date),
                        "amount": amount, "payment": payment_mode,
                        "description": description, "vendor": vendor
                    })
                    st.success("✅ Expense recorded!")
        
        today = str(datetime.now().date())
        today_exp = [e for e in st.session_state.expenses if e['date'] == today]
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Today's Expenses", f"₹{sum(e['amount'] for e in today_exp)}")
        c2.metric("This Month", f"₹{sum(e['amount'] for e in st.session_state.expenses)}")
        c3.metric("Total Records", len(st.session_state.expenses))
        
        st.markdown("### 📋 Recent Expenses")
        for exp in reversed(st.session_state.expenses[-10:]):
            st.warning(f"📅 {exp['date']} | **{exp['category']}** | ₹{exp['amount']:,} | {exp.get('description', '')}")
    
    with tab2:
        st.markdown("### 🔄 Recurring Expenses")
        
        with st.expander("➕ Add Recurring Expense", expanded=True):
            with st.form("recurring_form"):
                c1, c2 = st.columns(2)
                with c1:
                    rec_category = st.selectbox("Category", ["Rent", "Internet", "Telephone", "Insurance", "EMIs"])
                    rec_amount = st.number_input("Amount (₹)", min_value=0)
                with c2:
                    rec_frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"])
                    rec_start = st.date_input("Start Date", datetime.now().date())
                
                rec_vendor = st.text_input("Vendor Name")
                rec_reminder = st.checkbox("Send Reminder", value=True)
                
                if st.form_submit_button(f"💾 Save Recurring"):
                    st.success("✅ Recurring expense added!")
        
        st.markdown("### 📋 Active Recurring Expenses")
        
        recurring_items = [
            {"category": "Rent", "amount": 8000, "frequency": "Monthly", "vendor": "Property Owner", "next_due": "2026-04-01"},
            {"category": "Internet", "amount": 999, "frequency": "Monthly", "vendor": "Jio Fiber", "next_due": "2026-03-15"},
            {"category": "Electricity", "amount": 3500, "frequency": "Monthly", "vendor": "WBSEB", "next_due": "2026-03-20"},
        ]
        
        for rec in recurring_items:
            with st.expander(f"🔄 {rec['category']} - ₹{rec['amount']:,} ({rec['frequency']})"):
                c1, c2 = st.columns(2)
                c1.write(f"**Vendor:** {rec['vendor']}")
                c2.write(f"**Next Due:** {rec['next_due']}")
                if st.button(f"💸 Pay Now", key=f"pay_rec_{rec['category']}"):
                    st.success("Payment recorded!")
    
    with tab3:
        st.markdown("### 📊 Expense Analysis")
        
        c1, c2 = st.columns(2)
        with c1:
            exp_month = st.date_input("Select Month", datetime.now().date(), format="YYYY-MM")
        with c2:
            exp_category = st.selectbox("Category", ["All"] + ["Rent", "Electricity", "Salary", "Transport", "Internet", "Telephone", "Water", "Maintenance", "Insurance", "License Fee", "Marketing", "Miscellaneous"])
        
        current_month = datetime.now().strftime("%Y-%m")
        month_exp = [e for e in st.session_state.expenses if e['date'].startswith(current_month)]
        
        if exp_category != "All":
            month_exp = [e for e in month_exp if e['category'] == exp_category]
        
        total_exp = sum(e['amount'] for e in month_exp)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Expenses", f"₹{total_exp:,}")
        c2.metric("Transactions", len(month_exp))
        c3.metric("Average", f"₹{total_exp // len(month_exp) if month_exp else 0:,}")
        
        st.markdown("### 📈 Category-wise Breakdown")
        
        categories = {}
        for e in month_exp:
            categories[e['category']] = categories.get(e['category'], 0) + e['amount']
        
        for cat, amt in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            st.write(f"**{cat}:** ₹{amt:,} ({amt*100//total_exp if total_exp else 0}%)")
    
    with tab4:
        st.markdown("### 📂 Manage Categories")
        
        with st.expander("➕ Add Category"):
            with st.form("cat_form"):
                new_cat = st.text_input("Category Name")
                new_cat_desc = st.text_input("Description")
                if st.form_submit_button("➕ Add"):
                    st.success("Category added!")
        
        st.markdown("### 📋 Default Categories")
        
        default_categories = [
            {"name": "Rent", "description": "Shop/Godown Rent", "icon": "🏠"},
            {"name": "Electricity", "description": "Electricity Bills", "icon": "💡"},
            {"name": "Salary", "description": "Staff Salaries", "icon": "👥"},
            {"name": "Transport", "description": "Delivery/Transportation", "icon": "🚚"},
            {"name": "Internet", "description": "Internet & WiFi", "icon": "📶"},
            {"name": "Telephone", "description": "Phone Bills", "icon": "📞"},
            {"name": "Water", "description": "Water Supply", "icon": "💧"},
            {"name": "Maintenance", "description": "Equipment/Shop Maintenance", "icon": "🔧"},
            {"name": "Insurance", "description": "Business Insurance", "icon": "🛡️"},
            {"name": "License Fee", "description": "Renewal Fees", "icon": "📜"},
            {"name": "Marketing", "description": "Advertising/Promotions", "icon": "📢"},
            {"name": "Miscellaneous", "description": "Other Expenses", "icon": "📦"},
        ]
        
        for cat in default_categories:
            st.info(f"{cat['icon']} **{cat['name']}** - {cat['description']}")

def page_reports():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">💰 Financial Analytics Dashboard</h1>', unsafe_allow_html=True)
    
    from datetime import datetime, timedelta
    
    today = datetime.now().date()
    current_month = today.strftime("%Y-%m")
    current_year = today.strftime("%Y")
    
    # Generate month options for dropdown (last 24 months)
    month_options = []
    for i in range(23, -1, -1):
        month_date = today.replace(day=1) - timedelta(days=i*30)
        month_options.append(month_date.strftime("%Y-%m"))
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Monthly View", "📊 Last 6 Months", "📆 Yearly View", "📋 All Transactions"])
    
    with tab1:
        st.markdown("### 📅 Select Month")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            selected_month = st.selectbox("Choose Month", month_options, index=len(month_options)-1)
        
        month_name = datetime.strptime(selected_month, "%Y-%m").strftime("%B %Y")
        st.markdown(f"**Showing data for: {month_name}**")
        
        # Sales for selected month
        sel_month_sales = [s for s in st.session_state.daily_sales if s['date'].startswith(selected_month)]
        sel_month_income = sum(s['total'] for s in sel_month_sales)
        sel_month_profit = sum(s['profit'] for s in sel_month_sales)
        
        # Expenses for selected month
        sel_month_expenses = [e for e in st.session_state.expenses if e['date'].startswith(selected_month)]
        sel_month_total_expenses = sum(e['amount'] for e in sel_month_expenses)
        
        # Fixed costs
        sel_rent = sum(e['amount'] for e in sel_month_expenses if e['category'] == 'Rent')
        sel_electricity = sum(e['amount'] for e in sel_month_expenses if e['category'] == 'Electricity')
        sel_salary = sum(e['amount'] for e in sel_month_expenses if e['category'] == 'Salary')
        sel_transport = sum(e['amount'] for e in sel_month_expenses if e['category'] == 'Transport')
        
        # Net profit
        sel_net = sel_month_profit - sel_month_total_expenses
        
        st.markdown("---")
        st.markdown(f"### 💰 {month_name} Summary")
        
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("💰 Sales", f"₹{sel_month_income:,}")
        c2.metric("📈 Profit", f"₹{sel_month_profit:,}")
        c3.metric("💸 Expenses", f"₹{sel_month_total_expenses:,}")
        c4.metric("⚡ Electricity", f"₹{sel_electricity:,}")
        c5.metric("🏠 Rent", f"₹{sel_rent:,}")
        
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("👥 Salary", f"₹{sel_salary:,}")
        c2.metric("🚚 Transport", f"₹{sel_transport:,}")
        
        # Calculate inventory cost (same for all months - current value)
        inventory_cost = sum(m.get('cost', 0) * m['stock'] for m in st.session_state.inventory)
        c3.metric("📦 Inventory Cost", f"₹{inventory_cost:,}")
        
        # Net profit after all expenses
        net_profit = sel_month_profit - sel_month_total_expenses
        c4.metric("✅ Net Profit", f"₹{net_profit:,}", delta_color="normal" if net_profit >= 0 else "inverse")
        
        # Transactions count
        c5.metric("📝 Transactions", len(sel_month_sales))
        
        # Profit margin
        if sel_month_income > 0:
            margin = (sel_month_profit / sel_month_income) * 100
            net_margin = (net_profit / sel_month_income) * 100
            c1, c2 = st.columns(2)
            c1.progress(min(margin / 100, 1.0))
            c1.caption(f"Gross Profit Margin: {margin:.1f}%")
            c2.progress(min(net_margin / 100, 1.0))
            c2.caption(f"Net Profit Margin: {net_margin:.1f}%")
        
        # Sales details for selected month
        if sel_month_sales:
            st.markdown("#### 📋 Sales Transactions")
            for s in sel_month_sales:
                st.info(f"📅 {s['date']} | 👤 {s['customer']} | 💰 ₹{s['total']} | 💵 Profit: ₹{s['profit']} | 💳 {s['payment']}")
        else:
            st.info("No sales data for this month")
        
        # Expenses details for selected month
        if sel_month_expenses:
            st.markdown("#### 💸 Expenses")
            for e in sel_month_expenses:
                st.warning(f"📅 {e['date']} | 🏷️ {e['category']} | 💰 ₹{e['amount']}")
        else:
            st.info("No expenses data for this month")
    
    with tab2:
        st.markdown("### 📊 LAST 6 MONTHS ANALYSIS")
        
        # Get last 6 months
        last_6_months = []
        for i in range(5, -1, -1):
            month_date = today.replace(day=1) - timedelta(days=i*30)
            last_6_months.append(month_date.strftime("%Y-%m"))
        
        months_data = []
        for month_str in last_6_months:
            month_name = datetime.strptime(month_str, "%Y-%m").strftime("%b %Y")
            
            # Sales
            m_sales = [s for s in st.session_state.daily_sales if s['date'].startswith(month_str)]
            m_income = sum(s['total'] for s in m_sales)
            m_profit = sum(s['profit'] for s in m_sales)
            
            # Expenses
            m_expenses = [e for e in st.session_state.expenses if e['date'].startswith(month_str)]
            m_total_exp = sum(e['amount'] for e in m_expenses)
            
            # Fixed costs
            m_rent = sum(e['amount'] for e in m_expenses if e['category'] == 'Rent')
            m_electricity = sum(e['amount'] for e in m_expenses if e['category'] == 'Electricity')
            m_salary = sum(e['amount'] for e in m_expenses if e['category'] == 'Salary')
            
            # Net profit
            m_net = m_profit - m_total_exp
            
            months_data.append({
                "month": month_name,
                "income": m_income,
                "profit": m_profit,
                "expenses": m_total_exp,
                "rent": m_rent,
                "electricity": m_electricity,
                "salary": m_salary,
                "net": m_net
            })
        
        # Display table
        st.markdown("#### 📋 Monthly Summary Table")
        table_data = []
        total_6m_income = 0
        total_6m_profit = 0
        total_6m_expenses = 0
        total_6m_rent = 0
        total_6m_electricity = 0
        total_6m_salary = 0
        total_6m_net = 0
        
        for data in months_data:
            total_6m_income += data['income']
            total_6m_profit += data['profit']
            total_6m_expenses += data['expenses']
            total_6m_rent += data['rent']
            total_6m_electricity += data['electricity']
            total_6m_salary += data['salary']
            total_6m_net += data['net']
            
            table_data.append({
                "Month": data['month'],
                "Sales": f"₹{data['income']:,}",
                "Profit": f"₹{data['profit']:,}",
                "Expenses": f"₹{data['expenses']:,}",
                "Rent": f"₹{data['rent']:,}",
                "Electricity": f"₹{data['electricity']:,}",
                "Salary": f"₹{data['salary']:,}",
                "Net Profit": f"₹{data['net']:,}"
            })
        
        if table_data:
            import pandas as pd
            df = pd.DataFrame(table_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        # 6 Month Totals
        st.markdown("#### 📈 Last 6 Months Total")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Sales (6M)", f"₹{total_6m_income:,}")
        c2.metric("Total Profit (6M)", f"₹{total_6m_profit:,}")
        c3.metric("Total Expenses (6M)", f"₹{total_6m_expenses:,}")
        c4.metric("Net Profit (6M)", f"₹{total_6m_net:,}")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Rent (6M)", f"₹{total_6m_rent:,}")
        c2.metric("Total Electricity (6M)", f"₹{total_6m_electricity:,}")
        c3.metric("Total Salary (6M)", f"₹{total_6m_salary:,}")
        avg_monthly_profit = total_6m_net // 6
        c4.metric("Avg Monthly Profit", f"₹{avg_monthly_profit:,}")
    
    with tab3:
        st.markdown("### 📆 YEARLY OVERVIEW")
        
        year_sales = [s for s in st.session_state.daily_sales if s['date'].startswith(current_year)]
        year_income = sum(s['total'] for s in year_sales)
        year_profit = sum(s['profit'] for s in year_sales)
        year_expenses = sum(e['amount'] for e in st.session_state.expenses if e['date'].startswith(current_year))
        year_net = year_profit - year_expenses
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Yearly Sales", f"₹{year_income:,}")
        c2.metric("Yearly Gross Profit", f"₹{year_profit:,}")
        c3.metric("Yearly Expenses", f"₹{year_expenses:,}")
        c4.metric("Yearly Net Profit", f"₹{year_net:,}", delta_color="normal" if year_net >= 0 else "inverse")
        
        # Monthly breakdown for the year
        st.markdown("#### 📊 Monthly Breakdown")
        year_months = []
        for i in range(12):
            month_date = today.replace(day=1) - timedelta(days=i*30)
            year_months.append(month_date.strftime("%Y-%m"))
        
        year_table = []
        for m in reversed(year_months):
            m_name = datetime.strptime(m, "%Y-%m").strftime("%b %Y")
            m_sales = [s for s in st.session_state.daily_sales if s['date'].startswith(m)]
            m_income = sum(s['total'] for s in m_sales)
            m_profit = sum(s['profit'] for s in m_sales)
            m_exp = sum(e['amount'] for e in st.session_state.expenses if e['date'].startswith(m))
            m_net = m_profit - m_exp
            
            year_table.append({
                "Month": m_name,
                "Sales": f"₹{m_income:,}",
                "Profit": f"₹{m_profit:,}",
                "Expenses": f"₹{m_exp:,}",
                "Net": f"₹{m_net:,}"
            })
        
        if year_table:
            import pandas as pd
            df = pd.DataFrame(year_table)
            st.dataframe(df, use_container_width=True, hide_index=True)
    
    with tab4:
        st.markdown("### 📋 ALL TRANSACTIONS")
        
        # All Sales
        st.markdown("#### 💰 All Sales")
        for s in reversed(st.session_state.daily_sales):
            st.info(f"📅 {s['date']} | 👤 {s['customer']} | 💰 ₹{s['total']} | 💵 Profit: ₹{s['profit']} | 💳 {s['payment']}")
        
        st.markdown("---")
        
        # All Expenses
        st.markdown("#### 💸 All Expenses")
        for e in reversed(st.session_state.expenses):
            st.warning(f"📅 {e['date']} | 🏷️ {e['category']} | 💰 ₹{e['amount']} | 💳 {e.get('payment', 'Cash')}")


def page_online_store():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">🛍️ {t["online_store"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏪 Browse Medicines", "🛒 Shopping Cart", "📝 Order Form", "💳 Payments", "🏠 My Orders"])
    
    with tab1:
        st.markdown("### 💊 Browse Medicines")
        
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            search_med = st.text_input("🔍 Search Medicines", placeholder="Search by name, category, or manufacturer...")
        with c2:
            category_filter = st.selectbox("Category", ["All", "Pain/Fever", "Diabetes", "BP/Heart", "Antibiotic", "Gastric", "Allergy", "Vitamin", "Syrup", "Ointment", "Eye/Ear Drops", "Injection"])
        with c3:
            sort_by = st.selectbox("Sort By", ["Name A-Z", "Price Low-High", "Price High-Low", "Stock Low-High", "Popular"])
        
        st.markdown("### Popular Categories")
        cat_cols = st.columns(5)
        categories = ["Pain/Fever", "Diabetes", "Antibiotic", "Vitamin", "Syrup"]
        for i, cat in enumerate(categories):
            if cat_cols[i].button(f"📚 {cat}", key=f"cat_{cat}"):
                category_filter = cat
                st.rerun()
        
        st.markdown("---")
        
        meds = st.session_state.inventory
        if search_med:
            meds = [m for m in meds if search_med.lower() in m['name'].lower() or 
                   search_med.lower() in m.get('category', '').lower() or 
                   search_med.lower() in m.get('manufacturer', '').lower()]
        if category_filter != "All":
            meds = [m for m in meds if m.get('category') == category_filter]
        
        if sort_by == "Name A-Z":
            meds = sorted(meds, key=lambda x: x['name'])
        elif sort_by == "Price Low-High":
            meds = sorted(meds, key=lambda x: x.get('price', 0))
        elif sort_by == "Price High-Low":
            meds = sorted(meds, key=lambda x: x.get('price', 0), reverse=True)
        elif sort_by == "Stock Low-High":
            meds = sorted(meds, key=lambda x: x.get('stock', 0))
        
        for med in meds:
            with st.expander(f"💊 **{med['name']}** - ₹{med['price']}"):
                c1, c2, c3 = st.columns(3)
                c1.write(f"📚 **{med.get('category', 'N/A')}**")
                c2.write(f"🏭 {med.get('manufacturer', 'N/A')}")
                c3.write(f"📦 Stock: {med['stock']}")
                
                c1, c2 = st.columns(2)
                c1.write(f"💰 MRP: ₹{med.get('price', 0)}")
                c2.write(f"🧾 GST: {med.get('gst', 0)}%")
                
                if med.get('expiry'):
                    c1.write(f"📅 Exp: {med['expiry']}")
                if med.get('pack_size'):
                    c2.write(f"📏 Pack: {med['pack_size']}")
                
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    qty = st.number_input("Quantity", min_value=1, max_value=med['stock'], value=1, key=f"qty_{med['id']}")
                with col2:
                    total_price = med['price'] * qty
                    st.write(f"**Total: ₹{total_price}**")
                with col3:
                    if st.button(f"🛒 Add to Cart", key=f"add_cart_{med['id']}"):
                        existing = next((i for i, item in enumerate(st.session_state.cart) if item['medicine'] == med['name']), None)
                        if existing is not None:
                            st.session_state.cart[existing]['qty'] += qty
                            st.session_state.cart[existing]['total'] = st.session_state.cart[existing]['price'] * st.session_state.cart[existing]['qty']
                        else:
                            st.session_state.cart.append({
                                "medicine": med['name'],
                                "price": med['price'],
                                "qty": qty,
                                "total": med['price'] * qty,
                                "category": med.get('category', ''),
                                "manufacturer": med.get('manufacturer', '')
                            })
                        st.success(f"Added {qty} x {med['name']}!")
        
        with st.expander("➕ Add Custom Medicine"):
            with st.form("custom_med"):
                c1, c2 = st.columns(2)
                with c1:
                    new_name = st.text_input("Medicine Name")
                    new_price = st.number_input("MRP (₹)", min_value=0)
                    new_stock = st.number_input("Stock", min_value=0)
                with c2:
                    new_category = st.selectbox("Category", ["Pain/Fever", "Diabetes", "BP/Heart", "Antibiotic", "Gastric", "Allergy", "Vitamin"])
                    new_manufacturer = st.text_input("Manufacturer")
                
                if st.form_submit_button("➕ Add to Store"):
                    st.session_state.inventory.append({
                        "id": len(st.session_state.inventory) + 1,
                        "name": new_name, "price": new_price, "stock": new_stock,
                        "category": new_category, "cost": new_price * 0.7,
                        "expiry": "2027-12", "min_stock": 50,
                        "manufacturer": new_manufacturer, "gst": 12
                    })
                    st.success("Medicine added to store!")
    
    with tab2:
        st.markdown("### 🛒 Shopping Cart")
        
        if not st.session_state.cart:
            st.info("🛒 Your cart is empty! Start shopping...")
            st.markdown("### Popular Products")
            for med in st.session_state.inventory[:5]:
                with st.expander(f"💊 {med['name']} - ₹{med['price']}"):
                    if st.button(f"Add to Cart", key=f"quick_{med['id']}"):
                        st.session_state.cart.append({
                            "medicine": med['name'], "price": med['price'],
                            "qty": 1, "total": med['price'],
                            "category": med.get('category', ''),
                            "manufacturer": med.get('manufacturer', '')
                        })
                        st.success("Added!")
        else:
            cart_total = 0
            cart_items = len(st.session_state.cart)
            
            st.markdown("#### Cart Items")
            for i, item in enumerate(st.session_state.cart):
                with st.container():
                    c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
                    c1.write(f"💊 **{item['medicine']}**")
                    c2.write(f"₹{item['price']} x {item['qty']}")
                    c3.write(f"**₹{item['total']}**")
                    if c4.button("🗑️", key=f"remove_{i}"):
                        st.session_state.cart.pop(i)
                        st.rerun()
                cart_total += item['total']
            
            st.markdown("---")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Items", cart_items)
            c2.metric("Subtotal", f"₹{cart_total:,}")
            
            gst = cart_total * 0.12
            delivery = 0 if cart_total >= 500 else 50
            final_total = cart_total + gst + delivery
            c3.metric("Final Total", f"₹{final_total:,.0f}")
            
            st.markdown("---")
            
            c1, c2 = st.columns(2)
            c1.write(f"📦 Delivery Charges: {'FREE' if cart_total >= 500 else '₹50'}")
            c2.write(f"🧾 GST (12%): ₹{gst:,.0f}")
            
            if st.button("🗑️ Clear Cart", type="primary"):
                st.session_state.cart = []
                st.rerun()
    
    with tab3:
        st.markdown("### 📝 Order Details")
        
        with st.form("order_form"):
            c1, c2 = st.columns(2)
            with c1:
                customer_name = st.text_input("👤 Customer Name *")
                customer_phone = st.text_input("📱 Phone Number *")
                customer_email = st.text_input("📧 Email (Optional)")
            with c2:
                customer_address = st.text_area("🏠 Delivery Address *", height=80)
                delivery_notes = st.text_area("📝 Delivery Notes", placeholder="Ring bell, leave at gate, etc.")
            
            st.markdown("---")
            st.markdown("#### 🕐 Delivery Options")
            
            c1, c2 = st.columns(2)
            with c1:
                delivery_type = st.radio("Delivery Type", ["Home Delivery", "Pickup from Store"])
            with c2:
                delivery_time = st.selectbox("Preferred Time", ["Morning (9AM-12PM)", "Afternoon (12PM-3PM)", "Evening (3PM-6PM)", "Night (6PM-9PM)", "Any Time"])
            
            if delivery_type == "Pickup from Store":
                st.info("📍 Pickup Location: Kalyani Medical Hall, Putsuri, Burdwan, WB")
            
            st.markdown("---")
            
            if st.form_submit_button("✅ Proceed to Payment"):
                if not customer_name or not customer_phone or not customer_address:
                    st.error("Please fill in all required fields!")
                else:
                    st.session_state.checkout_data = {
                        "customer": customer_name,
                        "phone": customer_phone,
                        "email": customer_email,
                        "address": customer_address,
                        "notes": delivery_notes,
                        "delivery_type": delivery_type,
                        "delivery_time": delivery_time,
                        "cart": st.session_state.cart.copy(),
                        "subtotal": sum(item['total'] for item in st.session_state.cart),
                        "gst": sum(item['total'] for item in st.session_state.cart) * 0.12,
                        "delivery": 0 if sum(item['total'] for item in st.session_state.cart) >= 500 else 50
                    }
                    st.success("Proceeding to payment!")
                    st.rerun()
    
    with tab4:
        st.markdown("### 💳 Payment")
        
        if 'checkout_data' not in st.session_state or not st.session_state.checkout_data:
            st.warning("Please complete order form first!")
        else:
            data = st.session_state.checkout_data
            total = data['subtotal'] + data['gst'] + data['delivery']
            
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown(f"""
                ### 📋 Order Summary
                - **Customer:** {data['customer']}
                - **Phone:** {data['phone']}
                - **Address:** {data['address']}
                - **Delivery:** {data['delivery_type']} - {data['delivery_time']}
                """)
                
                st.markdown("### 🛒 Items")
                for item in data['cart']:
                    st.write(f"• {item['medicine']} x {item['qty']} = ₹{item['total']}")
            
            with c2:
                st.markdown("### 💰 Payment Details")
                st.metric("Subtotal", f"₹{data['subtotal']:,.0f}")
                st.metric("GST (12%)", f"₹{data['gst']:,.0f}")
                st.metric("Delivery", f"₹{data['delivery']}")
                st.markdown("---")
                st.metric("**Total**", f"₹{total:,.0f}")
                
                st.markdown("### 💳 Payment Method")
                payment_method = st.radio("Select", ["💵 Cash on Delivery (COD)", "📱 UPI Payment", "💳 Card Payment", "🏦 Bank Transfer"])
                
                if payment_method == "💵 Cash on Delivery (COD)":
                    st.info("Pay ₹{total} at the time of delivery")
                elif payment_method == "📱 UPI Payment":
                    st.info("Scan QR Code or Pay to UPI: kalyanimedical@upi")
                    st.markdown("![QR Code](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=kalyanimedical@upi&pn=Kalyani%20Medical%20Hall)")
                elif payment_method == "💳 Card Payment":
                    st.info("Redirect to payment gateway...")
                elif payment_method == "🏦 Bank Transfer":
                    st.info("Account: 1234567890 | IFSC: ABCD0123456")
            
            if st.button("✅ Place Order", type="primary"):
                order = {
                    "id": len(st.session_state.online_orders) + 1,
                    "date": str(datetime.now().date()),
                    "time": datetime.now().strftime("%H:%M"),
                    "customer": data['customer'],
                    "phone": data['phone'],
                    "email": data.get('email', ''),
                    "address": data['address'],
                    "notes": data.get('notes', ''),
                    "delivery_type": data['delivery_type'],
                    "items": data['cart'].copy(),
                    "subtotal": data['subtotal'],
                    "gst": data['gst'],
                    "delivery": data['delivery'],
                    "total": total,
                    "payment": payment_method.split()[1] if payment_method else "COD",
                    "status": "Pending",
                    "payment_status": "Pending" if "COD" in payment_method else "Paid"
                }
                st.session_state.online_orders.append(order)
                st.session_state.cart = []
                if 'checkout_data' in st.session_state:
                    del st.session_state['checkout_data']
                st.success(f"✅ Order #{order['id']} placed successfully!")
                st.rerun()
    
    with tab5:
        st.markdown("### 🏠 My Orders")
        
        if not st.session_state.online_orders:
            st.info("No orders yet!")
        else:
            search_order = st.text_input("🔍 Search Order", placeholder="Order ID or Phone")
            
            orders = st.session_state.online_orders
            if search_order:
                orders = [o for o in orders if search_order in str(o['id']) or search_order in o.get('phone', '')]
            
            for order in reversed(orders):
                status_icons = {
                    "Pending": "🟡", "Confirmed": "🔵", "Processing": "⚙️",
                    "Packed": "📦", "Shipped": "🚚", "Out for Delivery": "🏃",
                    "Delivered": "✅", "Cancelled": "❌"
                }
                status = status_icons.get(order['status'], "⏳")
                
                with st.expander(f"{status} Order #{order['id']} | {order['date']} | ₹{order['total']}"):
                    c1, c2 = st.columns(2)
                    c1.write(f"**Customer:** {order['customer']}")
                    c2.write(f"**Phone:** {order['phone']}")
                    c1.write(f"**Payment:** {order['payment']} ({order.get('payment_status', 'Pending')})")
                    c2.write(f"**Status:** {order['status']}")
                    st.write(f"**Address:** {order.get('address', 'N/A')}")
                    
                    st.markdown("#### 🛒 Items")
                    for item in order.get('items', []):
                        st.write(f"• {item['medicine']} x {item['qty']} = ₹{item['total']}")
                    
                    c1, c2, c3 = st.columns(3)
                    c1.write(f"**Subtotal:** ₹{order.get('subtotal', 0)}")
                    c2.write(f"**GST:** ₹{order.get('gst', 0)}")
                    c3.write(f"**Delivery:** ₹{order.get('delivery', 0)}")


def page_online_orders():
    t = translations[st.session_state.lang]
    st.markdown(f'<h1 class="gradient-text" style="font-size:1.8rem;">📦 {t["online_orders"]}</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 All Orders", "🆕 New Order", "📊 Analytics", "🚚 Tracking", "⚙️ Settings"])
    
    with tab1:
        st.markdown("### 📦 Order Management")
        
        c1, c2, c3, c4 = st.columns(4)
        pending = len([o for o in st.session_state.online_orders if o['status'] == "Pending"])
        confirmed = len([o for o in st.session_state.online_orders if o['status'] == "Confirmed"])
        delivered = len([o for o in st.session_state.online_orders if o['status'] == "Delivered"])
        total_revenue = sum(o['total'] for o in st.session_state.online_orders)
        
        c1.metric("Pending", pending)
        c2.metric("Confirmed", confirmed)
        c3.metric("Delivered", delivered)
        c4.metric("Revenue", f"₹{total_revenue:,}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            filter_status = st.selectbox("Filter Status", ["All", "Pending", "Confirmed", "Processing", "Packed", "Shipped", "Out for Delivery", "Delivered", "Cancelled"])
        with c2:
            filter_date = st.date_input("Filter by Date", datetime.now().date())
        with c3:
            filter_payment = st.selectbox("Payment", ["All", "COD", "UPI", "Card", "Bank Transfer"])
        
        orders = st.session_state.online_orders
        
        if filter_status != "All":
            orders = [o for o in orders if o['status'] == filter_status]
        if str(filter_date):
            orders = [o for o in orders if o['date'] == str(filter_date)]
        if filter_payment != "All":
            orders = [o for o in orders if o.get('payment') == filter_payment]
        
        for order in reversed(orders):
            status_icons = {
                "Pending": "🟡", "Confirmed": "🔵", "Processing": "⚙️",
                "Packed": "📦", "Shipped": "🚚", "Out for Delivery": "🏃",
                "Delivered": "✅", "Cancelled": "❌"
            }
            status = status_icons.get(order['status'], "⏳")
            
            with st.expander(f"{status} Order #{order['id']} | {order['date']} | ₹{order['total']}"):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"**👤 Customer:** {order['customer']}")
                    st.markdown(f"**📱 Phone:** {order['phone']}")
                    if order.get('email'):
                        st.markdown(f"**📧 Email:** {order['email']}")
                with c2:
                    st.markdown(f"**💳 Payment:** {order['payment']}")
                    st.markdown(f"**📦 Payment Status:** {order.get('payment_status', 'Pending')}")
                    st.markdown(f"**🚚 Delivery:** {order.get('delivery_type', 'Home Delivery')}")
                
                st.markdown("---")
                st.markdown("#### 🛒 Order Items")
                for item in order.get('items', []):
                    st.markdown(f"- **{item['medicine']}** x {item['qty']} = ₹{item['total']}")
                
                st.markdown("---")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Subtotal", f"₹{order.get('subtotal', 0)}")
                c2.metric("GST", f"₹{order.get('gst', 0)}")
                c3.metric("Delivery", f"₹{order.get('delivery', 0)}")
                c4.metric("Total", f"₹{order['total']}")
                
                st.markdown("#### Update Status")
                c1, c2, c3, c4, c5, c6 = st.columns(6)
                if c1.button("✅ Confirm", key=f"c_{order['id']}"):
                    order['status'] = "Confirmed"
                    st.rerun()
                if c2.button("⚙️ Process", key=f"p_{order['id']}"):
                    order['status'] = "Processing"
                    st.rerun()
                if c3.button("📦 Pack", key=f"pk_{order['id']}"):
                    order['status'] = "Packed"
                    st.rerun()
                if c4.button("🚚 Ship", key=f"s_{order['id']}"):
                    order['status'] = "Shipped"
                    st.rerun()
                if c5.button("🏃 Deliver", key=f"d_{order['id']}"):
                    order['status'] = "Delivered"
                    st.rerun()
                if c6.button("❌ Cancel", key=f"x_{order['id']}"):
                    order['status'] = "Cancelled"
                    st.rerun()
                
                if st.button(f"🗑️ Delete Order", key=f"del_{order['id']}"):
                    st.session_state.online_orders.remove(order)
                    st.success("Order deleted!")
                    st.rerun()
    
    with tab2:
        st.markdown("### 🆕 Create New Order")
        
        with st.form("new_order"):
            c1, c2 = st.columns(2)
            with c1:
                o_customer = st.text_input("Customer Name *")
                o_phone = st.text_input("Phone *")
                o_email = st.text_input("Email")
            with c2:
                o_address = st.text_area("Address *", height=80)
                o_payment = st.selectbox("Payment Mode", ["COD", "UPI", "Card", "Bank Transfer"])
            
            st.markdown("#### Add Items")
            
            if 'order_items' not in st.session_state:
                st.session_state.order_items = []
            
            item_name = st.selectbox("Select Medicine", [m['name'] for m in st.session_state.inventory])
            item_qty = st.number_input("Quantity", min_value=1, value=1)
            item_total = 0
            
            selected_med = next((m for m in st.session_state.inventory if m['name'] == item_name), None)
            if selected_med:
                item_total = selected_med['price'] * item_qty
                st.write(f"**Unit Price:** ₹{selected_med['price']} | **Total:** ₹{item_total}")
            
            if st.button("➕ Add Item"):
                if selected_med:
                    st.session_state.order_items.append({
                        "medicine": selected_med['name'],
                        "price": selected_med['price'],
                        "qty": item_qty,
                        "total": item_total
                    })
                    st.success("Item added!")
            
            if st.session_state.order_items:
                st.markdown("#### Added Items")
                for i, item in enumerate(st.session_state.order_items):
                    st.write(f"• {item['medicine']} x {item['qty']} = ₹{item['total']}")
            
            if st.form_submit_button("💾 Create Order"):
                if not o_customer or not o_phone or not o_address:
                    st.error("Please fill required fields!")
                else:
                    total = sum(item['total'] for item in st.session_state.order_items)
                    st.session_state.online_orders.append({
                        "id": len(st.session_state.online_orders) + 1,
                        "date": str(datetime.now().date()),
                        "time": datetime.now().strftime("%H:%M"),
                        "customer": o_customer,
                        "phone": o_phone,
                        "email": o_email,
                        "address": o_address,
                        "items": st.session_state.order_items.copy(),
                        "subtotal": total,
                        "gst": total * 0.12,
                        "delivery": 0 if total >= 500 else 50,
                        "total": total + (total * 0.12) + (0 if total >= 500 else 50),
                        "payment": o_payment,
                        "status": "Pending",
                        "payment_status": "Pending" if o_payment == "COD" else "Paid"
                    })
                    st.session_state.order_items = []
                    st.success("✅ Order created!")
                    st.rerun()
            
            if st.button("🗑️ Clear Items"):
                st.session_state.order_items = []
                st.rerun()
    
    with tab3:
        st.markdown("### 📊 Order Analytics")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Orders", len(st.session_state.online_orders))
        c2.metric("Total Revenue", f"₹{sum(o['total'] for o in st.session_state.online_orders):,}")
        c3.metric("Avg Order Value", f"₹{sum(o['total'] for o in st.session_state.online_orders) // max(len(st.session_state.online_orders), 1):,}")
        c4.metric("COD Orders", len([o for o in st.session_state.online_orders if o.get('payment') == 'COD']))
        
        st.markdown("#### Orders by Status")
        status_counts = {}
        for o in st.session_state.online_orders:
            status_counts[o['status']] = status_counts.get(o['status'], 0) + 1
        for status, count in status_counts.items():
            st.write(f"**{status}:** {count}")
        
        st.markdown("#### Top Selling Products")
        product_counts = {}
        for o in st.session_state.online_orders:
            for item in o.get('items', []):
                product_counts[item['medicine']] = product_counts.get(item['medicine'], 0) + item['qty']
        for product, qty in sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"• **{product}:** {qty} units")
    
    with tab4:
        st.markdown("### 🚚 Order Tracking")
        
        track_id = st.text_input("Enter Order ID to Track")
        
        if track_id:
            order = next((o for o in st.session_state.online_orders if str(o['id']) == track_id), None)
            if order:
                st.markdown(f"### Order #{order['id']} Status")
                
                stages = ["Pending", "Confirmed", "Processing", "Packed", "Shipped", "Out for Delivery", "Delivered"]
                current = stages.index(order['status']) if order['status'] in stages else 0
                
                for i, stage in enumerate(stages):
                    if i < current:
                        st.success(f"✅ {stage}")
                    elif i == current:
                        st.warning(f"🔄 {stage}")
                    else:
                        st.info(f"⏳ {stage}")
                
                st.markdown(f"""
                - **Customer:** {order['customer']}
                - **Phone:** {order['phone']}
                - **Items:** {len(order.get('items', []))}
                - **Total:** ₹{order['total']}
                """)
            else:
                st.error("Order not found!")
    
    with tab5:
        st.markdown("### ⚙️ Online Store Settings")
        
        with st.expander("💰 Payment Settings"):
            st.toggle("Enable COD", value=True)
            st.toggle("Enable UPI", value=True)
            st.toggle("Enable Card Payment", value=True)
            st.toggle("Enable Bank Transfer", value=True)
            
            st.text_input("UPI ID", value="kalyanimedical@upi")
            st.text_input("Bank Account Number", value="1234567890")
            st.text_input("Bank IFSC Code", value="ABCD0123456")
        
        with st.expander("🚚 Delivery Settings"):
            st.number_input("Free Delivery Minimum (₹)", value=500)
            st.number_input("Delivery Charge (₹)", value=50)
            st.text_area("Delivery Areas", value="Putsuri, Burdwan, Memari, and nearby areas")
        
        with st.expander("🧾 Invoice Settings"):
            st.text_input("Shop Name", value="Kalyani Medical Hall")
            st.text_input("Shop Address", value="Putsuri, Burdwan, WB")
            st.text_input("GST Number", value="19AABCU9603R1ZM")
        
        with st.expander("🔔 Notification Settings"):
            st.toggle("SMS Notifications", value=True)
            st.toggle("Email Notifications", value=True)
            st.toggle("WhatsApp Notifications", value=True)

# ============================================================
# MAIN
# ============================================================

def main():
    render_sidebar()
    
    pages = {
        "dashboard": page_dashboard,
        "sales": page_sales,
        "inventory": page_inventory,
        "staff": page_staff,
        "customers": page_customers,
        "doctors": page_doctors,
        "expenses": page_expenses,
        "reports": page_reports,
        "online_store": page_online_store,
        "online_orders": page_online_orders,
    }
    
    pages.get(st.session_state.current_page, page_dashboard)()

if __name__ == "__main__":
    main()
