# Contain file in /tmp with some customizations

file { 'tmp/school':
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love puppet',
}
