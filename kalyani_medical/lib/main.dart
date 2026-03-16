import 'package:flutter/material.dart';

void main() {
  runApp(const KalyaniMedicalApp());
}

class AppData {
  static final AppData _instance = AppData._internal();
  factory AppData() => _instance;
  AppData._internal();
  
  int currentIndex = 0;
  String currentTheme = 'medical_blue';
  String currentLang = 'en';
  
  List<Map<String, dynamic>> cart = [];
  
  final medicines = [
    {"id": 1, "name": "Paracetamol 500mg", "category": "Pain/Fever", "price": 30.0, "cost": 18.0, "stock": 150, "expiry": "2027-06", "minStock": 50, "manufacturer": "Cipla"},
    {"id": 2, "name": "Metformin 500mg", "category": "Diabetes", "price": 45.0, "cost": 28.0, "stock": 80, "expiry": "2027-03", "minStock": 50, "manufacturer": "Sun Pharma"},
    {"id": 3, "name": "Amlodipine 5mg", "category": "BP/Heart", "price": 35.0, "cost": 20.0, "stock": 120, "expiry": "2027-01", "minStock": 50, "manufacturer": "Zydus"},
    {"id": 4, "name": "Cetirizine 10mg", "category": "Allergy", "price": 25.0, "cost": 15.0, "stock": 200, "expiry": "2027-08", "minStock": 50, "manufacturer": "Dr. Reddy's"},
    {"id": 5, "name": "Azithromycin 500mg", "category": "Antibiotic", "price": 120.0, "cost": 85.0, "stock": 25, "expiry": "2026-12", "minStock": 30, "manufacturer": "Cipla"},
    {"id": 6, "name": "Pantoprazole 40mg", "category": "Gastric", "price": 85.0, "cost": 55.0, "stock": 15, "expiry": "2027-04", "minStock": 30, "manufacturer": "Lupin"},
    {"id": 7, "name": "Aspirin 75mg", "category": "BP/Heart", "price": 28.0, "cost": 15.0, "stock": 180, "expiry": "2027-12", "minStock": 50, "manufacturer": "USV"},
    {"id": 8, "name": "Glimepiride 1mg", "category": "Diabetes", "price": 55.0, "cost": 35.0, "stock": 45, "expiry": "2027-06", "minStock": 50, "manufacturer": "Abbott"},
    {"id": 9, "name": "Omeprazole 20mg", "category": "Gastric", "price": 30.0, "cost": 18.0, "stock": 35, "expiry": "2027-02", "minStock": 40, "manufacturer": "Cipla"},
    {"id": 10, "name": "Vitamin B Complex", "category": "Vitamin", "price": 45.0, "cost": 28.0, "stock": 100, "expiry": "2027-11", "minStock": 50, "manufacturer": "Mankind"},
    {"id": 11, "name": "Calcium D3", "category": "Vitamin", "price": 120.0, "cost": 75.0, "stock": 70, "expiry": "2027-08", "minStock": 40, "manufacturer": "Abbott"},
    {"id": 12, "name": "Combiflam", "category": "Pain/Fever", "price": 20.0, "cost": 12.0, "stock": 200, "expiry": "2027-07", "minStock": 60, "manufacturer": "Sanofi"},
    {"id": 13, "name": "Dolo 650", "category": "Pain/Fever", "price": 35.0, "cost": 20.0, "stock": 180, "expiry": "2027-12", "minStock": 50, "manufacturer": "Micro Labs"},
    {"id": 14, "name": "Montek LC", "category": "Allergy", "price": 95.0, "cost": 60.0, "stock": 55, "expiry": "2027-04", "minStock": 30, "manufacturer": "Sun Pharma"},
    {"id": "15,", "name": "Augmentin 625mg", "category": "Antibiotic", "price": 320.0, "cost": 220.0, "stock": 20, "expiry": "2026-11", "minStock": 25, "manufacturer": "GSK"},
  ];
  
