import 'package:flutter/material.dart';
import 'package:ecotag/services/auth_service.dart'; 

class LoginPage extends StatelessWidget {
  final AuthService _authService = AuthService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login")),
      body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Image.asset('assets/EcoTag.png', height: 200), // Replace 'assets/logo.png' with your logo's asset path
          SizedBox(height: 20), // Add some spacing
          Text('Ecotag', style: TextStyle(fontSize: 24, color: Color(0xFF6BABAD))), // Replace 'Welcome to MyApp' with your text
          SizedBox(height: 20), // Add some spacing
          ElevatedButton(
            onPressed: () async {
              if (await _authService.isLoggedIn()) {
                Navigator.pushReplacementNamed(context, '/home');
              } else {
                bool success = await _authService.login(); // Attempt to log in
                if (success) {
                  Navigator.pushReplacementNamed(context, '/home');
                } else {
                  // Handle login error (show a message, etc.)
                  print("Login failed. Please try again."); // Debugging log
                }
              }
            },
            child: Text("Login with Auth0"),
          ),
        ],
      ),
    ),
    );
  }
}

