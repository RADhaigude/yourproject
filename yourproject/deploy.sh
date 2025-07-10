#!/bin/bash
echo "✅ Restarting app..."
# For Node.js app
pm2 restart app.js

# OR for Apache
# sudo systemctl restart apache2
