
import os

mappings = {
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
    "import 'screens/": "import 'package:zariya_app/features/",
    "import 'models/order.dart';": "import 'package:zariya_app/features/profile/data/order.dart';",
    "import 'providers/": "import 'package:zariya_app/features/",
}

def fix_imports():
    for root, dirs, files in os.walk('lib'):
        for file in files:
            if file.endswith('.dart'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                changed = False
                for key, value in mappings.items():
                    if key in content:
                        content = content.replace(key, value)
                        changed = True
                
                # Further refinements
                if 'package:zariya_app/features/auth_provider.dart' in content:
                    content = content.replace('package:zariya_app/features/auth_provider.dart', 'package:zariya_app/features/auth/data/auth_provider.dart')
                    changed = True
                if 'package:zariya_app/features/product_provider.dart' in content:
                    content = content.replace('package:zariya_app/features/product_provider.dart', 'package:zariya_app/features/shop/data/product_provider.dart')
                    changed = True
                if 'package:zariya_app/features/cart_provider.dart' in content:
                    content = content.replace('package:zariya_app/features/cart_provider.dart', 'package:zariya_app/features/cart/data/cart_provider.dart')
                    changed = True
                if 'package:zariya_app/features/wishlist_provider.dart' in content:
                    content = content.replace('package:zariya_app/features/wishlist_provider.dart', 'package:zariya_app/features/shop/data/wishlist_provider.dart')
                    changed = True
                if 'package:zariya_app/features/theme_provider.dart' in content:
                    content = content.replace('package:zariya_app/features/theme_provider.dart', 'package:zariya_app/core/services/theme_provider.dart')
                    changed = True
                
                # Screen specific replacements
                screens = {
                    'splash_screen.dart': 'shop/presentation/splash_screen.dart',
                    'home_screen.dart': 'shop/presentation/home_screen.dart',
                    'product_list_screen.dart': 'shop/presentation/product_list_screen.dart',
                    'product_detail_screen.dart': 'shop/presentation/product_detail_screen.dart',
                    'cart_screen.dart': 'cart/presentation/cart_screen.dart',
                    'checkout_screen.dart': 'cart/presentation/checkout_screen.dart',
                    'auth_screen.dart': 'auth/presentation/auth_screen.dart',
                    'profile_screen.dart': 'profile/presentation/profile_screen.dart',
                    'order_screens.dart': 'profile/presentation/order_screens.dart',
                    'wishlist_screen.dart': 'shop/presentation/wishlist_screen.dart',
                    'vto_screen.dart': 'extras/presentation/vto_screen.dart',
                    'certificate_screen.dart': 'profile/presentation/certificate_screen.dart',
                    'address_screen.dart': 'profile/presentation/address_screen.dart',
                }
                
                for s_key, s_val in screens.items():
                    bad_import = f'package:zariya_app/features/{s_key}'
                    good_import = f'package:zariya_app/features/{s_val}'
                    if bad_import in content:
                        content = content.replace(bad_import, good_import)
                        changed = True

                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    fix_imports()
