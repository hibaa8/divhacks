import 'package:flutter/material.dart';

class HomeContentPage extends StatefulWidget {
  const HomeContentPage({Key? key}) : super(key: key);

  @override
  State<HomeContentPage> createState() => _HomeContentPageState();
}

class _HomeContentPageState extends State<HomeContentPage> {
  final TextEditingController _urlController = TextEditingController();
  String _submittedUrl = '';

  // Function to handle URL submission
  void _submitUrl() {
    setState(() {
      _submittedUrl = _urlController.text;
    });
    // You can now use _submittedUrl to check for sustainability score, etc.
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD), // Light background color
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 20.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              // App Logo
              Image.asset(
                'assets/EcoTag.png',
                width: 240, // Adjust size of the logo
                height: 240,
              
              ),

              // App Name
              const Text(
                'ecotag',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF6BABAD),
                ),
              ),
              const SizedBox(height: 20),

              // URL Input Bar
              TextField(
                controller: _urlController,
                decoration: InputDecoration(
                  filled: true,
                  fillColor: Colors.white,
                  hintText: 'Enter Clothing URL',
                  prefixIcon: const Icon(
                    Icons.link,
                    color: Color(0xFF34716C),
                  ),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(30),
                    borderSide: BorderSide.none,
                  ),
                  contentPadding: const EdgeInsets.symmetric(vertical: 15.0, horizontal: 20.0),
                ),
              ),
              const SizedBox(height: 20),

              // Submit Button
              ElevatedButton(
                onPressed: _submitUrl,
                style: ElevatedButton.styleFrom(
                  foregroundColor: const Color(0xFF34716C),
                  backgroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30),
                  ),
                ),
                child: const Text(
                  'Submit',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 40),

              // Display Submitted URL (can replace with sustainability info later)
              _submittedUrl.isNotEmpty
                  ? Text(
                      'Submitted URL: $_submittedUrl',
                      style: const TextStyle(
                        fontSize: 16,
                        color: Color(0xFF34716C),
                      ),
                    )
                  : const Text(
                      'Enter a URL to check sustainability',
                      style: TextStyle(
                        fontSize: 16,
                        color: Color(0xFF808185),
                      ),
                    ),
            ],
          ),
        ),
      ),
    );
  }
}
