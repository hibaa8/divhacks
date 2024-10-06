import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart'; // Import Google Fonts
import 'package:ecotag/services/auth_service.dart'; 
import 'home_page.dart';
import 'login_page.dart';

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  final AuthService _authService = AuthService();

  @override
  void initState() {
    super.initState();
    _checkAuthentication();
  }

  Future<void> _checkAuthentication() async {
    await Future.delayed(Duration(seconds: 2)); // Simulate splash delay
    bool isAuthenticated = await _authService.checkAuthStatus(); // Check if user is authenticated

    if (isAuthenticated) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => HomePage()), // Navigate to HomePage if authenticated
      );
    } else {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => LoginPage()), // Navigate to LoginPage if not authenticated
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD), // Background color (light grayish blue)
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AnimatedOpacity(
              opacity: 1.0,
              duration: Duration(seconds: 1),
              child: Image.asset(
                'assets/EcoTag.png',
                width: 240, // Adjust size of the logo
                height: 240,
              ),
            ),
            SizedBox(height: 20),
            AnimatedOpacity(
              opacity: 1.0,
              duration: Duration(seconds: 1),
              child: Text(
                'fabrich',
                style: GoogleFonts.lato( // Using Google Font 'Lato'
                  textStyle: TextStyle(
                    fontSize: 36, // Larger text size for a modern look
                    fontWeight: FontWeight.bold,
                    color: //hex code color
                        Color(0xFF6BABAD), // Dark blue color
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}



