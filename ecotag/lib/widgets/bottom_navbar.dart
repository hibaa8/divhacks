import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:google_nav_bar/google_nav_bar.dart';

class MyBottomNavBar extends StatelessWidget {
  final int currentIndex;
  final Function(int) onTap;

  MyBottomNavBar({required this.currentIndex, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 65,
      margin: EdgeInsets.only(
        left: 24,
        right: 24,
        bottom: 24,
      ),
      decoration: BoxDecoration(
        color: Color(0xFF6BABAD),
        borderRadius: BorderRadius.circular(55),
        border: Border.all(
          color: Color.fromARGB(255, 12, 55, 91),
          width: 3, 
        ),
        boxShadow: [
          BoxShadow(
            blurRadius: 20,
            color: Colors.black.withOpacity(0.1),
          ),
        ],
      ),
      child: GNav(
        selectedIndex: currentIndex,
        onTabChange: (index) => onTap(index),
        iconSize: 24,
        color: Color.fromARGB(255, 12, 55, 91),
        activeColor: Colors.white,
        padding: EdgeInsets.symmetric(horizontal: 20, vertical: 14),
        gap: 8.5,
        tabs: [
          GButton(
            icon: Icons.article,
            text: 'Feed',
            textStyle: 
            GoogleFonts.roboto(
              fontSize: 16,
              color: Colors.white,
            ),
          ),
          GButton(
            icon: Icons.eco,
            text: 'Search',
            textStyle: GoogleFonts.roboto(
              fontSize: 16,
              fontWeight: FontWeight.w500,
              color: Colors.white,
            ),
          ),
          GButton(
            icon: Icons.checkroom, 
            text: 'Closet',
            textStyle: GoogleFonts.roboto(
              fontSize: 16,
              fontWeight: FontWeight.w500,
              color: Colors.white,
            ),
          ),
        ],
      ),
    );
  }
}
