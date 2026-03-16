import 'package:flutter/material.dart';

void main() => runApp(const KalyaniCustomerApp());

class AppData {
  static final AppData _instance = AppData._internal();
  factory AppData() => _instance;
  AppData._internal();
  int currentIndex = 0;
  String currentLang = 'en';
  List<Map<String, dynamic>> cart = [];
  List<Map<String, dynamic>> orders = [];
  
  final medicines = [
    {"id": 1, "name": "Paracetamol 500mg", "category": "Pain/Fever", "price": 30.0, "manufacturer": "Cipla", "description": "Relieves pain and fever"},
    {"id": 2, "name": "Metformin 500mg", "category": "Diabetes", "price": 45.0, "manufacturer": "Sun Pharma", "description": "For diabetes management"},
    {"id": 3, "name": "Amlodipine 5mg", "category": "BP/Heart", "price": 35.0, "manufacturer": "Zydus", "description": "Blood pressure medication"},
    {"id": 4, "name": "Cetirizine 10mg", "category": "Allergy", "price": 25.0, "manufacturer": "Dr. Reddy's", "description": "Anti-allergy tablet"},
    {"id": 5, "name": "Azithromycin 500mg", "category": "Antibiotic", "price": 120.0, "manufacturer": "Cipla", "description": "Antibiotic for infections"},
    {"id": 6, "name": "Pantoprazole 40mg", "category": "Gastric", "price": 85.0, "manufacturer": "Lupin", "description": "For acidity and GERD"},
    {"id": 7, "name": "Aspirin 75mg", "category": "BP/Heart", "price": 28.0, "manufacturer": "USV", "description": "Blood thinner"},
    {"id": 8, "name": "Vitamin B Complex", "category": "Vitamin", "price": 45.0, "manufacturer": "Mankind", "description": "Energy vitamin"},
    {"id": 9, "name": "Calcium D3", "category": "Vitamin", "price": 120.0, "manufacturer": "Abbott", "description": "Bone health"},
    {"id": 10, "name": "Dolo 650", "category": "Pain/Fever", "price": 35.0, "manufacturer": "Micro Labs", "description": "Pain relief"},
  ];
  
  List<String> get categories => medicines.map((m) => m['category']).toSet().toList();
  
  double get cartTotal => cart.fold(0.0, (sum, item) => sum + (item['price'] * item['qty']));
}

final translations = {
  "en": {
    "home": "Home", "medicines": "Medicines", "cart": "Cart", "orders": "My Orders", "profile": "Profile",
    "search": "Search medicines...", "categories": "Categories", "add_to_cart": "Add to Cart", "view_cart": "View Cart",
    "checkout": "Checkout", "total": "Total", "empty_cart": "Your cart is empty", "order_placed": "Order Placed!",
    "order_id": "Order ID", "status": "Status", "pending": "Pending", "delivered": "Delivered", "shipped": "Shipped",
    "items": "items", "price": "Price", "quantity": "Quantity", "remove": "Remove", "continue_shopping": "Continue Shopping",
    "place_order": "Place Order", "contact": "Contact Us", "about": "About", "welcome": "Welcome to", "shop_name": "Kalyani Medical Hall",
    "tagline": "30 Years Trust with Empathy and Care", "location": "Putsuri, Burdwan", "phone": "9619464843",
    "all_categories": "All", "out_of_stock": "Out of Stock", "in_stock": "In Stock",
  },
  "bn": {
    "home": "হোম", "medicines": "ওষুধ", "cart": "কার্ট", "orders": "আমার অর্ডার", "profile": "প্রোফাইল",
    "search": "ওষুধ খুঁজুন...", "categories": "শ্রেণী", "add_to_cart": "কার্টে যোগ", "view_cart": "কার্ট দেখুন",
    "checkout": "চেকআউট", "total": "মোট", "empty_cart": "আপনার কার্ট খালি", "order_placed": "অর্ডার হয়েছে!",
    "order_id": "অর্ডার আইডি", "status": "অবস্থা", "pending": "মেয়াদী", "delivered": "প্রাপ্ত", "shipped": "পাঠানো",
    "items": "টি", "price": "দাম", "quantity": "পরিমাণ", "remove": "মুছুন", "continue_shopping": "আরও কেনাকুঁজা",
    "place_order": "অর্ডার করুন", "contact": "যোগাযোগ", "about": "সম্পর্কে", "welcome": "স্বাগতম", "shop_name": "কল্যাণী মেডিক্যাল হল",
    "tagline": "৩০ বছরের বিশ্বাস ও সেবা", "location": "পুটসুড়ি, বর্ধমান", "phone": "৯৬১৯৪৬৪৮৪৩",
    "all_categories": "সব", "out_of_stock": "স্টকে নেই", "in_stock": "স্টকে আছে",
  }
};