  final suppliers = [
    {"id": 1, "name": "Amit Pharma Distributors", "phone": "9831234567", "address": "Kolkata", "balance": 50000},
    {"id": 2, "name": "Bengal Medical Co", "phone": "9876543210", "address": "Asansol", "balance": 35000},
    {"id": 3, "name": "City Drug House", "phone": "9901234567", "address": "Durgapur", "balance": 25000},
  ];
  
  final staff = [
    {"id": 1, "name": "Rajesh Kumar", "phone": "9123456789", "role": "Manager", "salary": 18000, "attendance": 25},
    {"id": 2, "name": "Sunita Devi", "phone": "9876543211", "role": "Pharmacist", "salary": 15000, "attendance": 24},
    {"id": 3, "name": "Mohan Lal", "phone": "9812345678", "role": "Helper", "salary": 10000, "attendance": 26},
  ];
  
  final customers = [
    {"id": 1, "name": "Babulal Saha", "phone": "9876111222", "bloodGroup": "B+", "allergies": "Penicillin", "points": 150, "balance": 0},
    {"id": 2, "name": "Usha Rani", "phone": "9876333444", "bloodGroup": "O+", "allergies": "", "points": 320, "balance": 500},
    {"id": 3, "name": "Subhash Chandra", "phone": "9876555666", "bloodGroup": "A+", "allergies": "Aspirin", "points": 80, "balance": 0},
  ];
  
  final doctors = [
    {"id": 1, "name": "Dr. Anjan Sen", "phone": "9001234567", "specialty": "General Medicine", "hospital": "Sen Clinic", "patients": 45},
    {"id": 2, "name": "Dr. Moushumi", "phone": "9901234567", "specialty": "Gynecologist", "hospital": "Maternity Home", "patients": 30},
    {"id": 3, "name": "Dr. Tapan Das", "phone": "9831234567", "specialty": "Cardiologist", "hospital": "Heart Care", "patients": 25},
  ];
  
  final sales = [
    {"customer": "Babulal Saha", "total": 450, "profit": 120, "time": "10:30 AM", "items": 3},
    {"customer": "Usha Rani", "total": 890, "profit": 250, "time": "11:15 AM", "items": 5},
    {"customer": "Subhash Chandra", "total": 320, "profit": 80, "time": "12:00 PM", "items": 2},
    {"customer": "Mina Devi", "total": 1250, "profit": 380, "time": "01:30 PM", "items": 4},
  ];
  
  final expenses = [
    {"category": "Rent", "amount": 15000, "date": "Today", "note": "Monthly"},
    {"category": "Electricity", "amount": 2500, "date": "Yesterday", "note": "Bill"},
    {"category": "Salary", "amount": 43000, "date": "1 Mar", "note": "Staff"},
    {"category": "Internet", "amount": 999, "date": "28 Feb", "note": "Monthly"},
  ];
  
  final onlineOrders = [
    {"id": 101, "customer": "Ravi Kumar", "items": 3, "total": 450, "status": "Pending"},
    {"id": 102, "customer": "Priya Singh", "items": 5, "total": 890, "status": "Shipped"},
    {"id": 103, "customer": "Amit Roy", "items": 2, "total": 320, "status": "Delivered"},
  ];
  
  List<Map<String, dynamic>> get lowStockMedicines => 
    medicines.where((m) => m['stock'] < m['minStock']).toList();
  
  double get totalStockValue => 
    medicines.fold(0.0, (sum, m) => sum + (m['stock'] * m['price']));
  
  double get todaySales => sales.fold(0.0, (sum, s) => sum + (s['total'] as num).toDouble());
  double get todayProfit => sales.fold(0.0, (sum, s) => sum + (s['profit'] as num).toDouble());
  double get todayExpenses => expenses.fold(0.0, (sum, e) => sum + (e['amount'] as num).toDouble());
}

