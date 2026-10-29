[app]

source.dir = .
version = 0.1
title = My Python App
package.name = mypythonapp
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 33
android.min_api = 21
android.sdk_version = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