String t(String key) => translations[AppData().currentLang]?[key] ?? translations['en']![key]!;

class KalyaniCustomerApp extends StatelessWidget {
  const KalyaniCustomerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Kalyani Medical Hall',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal, brightness: Brightness.light),
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
        children: const [HomeScreen(), MedicinesScreen(), CartScreen(), OrdersScreen(), ProfileScreen()],
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: AppData().currentIndex,
        onDestinationSelected: (i) => setState(() => AppData().currentIndex = i),
        destinations: [
          NavigationDestination(icon: const Icon(Icons.home), label: t('home')),
          NavigationDestination(icon: const Icon(Icons.medication), label: t('medicines')),
          NavigationDestination(icon: const Icon(Icons.shopping_cart), label: t('cart')),
          NavigationDestination(icon: const Icon(Icons.receipt_long), label: t('orders')),
          NavigationDestination(icon: const Icon(Icons.person), label: t('profile')),
        ],
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    return Scaffold(
      appBar: AppBar(
        title: Column(
          children: [
            const Text('💊 Kalyani Medical Hall', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18)),
            Text(t('tagline'), style: const TextStyle(fontSize: 10)),
          ],
        ),
        centerTitle: true,
        toolbarHeight: 60,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Card(
              color: Theme.of(context).colorScheme.primaryContainer,
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  children: [
                    const Icon(Icons.local_pharmacy, size: 48),
                    const SizedBox(height: 8),
                    Text(t('welcome'), style: Theme.of(context).textTheme.titleMedium),
                    Text(t('shop_name'), style: Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.bold)),
                    const SizedBox(height: 8),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Icon(Icons.location_on, size: 16),
                        const SizedBox(width: 4),
                        Text(t('location')),
                      ],
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
            Text(t('categories'), style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            SizedBox(
              height: 100,
              child: ListView(
                scrollDirection: Axis.horizontal,
                children: data.categories.map((cat) => Card(
                  margin: const EdgeInsets.only(right: 8),
                  child: InkWell(
                    onTap: () {
                      data.currentIndex = 1;
                      (context.findAncestorStateOfType<_MainScreenState>())?.setState(() {});
                    },
                    borderRadius: BorderRadius.circular(12),
                    child: Container(
                      width: 100,
                      padding: const EdgeInsets.all(12),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.category, color: Theme.of(context).colorScheme.primary),
                          const SizedBox(height: 8),
                          Text(cat, textAlign: TextAlign.center, style: const TextStyle(fontSize: 12)),
                        ],
                      ),
                    ),
                  ),
                )).toList(),
              ),
            ),
            const SizedBox(height: 16),
            Text(t('medicines'), style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            GridView.builder(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 0.85, crossAxisSpacing: 10, mainAxisSpacing: 10),
              itemCount: 4,
              itemBuilder: (ctx, i) {
                final m = data.medicines[i];
                return Card(
                  child: Padding(
                    padding: const EdgeInsets.all(12),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Center(child: Icon(Icons.medication, size: 40, color: Theme.of(context).colorScheme.primary)),
                        const SizedBox(height: 8),
                        Text(m['name'], style: const TextStyle(fontWeight: FontWeight.bold), maxLines: 2, overflow: TextOverflow.ellipsis),
                        Text(m['category'], style: Theme.of(context).textTheme.bodySmall),
                        const Spacer(),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('₹${m['price']}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Theme.of(context).colorScheme.primary)),
                            IconButton(icon: const Icon(Icons.add_shopping_cart), onPressed: () {
                              data.cart.add({...m, 'qty': 1});
                              ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('${m['name']} added to cart'), duration: const Duration(seconds: 1)));
                            }),
                          ],
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
            const SizedBox(height: 16),
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  children: [
                    const Icon(Icons.phone, color: Colors.green, size: 32),
                    const SizedBox(height: 8),
                    Text(t('contact'), style: Theme.of(context).textTheme.titleMedium),
                    Text(t('phone'), style: Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.bold)),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class MedicinesScreen extends StatefulWidget {
  const MedicinesScreen({super.key});

  @override
  State<MedicinesScreen> createState() => _MedicinesScreenState();
}

class _MedicinesScreenState extends State<MedicinesScreen> {
  String selectedCategory = 'All';
  String searchQuery = '';

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    final categories = ['All', ...data.categories];
    var medicines = selectedCategory == 'All' ? data.medicines : data.medicines.where((m) => m['category'] == selectedCategory).toList();
    if (searchQuery.isNotEmpty) {
      medicines = medicines.where((m) => m['name'].toLowerCase().contains(searchQuery.toLowerCase())).toList();
    }

    return Scaffold(
      appBar: AppBar(title: Text(t('medicines'))),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(
              onChanged: (v) => setState(() => searchQuery = v),
              decoration: InputDecoration(
                hintText: t('search'),
                prefixIcon: const Icon(Icons.search),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                filled: true,
              ),
            ),
          ),
          SizedBox(
            height: 40,
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 12),
              itemCount: categories.length,
              itemBuilder: (ctx, i) => Padding(
                padding: const EdgeInsets.symmetric(horizontal: 4),
                child: FilterChip(
                  label: Text(categories[i]),
                  selected: selectedCategory == categories[i],
                  onSelected: (s) => setState(() => selectedCategory = categories[i]),
                ),
              ),
            ),
          ),
          const SizedBox(height: 8),
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(12),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 0.75, crossAxisSpacing: 10, mainAxisSpacing: 10),
              itemCount: medicines.length,
              itemBuilder: (ctx, i) {
                final m = medicines[i];
                return Card(
                  child: Padding(
                    padding: const EdgeInsets.all(12),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Center(child: Icon(Icons.medication, size: 48, color: Theme.of(context).colorScheme.primary)),
                        Text(m['name'], style: const TextStyle(fontWeight: FontWeight.bold), maxLines: 2, overflow: TextOverflow.ellipsis),
                        Text(m['category'], style: Theme.of(context).textTheme.bodySmall),
                        Text(m['manufacturer'], style: Theme.of(context).textTheme.bodySmall),
                        const Spacer(),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('₹${m['price']}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18, color: Theme.of(context).colorScheme.primary)),
                            ElevatedButton(
                              onPressed: () {
                                data.cart.add({...m, 'qty': 1});
                                ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('${m['name']} added'), duration: const Duration(seconds: 1)));
                              },
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
          ),
        ],
      ),
    );
  }
}

