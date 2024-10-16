import 'package:ecotag/screens/closet_page.dart';
import 'package:ecotag/screens/profile_page.dart';
import 'package:flutter/material.dart';
import 'screens/splash_screen.dart'; // Import your splash screen
import 'screens/home_page.dart'; // Import your home page
import 'screens/login_page.dart'; // Import your login page

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ecotag',

      initialRoute: '/', // Initial route
      routes: {
        '/': (context) => SplashScreen(), // Splash Screen
        '/home': (context) => HomePage(), // Home Page
        '/login': (context) => LoginPage(), // Login Page
        '/profile': (context) => ProfilePage(),// Closet Page
      },
    );
  }
}
