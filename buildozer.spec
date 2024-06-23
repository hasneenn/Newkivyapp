[app]

# (str) Title of your application
title = RecoveryApp

# (str) Package name
package.name = recoveryapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.hasneen

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported bootstraps
android.bootstrap = sdl2

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (int) Android NDK version to use
android.ndk = 21b

# (bool) Enable Android logcat
android.logcat_filters = *:S python:D

# (list) View your own logcat tags
android.logcat_filter = *:S python:D

# (bool) Android automatically add permissions
android.permissions = INTERNET

# (list) Additional Java .jar or .aar libraries to add
#android.add_jars =

# (str) packaging type
# android.archs = armeabi-v7a, arm64-v8a