class CartScreen extends StatelessWidget {
  const CartScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    return Scaffold(
      appBar: AppBar(title: Text(t('cart'))),
      body: data.cart.isEmpty
        ? Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            const Icon(Icons.shopping_cart_outlined, size: 80, color: Colors.grey),
            const SizedBox(height: 16),
            Text(t('empty_cart'), style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 16),
            ElevatedButton(onPressed: () => data.currentIndex = 1, child: Text(t('continue_shopping'))),
          ]))
        : Column(
            children: [
              Expanded(
                child: ListView.builder(
                  padding: const EdgeInsets.all(8),
                  itemCount: data.cart.length,
                  itemBuilder: (ctx, i) {
                    final item = data.cart[i];
                    return Card(
                      margin: const EdgeInsets.only(bottom: 8),
                      child: ListTile(
                        leading: CircleAvatar(child: Text('${item['qty']}')),
                        title: Text(item['name']),
                        subtitle: Text('₹${item['price']} x ${item['qty']}'),
                        trailing: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text('₹${item['price'] * item['qty']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                            IconButton(icon: const Icon(Icons.delete, color: Colors.red), onPressed: () {
                              data.cart.removeAt(i);
                              (context.findAncestorStateOfType<State>())?.setState(() {});
                            }),
                          ],
                        ),
                      ),
                    );
                  },
                ),
              ),
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Theme.of(context).colorScheme.primaryContainer,
                  borderRadius: const BorderRadius.vertical(top: Radius.circular(20)),
                ),
                child: Column(
                  children: [
                    Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
                      Text(t('total'), style: Theme.of(context).textTheme.titleLarge),
                      Text('₹${data.cartTotal}', style: Theme.of(context).textTheme.headlineMedium?.copyWith(fontWeight: FontWeight.bold)),
                    ]),
                    const SizedBox(height: 16),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () {
                          final orderId = DateTime.now().millisecondsSinceEpoch;
                          data.orders.add({'id': orderId, 'items': data.cart.length, 'total': data.cartTotal, 'status': 'Pending', 'date': DateTime.now().toString().split(' ')[0]});
                          data.cart.clear();
                          showDialog(context: context, builder: (ctx) => AlertDialog(
                            title: Text(t('order_placed')),
                            content: Text('${t('order_id')}: #$orderId'),
                            actions: [TextButton(onPressed: () { Navigator.pop(ctx); data.currentIndex = 3; }, child: const Text('OK'))],
                          ));
                        },
                        style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(16)),
                        child: Text(t('place_order'), style: const TextStyle(fontSize: 18)),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
    );
  }
}

