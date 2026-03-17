# 📱 App Store Setup Guide

## Icons & Screenshots

### Option 1: Use Free Online Tool (Easiest)

1. Go to: **https://www.appicon.co** or **https://icon.kitchen**
2. Upload a photo or use the medicine/medical cross emoji
3. Download both iOS and Android icons

### Option 2: Create Icons Yourself

1. Create a 1024x1024 PNG image with:
   - **Admin App**: Blue background (#0284c7) + 💊 emoji + "KMH"
   - **Customer App**: Green background (#16a34a) + 🏥 emoji + "KMH"

2. Place icons in:
   - `kalyani_medical/assets/icon/icon.png`
   - `kalyani_medical_customer/assets/icon/icon.png`

### Generate Icons

```bash
cd kalyani_medical
flutter pub get
flutter pub run flutter_launcher_icons

cd ../kalyani_medical_customer
flutter pub get
flutter pub run flutter_launcher_icons
```

---

## 📋 Store Requirements

### Google Play Store
1. App name: "Kalyani Medical Hall"
2. Description: Medical shop CRM for managing inventory, sales, customers
3. Screenshots: 2-3 phone screenshots
4. Privacy Policy: Required (can use free policy generator)

### Apple App Store
1. App name: "Kalyani Medical"
2. Description: Medical shop management app
3. Screenshots: iPhone screenshots (6.5" and 5.5")
4. Privacy Policy: Required

---

## 🚀 Build for Stores

### Android (APK/AAB)
```bash
flutter build apk --release
# Output: build/app/outputs/flutter-apk/app-release.apk

# Or App Bundle (recommended for Play Store)
flutter build appbundle --release
```

### iOS (requires Mac)
```bash
flutter build ios --release
```
Then use Xcode or Transporter to upload to App Store.

---

## 📞 Contact for Help

If you need help, share this with a developer:
- GitHub: https://github.com/animesh-sketch/kalyani-med
- Apps: kalyani_medical (Admin) & kalyani_medical_customer
