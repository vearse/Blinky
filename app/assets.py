from flask_assets import Bundle

app_css = Bundle('app.css',   output='styles/app.css')

# blinky_css = Bundle('blinky.css',   output='styles/brand.css')

app_js = Bundle('app.js', filters='jsmin', output='scripts/app.js')

vendor_css = Bundle('vendor/bootstrap.min.css', output='styles/vendor.css')

vendor_js = Bundle(
    'vendor/jquery.min.js',
    'vendor/bootstrap.min.js',
    'vendor/tablesort.min.js',
    'vendor/zxcvbn.js',
    filters='jsmin',
    output='scripts/vendor.js')
