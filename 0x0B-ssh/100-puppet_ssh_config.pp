# create a file in /tmp directory
file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
