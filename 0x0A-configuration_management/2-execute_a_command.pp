# Use exec resource type to kill process
exec {'killmenow':
  command => '/usr/bin/pkill killmenow',
  returns => [0, 1],
}
