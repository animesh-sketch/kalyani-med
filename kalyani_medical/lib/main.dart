import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:uuid/uuid.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initDemoData();
  runApp(const KalyaniMedicalApp());
}

const _uuid = Uuid();

Future<void> initDemoData() async {
  final prefs = await SharedPreferences.getInstance();
  
  if (!prefs.containsKey('initialized')) {
    await prefs.setBool('initialized', true);
    
    // Demo Inventory
    final inventory = [
      {"id": "1", "name": "Paracetamol 500mg", "category": "Pain/Fever", "price": 30.0, "cost": 18.0, "stock": 150, "expiry": "2027-06", "minStock": 50, "manufacturer": "Cipla"},
      {"id": "2", "name": "Metformin 500mg", "category": "Diabetes", "price": 45.0, "cost": 28.0, "stock": 80, "expiry": "2027-03", "minStock": 50, "manufacturer": "Sun Pharma"},
      {"id": "3", "name": "Amlodipine 5mg", "category": "BP/Heart", "price": 35.0, "cost": 20.0, "stock": 120, "expiry": "2027-01", "minStock": 50, "manufacturer": "Zydus"},
      {"id": "4", "name": "Cetirizine 10mg", "category": "Allergy", "price": 25.0, "cost": 15.0, "stock": 200, "expiry": "2027-08", "minStock": 50, "manufacturer": "Dr. Reddy's"},
      {"id": "5", "name": "Azithromycin 500mg", "category": "Antibiotic", "price": 120.0, "cost": 85.0, "stock": 25, "expiry": "2026-12", "minStock": 30, "manufacturer": "Cipla"},
      {"id": "6", "name": "Pantoprazole 40mg", "category": "Gastric", "price": 85.0, "cost": 55.0, "stock": 15, "expiry": "2027-04", "minStock": 30, "manufacturer": "Lupin"},
      {"id": "7", "name": "Aspirin 75mg", "category": "BP/Heart", "price": 28.0, "cost": 15.0, "stock": 180, "expiry": "2027-12", "minStock": 50, "manufacturer": "USV"},
      {"id": "8", "name": "Glimepiride 1mg", "category": "Diabetes", "price": 55.0, "cost": 35.0, "stock": 45, "expiry": "2027-06", "minStock": 50, "manufacturer": "Abbott"},
      {"id": "9", "name": "Omeprazole 20mg", "category": "Gastric", "price": 30.0, "cost": 18.0, "stock": 35, "expiry": "2027-02", "minStock": 40, "manufacturer": "Cipla"},
      {"id": "10", "name": "Vitamin B Complex", "category": "Vitamin", "price": 45.0, "cost": 28.0, "stock": 100, "expiry": "2027-11", "minStock": 50, "manufacturer": "Mankind"},
    ];
    
    for (var item in inventory) {
      await prefs.setString('med_${item["id"]}', item.toString());
    }
    
    // Demo Suppliers
    final suppliers = [
      {"id": "1", "name": "Amit Pharma Distributors", "phone": "9831234567", "address": "Kolkata", "balance": 50000},
      {"id": "2", "name": "Bengal Medical Co", "phone": "9876543210", "address": "Asansol", "balance": 35000},
      {"id": "3", "name": "City Drug House", "phone": "9901234567", "address": "Durgapur", "balance": 25000},
    ];
    
    for (var s in suppliers) {
      await prefs.setString('sup_${s["id"]}', s.toString());
    }
    
    // Demo Staff
    final staff = [
      {"id": "1", "name": "Rajesh Kumar", "phone": "9123456789", "role": "Manager", "salary": 18000, "attendance": 25},
      {"id": "2", "name": "Sunita Devi", "phone": "9876543211", "role": "Pharmacist", "salary": 15000, "attendance": 24},
      {"id": "3", "name": "Mohan Lal", "phone": "9812345678", "role": "Helper", "salary": 10000, "attendance": 26},
    ];
    
    for (var s in staff) {
      await prefs.setString('staff_${s["id"]}', s.toString());
    }
    
    // Demo Customers
    final customers = [
      {"id": "1", "name": "Babulal Saha", "phone": "9876111222", "bloodGroup": "B+", "allergies": "Penicillin", "points": 150, "balance": 0},
      {"id": "2", "name": "Usha Rani", "phone": "9876333444", "bloodGroup": "O+", "allergies": "", "points": 320, "balance": 500},
      {"id": "3", "name": "Subhash Chandra", "phone": "9876555666", "bloodGroup": "A+", "allergies": "Aspirin", "points": 80, "balance": 0},
    ];
    
    for (var c in customers) {
      await prefs.setString('cust_${c["id"]}', c.toString());
    }
    
    // Demo Doctors
    final doctors = [
      {"id": "1", "name": "Dr. Anjan Sen", "phone": "9001234567", "specialty": "General Medicine", "hospital": "Sen Clinic", "patients": 45},
      {"id": "2", "name": "Dr. Moushumi", "phone": "9901234567", "specialty": "Gynecologist", "hospital": "Maternity Home", "patients": 30},
      {"id": "3", "name": "Dr. Tapan Das", "phone": "9831234567", "specialty": "Cardiologist", "hospital": "Heart Care", "patients": 25},
    ];
    
    for (var d in doctors) {
      await prefs.setString('doc_${d["id"]}', d.toString());
    }
  }
}

