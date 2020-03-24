# pkill
exec {'killmenow':
  provider  => 'shell',
  command   => 'usr/bin/pkill -f killmenow'
}
