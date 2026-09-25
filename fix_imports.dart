
import 'dart:io';

void main() {
  final dir = Directory('lib');
  final mappings = {
    "import 'core/theme.dart';": "import 'package:zariya_app/core/theme/app_theme.dart';",
    "import '../core/theme.dart';": "import 'package:zariya_app/core/theme/app_theme.dart';",
    "import '../core/api_service.dart';": "import 'package:zariya_app/core/services/api_service.dart';",
    "import '../core/offline_cache.dart';": "import 'package:zariya_app/core/services/offline_cache.dart';",
    "import '../core/payment_service.dart';": "import 'package:zariya_app/core/services/payment_service.dart';",
    "import '../core/secure_storage.dart';": "import 'package:zariya_app/features/auth/data/secure_storage.dart';",
    "import '../core/biometric_helper.dart';": "import 'package:zariya_app/features/auth/data/biometric_helper.dart';",
    "import '../core/constants.dart';": "import 'package:zariya_app/core/utils/constants.dart';",
    "import '../core/haptic_helper.dart';": "import 'package:zariya_app/core/utils/haptic_helper.dart';",
    "import '../core/share_helper.dart';": "import 'package:zariya_app/core/utils/share_helper.dart';",
    "import '../core/app_strings.dart';": "import 'package:zariya_app/core/utils/app_strings.dart';",
    "import '../core/search_history.dart';": "import 'package:zariya_app/features/shop/data/search_history.dart';",
    "import '../models/product.dart';": "import 'package:zariya_app/features/shop/data/product.dart';",
    "import '../models/cart.dart';": "import 'package:zariya_app/features/cart/data/cart.dart';",
    "import '../models/order.dart';": "import 'package:zariya_app/features/profile/data/order.dart';",
    "import '../models/user.dart';": "import 'package:zariya_app/features/profile/data/user.dart';",
    "import '../providers/auth_provider.dart';": "import 'package:zariya_app/features/auth/data/auth_provider.dart';",
    "import '../providers/product_provider.dart';": "import 'package:zariya_app/features/shop/data/product_provider.dart';",
    "import '../providers/cart_provider.dart';": "import 'package:zariya_app/features/cart/data/cart_provider.dart';",
    "import '../providers/wishlist_provider.dart';": "import 'package:zariya_app/features/shop/data/wishlist_provider.dart';",
    "import '../providers/theme_provider.dart';": "import 'package:zariya_app/core/services/theme_provider.dart';",
    "import '../providers/lang_provider.dart';": "import 'package:zariya_app/core/services/lang_provider.dart';",
    "import '../providers/recently_viewed_provider.dart';": "import 'package:zariya_app/features/shop/data/recently_viewed_provider.dart';",
    "import '../providers/loyalty_provider.dart';": "import 'package:zariya_app/features/profile/data/loyalty_provider.dart';",
    "import '../widgets/product_card.dart';": "import 'package:zariya_app/shared/widgets/product_card.dart';",
    "import '../widgets/shimmer_card.dart';": "import 'package:zariya_app/shared/widgets/shimmer_card.dart';",
    "import '../widgets/offline_banner.dart';": "import 'package:zariya_app/shared/widgets/offline_banner.dart';",
    "import '../widgets/emi_calculator.dart';": "import 'package:zariya_app/shared/widgets/emi_calculator.dart';",
    "import '../widgets/price_alert_sheet.dart';": "import 'package:zariya_app/shared/widgets/price_alert_sheet.dart';",
    // Screen mappings (for main.dart mostly)
    "import 'screens/": "import 'package:zariya_app/features/",
    "import 'models/order.dart';": "import 'package:zariya_app/features/profile/data/order.dart';",
    "import 'providers/": "import 'package:zariya_app/features/", // This will need manual fix for core/services ones
  };

  // Special case for main.dart which has different relative paths
  
  if (dir.existsSync()) {
    dir.listSync(recursive: true).forEach((file) {
      if (file is File && file.path.endsWith('.dart')) {
        var content = file.readAsStringSync();
        var changed = false;
        
        mappings.forEach((key, value) {
          if (content.contains(key)) {
            content = content.replaceAll(key, value);
            changed = true;
          }
        });
        
        // Fix some manual overlaps
        if (content.contains('package:zariya_app/features/auth_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/auth_provider.dart', 'package:zariya_app/features/auth/data/auth_provider.dart');
           changed = true;
        }
        if (content.contains('package:zariya_app/features/product_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/product_provider.dart', 'package:zariya_app/features/shop/data/product_provider.dart');
           changed = true;
        }
        if (content.contains('package:zariya_app/features/cart_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/cart_provider.dart', 'package:zariya_app/features/cart/data/cart_provider.dart');
           changed = true;
        }
        if (content.contains('package:zariya_app/features/wishlist_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/wishlist_provider.dart', 'package:zariya_app/features/shop/data/wishlist_provider.dart');
           changed = true;
        }
        if (content.contains('package:zariya_app/features/recently_viewed_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/recently_viewed_provider.dart', 'package:zariya_app/features/shop/data/recently_viewed_provider.dart');
           changed = true;
        }
        if (content.contains('package:zariya_app/features/theme_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/theme_provider.dart', 'package:zariya_app/core/services/theme_provider.dart');
           changed = true;
        }
        if (content.contains('package:zariya_app/features/lang_provider.dart')) {
           content = content.replaceAll('package:zariya_app/features/lang_provider.dart', 'package:zariya_app/core/services/lang_provider.dart');
           changed = true;
        }
        
        // Screens in main.dart
        content = content.replaceAll('package:zariya_app/features/splash_screen.dart', 'package:zariya_app/features/shop/presentation/splash_screen.dart');
        content = content.replaceAll('package:zariya_app/features/home_screen.dart', 'package:zariya_app/features/shop/presentation/home_screen.dart');
        content = content.replaceAll('package:zariya_app/features/product_list_screen.dart', 'package:zariya_app/features/shop/presentation/product_list_screen.dart');
        content = content.replaceAll('package:zariya_app/features/product_detail_screen.dart', 'package:zariya_app/features/shop/presentation/product_detail_screen.dart');
        content = content.replaceAll('package:zariya_app/features/cart_screen.dart', 'package:zariya_app/features/cart/presentation/cart_screen.dart');
        content = content.replaceAll('package:zariya_app/features/checkout_screen.dart', 'package:zariya_app/features/cart/presentation/checkout_screen.dart');
        content = content.replaceAll('package:zariya_app/features/auth_screen.dart', 'package:zariya_app/features/auth/presentation/auth_screen.dart');
        content = content.replaceAll('package:zariya_app/features/profile_screen.dart', 'package:zariya_app/features/profile/presentation/profile_screen.dart');
        content = content.replaceAll('package:zariya_app/features/order_screens.dart', 'package:zariya_app/features/profile/presentation/order_screens.dart');
        content = content.replaceAll('package:zariya_app/features/wishlist_screen.dart', 'package:zariya_app/features/shop/presentation/wishlist_screen.dart');
        content = content.replaceAll('package:zariya_app/features/custom_jewelry_screen.dart', 'package:zariya_app/features/profile/presentation/custom_jewelry_screen.dart');
        content = content.replaceAll('package:zariya_app/features/vto_screen.dart', 'package:zariya_app/features/extras/presentation/vto_screen.dart');
        content = content.replaceAll('package:zariya_app/features/gifting_quiz_screen.dart', 'package:zariya_app/features/extras/presentation/gifting_quiz_screen.dart');
        content = content.replaceAll('package:zariya_app/features/compare_screen.dart', 'package:zariya_app/features/shop/presentation/compare_screen.dart');
        content = content.replaceAll('package:zariya_app/features/ring_size_guide_screen.dart', 'package:zariya_app/features/extras/presentation/ring_size_guide_screen.dart');
        content = content.replaceAll('package:zariya_app/features/gold_exchange_screen.dart', 'package:zariya_app/features/extras/presentation/gold_exchange_screen.dart');
        content = content.replaceAll('package:zariya_app/features/jewelry_care_screen.dart', 'package:zariya_app/features/extras/presentation/jewelry_care_screen.dart');
        content = content.replaceAll('package:zariya_app/features/about_screen.dart', 'package:zariya_app/features/extras/presentation/about_screen.dart');
        content = content.replaceAll('package:zariya_app/features/certificate_screen.dart', 'package:zariya_app/features/profile/presentation/certificate_screen.dart');
        content = content.replaceAll('package:zariya_app/features/address_screen.dart', 'package:zariya_app/features/profile/presentation/address_screen.dart');
        content = content.replaceAll('package:zariya_app/features/my_requests_screen.dart', 'package:zariya_app/features/profile/presentation/my_requests_screen.dart');
        content = content.replaceAll('package:zariya_app/features/store_locator_screen.dart', 'package:zariya_app/features/extras/presentation/store_locator_screen.dart');
        content = content.replaceAll('package:zariya_app/features/appointment_screen.dart', 'package:zariya_app/features/extras/presentation/appointment_screen.dart');
        content = content.replaceAll('package:zariya_app/features/feedback_screen.dart', 'package:zariya_app/features/profile/presentation/feedback_screen.dart');

        if (changed) {
          file.writeAsStringSync(content);
          print('Updated ${file.path}');
        }
      }
    });
  }
}