class OrdersScreen extends StatelessWidget {
  const OrdersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    return Scaffold(
      appBar: AppBar(title: Text(t('orders'))),
      body: data.orders.isEmpty
        ? Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            const Icon(Icons.receipt_long_outlined, size: 80, color: Colors.grey),
            const SizedBox(height: 16),
            Text('No orders yet', style: Theme.of(context).textTheme.titleLarge),
          ]))
        : ListView.builder(
            padding: const EdgeInsets.all(8),
            itemCount: data.orders.length,
            itemBuilder: (ctx, i) {
              final o = data.orders[i];
              Color statusColor = o['status'] == 'Pending' ? Colors.orange : o['status'] == 'Shipped' ? Colors.blue : Colors.green;
              return Card(
                margin: const EdgeInsets.only(bottom: 8),
                child: ListTile(
                  leading: CircleAvatar(backgroundColor: statusColor.shade100, child: Icon(Icons.receipt, color: statusColor)),
                  title: Text('Order #${o['id']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                  subtitle: Text('${o['items']} items | ${o['date']}'),
                  trailing: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('₹${o['total']}', style: const TextStyle(fontWeight: FontWeight.bold)),
                      Chip(label: Text(o['status'], style: TextStyle(color: statusColor, fontSize: 10)), backgroundColor: statusColor.shade50, padding: EdgeInsets.zero),
                    ],
                  ),
                ),
              );
            },
          ),
    );
  }
}

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final data = AppData();
    return Scaffold(
      appBar: AppBar(title: Text(t('profile'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                children: [
                  const CircleAvatar(radius: 40, child: Icon(Icons.person, size: 40)),
                  const SizedBox(height: 16),
                  Text('Guest User', style: Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight: FontWeight.bold)),
                  Text(t('shop_name'), style: Theme.of(context).textTheme.bodyMedium),
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
                  title: Text(t('profile')),
                  trailing: SegmentedButton<String>(
                    segments: const [ButtonSegment(value: 'en', label: Text('EN')), ButtonSegment(value: 'bn', label: Text('বাং'))],
                    selected: {data.currentLang},
                    onSelectionChanged: (s) => setState(() => data.currentLang = s.first),
                  ),
                ),
                const Divider(height: 1),
                ListTile(leading: const Icon(Icons.phone, color: Colors.green), title: Text(t('contact')), subtitle: const Text('9619464843 | 7977932585')),
                const Divider(height: 1),
                ListTile(leading: const Icon(Icons.location_on), title: Text(t('location')), subtitle: const Text('Putsuri, Burdwan, WB')),
                const Divider(height: 1),
                ListTile(leading: const Icon(Icons.info), title: const Text('About'), subtitle: Text(t('tagline'))),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