class AppData {
  static final AppData _instance = AppData._internal();
  factory AppData() => _instance;
  AppData._internal();
  
  int currentIndex = 0;
  String currentTheme = 'medical_blue';
  String currentLang = 'en';
  
  List<Map<String, dynamic>> inventory = [];
  List<Map<String, dynamic>> suppliers = [];
  List<Map<String, dynamic>> staff = [];
  List<Map<String, dynamic>> customers = [];
  List<Map<String, dynamic>> doctors = [];
  List<Map<String, dynamic>> sales = [];
  List<Map<String, dynamic>> expenses = [];
  List<Map<String, dynamic>> onlineOrders = [];
  List<Map<String, dynamic>> cart = [];
}

final translations = {
  "en": {
    "dashboard": "Dashboard",
    "sales": "Sales",
    "inventory": "Inventory & Purchase",
    "staff": "Staff",
    "customers": "Customers",
    "doctors": "Doctors",
    "expenses": "Expenses",
    "reports": "Reports",
    "online_store": "Online Store",
    "online_orders": "Online Orders",
    "today_sales": "Today's Sales",
    "today_profit": "Today's Profit",
    "today_expenses": "Today's Expenses",
    "low_stock": "Low Stock",
    "medicines": "Medicines",
    "suppliers": "Suppliers",
    "add": "Add",
    "save": "Save",
    "search": "Search",
    "category": "Category",
    "price": "Price",
    "stock": "Stock",
    "total": "Total",
    "profit": "Profit",
    "name": "Name",
    "phone": "Phone",
    "address": "Address",
    "salary": "Salary",
    "amount": "Amount",
    "new_sale": "New Sale",
    "add_medicine": "Add Medicine",
    "add_supplier": "Add Supplier",
    "add_staff": "Add Staff",
    "add_customer": "Add Customer",
    "contact": "Contact",
    "years_trust": "30 Years Trust",
    "location": "Putsuri, Burdwan",
  },
  "bn": {
    "dashboard": "ড্যাশবোর্ড",
    "sales": "বিক্রয়",
    "inventory": "মজুদ ও ক্রয়",
    "staff": "কর্মী",
    "customers": "গ্রাহক",
    "doctors": "ডাক্তার",
    "expenses": "খরচ",
    "reports": "রিপোর্ট",
    "online_store": "অনলাইন স্টোর",
    "online_orders": "অনলাইন অর্ডার",
    "today_sales": "আজকের বিক্রয়",
    "today_profit": "আজকের লাভ",
    "today_expenses": "আজকের খরচ",
    "low_stock": "কম স্টক",
    "medicines": "ওষুধ",
    "suppliers": "সরবরাহকারী",
    "add": "যোগ",
    "save": "সংরক্ষণ",
    "search": "খুঁজুন",
    "category": "শ্রেণী",
    "price": "দাম",
    "stock": "স্টক",
    "total": "মোট",
    "profit": "লাভ",
    "name": "নাম",
    "phone": "ফোন",
    "address": "ঠিকানা",
    "salary": "বেতন",
    "amount": "পরিমাণ",
    "new_sale": "নতুন বিক্রয়",
    "add_medicine": "ওষুধ যোগ",
    "add_supplier": "সরবরাহকারী যোগ",
    "add_staff": "কর্মী যোগ",
    "add_customer": "গ্রাহক যোগ",
    "contact": "যোগাযোগ",
    "years_trust": "৩০ বছরের বিশ্বাস",
    "location": "পুটসুড়ি, বর্ধমান",
  }
};

