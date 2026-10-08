[app]
title = Cuba.TV
package.name = cubatv
package.domain = org.cubatv

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 1.0.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests,beautifulsoup4,plyer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

android.presplash_color = #1a1a1a
android.presplash = assets/icons/splash.png
android.icon = assets/icons/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