final translations = {
  "en": {
    "dashboard": "Dashboard", "sales": "Sales", "inventory": "Inventory", "staff": "Staff",
    "customers": "Customers", "doctors": "Doctors", "expenses": "Expenses", "reports": "Reports",
    "online_store": "Online Store", "online_orders": "Online Orders", "settings": "Settings",
    "today_sales": "Today's Sales", "today_profit": "Today's Profit", "today_expenses": "Today's Expenses",
    "low_stock": "Low Stock", "total_medicines": "Total Medicines", "suppliers": "Suppliers",
    "add": "Add", "save": "Save", "search": "Search...", "category": "Category", "price": "Price",
    "stock": "Stock", "total": "Total", "profit": "Profit", "name": "Name", "phone": "Phone",
    "address": "Address", "salary": "Salary", "amount": "Amount", "new_sale": "New Sale",
    "recent_sales": "Recent Sales", "add_medicine": "Add Medicine", "add_supplier": "Add Supplier",
    "add_staff": "Add Staff", "add_customer": "Add Customer", "contact": "Contact",
    "years_trust": "30 Years Trust", "location": "Putsuri, Burdwan", "theme": "Theme",
    "language": "Language", "low_stock_alert": "Low Stock Alert", "expiring_soon": "Expiring Soon",
    "all_well": "All medicines well stocked!", "view_all": "View All", "quick_actions": "Quick Actions",
    "add_expense": "Add Expense", "orders": "Orders", "pending": "Pending", "shipped": "Shipped",
    "delivered": "Delivered", "cart": "Cart", "checkout": "Checkout", "empty_cart": "Cart is empty",
  },
  "bn": {
    "dashboard": "ড্যাশবোর্ড", "sales": "বিক্রয়", "inventory": "মজুদ", "staff": "কর্মী",
    "customers": "গ্রাহক", "doctors": "ডাক্তার", "expenses": "খরচ", "reports": "রিপোর্ট",
    "online_store": "অনলাইন স্টোর", "online_orders": "অনলাইন অর্ডার", "settings": "সেটিংস",
    "today_sales": "আজকের বিক্রয়", "today_profit": "আজকের লাভ", "today_expenses": "আজকের খরচ",
    "low_stock": "কম স্টক", "total_medicines": "মোট ওষুধ", "suppliers": "সরবরাহকারী",
    "add": "যোগ", "save": "সংরক্ষণ", "search": "খুঁজুন...", "category": "শ্রেণী", "price": "দাম",
    "stock": "স্টক", "total": "মোট", "profit": "লাভ", "name": "নাম", "phone": "ফোন",
    "address": "ঠিকানা", "salary": "বেতন", "amount": "পরিমাণ", "new_sale": "নতুন বিক্রয়",
    "recent_sales": "সাম্প্রতিক বিক্রয়", "add_medicine": "ওষুধ যোগ", "add_supplier": "সরবরাহকারী যোগ",
    "add_staff": "কর্মী যোগ", "add_customer": "গ্রাহক যোগ", "contact": "যোগাযোগ",
    "years_trust": "৩০ বছরের বিশ্বাস", "location": "পুটসুড়ি, বর্ধমান", "theme": "থিম",
    "language": "ভাষা", "low_stock_alert": "কম স্টক সতর্কতা", "expiring_soon": "শীঘ্র মেয়াদ",
    "all_well": "সব ওষুধ মজুদ আছে!", "view_all": "সব দেখুন", "quick_actions": "দ্রুত কাজ",
    "add_expense": "খরচ যোগ", "orders": "অর্ডার", "pending": "মেয়াদী", "shipped": "পাঠানো",
    "delivered": "প্রাপ্ত", "cart": "কার্ট", "checkout": "চেকআউট", "empty_cart": "কার্ট খালি",
  }
};

String t(String key) => translations[AppData().currentLang]?[key] ?? translations['en']![key]!;