String t(String key) => translations[AppData().currentLang]?[key] ?? translations['en']![key]!;

class KalyaniMedicalApp extends StatelessWidget {
  const KalyaniMedicalApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Kalyani Medical Hall',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.teal,
        useMaterial3: true,
      ),
      home: const MainScreen(),
    );
  }
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(
        index: AppData().currentIndex,
        children: const [
          DashboardScreen(),
          InventoryScreen(),
          SalesScreen(),
          CustomersScreen(),
          StaffScreen(),
          DoctorsScreen(),
          ExpensesScreen(),
          OnlineStoreScreen(),
        ],
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: AppData().currentIndex,
        onDestinationSelected: (i) => setState(() => AppData().currentIndex = i),
        destinations: [
          NavigationDestination(icon: const Icon(Icons.dashboard), label: t('dashboard')),
          NavigationDestination(icon: const Icon(Icons.inventory_2), label: t('inventory')),
          NavigationDestination(icon: const Icon(Icons.point_of_sale), label: t('sales')),
          NavigationDestination(icon: const Icon(Icons.people), label: t('customers')),
          NavigationDestination(icon: const Icon(Icons.personnel), label: t('staff')),
          NavigationDestination(icon: const Icon(Icons.local_hospital), label: t('doctors')),
          NavigationDestination(icon: const Icon(Icons.account_balance_wallet), label: t('expenses')),
          NavigationDestination(icon: const Icon(Icons.shopping_cart), label: t('online_store')),
        ],
      ),
    );
  }
}

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Kalyani Medical Hall'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.language),
            onPressed: () {
              setState(() {
                AppData().currentLang = AppData().currentLang == 'en' ? 'bn' : 'en';
              });
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  children: [
                    const Text('💊', style: TextStyle(fontSize: 48)),
                    const SizedBox(height: 8),
                    Text(t('years_trust'), style: Theme.of(context).textTheme.titleMedium),
                    const SizedBox(height: 4),
                    Text(t('location'), style: Theme.of(context).textTheme.bodySmall),
                    const SizedBox(height: 8),
                    const Text('📞 9619464843 | 7977932585'),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(child: _StatCard(t('today_sales'), '₹12,450', Icons.currency_rupee, Colors.green)),
                const SizedBox(width: 8),
                Expanded(child: _StatCard(t('today_profit'), '₹3,680', Icons.trending_up, Colors.blue)),
              ],
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(child: _StatCard(t('today_expenses'), '₹850', Icons.money_off, Colors.red)),
                const SizedBox(width: 8),
                Expanded(child: _StatCard(t('low_stock'), '3', Icons.warning_amber, Colors.orange)),
              ],
            ),
            const SizedBox(height: 16),
            Text(t('suppliers'), style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  ListTile(leading: const Icon(Icons.business), title: const Text('Amit Pharma'), trailing: const Text('₹50,000')),
                  const Divider(height: 1),
                  ListTile(leading: const Icon(Icons.business), title: const Text('Bengal Medical'), trailing: const Text('₹35,000')),
                  const Divider(height: 1),
                  ListTile(leading: const Icon(Icons.business), title: const Text('City Drug House'), trailing: const Text('₹25,000')),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _StatCard extends StatelessWidget {
  final String title;
  final String value;
  final IconData icon;
  final Color color;

  const _StatCard(this.title, this.value, this.icon, this.color);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Icon(icon, color: color, size: 20),
            const SizedBox(height: 4),
            Text(title, style: Theme.of(context).textTheme.bodySmall),
            Text(value, style: Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}

class InventoryScreen extends StatelessWidget {
  const InventoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final medicines = [
      {"name": "Paracetamol 500mg", "category": "Pain/Fever", "price": 30.0, "stock": 150},
      {"name": "Metformin 500mg", "category": "Diabetes", "price": 45.0, "stock": 80},
      {"name": "Amlodipine 5mg", "category": "BP/Heart", "price": 35.0, "stock": 120},
      {"name": "Cetirizine 10mg", "category": "Allergy", "price": 25.0, "stock": 200},
      {"name": "Azithromycin 500mg", "category": "Antibiotic", "price": 120.0, "stock": 25},
    ];

    return Scaffold(
      appBar: AppBar(title: Text(t('inventory')), actions: [IconButton(icon: const Icon(Icons.add), onPressed: () {})]),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(decoration: InputDecoration(hintText: t('search'), prefixIcon: const Icon(Icons.search), border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)))),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: medicines.length,
              itemBuilder: (ctx, i) {
                final m = medicines[i];
                return Card(
                  margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
                  child: ListTile(
                    title: Text(m['name'] as String),
                    subtitle: Text('${m['category']} | Stock: ${m['stock']}'),
                    trailing: Text('₹${m['price']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                    leading: CircleAvatar(child: Text('${m['stock']}')),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

class SalesScreen extends StatelessWidget {
  const SalesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final recentSales = [
      {"customer": "Babulal Saha", "total": 450, "profit": 120, "time": "10:30 AM"},
      {"customer": "Usha Rani", "total": 890, "profit": 250, "time": "11:15 AM"},
      {"customer": "Subhash Chandra", "total": 320, "profit": 80, "time": "12:00 PM"},
    ];

    return Scaffold(
      appBar: AppBar(title: Text(t('sales'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          ElevatedButton.icon(onPressed: () {}, icon: const Icon(Icons.add), label: Text(t('new_sale')), style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(16))),
          const SizedBox(height: 16),
          Text(t('recent_sales'), style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 8),
          ...recentSales.map((s) => Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              title: Text(s['customer'] as String),
              subtitle: Text(s['time'] as String),
              trailing: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text('₹${s['total']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                  Text('+₹${s['profit']} profit', style: const TextStyle(color: Colors.green, fontSize: 12)),
                ],
              ),
            ),
          )),
        ],
      ),
    );
  }
}

class CustomersScreen extends StatelessWidget {
  const CustomersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final customers = [
      {"name": "Babulal Saha", "phone": "9876111222", "bloodGroup": "B+", "points": 150, "balance": 0},
      {"name": "Usha Rani", "phone": "9876333444", "bloodGroup": "O+", "points": 320, "balance": 500},
      {"name": "Subhash Chandra", "phone": "9876555666", "bloodGroup": "A+", "points": 80, "balance": 0},
    ];

    return Scaffold(
      appBar: AppBar(title: Text(t('customers'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: customers.length,
        itemBuilder: (ctx, i) {
          final c = customers[i];
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(child: Text(c['name'][0])),
              title: Text(c['name']),
              subtitle: Text('${c['phone']} | ${c['bloodGroup']} | ⭐${c['points']}'),
              trailing: c['balance'] > 0 ? Chip(label: Text('₹${c['balance']}'), backgroundColor: Colors.red.shade100) : null,
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(onPressed: () {}, child: const Icon(Icons.add)),
    );
  }
}

class StaffScreen extends StatelessWidget {
  const StaffScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final staff = [
      {"name": "Rajesh Kumar", "phone": "9123456789", "role": "Manager", "salary": 18000},
      {"name": "Sunita Devi", "phone": "9876543211", "role": "Pharmacist", "salary": 15000},
      {"name": "Mohan Lal", "phone": "9812345678", "role": "Helper", "salary": 10000},
    ];

    return Scaffold(
      appBar: AppBar(title: Text(t('staff'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: staff.length,
        itemBuilder: (ctx, i) {
          final s = staff[i];
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: const CircleAvatar(child: Icon(Icons.person)),
              title: Text(s['name']),
              subtitle: Text('${s['role']} | ${s['phone']}'),
              trailing: Text('₹${s['salary']}/-', style: const TextStyle(fontWeight: FontWeight.bold)),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(onPressed: () {}, child: const Icon(Icons.add)),
    );
  }
}

class DoctorsScreen extends StatelessWidget {
  const DoctorsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final doctors = [
      {"name": "Dr. Anjan Sen", "phone": "9001234567", "specialty": "General Medicine", "hospital": "Sen Clinic"},
      {"name": "Dr. Moushumi", "phone": "9901234567", "specialty": "Gynecologist", "hospital": "Maternity Home"},
      {"name": "Dr. Tapan Das", "phone": "9831234567", "specialty": "Cardiologist", "hospital": "Heart Care"},
    ];

    return Scaffold(
      appBar: AppBar(title: Text(t('doctors'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: doctors.length,
        itemBuilder: (ctx, i) {
          final d = doctors[i];
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: const CircleAvatar(child: Icon(Icons.medical_services)),
              title: Text(d['name']),
              subtitle: Text('${d['specialty']} | ${d['hospital']}'),
              trailing: IconButton(icon: const Icon(Icons.phone), onPressed: () {}),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(onPressed: () {}, child: const Icon(Icons.add)),
    );
  }
}

class ExpensesScreen extends StatelessWidget {
  const ExpensesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final expenses = [
      {"category": "Rent", "amount": 15000, "date": "Today"},
      {"category": "Electricity", "amount": 2500, "date": "Yesterday"},
      {"category": "Salary", "amount": 43000, "date": "1 Mar"},
    ];

    return Scaffold(
      appBar: AppBar(title: Text(t('expenses'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          ElevatedButton.icon(onPressed: () {}, icon: const Icon(Icons.add), label: Text(t('add_expense')), style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(16))),
          const SizedBox(height: 16),
          ...expenses.map((e) => Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: const CircleAvatar(child: Icon(Icons.money_off)),
              title: Text(e['category']),
              subtitle: Text(e['date']),
              trailing: Text('₹${e['amount']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            ),
          )),
        ],
      ),
    );
  }
}

class OnlineStoreScreen extends StatelessWidget {
  const OnlineStoreScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final products = [
      {"name": "Paracetamol 500mg", "price": 30, "category": "Pain/Fever"},
      {"name": "Metformin 500mg", "price": 45, "category": "Diabetes"},
      {"name": "Vitamin B Complex", "price": 45, "category": "Vitamin"},
      {"name": "Calcium D3", "price": 120, "category": "Vitamin"},
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text(t('online_store')),
        actions: [
          Stack(
            children: [
              IconButton(icon: const Icon(Icons.shopping_cart), onPressed: () {}),
              Positioned(right: 8, top: 8, child: Container(padding: const EdgeInsets.all(4), decoration: const BoxDecoration(color: Colors.red, shape: BoxShape.circle), child: const Text('0', style: TextStyle(fontSize: 10, color: Colors.white)))),
            ],
          ),
        ],
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(16),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 0.8, crossAxisSpacing: 12, mainAxisSpacing: 12),
        itemCount: products.length,
        itemBuilder: (ctx, i) {
          final p = products[i];
          return Card(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Expanded(child: Icon(Icons.medication, size: 48)),
                  Text(p['name'], style: const TextStyle(fontWeight: FontWeight.bold), maxLines: 2, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: 4),
                  Text(p['category'], style: Theme.of(context).textTheme.bodySmall),
                  const Spacer(),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('₹${p['price']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 18)),
                      ElevatedButton(onPressed: () {}, child: const Text('Add')),
                    ],
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
