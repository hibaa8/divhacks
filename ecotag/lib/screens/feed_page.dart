import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:ecotag/widgets/drawer.dart'; // Import the drawer widget
import 'package:mongo_dart/mongo_dart.dart' as mongo;

class FeedPage extends StatefulWidget {
  const FeedPage({Key? key}) : super(key: key);

  @override
  State<FeedPage> createState() => _FeedPageState();
}

class _FeedPageState extends State<FeedPage> {
  List<Map<String, dynamic>> items = []; // List to store items fetched from MongoDB

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    var db = await mongo.Db.create('mongodb+srv://hibaaltaf98:HotChocolate333!@cluster0.eokpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0');
    await db.open();
    var collection = db.collection('main'); // Replace with your collection name

    // Fetch items from the database
    var fetchedItems = await collection.find().toList();
    await db.close();

    setState(() {
      items = fetchedItems; // Store the fetched items in the list
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD),
      drawer: MyDrawer(), // Add drawer to the screen
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
          ListView.builder(
            padding: const EdgeInsets.symmetric(horizontal: 10),
            shrinkWrap: true, // Allow the ListView to shrink to fit its content
            physics: const NeverScrollableScrollPhysics(), // Disable scrolling of ListView
            itemCount: items.length, // Use the length of items
            itemBuilder: (context, index) {
              return _buildArticleCard(context, items[index]['title']);
            },
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
            options: CarouselOptions(height: 400.0),
            items: items.map((item) {
              return Builder(
                builder: (BuildContext context) {
                  return Container(
                    width: MediaQuery.of(context).size.width,
                    margin: const EdgeInsets.symmetric(horizontal: 5.0),
                    decoration: BoxDecoration(
                      color: Colors.amber,
                    ),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Image.network(item['imageUrl'], fit: BoxFit.cover), // Assuming there's an 'imageUrl' field
                        const SizedBox(height: 10),
                        Text(
                          item['title'], // Assuming there's a 'title' field
                          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 5),
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 10.0),
                          child: Text(
                            item['description'], // Assuming there's a 'description' field
                            textAlign: TextAlign.center,
                            style: const TextStyle(fontSize: 14),
                          ),
                        ),
                      ],
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
