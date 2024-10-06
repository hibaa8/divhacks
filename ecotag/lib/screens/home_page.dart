import 'package:ecotag/screens/closet_page.dart';
import 'package:ecotag/screens/feed_page.dart';
import 'package:ecotag/screens/home_content_page.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:ecotag/widgets/bottom_navbar.dart';
import 'package:ecotag/widgets/drawer.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _currentIndex = 0;

  PageController _pageController = PageController(initialPage: 0);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FD),
      drawer: MyDrawer(),
      body: PageView(
        controller: _pageController,
        onPageChanged: (newIndex) {
          setState(() {
            _currentIndex = newIndex;
          });
        },
        children: const <Widget>[
          FeedPage(),
          HomeContentPage(),
          ClosetPage(),
        ],
        
      ),
      bottomNavigationBar: MyBottomNavBar(
        currentIndex: _currentIndex,
        onTap: (newIndex) {
          setState(() {
            _currentIndex = newIndex;
            _pageController.jumpToPage(newIndex);
          });
        },
  
      ),
    );
  }
}
