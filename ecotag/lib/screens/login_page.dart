import 'package:flutter/material.dart';
import 'package:ecotag/services/auth_service.dart'; 

class LoginPage extends StatelessWidget {
  final AuthService _authService = AuthService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 24.0), // Added padding for better alignment
        child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            // Logo section
            Image.asset('assets/EcoTag.png', height: 150), // Reduced the height for a sleeker look
            const SizedBox(height: 40), // Added more spacing for better balance

            // App name with modernized styling
            const Text(
              'fabrich',
              style: TextStyle(
                fontSize: 32, // Increased font size for emphasis
                fontWeight: FontWeight.bold, // Added boldness for better visibility
                color: Color(0xFF34716C),
              ),
            ),
            const SizedBox(height: 60), // Increased spacing for a cleaner layout

            // Login button section
            Container(
              width: 200, // Set your desired width here
              child: ElevatedButton(
                onPressed: () async {
                  if (await _authService.isLoggedIn()) {
                    Navigator.pushReplacementNamed(context, '/home');
                  } else {
                    bool success = await _authService.login();
                    if (success) {
                      Navigator.pushReplacementNamed(context, '/home');
                    } else {
                      // Handle login error
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text("Login failed. Please try again.")),
                      );
                    }
                  }
                },
                style: ElevatedButton.styleFrom(
                  foregroundColor: const Color(0xFF34716C),
                  backgroundColor: Colors.white,
                  minimumSize: Size(double.infinity, 50), // Full width button with fixed height
                ),
                child: Text("Login with Auth0"),
              ),
            ),
          
          ],
        ),
      ),
      ),
    );
  }
}




