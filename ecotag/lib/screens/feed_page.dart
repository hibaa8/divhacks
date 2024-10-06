import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'package:google_fonts/google_fonts.dart';

class FeedPage extends StatefulWidget {
  const FeedPage({Key? key}) : super(key: key);

  @override
  State<FeedPage> createState() => _FeedPageState();
}

class _FeedPageState extends State<FeedPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD),
      body: ListView( // Allow scrolling if content overflows
          children: [
            const SizedBox(height: 10), // Increase padding to move text down
            
            // Top Header Text
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20.0),
              child: Text(
                'Sustainable Clothing Articles',
                style: GoogleFonts.lato(
                  textStyle: const TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF34716C),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 10),

            // Article List
            ListView(
              padding: const EdgeInsets.symmetric(horizontal: 10),
              shrinkWrap: true, // Allow the ListView to shrink to fit its content
              physics: const NeverScrollableScrollPhysics(), // Disable scrolling of ListView
              children: [
                _buildArticleCard(context, 'The Future of Sustainable Fashion'),
                _buildArticleCard(context, 'Eco-friendly Fabrics for Your Wardrobe'),
              ],
            ),

            const SizedBox(height: 20), // Add space before the carousel text

            // Recommended Clothing Section
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20.0),
              child: Text(
                'Recommended Clothing',
                style: GoogleFonts.lato(
                  textStyle: const TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF34716C),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 20), // Add space between the header and carousel

            // Carousel Section
            CarouselSlider(
              options: CarouselOptions(
                height: 150, // Make carousel height smaller for modern look
                enlargeCenterPage: true,
                viewportFraction: 0.6, // Adjust the viewport for more centered focus
              ),
              items: [1, 2, 3, 4, 5].map((i) {
                return Builder(
                  builder: (BuildContext context) {
                    return Container(
                      margin: const EdgeInsets.symmetric(horizontal: 5.0),
                      decoration: BoxDecoration(
                        color: const Color(0xFF6BABAD),
                        borderRadius: BorderRadius.circular(20), // Rounded corners for modern look
                        boxShadow: [
                          BoxShadow(
                            color: Colors.grey.withOpacity(0.3),
                            spreadRadius: 2,
                            blurRadius: 5,
                            offset: const Offset(0, 3), // Shadow effect
                          ),
                        ],
                      ),
                      child: Center(
                        child: Text(
                          'Clothing Item $i',
                          style: const TextStyle(
                            fontSize: 16.0,
                            color: Colors.white,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    );
                  },
                );
              }).toList(),
            ),
            const SizedBox(height: 40), // Space at the bottom of the page
          ],
        ),
      );
  }

  // Method to build the article cards
  Widget _buildArticleCard(BuildContext context, String title) {
    return Card(
      margin: const EdgeInsets.all(10),
      elevation: 5,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(15), // Round the article card corners
      ),
      child: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Text(
          title,
          style: GoogleFonts.lato(
            textStyle: const TextStyle(
              fontSize: 18,
              color: Color(0xFF34716C),
            ),
          ),
        ),
      ),
    );
  }
}