final themeConfigs = {
  "medical_blue": {"primary": const Color(0xFF0284c7), "bg": const Color(0xFFf0f9ff), "name": "Medical Blue"},
  "nature_green": {"primary": const Color(0xFF16a34a), "bg": const Color(0xFFf0fdf4), "name": "Nature Green"},
  "royal_purple": {"primary": const Color(0xFF7c3aed), "bg": const Color(0xFFfaf5ff), "name": "Royal Purple"},
  "elegant_gold": {"primary": const Color(0xFFb45309), "bg": const Color(0xFFfffbeb), "name": "Elegant Gold"},
  "ruby_red": {"primary": const Color(0xFFdc2626), "bg": const Color(0xFFfef2f2), "name": "Ruby Red"},
  "ocean_teal": {"primary": const Color(0xFF0891b2), "bg": const Color(0xFFecfeff), "name": "Ocean Teal"},
  "sunset_orange": {"primary": const Color(0xFFea580c), "bg": const Color(0xFFfff7ed), "name": "Sunset Orange"},
  "dark_mode": {"primary": const Color(0xFF6366f1), "bg": const Color(0xFF1e1e2e), "name": "Dark Mode"},
};

class KalyaniMedicalApp extends StatelessWidget {
  const KalyaniMedicalApp({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = themeConfigs[AppData().currentTheme]!;
    final isDark = AppData().currentTheme == 'dark_mode';
    
    return MaterialApp(
      title: 'Kalyani Medical Hall',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: theme['primary'],
          brightness: isDark ? Brightness.dark : Brightness.light,
        ),
        scaffoldBackgroundColor: isDark ? const Color(0xFF1e1e2e) : theme['bg'],
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
          OnlineOrdersScreen(),
          SettingsScreen(),
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
          NavigationDestination(icon: const Icon(Icons.person), label: t('staff')),
          NavigationDestination(icon: const Icon(Icons.local_hospital), label: t('doctors')),
          NavigationDestination(icon: const Icon(Icons.account_balance_wallet), label: t('expenses')),
          NavigationDestination(icon: const Icon(Icons.shopping_bag), label: t('online_store')),
          NavigationDestination(icon: const Icon(Icons.local_shipping), label: t('online_orders')),
          NavigationDestination(icon: const Icon(Icons.settings), label: t('settings')),
        ],
      ),
    );
  }
}

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    final lowStock = data.lowStockMedicines;
    
    return Scaffold(
      appBar: AppBar(
        title: Column(
          children: [
            const Text('💊 Kalyani Medical Hall', style: TextStyle(fontWeight: FontWeight.bold)),
            Text(t('years_trust'), style: const TextStyle(fontSize: 12)),
          ],
        ),
        centerTitle: true,
        toolbarHeight: 70,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Row(
                  children: [
                    Expanded(
                      child: Column(
                        children: [
                          Text(t('location'), style: Theme.of(context).textTheme.bodySmall),
                          const SizedBox(height: 8),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              const Icon(Icons.phone, size: 16),
                              const SizedBox(width: 4),
                              const Text('9619464843'),
                              const Text(' | '),
                              const Text('7977932585'),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(child: _StatCard(t('today_sales'), '₹${data.todaySales.toStringAsFixed(0)}', Icons.currency_rupee, Colors.green)),
                const SizedBox(width: 8),
                Expanded(child: _StatCard(t('today_profit'), '₹${data.todayProfit.toStringAsFixed(0)}', Icons.trending_up, Colors.blue)),
              ],
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(child: _StatCard(t('today_expenses'), '₹${data.todayExpenses.toStringAsFixed(0)}', Icons.money_off, Colors.red)),
                const SizedBox(width: 8),
                Expanded(child: _StatCard(t('total_medicines'), '${data.medicines.length}', Icons.medication, Colors.purple)),
              ],
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(child: _StatCard(t('low_stock'), '${lowStock.length}', Icons.warning_amber, Colors.orange)),
                const SizedBox(width: 8),
                Expanded(child: _StatCard(t('suppliers'), '${data.suppliers.length}', Icons.business, Colors.teal)),
              ],
            ),
            const SizedBox(height: 20),
            Text(t('suppliers'), style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: data.suppliers.asMap().entries.map((e) {
                  final s = e.value;
                  return Column(
                    children: [
                      ListTile(
                        leading: CircleAvatar(backgroundColor: Theme.of(context).colorScheme.primaryContainer, 
                          child: Text('${e.key + 1}', style: TextStyle(color: Theme.of(context).colorScheme.onPrimaryContainer))),
                        title: Text(s['name']),
                        subtitle: Text('${s['phone']} | ${s['address']}'),
                        trailing: Text('₹${s['balance']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                      ),
                      if (e.key < data.suppliers.length - 1) const Divider(height: 1),
                    ],
                  );
                }).toList(),
              ),
            ),
            const SizedBox(height: 20),
            Text(t('quick_actions'), style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(child: _ActionButton(t('new_sale'), Icons.add_circle, () => AppData().currentIndex = 2)),
                const SizedBox(width: 8),
                Expanded(child: _ActionButton(t('add_medicine'), Icons.medication, () {})),
                const SizedBox(width: 8),
                Expanded(child: _ActionButton(t('add_expense'), Icons.money_off, () => AppData().currentIndex = 6)),
              ],
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

class _ActionButton extends StatelessWidget {
  final String label;
  final IconData icon;
  final VoidCallback onTap;

  const _ActionButton(this.label, this.icon, this.onTap);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 8),
          child: Column(
            children: [
              Icon(icon, color: Theme.of(context).colorScheme.primary),
              const SizedBox(height: 4),
              Text(label, style: const TextStyle(fontSize: 11), textAlign: TextAlign.center, maxLines: 2),
            ],
          ),
        ),
      ),
    );
  }
}

