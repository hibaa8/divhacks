import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../utils/constants.dart';

const String CALLBACK_URL = 'com.example.ecotag://login-callback';
const String LOGOUT_URL = 'com.example.ecotag://logout-callback';

class AuthService {
  final Auth0 auth0 = Auth0(
    AUTH0_DOMAIN,
    AUTH0_CLIENT_ID,
  );
  
  final FlutterSecureStorage storage = FlutterSecureStorage(); // For secure storage
  Future<bool> isLoggedIn() async {
    return await auth0.credentialsManager.hasValidCredentials();
  }


  Future<bool> checkAuthStatus() async {
    try {
      return await auth0.credentialsManager.hasValidCredentials();
    } catch (e) {
      return false;
    }
  }

  Future<bool> login() async {
    try {
      final credentials = await auth0.webAuthentication().login(redirectUrl: CALLBACK_URL);
      await auth0.credentialsManager.storeCredentials(credentials);
      // Store additional user info in secure storage if needed
      await storage.write(key: 'access_token', value: credentials.accessToken); // Store access token
      return true;
    } catch (e) {
      return false;
    }
  }

  Future<void> logout() async {
    try {
      await auth0.webAuthentication().logout(returnTo: LOGOUT_URL);
      await auth0.credentialsManager.clearCredentials();
      await storage.delete(key: 'access_token'); // Clear the stored token on logout
    } catch (e) {
      // Handle errors
    }
  }
}
