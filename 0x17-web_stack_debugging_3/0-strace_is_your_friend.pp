# Fix apache2 server error

exec { 'Fix apache2 server':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
