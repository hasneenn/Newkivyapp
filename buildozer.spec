[app]

# Title of your application
title = RecoveryApp

# Package name
package.name = recoveryapp

# Package domain (needed for android/ios packaging)
package.domain = org.hasneen

# Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# Application versioning (method 1)
version = 1.0

# Application requirements
requirements = python3,kivy,requests

# Supported bootstraps
p4a.bootstrap = sdl2

# Permissions
android.permissions = INTERNET

# Target Android API, should be as high as possible
android.api = 30

# Minimum API your APK will support
android.minapi = 21

# Android SDK and NDK versions
android.sdk = 25
android.ndk = 25b

# Enable Android logcat
android.logcat_filters = *:S python:D

# Source directory where your main.py is located
source.dir = .

# Additional Java .jar or .aar libraries to add
android.add_jars = foo.jar, bar.jar

[buildozer]

# Log level (1 = debug, 2 = info, 3 = warning, 4 = error)
log_level = 2
warn_on_root = 1

# Automatically accept SDK licenses
android.accept_sdk_license = True
