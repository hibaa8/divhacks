import 'package:ecotag/widgets/drawer.dart';
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
  final AuthService _authService = AuthService(); // Initialize Auth Service
  List<Map<String, dynamic>> items = []; // Declare the items list

  @override
  void initState() {
    super.initState();
    fetchWardrobeItems(); // Fetch wardrobe items
  }

  Future<void> fetchWardrobeItems() async {
    // Here, you would typically call your API or database to get wardrobe items.
    // This is a sample data list for demonstration.
    setState(() {
      items = [
        {
          'imageUrl': 'https://your-image-url.com/item1.jpg',
          'title': 'Stylish Shirt',
          'description': 'A stylish shirt for every occasion.',
        },
        {
          'imageUrl': 'https://your-image-url.com/item2.jpg',
          'title': 'Comfortable Pants',
          'description': 'Comfortable pants for daily wear.',
        },
        {
          'imageUrl': 'https://your-image-url.com/item3.jpg',
          'title': 'Trendy Jacket',
          'description': 'A trendy jacket to keep you warm.',
        },
      ];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD),
      drawer: MyDrawer(), // Add drawer to the screen
      body: Column(
        children: [
          const SizedBox(height: 30), // Padding at the top

          // Profile Section
          Container(
            padding: const EdgeInsets.fromLTRB(16, 16, 16, 16),
            decoration: const BoxDecoration(
              color: Color(0xFF34716C), // Profile section background
              borderRadius: BorderRadius.vertical(bottom: Radius.circular(20)),
            ),
            child: Column(
              children: [
                const CircleAvatar(
                  radius: 40,
                  backgroundImage: NetworkImage('https://your-image-url.com'), // Replace with your profile image URL
                ),
                const SizedBox(height: 10),
                Text(
                  'Hello, User!',
                  style: GoogleFonts.lato(
                    textStyle: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 30), // Padding below profile section

          // Wardrobe Heading
          Text(
            'Your Wardrobe',
            style: GoogleFonts.lato(
              textStyle: const TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Color(0xFF34716C),
              ),
            ),
          ),

          const SizedBox(height: 20), // Spacing before the carousel

          // Carousel Slider
          Expanded(
            child: CarouselSlider(
              options: CarouselOptions(height: 400.0),
              items: items.map((item) {
                return Builder(
                  builder: (BuildContext context) {
                    return Container(
                      width: MediaQuery.of(context).size.width * 0.8,
                      margin: const EdgeInsets.symmetric(horizontal: 10.0),
                      decoration: BoxDecoration(
                        color: const Color(0xFF34716C),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(
                            item['title'],
                            style: const TextStyle(
                              fontSize: 16.0,
                              fontWeight: FontWeight.bold,
                              color: Colors.white,
                            ),
                          ),
                          const SizedBox(height: 5),
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 10.0),
                            child: Text(
                              item['description'],
                              textAlign: TextAlign.center,
                              style: const TextStyle(
                                fontSize: 14.0,
                                color: Colors.white,
                              ),
                            ),
                          ),
                          const SizedBox(height: 10), // Space between description and icon
                          Image(
                            image: const AssetImage('assets/SHIRT.png'), // Heart icon
                            width: 60,
                            height: 60,
                          ),
                        ],
                      ),
                    );
                  },
                );
              }).toList(),
            ),
          ),

          const SizedBox(height: 20), // Spacing before the logout button

          // Log Out Button
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0), // Add horizontal padding
            child: ElevatedButton(
              onPressed: () async {
                await _authService.logout(); // Handle logout
                Navigator.pushReplacementNamed(context, '/login');
              },
              style: ElevatedButton.styleFrom(
                foregroundColor: const Color(0xFF34716C),
                backgroundColor: Colors.white,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
                minimumSize: const Size(double.infinity, 50), // Full width button
                elevation: 0, // Flat, modern button style
              ),
              child: const Text(
                'Log Out',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),

          const SizedBox(height: 30), // Padding at the bottom
        ],
      ),
    );
  }
}