class InventoryScreen extends StatelessWidget {
  const InventoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    final lowStock = data.lowStockMedicines;
    
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        appBar: AppBar(
          title: Text(t('inventory')),
          bottom: TabBar(
            tabs: [
              Tab(text: t('medicines')),
              Tab(text: t('low_stock')),
              Tab(text: t('suppliers')),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            ListView.builder(
              padding: const EdgeInsets.all(8),
              itemCount: data.medicines.length,
              itemBuilder: (ctx, i) {
                final m = data.medicines[i];
                final isLow = m['stock'] < m['minStock'];
                return Card(
                  color: isLow ? Colors.red.shade50 : null,
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: isLow ? Colors.red : Theme.of(context).colorScheme.primaryContainer,
                      child: Icon(Icons.medication, color: isLow ? Colors.red : Theme.of(context).colorScheme.onPrimaryContainer),
                    ),
                    title: Text(m['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
                    subtitle: Text('${m['category']} | ${m['manufacturer']} | Exp: ${m['expiry']}'),
                    trailing: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        Text('₹${m['price']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                        Text('Stock: ${m['stock']}', style: TextStyle(color: isLow ? Colors.red : Colors.green, fontWeight: FontWeight.bold)),
                      ],
                    ),
                  ),
                );
              },
            ),
            lowStock.isEmpty 
              ? Center(child: Text(t('all_well'), style: const TextStyle(fontSize: 18)))
              : ListView.builder(
                  padding: const EdgeInsets.all(8),
                  itemCount: lowStock.length,
                  itemBuilder: (ctx, i) {
                    final m = lowStock[i];
                    return Card(
                      color: Colors.red.shade50,
                      child: ListTile(
                        leading: const CircleAvatar(backgroundColor: Colors.red, child: Icon(Icons.warning, color: Colors.white)),
                        title: Text(m['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
                        subtitle: Text('Min: ${m['minStock']} | Current: ${m['stock']}'),
                        trailing: Text('Low!', style: const TextStyle(color: Colors.red, fontWeight: FontWeight.bold)),
                      ),
                    );
                  },
                ),
            ListView.builder(
              padding: const EdgeInsets.all(8),
              itemCount: data.suppliers.length,
              itemBuilder: (ctx, i) {
                final s = data.suppliers[i];
                return Card(
                  child: ListTile(
                    leading: const CircleAvatar(child: Icon(Icons.business)),
                    title: Text(s['name']),
                    subtitle: Text('${s['phone']} | ${s['address']}'),
                    trailing: Text('₹${s['balance']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                  ),
                );
              },
            ),
          ],
        ),
        floatingActionButton: FloatingActionButton(onPressed: () {}, child: const Icon(Icons.add)),
      ),
    );
  }
}

class SalesScreen extends StatelessWidget {
  const SalesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(
        title: Text(t('sales')),
        actions: [
          IconButton(icon: const Icon(Icons.history), onPressed: () {}),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            color: Theme.of(context).colorScheme.primaryContainer,
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                children: [
                  const Icon(Icons.point_of_sale, size: 48),
                  const SizedBox(height: 8),
                  Text(t('new_sale'), style: Theme.of(context).textTheme.headlineSmall),
                  const SizedBox(height: 16),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton.icon(
                      onPressed: () {},
                      icon: const Icon(Icons.add),
                      label: Text(t('new_sale')),
                      style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(16)),
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          Text(t('recent_sales'), style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          ...data.sales.map((s) => Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.green.shade100,
                child: const Icon(Icons.person, color: Colors.green),
              ),
              title: Text(s['customer'], style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('${s['items']} items | ${s['time']}'),
              trailing: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text('₹${s['total']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                  Text('+₹${s['profit']}', style: const TextStyle(color: Colors.green, fontSize: 12)),
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
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(title: Text(t('customers'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(8),
        itemCount: data.customers.length,
        itemBuilder: (ctx, i) {
          final c = data.customers[i];
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Theme.of(context).colorScheme.primaryContainer,
                child: Text(c['name'][0], style: TextStyle(color: Theme.of(context).colorScheme.onPrimaryContainer)),
              ),
              title: Text(c['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('${c['phone']} | 🩸 ${c['bloodGroup']}'),
                  if (c['allergies'].isNotEmpty) Text('⚠️ Allergies: ${c['allergies']}', style: const TextStyle(color: Colors.red, fontSize: 12)),
                ],
              ),
              trailing: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text('⭐ ${c['points']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                  if (c['balance'] > 0) Chip(label: Text('₹${c['balance']}'), backgroundColor: Colors.red.shade100, padding: EdgeInsets.zero),
                ],
              ),
              isThreeLine: c['allergies'].isNotEmpty,
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
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(title: Text(t('staff'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(8),
        itemCount: data.staff.length,
        itemBuilder: (ctx, i) {
          final s = data.staff[i];
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.blue.shade100,
                child: const Icon(Icons.person, color: Colors.blue),
              ),
              title: Text(s['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('${s['role']} | 📞 ${s['phone']} | ✅ ${s['attendance']} days'),
              trailing: Text('₹${s['salary']}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
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
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(title: Text(t('doctors'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(8),
        itemCount: data.doctors.length,
        itemBuilder: (ctx, i) {
          final d = data.doctors[i];
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.purple.shade100,
                child: const Icon(Icons.medical_services, color: Colors.purple),
              ),
              title: Text(d['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('${d['specialty']} | 🏥 ${d['hospital']} | 👥 ${d['patients']} patients'),
              trailing: IconButton(icon: const Icon(Icons.phone, color: Colors.green), onPressed: () {}),
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
    final data = AppData();
    final total = data.todayExpenses;
    
    return Scaffold(
      appBar: AppBar(title: Text(t('expenses'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            color: Colors.red.shade50,
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Row(
                children: [
                  const Icon(Icons.money_off, color: Colors.red, size: 40),
                  const SizedBox(width: 16),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(t('today_expenses'), style: Theme.of(context).textTheme.titleMedium),
                      Text('₹$total', style: Theme.of(context).textTheme.headlineMedium?.copyWith(fontWeight: FontWeight.bold, color: Colors.red)),
                    ],
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: () {},
              icon: const Icon(Icons.add),
              label: Text(t('add_expense')),
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(16)),
            ),
          ),
          const SizedBox(height: 16),
          ...data.expenses.map((e) => Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.orange.shade100,
                child: const Icon(Icons.receipt, color: Colors.orange),
              ),
              title: Text(e['category'], style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('${e['date']} | ${e['note']}'),
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
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(
        title: Text(t('online_store')),
        actions: [
          Stack(
            children: [
              IconButton(icon: const Icon(Icons.shopping_cart), onPressed: () {}),
              if (data.cart.isNotEmpty)
                Positioned(right: 8, top: 8, child: Container(
                  padding: const EdgeInsets.all(4),
                  decoration: const BoxDecoration(color: Colors.red, shape: BoxShape.circle),
                  child: Text('${data.cart.length}', style: const TextStyle(fontSize: 10, color: Colors.white)),
                )),
            ],
          ),
        ],
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(12),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 0.75, crossAxisSpacing: 10, mainAxisSpacing: 10),
        itemCount: data.medicines.length,
        itemBuilder: (ctx, i) {
          final p = data.medicines[i];
          return Card(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Center(child: Icon(Icons.medication, size: 48, color: Theme.of(context).colorScheme.primary)),
                  const SizedBox(height: 8),
                  Text(p['name'], style: const TextStyle(fontWeight: FontWeight.bold), maxLines: 2, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: 4),
                  Text(p['category'], style: Theme.of(context).textTheme.bodySmall),
                  const Spacer(),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('₹${p['price']}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18, color: Theme.of(context).colorScheme.primary)),
                      ElevatedButton(
                        onPressed: () {
                          data.cart.add(p);
                          ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('${p['name']} added to cart'), duration: const Duration(seconds: 1)));
                        },
                        style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8)),
                        child: const Text('Add'),
                      ),
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

class OnlineOrdersScreen extends StatelessWidget {
  const OnlineOrdersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(title: Text(t('online_orders'))),
      body: ListView.builder(
        padding: const EdgeInsets.all(8),
        itemCount: data.onlineOrders.length,
        itemBuilder: (ctx, i) {
          final o = data.onlineOrders[i];
          Color statusColor;
          if (o['status'] == 'Pending') statusColor = Colors.orange;
          else if (o['status'] == 'Shipped') statusColor = Colors.blue;
          else statusColor = Colors.green;
          
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: statusColor.shade100,
                child: Icon(Icons.local_shipping, color: statusColor),
              ),
              title: Text('Order #${o['id']}', style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('${o['customer']} | ${o['items']} items'),
              trailing: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text('₹${o['total']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                  Chip(label: Text(o['status'], style: TextStyle(color: statusColor, fontSize: 12)), backgroundColor: statusColor.shade50, padding: EdgeInsets.zero),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  @override
  Widget build(BuildContext context) {
    final data = AppData();
    
    return Scaffold(
      appBar: AppBar(title: Text(t('settings'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  const Text('💊', style: TextStyle(fontSize: 48)),
                  const SizedBox(height: 8),
                  Text('Kalyani Medical Hall', style: Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight: FontWeight.bold)),
                  Text(t('years_trust'), style: Theme.of(context).textTheme.bodySmall),
                  const SizedBox(height: 8),
                  Text(t('location')),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          Card(
            child: Column(
              children: [
                ListTile(
                  leading: const Icon(Icons.language),
                  title: Text(t('language')),
                  trailing: SegmentedButton<String>(
                    segments: const [
                      ButtonSegment(value: 'en', label: Text('EN')),
                      ButtonSegment(value: 'bn', label: Text('বাং')),
                    ],
                    selected: {data.currentLang},
                    onSelectionChanged: (s) => setState(() => data.currentLang = s.first),
                  ),
                ),
                const Divider(height: 1),
                ListTile(
                  leading: const Icon(Icons.palette),
                  title: Text(t('theme')),
                  subtitle: Text(themeConfigs[data.currentTheme]!['name']),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: themeConfigs.entries.map((e) => ChoiceChip(
              label: Text(e.value['name']),
              selected: data.currentTheme == e.key,
              onSelected: (s) => setState(() => data.currentTheme = e.key),
            )).toList(),
          ),
          const SizedBox(height: 16),
          Card(
            child: Column(
              children: [
                ListTile(
                  leading: const Icon(Icons.phone, color: Colors.green),
                  title: Text(t('contact')),
                  subtitle: const Text('9619464843 | 7977932585'),
                ),
                const Divider(height: 1),
                const ListTile(
                  leading: Icon(Icons.info),
                  title: Text('Version'),
                  subtitle: Text('1.0.0'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
