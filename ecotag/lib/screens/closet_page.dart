import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:ecotag/services/auth_service.dart';

class ClosetPage extends StatefulWidget {
  const ClosetPage({Key? key}) : super(key: key);

  @override
  State<ClosetPage> createState() => _ClosetPageState();
}

class _ClosetPageState extends State<ClosetPage> {
  final AuthService _authService = AuthService();  // Initialize Auth Service

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD),
      body: Column(
        children: [
          SizedBox(height: 30),  // For padding at the top
          // Profile Section
          Container(
            padding: EdgeInsets.fromLTRB(16, 16, 16, 16),
            decoration: BoxDecoration(
              color: const Color(0xFF34716C),  // Profile section background
              borderRadius: BorderRadius.vertical(bottom: Radius.circular(20)),
            ),
            child: Column(
              children: [
                CircleAvatar(
                  radius: 40,
                  backgroundImage: NetworkImage('https://your-image-url.com'), // Replace with your profile image URL
                ),
                SizedBox(height: 10),
                Text(
                  'Hello, User!',
                  style: GoogleFonts.lato(
                    textStyle: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
          ),
          SizedBox(height: 20), // Padding below profile section
          Text(
            'Your Wardrobe',
            style: GoogleFonts.lato(
              textStyle: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: const Color(0xFF34716C),
              ),
            ),
          ),
          Expanded(
            child: CarouselSlider(
              options: CarouselOptions(height: 200),
              items: [1, 2, 3, 4, 5].map((i) {
                return Builder(
                  builder: (BuildContext context) {
                    return Container(
                      width: MediaQuery.of(context).size.width,
                      margin: EdgeInsets.symmetric(horizontal: 5.0),
                      decoration: BoxDecoration(
                        color: const Color(0xFF34716C), // Green color
                        borderRadius: BorderRadius.circular(12), // Rounded edges
                      ),
                      child: Center(
                        child: Text(
                          'Liked Item $i',
                          style: TextStyle(fontSize: 16.0, color: Colors.white), // White text
                        ),
                      ),
                    );
                  },
                );
              }).toList(),
            ),
          ),
          SizedBox(height: 20),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0), // Add horizontal padding
            child: ElevatedButton(
              onPressed: () async {
                await _authService.logout();  // Handle logout
                Navigator.pushReplacementNamed(context, '/login');
              },
              style: ElevatedButton.styleFrom(
                foregroundColor: const Color(0xFF34716C),
                backgroundColor: Colors.white,
                minimumSize: Size(double.infinity, 50), // Full width button with fixed height
              ),
              child: Text('Log Out'),
            ),
          ),
          SizedBox(height: 20), // Padding at the bottom
        ],
      ),
    );
  }
}
